from django import forms
from .models import Materials

class MaterialForm(forms.ModelForm):
    class Meta:
        model = Materials
        fields = ['title', 'type', 'file']
