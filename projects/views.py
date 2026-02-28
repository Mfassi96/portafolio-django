from django.shortcuts import render,get_object_or_404
from .models import Project

def project_index(request):
    # Trae todos los objetos de la base de datos
    projects = Project.objects.all()
    # Pasa esos proyectos al archivo HTML (que crearemos luego)
    context = {
        'projects': projects
    }
    return render(request, 'projects/project_index.html',context)

def project_view(request, pk):
    project = Project.objects.get(pk=pk)
    context = {
        'project': project
    }
    return render(request, 'projects/project_view.html',context)