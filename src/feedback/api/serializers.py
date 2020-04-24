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

from ..models import Feedback


class FeedbackSerializer(ModelSerializer):
    class Meta:
        model = Feedback
        fields = '__all__'

    def create(self, validated_data):
        user = validated_data['user']
        store = validated_data['store']
        subject = validated_data['subject']
        content = validated_data['content']
        feedback_obj = Feedback(
            user=user,
            store=store,
            subject=subject,
            content=content,
        )
        feedback_obj.save()
        return validated_data
