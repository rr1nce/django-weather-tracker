from django.forms import ModelForm, TextInput
from .models import City


class CityForm(ModelForm):
    class Meta:
        model = City
        fields = ['name']
        widgets = {'name': TextInput(attrs={'class': 'search', 'id': 'input__search', 'list': 'cities', 'placeholder': 'Enter city...'})}
