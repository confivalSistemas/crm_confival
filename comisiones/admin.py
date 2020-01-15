from django.contrib import admin
from .models import Comisiones

# Register your models here.
class ComisionesAdmin(admin.ModelAdmin):
    list_display = ('codigo', 'tipo', 'descripcion', 'valor')
admin.site.register(Comisiones, ComisionesAdmin)