from django.urls import path

from .views import (
    SendFeedbackAPIView,
)

urlpatterns = [
    path('send-feedback/', SendFeedbackAPIView.as_view(), name='api-send-fedback'),
]
