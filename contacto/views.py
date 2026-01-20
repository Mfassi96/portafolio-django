from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ContactoForm

def contact_view(request):
    if request.method == 'POST':
        form = ContactoForm(request.POST)
        if form.is_valid():
            form.save()  # Guarda el mensaje en la base de datos
            messages.success(request, "¡Mensaje enviado con éxito")
            return redirect('contacto') # Redirige para limpiar el formulario
    else:
        form = ContactoForm()
    
    return render(request, 'contacto/contacto.html', {'form': form})