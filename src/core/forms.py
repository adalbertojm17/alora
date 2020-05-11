import datetime

import usps
# noinspection PyUnresolvedReferences
from addresses.models import Address
# noinspection PyUnresolvedReferences
from alora.settings import API_KEY
# noinspection PyUnresolvedReferences
from business.models import Service
# noinspection PyUnresolvedReferences
from business.models import Store
from datetimepicker.widgets import DateTimePicker
from django import forms
from django.core.exceptions import ValidationError
from django.utils.timezone import now
from localflavor.us.forms import USStateField, USZipCodeField
from localflavor.us.us_states import STATE_CHOICES


class StoreForm(forms.Form):
    store = forms.ModelChoiceField(
        empty_label='Choose a Store',
        label='',
        required=True,
        queryset=Store.objects.all()
    )


class PickupForm(forms.ModelForm):
    street = forms.CharField(
        label='',
        max_length=120,
        widget=forms.TextInput(attrs={'placeholder': 'Street*'})
    )
    apt = forms.CharField(
        label='',
        required=False,
        max_length=50,
        widget=forms.TextInput(attrs={'placeholder': 'APT/Suite', 'pattern': '[0-9A-Za-z ]+',
                                      'title': ' alphanumeric '
                                               'characters '
                                               'only '
                                               'please'})

    )
    city = forms.CharField(
        label='',
        max_length=120,
        widget=forms.TextInput(attrs={'placeholder': 'City*'})

    )
    MODDED_STATE_CHOICES = list(STATE_CHOICES)
    MODDED_STATE_CHOICES.insert(0, ('', 'Select a State'))
    state = USStateField(
        label='',
        widget=forms.Select(choices=MODDED_STATE_CHOICES))

    zip_code = USZipCodeField(
        label='',
        widget=forms.TextInput(attrs={'placeholder': 'Zip Code*', 'pattern': '[0-9]+',
                                      'title': ' numeric '
                                               'characters '
                                               'only '
                                               'please'})
    )
    pickup_at = forms.DateTimeField(
        input_formats=("%a %b %d, %Y %I:%M %p",),
        localize=True,
        label='',
        widget=DateTimePicker(
            options={
                'validateOnBlur': False,
                'twelveHoursFormat': True,
                'format': 'D M d, Y g:i a',
                'formatTime': 'g:i a',
                'lang': 'en-us',
                'minDate': 0,
                'maxDate': '+1970/01/15'
            }
        )
    )

    class Meta:
        model = Address
        fields = '__all__'

    def clean(self):
        cleaned_data = super(PickupForm, self).clean()
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

        if address_data is not None:
            if 'Error' in address_data:
                error = address_data['Error']

                if error['Description'] == 'Address Not Found.':
                    raise forms.ValidationError("Please provide a valid address.")

            elif 'ReturnText' in address_data:
                return_text = address_data['ReturnText']

                if 'Default address' in return_text:
                    raise forms.ValidationError("A valid APT/Suite is required for this address")

            cleaned_data['street'] = address.address_2.title()
            cleaned_data['apt'] = address.address_1
            cleaned_data['city'] = address.city.title()
            cleaned_data['zip_code'] = address.zipcode
        return cleaned_data

    def clean_pickup_at(self):
        cleaned_data = super(PickupForm, self).clean()
        pickup_date = cleaned_data['pickup_at']

        if pickup_date < (now() + datetime.timedelta(days=0, hours=1, minutes=0)):
            raise ValidationError("Pick-up date/time must not be earlier than 1 hour from now.")
        if pickup_date > (now() + datetime.timedelta(days=15, hours=11, minutes=59)):
            raise ValidationError("Pick-up date/time can be at latest 15 days from now")
        return pickup_date


class DropOffForm(forms.ModelForm):
    street = forms.CharField(
        label='',
        max_length=120,
        widget=forms.TextInput(attrs={'placeholder': 'Street*'})
    )
    apt = forms.CharField(
        label='',
        required=False,
        max_length=30,
        widget=forms.TextInput(attrs={'placeholder': 'APT/Suite', 'pattern': '[0-9A-Za-z ]+',
                                      'title': ' alphanumeric '
                                               'characters '
                                               'only '
                                               'please'})
    )
    city = forms.CharField(
        label='',
        max_length=120,
        widget=forms.TextInput(attrs={'placeholder': 'City*'})

    )
    MODDED_STATE_CHOICES = list(STATE_CHOICES)
    MODDED_STATE_CHOICES.insert(0, ('', 'Select a State'))
    state = USStateField(
        label='',
        widget=forms.Select(choices=MODDED_STATE_CHOICES))

    zip_code = USZipCodeField(
        label='',
        widget=forms.TextInput(attrs={'placeholder': 'Zip Code*', 'pattern': '[0-9]+',
                                      'title': ' numeric '
                                               'characters '
                                               'only '
                                               'please'})
    )
    drop_off_at = forms.DateTimeField(
        input_formats=("%a %b %d, %Y %I:%M %p",),
        localize=True,
        label='',
        initial=None,
        widget=DateTimePicker(
            options={
                'validateOnBlur': False,
                'twelveHoursFormat': True,
                'format': 'D M d, Y g:i a',
                'formatTime': 'g:i a',
                'language': 'en-us',
                'minDate': '-1970/01/02',
                'maxDate': '+1970/01/16'
            },
        )
    )

    class Meta:
        model = Address
        fields = '__all__'

    def clean(self):
        cleaned_data = super(DropOffForm, self).clean()
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

    def clean_drop_off_at(self):
        cleaned_data = super(DropOffForm, self).clean()
        min_date_limit = self.initial['context']['pickup_date'] + datetime.timedelta(days=1)
        max_date_limit = self.initial['context']['pickup_date'] + datetime.timedelta(days=15)
        dropoff_date = cleaned_data['drop_off_at']

        if dropoff_date < min_date_limit:
            raise ValidationError("Drop-off date/time must not be earlier than 1 day after the Pick-up date/time")
        if dropoff_date > max_date_limit:
            raise ValidationError("Drop-off date/time can be at latest 15 days from the Pick-up date/time")
        return dropoff_date
