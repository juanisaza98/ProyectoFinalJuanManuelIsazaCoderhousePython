# Generated by Django 5.0.4 on 2024-05-23 08:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('producto', '0005_producto_fecha_actualizacion_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to='imagenes'),
        ),
    ]
