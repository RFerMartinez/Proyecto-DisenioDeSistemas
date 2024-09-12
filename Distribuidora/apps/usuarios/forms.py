# Librerías de python

# Librerias de Django
from django import forms
from django.contrib.auth.forms import UserCreationForm

# Módulos del proyecto
from .models import Cliente

# Formulario para que un cliente se pueda registrar, heredando de 'UserCreationForm', para la función básica de password
class FormularioRegistroCliente(UserCreationForm):

    class Meta:
        model = Cliente
        fields = ['username', 'first_name','last_name','email','password1','password2','numeroTelefono','provincia']
        # exclude = []

        labels = {
            'username': 'Nombre de usuario',
            'first_name': 'Nombre',
            'last_name': 'Apellido',
            'email': 'Correo electrónico',
            'password1': 'Contraseña',
            'password2': 'Confirmar contraseña',
            'numeroTelefono': 'Número de teléfono',
            'provincia': 'Provincia'
        }
