from django.db import models

from django.db import models

from django.db import models

class Project(models.Model):
    # Definimos las opciones dentro de una clase interna
    class Technology(models.TextChoices):
        PYTHON = "Python", "Python"
        PHP = "PHP", "PHP"
        LARAVEL = "Laravel", "Laravel"
        DJANGO = "Django", "Django"
        JAVA = "Java", "Java"
        JAVASCRIPT = "JavaScript", "JavaScript"

    title = models.CharField(max_length=100)
    description = models.TextField()
    
    # Aplicamos las opciones al CharField
    technology = models.CharField(
        max_length=20,
        choices=Technology.choices,
        default=Technology.PYTHON
    )
    
    image = models.ImageField(upload_to='projects/')
    url = models.URLField(blank=True)

    def __str__(self):
        return self.title