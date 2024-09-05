
from django import forms

from .models import Producto, UnidadMedida

class FormProducto(forms.ModelForm):
    
    # Pasandole el modelo sobre el cual se hará el formulario (para tener en cuenta los campos, labels)
    model = Producto

    # Para establecer los campos que se usaran para los labels
    fields = ['nombre', 'codigo', 'precio', 'costo', 'descripcion', 'caducidad', 'cantidad_minima', 'cantidad_maxima', 'categoria', 'unidad', ]

    # Tambén se puede usar el atributo 'exclude = ['campos_que_no_van']

    # Personalizando los labels
    #



