from django.db.models.query import QuerySet
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy

from django.views.generic.edit import CreateView
from django.views.generic.list import ListView

from .forms import FormularioRegistrarProducto
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
    paginate_by = 6
    # Definir como se hará referenca a los productos desde el template (via context)
    context_object_name = 'productos'

    # Método para agregar datos adicioanles al contexto
    def get_context_data(self, **kwargs):
        contexto = super().get_context_data(**kwargs)
        '''Realizar lógica y/o agregar datos al contexto. Realizar filtros'''
        contexto['titulo'] = 'Lista de Productos'
        return contexto
    
    # Definir/modificar la consulta
    def get_queryset(self):
        return Producto.objects.all().order_by('nombre')


# VISTA basada en clase para poder crear un nuevo producto
class CrearProducto(CreateView):
    template_name = "productos/crear.html"
    model = Producto
    form_class = FormularioRegistrarProducto

    # Si se completa la accion, se redirige al listado
    success_url = reverse_lazy("productos:listar")

    def get_context_data(self, **kwargs):
        contexto = super().get_context_data(**kwargs)
        contexto['titulo'] = 'Crear Nuevo Producto'
        return contexto
    
def mostrarDetalles(request, pk):
    producto = get_object_or_404(Producto, pk=pk)

    # Obtener los favoritos del usuario actual
    # if request.user.is_authenticated:
    #     favoritos = Favorito.objects.filter(usuario=request.user)
    #     favoritos_ids = list(favoritos.values_list('producto_id', flat=True))
    # else:
    #     favoritos_ids = []

    context = {
        'productos': producto,
        # 'favoritos_ids': favoritos_ids,
    }
    return render(request, 'productos/mostrarDetalles.html', context)

