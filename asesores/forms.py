from dal import autocomplete
from municipio.models import Municipio
from django import forms

class AsesorForm(forms.ModelForm):
     departamento= forms.ModelChoiceField(
        queryset = User.objects.all(),
        widget=autocomplete.ModelSelect2(url='asesores:asesores-autocomplete')
    )

    class Meta:
        model = Municipio
        fields = ('__all__')

  