from django.contrib.auth.models import User
from django.db import models


class DiaryEntry(models.Model):
  user = models.ForeignKey(
    User,
    on_delete=models.CASCADE,
  )
  entry_date = models.DateField(auto_now_add=True)
  content = models.TextField()

  # AI 결과 (일단 null 허용)
  emotion_label = models.CharField(max_length=20, null=True, blank=True)
  sentiment_score = models.FloatField(null=True, blank=True)

  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

  def __str__(self):
    return f"{self.user.username} - {self.entry_date}"