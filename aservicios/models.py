from django.db import models

class Servicio(models.Model):
    titulo =  models.CharField(max_length = 100)
    contenido = models.CharField(max_length = 255)
    imagen = models.ImageField(upload_to = 'aServicios')
    created = models.DateTimeField(auto_now_add = True)
    updated = models.DateTimeField(auto_now_add = True)

    class Meta:
        verbose_name = 'servicio'
        verbose_name_plural = 'servicios'
    
    def __str__(self):
        return self.titulo