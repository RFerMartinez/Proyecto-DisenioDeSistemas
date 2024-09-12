# Librerías de python

# Librerias de Django
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

# Módulos del proyecto
from .models import Cliente

# Formulario para que un cliente se pueda registrar, heredando de 'UserCreationForm', para la función básica de password
class FormularioRegistroCliente(forms.ModelForm):
    # Campos del modelo User
    username = forms.CharField(
        max_length=150,
        required=True,
        label="Nombre de usuario")
    
    first_name = forms.CharField(
        max_length=30,
        required=True,
        label="Nombre")
    
    last_name = forms.CharField(
        max_length=30,
        required=True,
        label="Apellido")
    
    email = forms.EmailField(
        required=True,
        label="Correo electrónico")
    
    password1 = forms.CharField(
        widget=forms.PasswordInput,
        required=True,
        label="Contraseña")
    
    password2 = forms.CharField(
        widget=forms.PasswordInput,
        required=True,
        label="Confirmar contraseña")
    
    # Sobreescribir el método 'clean' para validar que las contraseñas coincidan
    def clean(self):
        cleaned_data = super().clean()
        password1 = cleaned_data.get('password1')
        password2 = cleaned_data.get('password2')

        if password1 and password2 and password1 != password2:
            self.add_error('password2', 'Las contraseñas no coinciden')

        return cleaned_data
    
    # Sobreescribir el método 'save' para que se guarde primero el usuario, luego se guarde el 'cliente' con el registro relacionado
    def save(self, commit=True):
        # Guardamos el usuario primero
        user = User(
            username=self.cleaned_data['username'],
            first_name=self.cleaned_data['first_name'],
            last_name=self.cleaned_data['last_name'],
            email=self.cleaned_data['email']
        )
        user.set_password(self.cleaned_data['password1'])  # Cifrar la contraseña
        if commit:
            user.save()

        # Guardamos el cliente, relacionado con el usuario creado
        cliente = super().save(commit=False)
        cliente.usuario = user
        if commit:
            cliente.save()

        return cliente

    class Meta:
        model = Cliente
        fields = ['numeroTelefono','provincia']
        # exclude = []
