# noinspection PyUnresolvedReferences
from business.models import Service
from rest_framework.serializers import (
    ModelSerializer
)


class ServiceDetailSerializer(ModelSerializer):
    class Meta:
        model = Service
        fields = '__all__'
