from django.shortcuts import render
from django.views.generic import ListView, CreateView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .models import Topic_name, Comment
from .forms import TopicForm, CommentForm
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required


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

@login_required
def thread_detail_view(request, topic_id):
    thread = get_object_or_404(Topic_name, pk=topic_id)
    return render(request, "forum/topic_detail.html", context={"thread": thread})

@staff_member_required
def delete_thread_view(request, topic_id):
    thread = get_object_or_404(Topic_name, pk=topic_id)
    if request.user == thread.created_by:
        thread.delete()
    return redirect('forum:forum')


@login_required
def topic_detail(request, topic_id):
    topic = get_object_or_404(Topic_name, id=topic_id)
    comments = topic.comments.order_by('created_at')
    form = CommentForm()

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.topic = topic
            comment.author = request.user
            comment.save()
            return redirect('forum:thread_detail', topic_id=topic.id)

    return render(request, 'forum/topic_detail.html', {
        'topic': topic,
        'comments': comments,
        'form': form
    })