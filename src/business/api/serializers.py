# noinspection PyUnresolvedReferences
from addresses.api.serializers import AddressSerializer
from business.models import Service
from rest_framework.serializers import (
    ModelSerializer
)

from ..models import Store, ServingAreas


class ServingAreaSerializer(ModelSerializer):
    class Meta:
        model = ServingAreas
        fields = '__all__'


class StoreSerializer(ModelSerializer):
    address = AddressSerializer()
    serving_areas = ServingAreaSerializer(read_only=True, many=True)

    class Meta:
        model = Store
        exclude = ['manager']


class ServiceDetailSerializer(ModelSerializer):
    store = StoreSerializer()

    class Meta:
        model = Service
        fields = ('id', 'name', 'store')
