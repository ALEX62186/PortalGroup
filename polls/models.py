from django.db import models
from django.contrib.auth.models import User

class Poll(models.Model):
    SINGLE = "single"
    MULTIPLE = "multiple"
    POLL_TYPE_CHOICES = [
        (SINGLE, "Один вариант"),
        (MULTIPLE, "Несколько вариантов"),
    ]

    title = models.CharField(max_length=255, verbose_name="Название опроса")
    poll_type = models.CharField(
        max_length=10,
        choices=POLL_TYPE_CHOICES,
        default=SINGLE,
        verbose_name="Тип опроса"
    )
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Создатель")
    pub_date = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")

    def __str__(self):
        return self.title


class Choice(models.Model):
    poll = models.ForeignKey(Poll, on_delete=models.CASCADE, related_name="choices")
    text = models.CharField(max_length=255, verbose_name="Вариант ответа")
    votes = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.text} ({self.poll.title})"


class PollVote(models.Model):
    poll = models.ForeignKey(Poll, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    choice = models.ForeignKey(Choice, on_delete=models.CASCADE)
    voted_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ("poll", "user", "choice")
