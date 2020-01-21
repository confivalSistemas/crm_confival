from django.urls import path
from asesores.views import MunicipioAPI

urlpatterns = [
    path('api-municipio/', MunicipioAPI.as_view(), name="api-municipio"),    
]
