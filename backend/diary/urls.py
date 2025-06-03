from django.urls import path
from .views import EmotionRecordCreateView

urlpatterns = [
    path('emotion/', EmotionRecordCreateView.as_view(), name='emotion-create'),
]