from django.urls import path
from asesores import views

urlpatterns = [
    path('registro_asesores/', views.registro, name="registro_asesores"),    
]

# SUJETO A CAMBIOS DE URL DEACUERDO A LA NECESIDAD