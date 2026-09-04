from django.shortcuts import render
from .models import Info, Servicio
# Create your views here.
def home(request):
    perfil = Info.objects.first()
    lista_tecs = ["HTML", "CSS", "JS", "Python", "Django", "Git", "GitHub", "Bootstrap", "SQL", "Git", "GitHub","PHP"]
    tecnologias = sorted(list(set(lista_tecs)))
    return render(request, 'pages/home.html',{'perfil':perfil,'tecnologias':tecnologias})

def servicios(request):
    servicios = Servicio.objects.filter(activo=True)
    return render(request, 'pages/servicios.html', {'servicios': servicios})