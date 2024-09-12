from django.urls import path

from . import views

app_name = "usuarios" # Esto es para ahcer referencia desde el template. (desde el tempalte, llamar a las url)

urlpatterns = [
    path('IniciarSesion/', views.IniciarSesion, name="IniciarSesion"),
    path('Registrarse/', views.Registrarse, name="Registrarse"),
    path('CerrarSesion/', views.CerrarSesion, name="CerrarSesion"),
]