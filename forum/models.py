from django.db import models
from django.conf import settings
from django.utils import timezone

class Topic_name(models.Model):
    title = models.CharField(max_length=75)
    description = models.TextField()
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
