from django.db import models

# Create your models here.
class Contacto(models.Model):
    name = models.CharField(max_length=100, verbose_name="Nombre")
    email = models.EmailField(verbose_name="Correo Electrónico")
    subject = models.CharField(max_length=200, verbose_name="Asunto")
    message = models.TextField(verbose_name="Mensaje")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Enviado el")

    def __str__(self):
        return f"Mensaje de {self.name} - {self.subject}"