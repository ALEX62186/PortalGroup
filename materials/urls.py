# materials/urls.py
# materials/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.materials_list, name='materials_list'),
    path('add/', views.material_add, name='material_add'),
    path('edit/<int:pk>/', views.material_edit, name='material_edit'),
    path('delete/<int:pk>/', views.material_delete, name='material_delete'),
]


