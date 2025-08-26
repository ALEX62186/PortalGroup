from django.urls import path
from .views import forum_home
from .views import TreadListView, TreadCreateView

app_name = 'forum'

urlpatterns = [
    path('', forum_home, name='forum'),
    path('', TreadListView.as_view(), name='tread_list'),
    path('create/', TreadCreateView.as_view(), name='tread_create'),
]