# Librerías de python

# Librerias de Django
from django.db import models
from django.contrib.auth.models import AbstractUser

# Módulos del proyecto

# Entidad usuario
class Cliente(AbstractUser):
    numeroTelefono = models.CharField(max_length=15, unique=True, blank=True, null=True, verbose_name="Número de teléfono")
    PROVINCIAS = [
        ('Buenos Aires', 'Buenos Aires'),
        ('Chaco', 'Chaco'),
        ('Corrientes', 'Corrientes'),
        ('Formosa', 'Formosa'),
    ]
    provincia = models.CharField(max_length=15, blank=False, null=False, choices=PROVINCIAS, verbose_name='Provincia')

    # Agregamos related_name para evitar conflictos con el modelo User
    # groups = models.ManyToManyField(
    #     'auth.Group',
    #     related_name='cliente_set',  # Cambia el related_name para evitar conflicto
    #     blank=True,
    #     help_text='The groups this user belongs to.'
    # )
    
    # user_permissions = models.ManyToManyField(
    #     'auth.Permission',
    #     related_name='cliente_permissions_set',  # Cambia el related_name para evitar conflicto
    #     blank=True,
    #     help_text='Specific permissions for this user.'
    # )

    def __str__(self):
        return f"({self.username}) - {self.last_name.split()[0]}, {self.first_name.split()[0]}"
    
    class Meta:
        db_table = 'Cliente'
        ordering = ['last_name'] # ['-precio'] -> esto es para ordenar de manera descendente
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'
