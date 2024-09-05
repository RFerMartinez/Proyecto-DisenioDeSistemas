
from django.contrib import admin
from django.urls import path, include

from . import views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', views.home, name="home"),
    path('IniciarSesion/', views.IniciarSesion, name="IniciarSesion"),
    path('Registrarse/', views.Registrarse, name="Registrarse"),
    path('CerrarSesion/', views.CerrarSesion, name="CerrarSesion"),

    # includes
    path('productos/', include('apps.productos.urls')),
    path('categorias/', include('apps.categorias.urls')),
]
