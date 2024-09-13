
from django import forms

from .models import Producto, UnidadMedida

class FormularioRegistrarProducto(forms.ModelForm):

    class Meta:
        model = Producto
        fields = '__all__'
        widgets = {
            'codigo': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Código del producto',
                }
            ),
            'nombre': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Nombre del producto',
                }
            ),
            'precio': forms.NumberInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Precio del producto',
                }
            ),
            'costo': forms.NumberInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Costo del producto',
                }
            ),
            'descripcion': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Descripción del producto',
                    'rows': 3,  # Puedes ajustar el tamaño del textarea
                }
            ),
            'caducidad': forms.DateInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Fecha de caducidad',
                    'type': 'date',  # Para que se use un selector de fecha en HTML5
                }
            ),
            'cantidad_minima': forms.NumberInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Cantidad mínima',
                }
            ),
            'cantidad_maxima': forms.NumberInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Cantidad máxima',
                }
            ),
            'categoria': forms.Select(
                attrs={
                    'class': 'form-control',
                }
            ),
            'unidad': forms.Select(
                attrs={
                    'class': 'form-control',
                }
            ),
        }
    
    # Pasandole el modelo sobre el cual se hará el formulario (para tener en cuenta los campos, labels)
    

    # Para establecer los campos que se usaran para los labels
    # fields = ['nombre', 'codigo', 'precio', 'costo', 'descripcion', 'caducidad', 'cantidad_minima', 'cantidad_maxima', 'categoria', 'unidad', ]


    # Tambén se puede usar el atributo 'exclude = ['campos_que_no_van']

    # Personalizando los labels
    #



