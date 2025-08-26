
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from django.contrib.auth import views as auth_views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('polls/admin/', admin.site.urls),
    path('events/', include('events.urls')),
    path('polls/', include('polls.urls')),
    path('accounts/login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('accounts/logout/', auth_views.LogoutView.as_view(next_page='/'), name='logout'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', include('home.urls', namespace='main')),
    path('forum/', include('forum.urls', namespace='forum')),
    path('accounts/', include('accounts.urls')),
]