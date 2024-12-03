from django import forms
from .models import Car, Service


class CarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = ['car_model', 'category']


class ServiceForm(forms.ModelForm):
    class Meta:
        model = Service
        fields = ['service_name', 'price_small', 'price_medium', 'price_big']
