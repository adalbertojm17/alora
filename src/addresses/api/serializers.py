from rest_framework.serializers import (
    ModelSerializer
)

from ..models import Address


class AddressSerializer(ModelSerializer):
    class Meta:
        model = Address
        fields = '__all__'

    def create(self, validated_data):
        address_instance = Address.objects.create(
            **validated_data
        )
        return address_instance
