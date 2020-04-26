import datetime

# noinspection PyUnresolvedReferences
from addresses.models import Address
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
from pygeocoder import Geocoder
# noinspection PyUnresolvedReferences
from alora.settings import API_KEY

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
        widget=forms.TextInput(attrs={'placeholder': 'APT/Suite','pattern': '[0-9A-Za-z ]+',
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
        widget=forms.TextInput(attrs={'placeholder': 'Zip Code*'})
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
            }
        )
    )

    class Meta:
        model = Address
        fields = '__all__'
    def clean(self):
        cleaned_data = super(PickupForm, self).clean()
        address_validation = Geocoder(api_key=API_KEY)
        address = str(cleaned_data.get('street') + ", " + str(cleaned_data.get('city')) + ", " + str(
        cleaned_data.get('state')) + ", " + str(cleaned_data.get('zip_code')) + 'US')
        if not address_validation.geocode(address).valid_address:
            raise forms.ValidationError("Address is not valid")
        else:
            address = address_validation.geocode(address)
            cleaned_data['street'] = address.street_number +' '+ address.route
            cleaned_data['city'] = address.city
            cleaned_data['zip_code'] = address.postal_code
            return cleaned_data



    def clean_pickup_at(self):
        cleaned_data = super(PickupForm, self).clean()
        pickup_date = cleaned_data['pickup_at']

        if pickup_date < (now() + datetime.timedelta(days=0, hours=1, minutes=0)):
            raise ValidationError("Pick-up date/time must not be earlier than 1 hour from now.")
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
        widget=forms.TextInput(attrs={'placeholder': 'APT/Suite','pattern': '[0-9A-Za-z ]+',
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
        widget=forms.TextInput(attrs={'placeholder': 'Zip Code*'})
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
            },
        )
    )

    class Meta:
        model = Address
        fields = '__all__'

    def clean(self):
        cleaned_data = super(DropOffForm, self).clean()
        address_validation = Geocoder(api_key=API_KEY)
        address = str(cleaned_data.get('street') + ", " + str(cleaned_data.get('city')) + ", " + str(
            cleaned_data.get('state')) + ", " + str(cleaned_data.get('zip_code')) + 'US')
        if not address_validation.geocode(address).valid_address:
            raise ValidationError("Address is not valid")
        else:
            address = address_validation.geocode(address)
            cleaned_data['street'] = address.street_number + ' ' + address.route
            cleaned_data['city'] = address.city
            cleaned_data['zip_code'] = address.postal_code
            return cleaned_data

    def clean_drop_off_at(self):
        cleaned_data = super(DropOffForm, self).clean()
        date_limit = self.initial['context']['pickup_date'] + datetime.timedelta(days=1)
        dropoff_date = cleaned_data['drop_off_at']

        if dropoff_date < date_limit:
            raise ValidationError("Drop-off date/time must not be earlier than 1 day after the Pick-up date/time")
        return dropoff_date
