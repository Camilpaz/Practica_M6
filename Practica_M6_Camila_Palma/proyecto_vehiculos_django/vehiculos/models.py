from django.db import models

class Vehiculo(models.Model):
    tipo_vehiculo = [
        ('Particular', 'Particular'),
        ('Transporte', 'Transporte'),
        ('Carga', 'Carga'),
    ]
    marcas = [
        ('Fiat', 'Fiat'),
        ('Chevrolet', 'Chevrolet'),
        ('Ford', 'Ford'),
        ('Toyota', 'Toyota'),
    ]
    
    marca = models.CharField(max_length=20, blank=False, null=False, choices=marcas, default='Ford')
    modelo = models.CharField(max_length=100, blank=False, null=False)
    serial_carroceria = models.CharField (max_length=50, blank=False, null=False)
    serial_motor = models.CharField (max_length=50, blank=False, null=False)
    categoria = models.CharField(max_length=50, blank=False, null=False, choices=tipo_vehiculo, default='Particular')
    precio = models.IntegerField(blank=False, null=False)
    fecha_creacion = models.DateTimeField(null=False, blank=False, auto_now_add=True)
    fecha_modificacion = models.DateTimeField(null=False, blank=False, auto_now_add=False, auto_now=True)

    def condicion_precio(self):
        """Determina la condición del precio según el valor del vehículo."""
        if self.precio <= 10000:
            return 'Bajo'
        elif self.precio <= 30000:
            return 'Medio'
        else:
            return 'Alto'
        
    def __str__(self) -> str:
        return f"Marca: {self.marca} - Modelo: {self.modelo} - Serial carroceria: {self.serial_carroceria} - Serial motor: {self.serial_motor} Categoria: {self.categoria} - Precio: {self.precio}"

        
        super().save(*args, **kwargs)
    
    class Meta:
        permissions = [("can_edit_vehiculos", "Puede agregar, visualizar, modificar vehículos (no puede eliminar)")]
        ordering = ['precio']
        
    