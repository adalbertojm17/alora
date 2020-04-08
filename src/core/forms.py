import datetime

# noinspection PyUnresolvedReferences
from addresses.models import Address
from bootstrap_datepicker_plus import DateTimePickerInput
# noinspection PyUnresolvedReferences
from business.models import Service
# noinspection PyUnresolvedReferences
from business.models import Store
from django import forms
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
        widget=forms.TextInput(attrs={'placeholder': 'APT/Suite'})

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
        input_formats=("%B %d, %Y %I:%M",),
        localize=True,
        label='',
        widget=DateTimePickerInput(
            format="%m%m %d, %Y %I:%M",
            attrs={'placeholder': 'Pickup  Date/Time*'},

        )
    )

    class Meta:
        model = Address
        fields = '__all__'


class DropOffForm(forms.ModelForm):
    street = forms.CharField(
        label='',
        max_length=120,
        widget=forms.TextInput(attrs={'placeholder': 'Street*'})
    )
    apt = forms.CharField(
        label='',
        required=False,
        max_length=50,
        widget=forms.TextInput(attrs={'placeholder': 'APT/Suite'})

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
    dropoff_at = forms.DateTimeField(

        input_formats=("%B %d, %Y %I:%M",),
        label='',
        widget=DateTimePickerInput(
            attrs={
                'placeholder': 'Dropoff Date/Time*',
            },
            format="%m%m %d, %Y %I:%M",
            options={
                'minDate': (datetime.datetime.today() + datetime.timedelta(days=1)).strftime('%Y-%m-%d 00:00:00'),
                'maxDate': (datetime.datetime.today() + datetime.timedelta(days=7)).strftime('%Y-%m-%d 23:59:59'),
            }
        ),
        initial=None
    )

    class Meta:
        model = Address
        fields = '__all__'
