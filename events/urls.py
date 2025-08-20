from django.urls import path
from .views import EventListView, EventCreateView

urlpatterns = [
    path('', EventListView.as_view(), name='event_list'),  # список событий
    path('new/', EventCreateView.as_view(), name='event_create'),  # добавить событие
]
