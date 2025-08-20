from django.views.generic import ListView, CreateView
from django.shortcuts import render, redirect, get_object_or_404
from .models import Topic_name, Post
from .forms import TopicForm, PostForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin


def forum_home(request):
    topics = Topic_name.objects.all()
    return render(request, 'forum/forum.html', {'topics': topics})


class TreadListView(ListView):
    model = Topic_name
    template_name = 'forum/forum.html'
    contex_object_name = 'forum'
    ordering = ['start_time']


class TreadCreateView(LoginRequiredMixin, CreateView):
    model = Post
    template_name = 'forum/create_topic.html'
