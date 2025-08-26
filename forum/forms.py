from django import forms
from .models import Topic_name

class TopicForm(forms.ModelForm):

    class Meta:
        model = Topic_name
        fields = ['title', 'description']
