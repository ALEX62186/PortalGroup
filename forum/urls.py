from django.urls import path
from .views import forum_home
from forum import views
from .views import ThreadListView, ThreadCreateView, thread_detail_view

app_name = 'forum'

urlpatterns = [
    path('', forum_home, name='forum'),
    path('', ThreadListView.as_view(), name='tread_list'),
    path('create/', ThreadCreateView.as_view(), name='thread_create'),
    path('<int:topic_id>/', thread_detail_view, name='thread_detail')
]