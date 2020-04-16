from rest_framework.authentication import TokenAuthentication
from rest_framework.generics import (
    CreateAPIView
)

from .serializers import (
    FeedbackSerializer
)
from ..models import Feedback


class SendFeedbackAPIView(CreateAPIView):
    authentication_classes = [TokenAuthentication]
    serializer_class = FeedbackSerializer
    queryset = Feedback.objects.all()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
