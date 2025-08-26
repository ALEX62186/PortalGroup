from django.db import models
from django.conf import settings
from django.utils import timezone

class Topic_name(models.Model):
    title = models.CharField(max_length=75)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

class Post(models.Model):
    topic = models.ForeignKey(Topic_name, on_delete=models.CASCADE)
    content = models.TextField()
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    posted_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        permissions = [
            ('can_moderate_posts', 'Can moderate posts'),
        ]