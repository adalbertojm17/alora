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
    ModelSerializer,
    ChoiceField
)

from ..models import Feedback


class FeedbackSerializer(ModelSerializer):
    class Meta:
        model = Feedback
        fields = '__all__'
