from django import forms
from .models import Topic_name, Post

class TopicForm(forms.ModelForm):
    content = forms.CharField(widget=forms.Textarea, label="Повідомлення")

    class Meta:
        model = Topic_name
        fields = ['title']

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['content']