from django import forms
from .models import Plant, Remedies


class PlantForm(forms.ModelForm):
    class Meta:
        model = Plant
        fields = ['user', 'image']

