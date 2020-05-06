from rest_framework.authentication import TokenAuthentication
from rest_framework.generics import (
    CreateAPIView,
    RetrieveUpdateAPIView,
)
from rest_framework.response import Response

from .serializers import AddressSerializer
from ..models import Address


class CreateAddressAPIView(CreateAPIView):
    authentication_classes = [TokenAuthentication]
    serializer_class = AddressSerializer

    def perform_create(self, serializer):
        address = serializer.save()
        user = self.request.user
        user.address_id = address.id
        user.save()


class AddressAPIView(RetrieveUpdateAPIView):
    authentication_classes = [TokenAuthentication]
    queryset = Address.objects.all()
    serializer_class = AddressSerializer

    def get_queryset(self):
        user = self.request.user
        return Address.objects.all().filter(pk=user.address_id)

    def get_object(self):
        queryset = self.filter_queryset(self.get_queryset())
        obj = queryset.get(pk=self.request.user.address_id)
        self.check_object_permissions(self.request, obj)
        return obj

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.name = request.data.get("name")
        instance.save()

        serializer = self.serializer_class(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        return Response(serializer.data)
