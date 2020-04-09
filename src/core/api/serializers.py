import abc
from abc import ABC

# noinspection PyUnresolvedReferences
from accounts.models import Account
# noinspection PyUnresolvedReferences
from addresses.models import Address
# noinspection PyUnresolvedReferences
from business.models import Service, Store
# noinspection PyUnresolvedReferences,PyPackageRequirements
from core.models import Order
from localflavor.us.forms import USStateField, USZipCodeField
from localflavor.us.us_states import STATE_CHOICES
from rest_framework.fields import CharField, DateTimeField
from rest_framework.generics import get_object_or_404
from rest_framework.serializers import (
    Serializer,
    ChoiceField
)


class OrderSerializer(Serializer):
    store = ChoiceField(choices=[(store.id, store.name) for store in Store.objects.all()])
    pickup_street = CharField(
        max_length=120, )

    pickup_apt = CharField(
        required=False,
        max_length=50, )

    pickup_city = CharField(
        max_length=120, )

    MODDED_STATE_CHOICES = list(STATE_CHOICES)
    MODDED_STATE_CHOICES.insert(0, ('', 'Select a State'))
    pickup_state = USStateField()
    pickup_zip_code = USZipCodeField()
    pickup_at = DateTimeField(
        input_formats=("%B %d, %Y %I:%M %p",)
    )
    dropoff_street = CharField(
        max_length=120, )

    dropoff_apt = CharField(
        required=False,
        max_length=50, )

    dropoff_city = CharField(
        max_length=120, )

    MODDED_STATE_CHOICES = list(STATE_CHOICES)
    MODDED_STATE_CHOICES.insert(0, ('', 'Select a State'))
    dropoff_state = USStateField()
    dropoff_zip_code = USZipCodeField()
    dropoff_at = DateTimeField(
        input_formats=("%B %d, %Y %I:%M %p",)
    )

    class Meta(abc.ABCMeta):
        model = Address
        fields = '__all__'
