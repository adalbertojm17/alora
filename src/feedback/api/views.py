from rest_framework.authentication import TokenAuthentication
from rest_framework.generics import (
    CreateAPIView
)
from rest_framework.permissions import (
    IsAuthenticated)

from .serializers import (
    FeedbackSerializer
)
from ..models import Feedback


class SendFeedbackAPIView(CreateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = FeedbackSerializer
    queryset = Feedback.objects.all()
