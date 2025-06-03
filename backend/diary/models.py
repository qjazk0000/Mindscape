# backend/diary/models.py

from django.db import models
from django.conf import settings


class EmotionRecord(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="emotions"
    )
    text = models.TextField()
    emotions = models.JSONField()
    top_emotion = models.CharField(max_length=30)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.top_emotion} - {self.created_at.date()}"