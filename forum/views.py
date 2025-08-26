from django.shortcuts import render
from django.views.generic import ListView, CreateView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .models import Topic_name, Post
from .forms import TopicForm, PostForm

def forum_home(request):
    topics = Topic_name.objects.all()
    return render(request, 'forum/forum.html', {'topics': topics})


class ThreadListView(ListView):
    model = Topic_name
    template_name = 'forum/forum.html'
    context_object_name = 'topics'  # Виправлено: узгоджено з forum.html
    ordering = ['-created_at']  # Виправлено: використовуємо created_at

class ThreadCreateView(LoginRequiredMixin, CreateView):
    model = Topic_name  # Виправлено: створюємо тему
    form_class = TopicForm
    template_name = 'forum/create_topic.html'
    success_url = reverse_lazy('forum:forum')

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)