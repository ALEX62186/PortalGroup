from django.urls import path
from . import views

urlpatterns = [
    path('', views.PollListView.as_view(), name='poll_list'),
    path('<int:poll_id>/', views.poll_detail, name='poll_detail'),
    path('<int:poll_id>/vote/', views.vote_poll, name='vote_poll'), 
    path('<int:poll_id>/results/', views.poll_results, name='poll_results'),
    path('create/', views.create_poll, name='create_poll'),
    path('<int:poll_id>/edit/', views.edit_poll, name='edit_poll'),
    path('<int:poll_id>/delete/', views.delete_poll, name='delete_poll'),
]
