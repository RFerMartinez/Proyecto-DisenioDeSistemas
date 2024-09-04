from django.urls import path

from . import views

app_name = "productos" # Esto es para ahcer referencia desde el template. (desde el tempalte, llamar a las url)

urlpatterns = [
    path('listar/', views.ListarProductos.as_view(), name='listar'),

]