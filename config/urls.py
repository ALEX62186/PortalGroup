from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # Админка
    path('admin/', admin.site.urls),

    # Главная страница
    path('', TemplateView.as_view(template_name='home.html'), name='home'),

    # Аутентификация
    path('accounts/login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('accounts/logout/', auth_views.LogoutView.as_view(next_page='/'), name='logout'),
    path('accounts/', include('django.contrib.auth.urls')),

    # Приложения
    path('events/', include('events.urls')),       # События
    path('polls/', include('polls.urls')),         # Опросы
    path('materials/', include('materials.urls')), # Материалы
    path('diary/', include('diary.urls')),       # Электронный дневник (новое)
]

# Подключаем статику/медиа в режиме разработки
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
