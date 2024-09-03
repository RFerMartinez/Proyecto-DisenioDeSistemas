from django.db import models

class Categoria(models.Model):
    nombre = models.CharField(max_length=20, verbose_name='Nombre de Categoría')
    estado = models.BooleanField(default=True)

