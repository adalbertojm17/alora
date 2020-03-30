from bootstrap_datepicker_plus import DateTimePickerInput
from django import forms

from .models import Service


class OrderDetailsForm(forms.Form):
    type = forms.ModelChoiceField(queryset=Service.objects.values_list('service_type', flat=True).distinct())
    name = forms.ModelChoiceField(queryset=Service.objects.values_list('service_name', flat=True))
    quantity = forms.FloatField()
    street = forms.CharField(max_length=50)
    city = forms.CharField(max_length=50)
    state = forms.CharField(max_length=50)
    zipcode = forms.FloatField()
    pickup_time = forms.DateTimeField(widget=DateTimePickerInput(format='YYYY-MM-DD HH:MM:ss'))
    streetD = forms.CharField(max_length=50)
    cityD = forms.CharField(max_length=50)
    stateD = forms.CharField(max_length=50)
    zipcodeD = forms.FloatField()
    dropoff_time = forms.DateTimeField(widget=DateTimePickerInput(format='YYYY-MM-DD HH:MM:ss'))
