from django.contrib import admin

from .models import Producto, UnidadMedida

# Register your models here.
admin.site.register(Producto)
admin.site.register(UnidadMedida)