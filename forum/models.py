from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Topic_name(models.Model):
    title = models.CharField(max_length=75)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)


class Post(models.Model):
    topic = models.ForeignKey(Topic_name, on_delete=models.CASCADE)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    posted_at = models.DateTimeField(auto_now_add=True)
