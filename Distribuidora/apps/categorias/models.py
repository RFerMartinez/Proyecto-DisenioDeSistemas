from django.db import models

class Categoria(models.Model):
    nombre = models.CharField(max_length=20, verbose_name='Nombre de Categoría')
    estado = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.nombre}"
    
    class Meta:
        db_table = 'Categoria'
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'
        ordering = ['nombre']
