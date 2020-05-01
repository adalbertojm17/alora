from cities_light.models import Region
from rest_framework.authentication import TokenAuthentication
from rest_framework.generics import (
    ListAPIView,
    CreateAPIView
)
from rest_framework.response import Response

from .permissions import IsOwner
from .serializers import (
    PlaceOrderSerializer,
    OrderDetailSerializer,
    RegionSerializer,
    ItemSerializer
)
from ..models import Order, Item


class PlaceOrderAPIView(CreateAPIView):
    authentication_classes = [TokenAuthentication]
    serializer_class = PlaceOrderSerializer
    queryset = Order.objects.all()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class ItemListAPIView(ListAPIView):
    authentication_classes = [TokenAuthentication]
    queryset = Item.objects.all().order_by('name')
    serializer_class = ItemSerializer


class DisplayOrderAPIView(ListAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsOwner]
    serializer_class = OrderDetailSerializer

    def get_queryset(self):
        user = self.request.user
        return Order.objects.all().filter(user_id=user.id)


class RegionListAPIView(ListAPIView):
    authentication_classes = [TokenAuthentication]
    queryset = Region.objects.all().order_by('name')
    serializer_class = RegionSerializer

    def __init__(self, **kwargs):
        super(RegionListAPIView).__init__(**kwargs)
        self.object_list = self.filter_queryset(self.get_queryset())

    def list(self, request, *args, **kwargs):
        serializer = self.get_serializer(self.object_list, many=True)
        return Response({'data': serializer.data})
