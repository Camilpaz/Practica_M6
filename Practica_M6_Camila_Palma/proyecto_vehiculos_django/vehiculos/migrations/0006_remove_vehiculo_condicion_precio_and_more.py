# Generated by Django 5.1.3 on 2024-11-25 23:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vehiculos', '0005_alter_vehiculo_precio'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vehiculo',
            name='condicion_precio',
        ),
        migrations.AlterField(
            model_name='vehiculo',
            name='precio',
            field=models.IntegerField(),
        ),
    ]
