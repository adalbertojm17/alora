# noinspection PyUnresolvedReferences
from accounts.api.serializers import UserProfileSerializer
from addresses.api.serializers import AddressSerializer
# noinspection PyUnresolvedReferences
from addresses.models import Address
# noinspection PyUnresolvedReferences
from business.api.serializers import ServiceDetailSerializer
from business.api.serializers import StoreSerializer
# noinspection PyUnresolvedReferences
from business.models import Service, Store
from cities_light.models import Region
# noinspection PyUnresolvedReferences,PyPackageRequirements
from core.models import Item
# noinspection PyUnresolvedReferences,PyPackageRequirements
from core.models import Order
from rest_framework.serializers import (
    ModelSerializer
)


# noinspection PyCompatibility
class OrderDetailSerializer(ModelSerializer):
    store = StoreSerializer()
    pickup_location = AddressSerializer()
    dropoff_location = AddressSerializer()

    class Meta:
        model = Order
        fields = (
            'id', 'pickup_location', 'dropoff_location', 'store',
            'user', 'pickup_at', 'current_status', 'dropoff_at', 'created_at'
        )

    def _user(self, obj):
        request = getattr(self.context, 'request', None)
        if request:
            return request.user


# noinspection PyCompatibility
class PlaceOrderSerializer(ModelSerializer):
    pickup_location = AddressSerializer()
    dropoff_location = AddressSerializer()

    class Meta:
        model = Order
        fields = (
            'id', 'pickup_location', 'dropoff_location', 'store',
            'user', 'pickup_at', 'current_status', 'dropoff_at', 'created_at'
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


class RegionSerializer(ModelSerializer):
    class Meta:
        model = Region
        fields = '__all__'


class ItemSerializer(ModelSerializer):
    services = ServiceDetailSerializer()

    class Meta:
        model = Item
        fields = ('id', 'name', 'services', 'price')


class AddressValidationSerializer(ModelSerializer):
    def clean(self):
        cleaned_data = super(UserAddressForm, self).clean()
        address = usps.Address(
            name='None',
            address_2=cleaned_data.get('street'),
            address_1=cleaned_data.get('apt'),
            city=cleaned_data.get('city'),
            state=cleaned_data.get('state'),
            zipcode=cleaned_data.get('zip_code')
        )

        try:
            validator = usps.USPSApi('161ALORA3737', test=True)
            validation = validator.validate_address(address)
        except usps.USPSApiError:
            raise forms.ValidationError("Please provide a valid address.")

        address_data = validation.result['AddressValidateResponse']['Address']

        print(address_data)

        if address_data is not None:

            if 'Error' in address_data:
                raise forms.ValidationError("Please provide a valid address.")

            elif 'ReturnText' in address_data:
                return_text = address_data['ReturnText']

                if 'Default address' in return_text:
                    raise forms.ValidationError("A valid APT/Suite is required for this address.")
            cleaned_data['street'] = address.address_2.title()
            cleaned_data['apt'] = address.address_1
            cleaned_data['city'] = address.city.title()
            cleaned_data['zip_code'] = address.zipcode
            return cleaned_data
