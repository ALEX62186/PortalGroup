from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('announcements.urls')),
    path('login/', auth_views.LoginView.as_view(template_name='announcements/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='main_menu'), name='logout'),
    path('', views.main_menu, name='main_menu'),
    path('announcements/', views.announcement_list, name='announcement_list'),
    path('announcements/create/', views.announcement_create, name='announcement_create'),
    path('announcements/<int:pk>/edit/', views.announcement_edit, name='announcement_edit'),
    path('announcements/<int:pk>/delete/', views.announcement_delete, name='announcement_delete'),
]