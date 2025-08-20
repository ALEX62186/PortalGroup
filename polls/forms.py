from django import forms
from .models import Poll, Choice
from django.forms import modelformset_factory

class PollForm(forms.ModelForm):
    class Meta:
        model = Poll
        fields = ['question']

class ChoiceForm(forms.ModelForm):
    class Meta:
        model = Choice
        fields = ['text']

# Formset для вариантов
ChoiceFormSet = modelformset_factory(Choice, form=ChoiceForm, extra=1)
