from rest_framework.authentication import TokenAuthentication
from rest_framework.generics import (
    ListAPIView,
    CreateAPIView
)
from rest_framework.permissions import (
    IsAuthenticated, AllowAny)
from rest_framework.response import Response

from .permissions import IsOwner
from .serializers import (
    OrderSerializer
)
from ..models import Order


class CreateOrderAPIView(CreateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [AllowAny]
    serializer_class = OrderSerializer
    queryset = Order.objects.all()


class DisplayOrderAPIView(ListAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsOwner]
    serializer_class = OrderSerializer

    def get(self, request, *args, **kwargs):
        return Order.objects.all().filter(user_id=request.user.id)
