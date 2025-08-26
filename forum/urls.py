from django.urls import path
from .views import forum_home
from .views import ThreadListView, ThreadCreateView

app_name = 'forum'

urlpatterns = [
    path('', forum_home, name='forum'),
    # path('', TreadListView.as_view(), name='tread_list'),
    path('create/', ThreadCreateView.as_view(), name='thread_create'),
]