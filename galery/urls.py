from django.urls import path
from . import views

urlpatterns = [
    path('', views.galery_list, name='galery_list'),
    path('add/', views.galery_add, name='galery_add'),
    path('edit/<int:pk>/', views.galery_edit, name='galery_edit'),
    path('delete/<int:pk>/', views.galery_delete, name='galery_delete'),
]


