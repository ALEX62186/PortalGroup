from django.urls import path
from .views import advert_view, AdvertCreateView, delete_advert_view

app_name = 'advert'

urlpatterns = [
    path('', advert_view, name='advert'),
    path('create/', AdvertCreateView.as_view(), name='create'),
    path('<int:topic_id>/delete/', delete_advert_view, name='delete')
]