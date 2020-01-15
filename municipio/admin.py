from django.contrib import admin
from .models import Municipio

# Register your models here.
class MunicipioAdmin(admin.ModelAdmin):
    list_display = ('codigo', 'codigo_dane', 'departamento', 'municipio')
admin.site.register(Municipio, MunicipioAdmin)