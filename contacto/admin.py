from django.contrib import admin
from .models import Contacto

# Register your models here.
@admin.register(Contacto)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject', 'created_at')
    search_fields = ('name', 'email', 'subject')
    readonly_fields = ('created_at',)