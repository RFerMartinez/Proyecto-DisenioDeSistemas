
from django.db import models

from ..categorias.models import Categoria
from ..usuarios.models import Cliente

class UnidadMedida(models.Model):
    # CAMPOS DE LA TABLA 'UnidadMedida'
    nombre = models.CharField(max_length=20, unique=True, null=False, blank=False, verbose_name='Nombre')
    prefijo = models.CharField(max_length=5, unique=True, null=False, blank=False, verbose_name='Prefijo')
    estado = models.BooleanField(default=True)

    class Meta:
        db_table = "UnidadMedida"

    def __str__(self):
        return f"{self.prefijo} - {self.nombre}"

class Producto(models.Model):
    # CAMPOS DE LA TABLA 'PRODUCTO'
    codigo = models.CharField(unique=True, null=False, blank=False, verbose_name='Código')
    nombre = models.CharField(max_length=70, unique=True, null=False, blank=False, verbose_name='Nombre')
    precio = models.DecimalField(max_digits=8, decimal_places=2, null=False, blank=False, verbose_name='Precio')
    costo = models.DecimalField(max_digits=8, decimal_places=2, null=False, blank=False, verbose_name='Costo')
    descripcion = models.TextField(max_length=150, verbose_name='Descripción')
    caducidad = models.DateField(verbose_name='Fecha de caducidad')
    cantidad_minima = models.PositiveSmallIntegerField(null=False, blank=False, verbose_name='Cantidad Mínima')
    cantidad_maxima = models.PositiveSmallIntegerField(null=False, blank=False, verbose_name='Cantidad Máxima')
    estado = models.BooleanField(default=True)
    # IMAGEN
    imagen = models.ImageField(null=True, blank=True, upload_to="imagenProducto/")

    # relaciones a las tablas 'Categoría' y 'Unidad'
    categoria = models.ForeignKey(Categoria, related_name='productos', on_delete=models.CASCADE)
    unidad = models.ForeignKey(UnidadMedida, related_name='productos', on_delete=models.CASCADE)

    # La función '__str__' sirve para representar un objeto de la tabla, en lugar de 'object (1)'
    def __str__(self):
        return f"{self.codigo} - {self.nombre}"
    
    # Para acceder a los 'metadatos' o comportamiento adicional de la table (no de los campos)
    class Meta:
        db_table = 'Producto'
        ordering = ['nombre'] # ['-precio'] -> esto es para ordenar de manera descendente
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'

# Entidad de carrito
class Carrito(models.Model):
    producto = models.ForeignKey(Producto, related_name='carritos', on_delete=models.CASCADE)
    usuario = models.ForeignKey(Cliente, related_name='usuarios', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.usuario.username} - {self.producto.nombre}'