from django import forms
from .models import Poll, Choice
from django.forms import inlineformset_factory

class PollForm(forms.ModelForm):
    class Meta:
        model = Poll
        fields = ['title']  
class ChoiceForm(forms.ModelForm):
    class Meta:
        model = Choice
        fields = ['text']


ChoiceFormSet = inlineformset_factory(
    Poll, Choice, form=ChoiceForm, extra=1, can_delete=True
)
