from django.contrib import admin
from .models import Vehiculo


@admin.register(Vehiculo)
class VehiculoAdmin(admin.ModelAdmin):
    search_fields = ['marca', 'categoria', 'precio']
    list_display = ['marca', 'modelo', 'categoria', 'serial_carroceria', 'serial_motor', 'fecha_creacion', 'fecha_modificacion', 'precio']
    ordering = ['precio']
    list_filter = ['categoria', 'marca']
    