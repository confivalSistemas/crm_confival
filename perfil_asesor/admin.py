from django.contrib import admin
from .models import Perfilasesor

# Register your models here.
class PerfilasesorAdmin(admin.ModelAdmin):
    list_display = ('codigo', 'perfil')
admin.site.register(Perfilasesor, PerfilasesorAdmin)