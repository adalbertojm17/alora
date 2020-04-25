# noinspection PyUnresolvedReferences
from business.models import Service
from rest_framework.fields import CharField
from rest_framework.serializers import (
    ModelSerializer
)

from ..models import Store


class ServiceDetailSerializer(ModelSerializer):
    class Meta:
        model = Service
        fields = ('id', 'name', 'store')


class StoreSerializer(ModelSerializer):

    class Meta:
        model = Store
        exclude = ['manager']
