from rest_framework.authentication import TokenAuthentication
from rest_framework.generics import (
    CreateAPIView
)
from rest_framework.permissions import AllowAny

from .serializers import (
    FeedbackSerializer
)
from ..models import Feedback


class SendFeedbackAPIView(CreateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [AllowAny]
    serializer_class = FeedbackSerializer
    queryset = Feedback.objects.all()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
