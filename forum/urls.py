from django.urls import path
from .views import forum_home
from forum import views
from .views import ThreadListView, ThreadCreateView, topic_detail

app_name = 'forum'

urlpatterns = [
    path('', forum_home, name='forum'),
    path('', ThreadListView.as_view(), name='tread_list'),
    path('create/', ThreadCreateView.as_view(), name='thread_create'),
    path('<int:topic_id>/', topic_detail, name='thread_detail'),
    path('<int:topic_id>/delete/', views.delete_thread_view, name='delete_thread')
]