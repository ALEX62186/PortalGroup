from .models import Advertisement
from django import forms

class AdvertForm(forms.ModelForm):

    class Meta:
        model = Advertisement
        fields = ['title', 'description']