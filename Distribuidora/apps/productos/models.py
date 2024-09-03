
from django.db import models

from ..categorias.models import Categoria

class Producto(models.Model):
    # CAMPOS DE LA TABLA 'PRODUCTO'
    codigo = models.CharField(unique=True, null=False, blank=False, verbose_name='Código')
    nombre = models.CharField(max_length=70, unique=True, null=False, verbose_name='Nombre',)
    precio = models.DecimalField(max_digits=8, decimal_places=2, null=False, blank=False, verbose_name='Precio')
    costo = models.DecimalField(max_digits=8, decimal_places=2, null=False, blank=False, verbose_name='Costo')
    descripcion = models.TextField(max_length=150, verbose_name='Descripción')
    caducidad = models.DateField(verbose_name='Fecha caducidad')
    cantidad_minima = models.PositiveSmallIntegerField(null=False, blank=False, verbose_name='Cantidad Mínima')
    cantidad_minima = models.PositiveSmallIntegerField(null=False, blank=False, verbose_name='Cantidad Máxima')
    estado = models.BooleanField(default=True)

    # relaciones a las tablas 'Categoría' y 'Unidad'
    categoria = models.ForeignKey(Categoria, related_name='productos', on_delete=models.CASCADE)

    # La función '__str__' sirve para representar un objeto de la tabla, en lugar de 'object (1)'
    def __str__(self):
        return f"{self.codigo} - {self.nombre}"
    
    # Para acceder a los 'metadatos' o comportamiento adicional de la table (no de los campos)
    class Meta:
        db_table = 'Producto'
        ordering = ['nombre'] # ['-precio'] -> esto es para ordenar de manera descendente
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'
        '''
        Atributos adicionales:
        abstract = True -> para que la clase sea 'abstracta'
        permissions = [
            ('puede_ver_reporte')
        ]
        
        '''