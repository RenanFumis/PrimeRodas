from django import forms
from cars.models import Car

#Aqi estamos criando um formulário para o modelo Car de forma automática (mais prático)
class CarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = ['brand', 'model', 'factory_year', 'model_year', 'plate', 'value', 'photo', 'description']

        labels = {
                    'brand': 'Marca',
                    'model': 'Modelo',
                    'factory_year': 'Ano de fabricação',
                    'model_year': 'Ano do modelo',
                    'plate': 'Placa',
                    'value': 'Valor',
                    'photo': 'Imagem',
                    'description': 'Descrição',
                }
# O nome clean_<nome do campo> é um método que é chamado automaticamente pelo Django e serve para validar um campo específico

    def clean_value(self):
        value = self.cleaned_data.get('value')
        if value is not None and value < 100000:
            self.add_error('value', 'O valor do carro deve ser maior que R$100.000,00')
        return value





# Aqui estamos criando um formulário para o modelo Car de forma manual
# class CarForm(forms.Form):
#     model = forms.CharField(max_length=200)
#     brand = forms.ModelChoiceField(Brand.objects.all())
#     factory_year = forms.IntegerField()
#     model_year = forms.IntegerField()
#     plate = forms.CharField(max_length=10)
#     value = forms.FloatField()
#     photo = forms.ImageField()


#     def save(self):
#         car = Car(
#             model = self.cleaned_data['model'],
#             brand = self.cleaned_data['brand'],
#             factory_year = self.cleaned_data['factory_year'],
#             model_year = self.cleaned_data['model_year'],
#             plate = self.cleaned_data['plate'],
#             value = self.cleaned_data['value'],
#             photo = self.cleaned_data['photo'],
#         )
#         car.save()
#         return car

