from django.contrib import admin
from .models import Poll  # и любые другие модели

admin.site.register(Poll)