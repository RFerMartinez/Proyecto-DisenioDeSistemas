# Generated by Django 5.1 on 2024-09-04 01:03

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('categorias', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UnidadMedida',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=20, unique=True, verbose_name='Nombre')),
                ('prefijo', models.CharField(max_length=5, unique=True, verbose_name='Prefijo')),
                ('estado', models.BooleanField(default=True)),
            ],
            options={
                'db_table': 'UnidadMedida',
            },
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.CharField(unique=True, verbose_name='Código')),
                ('nombre', models.CharField(max_length=70, unique=True, verbose_name='Nombre')),
                ('precio', models.DecimalField(decimal_places=2, max_digits=8, verbose_name='Precio')),
                ('costo', models.DecimalField(decimal_places=2, max_digits=8, verbose_name='Costo')),
                ('descripcion', models.TextField(max_length=150, verbose_name='Descripción')),
                ('caducidad', models.DateField(verbose_name='Fecha caducidad')),
                ('cantidad_minima', models.PositiveSmallIntegerField(verbose_name='Cantidad Mínima')),
                ('cantidad_maxima', models.PositiveSmallIntegerField(verbose_name='Cantidad Máxima')),
                ('estado', models.BooleanField(default=True)),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='productos', to='categorias.categoria')),
                ('unidad', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='productos', to='productos.unidadmedida')),
            ],
            options={
                'verbose_name': 'Producto',
                'verbose_name_plural': 'Productos',
                'db_table': 'Producto',
                'ordering': ['nombre'],
            },
        ),
    ]
