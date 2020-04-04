import datetime

# noinspection PyUnresolvedReferences
from addresses.models import Address
from bootstrap_datepicker_plus import DateTimePickerInput
# noinspection PyUnresolvedReferences
from business.models import Service
from django import forms
from localflavor.us.forms import USStateField, USZipCodeField
from multiselectfield import MultiSelectFormField


class ServiceForm(forms.Form):
    services = MultiSelectFormField(choices=[(
        service.id,
        service.name
    )
        for service in Service.objects.all()
    ])


class PickupForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = '__all__'


class DropOffForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = '__all__'
