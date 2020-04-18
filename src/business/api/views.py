from rest_framework.authentication import TokenAuthentication, SessionAuthentication
from rest_framework.generics import (
    ListAPIView,
)
from rest_framework.permissions import (
    IsAuthenticated)
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import (
    ServiceDetailSerializer,
    StoreSerializer,
)
from ..models import Service, Store


class StoreListAPIView(ListAPIView):
    authentication_classes = [TokenAuthentication]
    queryset = Store.objects.all().order_by('name')
    serializer_class = StoreSerializer

    def __init__(self, **kwargs):
        super(StoreListAPIView).__init__(**kwargs)
        self.object_list = self.filter_queryset(self.get_queryset())

    def list(self, request, *args, **kwargs):
        serializer = self.get_serializer(self.object_list, many=True)
        return Response({'data': serializer.data})


class ServiceListAPIView(ListAPIView):
    authentication_classes = [TokenAuthentication]
    queryset = Service.objects.all().order_by('name')
    serializer_class = ServiceDetailSerializer


class ServiceDetailAPIView(APIView):
    authentication_classes = [TokenAuthentication]
    queryset = Service.objects.all()
    serializer_class = ServiceDetailSerializer
