from django import forms
from .models import Places


class AddPlaceForm(forms.ModelForm):
    class Meta:
        model = Places
        fields = ['title', 'description']
