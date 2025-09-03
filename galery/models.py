from django.db import models
from django.conf import settings
from django.core.validators import FileExtensionValidator
from django.core.exceptions import ValidationError

class Materials(models.Model):
    TYPE_CHOICES = [
        ('image', 'Зображення'),
        ('video', 'Відео'),
    ]

    title = models.CharField(max_length=255)
    type = models.CharField(max_length=10, choices=TYPE_CHOICES)
    file = models.FileField(
        upload_to='materials/',
        blank=True,
        null=True,
        validators=[FileExtensionValidator(allowed_extensions=['jpg', 'webp', 'jpeg', 'png', 'mp4', 'avi', 'mov', 'mkv'])]
    )
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def clean(self):
        if not self.file:
            raise ValidationError(f"Для типу '{self.get_type_display()}' необхідно завантажити файл.")
        if self.type == 'image' and self.file:
            if not any(self.file.name.lower().endswith(ext) for ext in ['jpg', 'webp', 'jpeg', 'png']):
                raise ValidationError("Для типу 'Зображення' дозволені лише файли .jpg, .jpeg, .png.")
        if self.type == 'video' and self.file:
            if not any(self.file.name.lower().endswith(ext) for ext in ['mp4', 'avi', 'mov', 'mkv']):
                raise ValidationError("Для типу 'Відео' дозволені лише файли .mp4, .avi, .mov, .mkv.")

    def __str__(self):
        return self.title