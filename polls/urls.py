from django.urls import path
from . import views

urlpatterns = [
    path('', views.PollListView.as_view(), name='poll_list'),
    path('create/', views.create_poll, name='create_poll'),
    path('add-choice-form/', views.add_choice_form, name='add_choice_form'),
    path('<int:poll_id>/', views.poll_detail, name='poll_detail'),
    path('<int:poll_id>/results/', views.poll_results, name='poll_results'),
    path('<int:poll_id>/edit/', views.edit_poll, name='edit_poll'),
    path('<int:poll_id>/delete/', views.delete_poll, name='delete_poll'),
]