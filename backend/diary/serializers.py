from rest_framework import serializers
from .models import EmotionRecord

class EmotionRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmotionRecord
        fields = ['id', 'text', 'emotions', 'top_emotion', 'created_at']
        read_only_fields = ['id', 'created_at']