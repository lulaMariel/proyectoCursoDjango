from django.db import models

class CategoriaProducto(models.Model):
    nombre = models.CharField(max_length = 50)
    created = models.DateTimeField(auto_now_add = True)
    updated = models.DateTimeField(auto_now_add = True)

    class Meta:
        verbose_name = 'Categoria Producto'
        verbose_name_plural = 'Categorias Producto'

    def __str__(self):
        return self.nombre

class Producto(models.Model):
    nombre = models.CharField(max_length = 50)
    categoria = models.ForeignKey(CategoriaProducto, on_delete = models.CASCADE)
    imagen = models.ImageField(upload_to = 'aTienda', null = True, blank = True)
    precio = models.FloatField()
    stock = models.BooleanField(default = True)
    created = models.DateTimeField(auto_now_add = True)
    updated = models.DateTimeField(auto_now_add = True)

    class Meta:
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'

    def __str__(self):
        return self.nombre