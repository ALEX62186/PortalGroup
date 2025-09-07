from django import forms
from .models import Galerys
class GaleryForm(forms.ModelForm):
    class Meta:
        model = Galerys
        fields = ['title', 'type', 'file']
