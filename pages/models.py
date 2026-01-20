from django.db import models

# Create your models here.
class Info(models.Model):
    name = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    profesion = models.CharField(max_length=100)
    imagen = models.ImageField(upload_to='perfil/')
    descripcion = models.TextField(blank=True, null=True)
    
    def __str__(self):
        return self.name    