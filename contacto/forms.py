from django import forms
from .models import Contacto

class ContactoForm(forms.ModelForm):
    class Meta:
        model = Contacto
        fields = ['name', 'email', 'subject', 'message']
        # Añadimos clases de Bootstrap para que se vea bien
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Tu nombre'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'correo@cdominio.com'}),
            'subject': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Asunto'}),
            'message': forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'placeholder': 'Escribe tu mensaje aquí...'}),
        }