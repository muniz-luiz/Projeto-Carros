from django import forms
from cars.models import Brand


class CarForm(forms.Form):
  model = forms.CharField(label='Modelo', max_length=200)
  brand = forms.ModelChoiceField(Brand.objects.all())
  factory_year = forms.IntegerField(label='Ano de Fabricação', required=False)
  model_year = forms.IntegerField(label='Ano do Modelo', required=False)
  value = forms.FloatField(label='Valor', required=False)
  plate = forms.CharField(label='Placa', max_length=10, required=False)
  photo = forms.ImageField(label='Foto', required=False)
