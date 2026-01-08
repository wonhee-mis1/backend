from django.db import models
from django.contrib.auth.models import User
class DiaryEntry(models.Model):
  user = models.ForeignKey(
    User,
    on_delete=models.CASCADE,
    related_name="diary_entries"
  )
  entry_date = models.DateField()
  content = models.TextField()

  # AI 결과 (일단 null 허용)
  emotion_label = models.CharField(max_length=20, null=True, blank=True)
  sentiment_score = models.FloatField(null=True, blank=True)

  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

  def __str__(self):
    return f"{self.user.username} - {self.entry_date}"