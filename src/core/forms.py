import datetime

# noinspection PyUnresolvedReferences
from addresses.models import Address
from bootstrap_datepicker_plus import DateTimePickerInput
# noinspection PyUnresolvedReferences
from business.models import Service
# noinspection PyUnresolvedReferences
from business.models import Store
from django import forms
from django.core.exceptions import ValidationError
from localflavor.us.forms import USStateField, USZipCodeField
from localflavor.us.us_states import STATE_CHOICES
from cities_light.models import Region


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
        input_formats=("%a %B %d, %Y %I:%M %p",),
        localize=True,
        label='',
        widget=DateTimePickerInput(
            format="ddd %m%m %d, %Y %I:%M A",
            attrs={'placeholder': 'Pickup  Date/Time*'},
            options={
                'locale': 'en',
                'minDate': (datetime.datetime.today() + datetime.timedelta(days=0)).strftime('%Y-%m-%d 00:00:00'),
            }
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
    drop_off_at = forms.DateTimeField(
        input_formats=("%a %B %d, %Y %I:%M %p",),
        localize=True,
        label='',
        initial=None,
        widget=DateTimePickerInput(
            format="ddd %m%m %d, %Y %I:%M A",
            attrs={'placeholder': 'Pickup  Date/Time*'},
            options={
                'minDate': (datetime.datetime.today() + datetime.timedelta(days=0)).strftime('%Y-%m-%d 00:00:00'),
            }
        )
    )

    class Meta:
        model = Address
        fields = '__all__'

    def clean_dropoff_at(self):
        cleaned_data = super(DropOffForm, self).clean()
        date_limit = self.initial['context']['pickup_date'] + datetime.timedelta(days=1)
        dropoff_date = cleaned_data['drop_off_at']

        if dropoff_date < date_limit:
            raise ValidationError("Drop-off date must not be earlier than 1 day after the pickup date")
        return dropoff_date

    def clean_city(self):
        if self.is_valid():
            print(self.cleaned_data['state'])
            city = self.cleaned_data["city"]

            try:
                Region.objects.get().filter(city = city)

            except Region.DoesNotExist:
                return city
            raise forms.ValidationError('city "%s" is not in the chosen state.' % city)
'''' '''
