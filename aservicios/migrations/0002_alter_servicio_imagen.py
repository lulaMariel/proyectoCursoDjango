# Generated by Django 5.1.4 on 2024-12-09 12:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aServicios', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='servicio',
            name='imagen',
            field=models.ImageField(upload_to='aServicios'),
        ),
    ]
