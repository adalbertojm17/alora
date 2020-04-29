# noinspection PyUnresolvedReferences
from business.models import Service
from rest_framework.serializers import (
    ModelSerializer
)

from ..models import Store

from addresses.api.serializers import AddressSerializer



class StoreSerializer(ModelSerializer):
    address = AddressSerializer()

    class Meta:
        model = Store
        exclude = ['manager']


class ServiceDetailSerializer(ModelSerializer):
    store = StoreSerializer()

    class Meta:
        model = Service
        fields = ('id', 'name', 'store')
