from django.urls import path
from asesores.views import MunicipioAPI, MunicipioAutocomplete

urlpatterns = [
    path('api-municipio/', MunicipioAPI.as_view(), name="api-municipio"),
    path('municipio-autocomplete/', MunicipioAutocomplete.as_view(create_field='name'), name='municipio-autocomplete'),    
]
