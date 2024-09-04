from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


#Vista para registrar usuarios 
def Registrarse(request):
    if request.method == 'GET':
        return render(request, 'Registrarse.html', {
            'form': UserCreationForm
        })
    else:
        if request.POST['password1'] == request.POST['password2']:
            # Register user
            try:
                user = User.objects.create_user(username=request.POST['username'], password=request.POST['password1'])
                user.save()
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



# Vista basada en función para el home
def home(request):
    template="home.html"
    ctx = {

    }
    return render(
        request=request,
        template_name=template,
        context=ctx
    )

def IniciarSesion(request):
    template="IniciarSesion.html"
    ctx = {

    }
    return render(
        request=request,
        template_name=template,
        context=ctx
    )

