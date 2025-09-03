from django.conf import settings
from django.db import models

class Portfolio(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="portfolios"
    )
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    screenshot = models.ImageField(
        upload_to="portfolio_screenshots/",  
        blank=True,
        null=True
    )
    file = models.FileField(
        upload_to="portfolio_files/",       
        blank=True,
        null=True
    )
    link = models.URLField(blank=True, null=True)

    # Дата создания и обновления
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
