from django.shortcuts import render, get_object_or_404
from .models import Project
from django.core.paginator import Paginator

def project_index(request):
    project_list = Project.objects.all().order_by('-id')
    
    paginator = Paginator(project_list, 6)
    
    page_number = request.GET.get('page')
    
    page_obj = paginator.get_page(page_number)
    context = {
        'projects': page_obj
    }
    return render(request, 'projects/project_index.html', context)


def project_view(request, pk):
    project = Project.objects.get(pk=pk)
    context = {
        'project': project
    }
    return render(request, 'projects/project_view.html',context)