from django.contrib import admin
from .models import Genero

# Register your models here.
class GeneroAdmin(admin.ModelAdmin):
    list_display = ('codigo', 'genero', 'abreviatura')
admin.site.register(Genero, GeneroAdmin)