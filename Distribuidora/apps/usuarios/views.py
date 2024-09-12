from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate

from .forms import FormularioRegistroCliente

#Vista para registrar usuarios 
def Registrarse(request):
    if request.method == 'GET':
        dato = {
            # 'form': UserCreationForm,
            'form': FormularioRegistroCliente,
            'titulo': 'Registrar usuario',
        }
        return render(request, 'Registrarse.html', context=dato)
    else:
        if request.POST['password1'] == request.POST['password2']:
            # Register user
            try:
                user = User.objects.create_user(username=request.POST['username'], password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('home')
            except: 
                return render(request, 'Registrarse.html', {
                'form': UserCreationForm,
                "error":'El usuario ya existe'
                })
        else:
            return render(request, 'Registrarse.html', {
                'form': UserCreationForm,
                "error":'Las Contraseñas no coinciden'
                })

# vista para iniciar sesion
def IniciarSesion(request):
    if request.method == 'GET':
        return render(request, 'IniciarSesion.html',{
            'form': AuthenticationForm
        })
    else:
        user = authenticate(request, username= request.POST['username'], password= request.POST['password'])
        if user is None:
            return render(request, 'IniciarSesion.html',{
                'form': AuthenticationForm,
                "error":'Usuario o contraseña incorrecta'
            })
        else:
            login(request, user)
            return redirect('home')
        

#Cerrar Sesion
def CerrarSesion(request):
    logout(request)
    return redirect('IniciarSesion')
        




