from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate

from .forms import FormularioRegistroCliente

#Vista para registrar usuarios 

'''
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
'''

def Registrarse(request):
    if request.method == 'POST':
        form = FormularioRegistroCliente(request.POST)
        
        if form.is_valid():
            # Obtener datos limpios del formulario
            password1 = form.cleaned_data['password1']
            password2 = form.cleaned_data['password2']
            
            # Verificar que las contraseñas coincidan
            if password1 != password2:
                return render(request, 'Registrarse.html', {
                    'form': form,
                    'error': 'Las contraseñas no coinciden'
                })
            
            try:
                # Guardar el usuario y cliente
                cliente = form.save(commit=False)
                cliente.usuario.set_password(password1)  # Cifrar la contraseña
                cliente.usuario.save()  # Guardar el usuario en la base de datos
                cliente.save()  # Guardar el cliente relacionado
                
                # Iniciar sesión automáticamente después de registrar al usuario
                login(request, cliente.usuario)
                
                return redirect('home')  # Redirige a la página de inicio
            except Exception as e:
                return render(request, 'Registrarse.html', {
                    'form': form,
                    'error': f'Error al registrar el usuario: {str(e)}'
                })
        else:
            return render(request, 'Registrarse.html', {
                'form': form,
                'error': 'Por favor corrige los errores en el formulario.'
            })
    
    else:
        # Método GET: mostrar el formulario vacío
        
        return render(request, 'Registrarse.html', {
            'form': FormularioRegistroCliente(),
            'titulo': 'Registrar usuario',
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
    return redirect('home')
        



