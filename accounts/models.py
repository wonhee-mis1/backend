from django.conf import settings
from django.db import models

class Profile(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='profile'
    )
    nickname = models.CharField(max_length=30)

    def __str__(self):
        return f'{self.user.username} ({self.nickname})'
