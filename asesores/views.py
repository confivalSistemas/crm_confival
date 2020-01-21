from django.shortcuts import render

from rest_framework.views import APIView
import json
from django.http import HttpResponse
from .models import AsesoresDb
from .serializers import MunicipioSerializer
from municipio.models import Municipio

#================================================
#==> SERIALIZADOR DE MUNICIPIO
class MunicipioAPI(APIView):
    serializer = MunicipioSerializer

    def get(self, request, format=None):
        lista = Municipio.objects.all()
        response = self.serializer(lista, many=True)

        return HttpResponse(json.dumps(response.data), content_type='application/json')
















# from dal import autocomplete
# from municipio.models import Municipio

# class AsesoresAutocomplete(autocomplete.Select2QuerySetView):
#     def get_queryset(self):
#         qs = Municipio.objects.all()
#         if self.q:
#             qs = qs.filter(codigo__istartswith=self.q)
#         return qs


