from django.forms import ModelForm
from .models import Person

class PersonaForm(ModelForm):
    class Meta:
        model = Person
        fields = '__all__'
