from django.shortcuts import render
from django.urls import reverse_lazy

from django.views.generic.edit import CreateView
from django.views.generic.list import ListView

from .forms import FormProducto
from .models import Producto

# VISTA basada en funcion para poder listar los produtos
def listar_productos(request):
    template = "productos/listar.html"
    # Hacer la consulta para pedir los productos en la base de datos
    productos = Producto.objects.all()
    ctx = {
        'productos' : productos,
    }
    return render(request, template, context=ctx)

# VISTA basada en clase para poder crear un nuevo producto
class CrearProducto(CreateView):
    template_name = "productos/crear.html"
    model = Producto
    form_class = FormProducto

    # Si se completa la accion, se redirige al listado
    success_url = reverse_lazy("productos:listar")

