from django.contrib import admin
from .models import EmotionRecord


@admin.register(EmotionRecord)
class EmotionRecordAdmin(admin.ModelAdmin):
    list_diplay = ("user", "top_emotion", "created_at")
    search_fields = ("user__username", "top_emotion")