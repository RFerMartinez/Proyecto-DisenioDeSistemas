from django.db.models.query import QuerySet
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

# VISTA basada en clase para poder listar los productos y paginarlos
class ListarProductos(ListView):
    # Definir el template para renderizar la lista
    template_name = 'productos/listar.html'
    # Definir el modelo sobre el cual se trabajará (para las querys)
    model = Producto
    # Definir la cantidad de productos por páginas
    paginate_by = 2
    # Definir como se hará referenca a los productos desde el template (via context)
    context_object_name = 'productos'

    # Método para agregar datos adicioanles al contexto
    def get_context_data(self, **kwargs):
        contexto = super().get_context_data(**kwargs)
        '''Realizar lógica y/o agregar datos al contexto. Realizar filtros'''
        return contexto
    
    # Definir/modificar la consulta
    def get_queryset(self):
        return Producto.objects.all().order_by('nombre')


# VISTA basada en clase para poder crear un nuevo producto
class CrearProducto(CreateView):
    template_name = "productos/crear.html"
    model = Producto
    form_class = FormProducto

    # Si se completa la accion, se redirige al listado
    success_url = reverse_lazy("productos:listar")

