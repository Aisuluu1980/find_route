from django import forms

from cities.models import City
from routes.models import Route


class RouteForm(forms.Form):
    # name = forms.CharField(label='Поезд', widget=forms.TextInput(attrs={'class': 'form-control js-example-basic-single','placeholder': 'Введите номер поезда'}))

    from_city = forms.ModelChoiceField(label='Откуда', queryset=City.objects.all(), widget=forms.Select(attrs={'class': 'form-control js-example-basic-single'}))
    to_city = forms.ModelChoiceField(label='Куда', queryset=City.objects.all(),widget=forms.Select(attrs={'class': 'form-control js-example-basic-single'}))
    cities = forms.ModelMultipleChoiceField(label='Через города', queryset=City.objects.all(), required=False, widget=forms.SelectMultiple(attrs={
        'class': 'form-control js-example-basic-multiple'}))
    traveling_time = forms.IntegerField(label='Время в пути', widget=forms.NumberInput(
        attrs={'class': 'form-control', 'placeholder': 'Время в пути'}))
    # class Meta:
    #     model = Route
    #     fields = '__all__'   #все поля для редактирования