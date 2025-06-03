from rest_framework import generics, permissions
from .models import EmotionRecord
from .serializers import EmotionRecordSerializer


class EmotionRecordCreateView(generics.CreateAPIView):
    serializer_class = EmotionRecordSerializer
    permission_classes = [permissions.IsAuthenticated]


    def perform_create(self, serializer):
        serializer.save(user=self.request.user)