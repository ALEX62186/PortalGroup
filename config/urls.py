
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from django.contrib.auth import views as auth_views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('polls/admin/', admin.site.urls),
    path('events/', include('events.urls')),
    path('polls/', include('polls.urls')),
    path('', include('home.urls', namespace='main')),
    path('forum/', include('forum.urls', namespace='forum')),
    path('accounts/', include('accounts.urls')),
]