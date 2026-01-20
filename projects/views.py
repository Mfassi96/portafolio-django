from django.shortcuts import render
from .models import Project

def project_index(request):
    # Trae todos los objetos de la base de datos
    projects = Project.objects.all()
    # Pasa esos proyectos al archivo HTML (que crearemos luego)
    context = {
        'projects': projects
    }
    return render(request, 'projects/project_index.html',context)