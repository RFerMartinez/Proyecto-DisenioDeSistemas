
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

from . import views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', views.home, name="home"),

    # includes
    path('productos/', include('apps.productos.urls')),
    path('categorias/', include('apps.categorias.urls')),
    path('usuarios/', include('apps.usuarios.urls')),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
