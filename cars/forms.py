from django import forms
from cars.models import Brand, Car


class CarForm(forms.Form):
  model = forms.CharField(label='Modelo', max_length=200)
  brand = forms.ModelChoiceField(Brand.objects.all())
  factory_year = forms.IntegerField(label='Ano de Fabricação', required=False)
  model_year = forms.IntegerField(label='Ano do Modelo', required=False)
  value = forms.FloatField(label='Valor', required=False)
  plate = forms.CharField(label='Placa', max_length=10, required=False)
  photo = forms.ImageField(label='Foto', required=False)

  def save(self):
    car = Car(
      model = self.cleaned_data['model'],
      brand = self.cleaned_data['brand'],
      factory_year = self.cleaned_data['factory_year'],
      model_year = self.cleaned_data['model_year'],
      value = self.cleaned_data['value'],
      plate = self.cleaned_data['plate'],
      photo = self.cleaned_data['photo'],
    )
  
    car.save()
    return car