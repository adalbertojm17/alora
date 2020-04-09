from rest_framework.generics import (
    ListAPIView,
    CreateAPIView
)
from rest_framework.permissions import (
    IsAuthenticated)
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST

from .permissions import IsOwner
from .serializers import (
    OrderSerializer
)
from ..models import Order


class CreateOrderAPIView(CreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = OrderSerializer

    def post(self, request, *args, **kwargs):
        data = request.data
        serializer = OrderSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            new_data = serializer.data
            return Response(new_data, status=HTTP_200_OK)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)


class DisplayOrderAPIView(ListAPIView):
    permission_classes = [IsOwner]
    serializer_class = OrderSerializer

    def get(self, request, *args, **kwargs):
        return Order.objects.all().filter(account_id=request.user.id)
