from django.urls import path
from .views import EventListView, EventCreateView, event_detail, edit_event, delete_event

urlpatterns = [
    path('', EventListView.as_view(), name='event_list'),
    path('create/', EventCreateView.as_view(), name='create_event'),
    path('<int:event_id>/edit/', edit_event, name='edit_event'),
    path('<int:event_id>/delete/', delete_event, name='delete_event'),
]
