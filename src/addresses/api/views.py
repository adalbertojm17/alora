from rest_framework import status
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.generics import (
    CreateAPIView,
    RetrieveUpdateAPIView,
)
from rest_framework.response import Response

from .permissions import (
    IsOwner,
)

from .serializers import AddressSerializer
from ..models import Address


class CreateAddressAPIView(CreateAPIView):
    authentication_classes = [TokenAuthentication]
    serializer_class = AddressSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)

        return Response(
            status=status.HTTP_201_CREATED,
            headers=headers)


class AddressAPIView(RetrieveUpdateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsOwner]
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
        serializer = self.serializer_class(request.user, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
