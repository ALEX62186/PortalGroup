from django import forms
from .models import Topic_name, Comment

class TopicForm(forms.ModelForm):

    class Meta:
        model = Topic_name
        fields = ['title', 'description']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
        widgets = {
            'content': forms.Textarea(attrs={'rows': 3, 'placeholder': 'Напиши коментар...'}),
        }