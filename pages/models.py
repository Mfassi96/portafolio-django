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

class Servicio(models.Model):
    titulo = models.CharField(max_length=100)
    descripcion = models.TextField()
    icono = models.CharField(max_length=50, help_text="Clase de Font Awesome, ej: fa-code")
    activo = models.BooleanField(default=True)
    
    def __str__(self):
        return self.titulo
    
    class Meta:
        verbose_name_plural = "Servicios"    