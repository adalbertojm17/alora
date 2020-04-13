# noinspection PyUnresolvedReferences
from accounts.models import Account
# noinspection PyUnresolvedReferences
from addresses.models import Address
# noinspection PyUnresolvedReferences
from business.models import Service, Store
# noinspection PyUnresolvedReferences,PyPackageRequirements
from core.models import Order
from rest_framework.serializers import (
    ModelSerializer
)


class AddressSerializer(ModelSerializer):
    class Meta:
        model = Address
        fields = '__all__'

    def create(self, validated_data):
        address_instance = Address.objects.create(
            **validated_data
        )
        return address_instance


# noinspection PyCompatibility
class OrderSerializer(ModelSerializer):
    pickup_location = AddressSerializer()
    dropoff_location = AddressSerializer()

    class Meta:
        model = Order
        fields = (
            'pickup_location', 'dropoff_location', 'store',
            'account', 'pickup_at', 'dropoff_at'
        )

    def _user(self, obj):
        request = getattr(self.context, 'request', None)
        if request:
            return request.user

    def create(self, validated_data):
        pickup_location_data = validated_data.pop('pickup_location')
        dropoff_location_data = validated_data.pop('dropoff_location')
        if pickup_location_data:
            pickup_location = Address.objects.get_or_create(**pickup_location_data)[0]
            validated_data['pickup_location'] = pickup_location

        if dropoff_location_data:
            dropoff_location = Address.objects.get_or_create(**dropoff_location_data)[0]
            validated_data['dropoff_location'] = dropoff_location

        return Order.objects.create(
            **validated_data
        )
