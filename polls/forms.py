from django import forms
from django.forms import inlineformset_factory
from django.views.generic import ListView

from .models import Poll, Choice

class PollForm(forms.ModelForm):
    class Meta:
        model = Poll
        fields = ['title', 'poll_type']

class ChoiceForm(forms.ModelForm):
    class Meta:
        model = Choice
        fields = ['text']
        
class PollListView(ListView):
    model = Poll
    template_name = 'polls/poll_list.html'
    context_object_name = 'polls'        

# InlineFormSet (будет использоваться в views)
ChoiceFormSet = inlineformset_factory(
    Poll, Choice, form=ChoiceForm, extra=2, can_delete=True
)
