# noinspection PyUnresolvedReferences
from business.models import Service
from rest_framework.serializers import (
    ModelSerializer
)

from ..models import Store


class ServiceDetailSerializer(ModelSerializer):
    class Meta:
        model = Service
        fields = '__all__'


class StoreSerializer(ModelSerializer):
    class Meta:
        model = Store
        fields = '__all__'


