# Generated by Django 5.1.4 on 2024-12-12 13:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aTienda', '0002_producto_created_producto_updated'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='categoriaproducto',
            options={'verbose_name': 'Categoria Producto', 'verbose_name_plural': 'Categorias Producto'},
        ),
        migrations.AlterField(
            model_name='producto',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to='aTienda'),
        ),
    ]
