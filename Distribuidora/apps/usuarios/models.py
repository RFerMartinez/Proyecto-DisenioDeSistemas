# Librerías de python

# Librerias de Django
from django.db import models
from django.contrib.auth.models import AbstractUser, User

# Módulos del proyecto

# Entidad usuario
class Cliente(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE, related_name='usuario')
    numeroTelefono = models.CharField(max_length=15, unique=True, blank=True, null=True, verbose_name="Número de teléfono")
    PROVINCIAS = [
        ('Buenos Aires', 'Buenos Aires'),
        ('Chaco', 'Chaco'),
        ('Corrientes', 'Corrientes'),
        ('Formosa', 'Formosa'),
    ]
    provincia = models.CharField(max_length=15, blank=False, null=False, choices=PROVINCIAS, verbose_name='Provincia')

    def __str__(self):
        return f"({self.username}) - {self.last_name.split()[0]}, {self.first_name.split()[0]}"
    
    class Meta:
        db_table = 'ClienteT'
        # ordering = ['last_name'] # ['-precio'] -> esto es para ordenar de manera descendente
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'

