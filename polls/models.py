from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Poll(models.Model):
    title = models.CharField(max_length=255)
    pub_date = models.DateTimeField(auto_now_add=True)  

    def __str__(self):
        return self.title


class Choice(models.Model):
    poll = models.ForeignKey(Poll, on_delete=models.CASCADE, related_name="choices")
    text = models.CharField(max_length=255)  
    votes = models.PositiveIntegerField(default=0) 
    def __str__(self):
        return self.text


class PollVote(models.Model):
    poll = models.ForeignKey(Poll, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    choice = models.ForeignKey(Choice, on_delete=models.CASCADE)
    voted_at = models.DateTimeField(auto_now_add=True)  
    class Meta:
        unique_together = ('poll', 'user') 
    def __str__(self):
        return f"{self.user.username} voted for '{self.choice.text}' in '{self.poll.title}'"
