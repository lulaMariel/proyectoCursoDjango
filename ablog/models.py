from django.db import models
from django.contrib.auth.models import User

class Categoria(models.Model):
    nombre =  models.CharField(max_length = 100)
    created = models.DateTimeField(auto_now_add = True)
    updated = models.DateTimeField(auto_now_add = True)

    class Meta:
        verbose_name = 'categoría'
        verbose_name_plural = 'categorías'
    
    def __str__(self):
        return self.nombre

class Post(models.Model):
    titulo =  models.CharField(max_length = 100)
    contenido = models.CharField(max_length = 255)
    imagen = models.ImageField(upload_to = 'aBlog', null = True, blank = True)
    autor = models.ForeignKey(User, on_delete = models.CASCADE)
    categorias = models.ManyToManyField(Categoria)
    created = models.DateTimeField(auto_now_add = True)
    updated = models.DateTimeField(auto_now_add = True)

    class Meta:
        verbose_name = 'post'
        verbose_name_plural = 'posts'
    
    def __str__(self):
        return f'{self.titulo, self.contenido, self.imagen}'

