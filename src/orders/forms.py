from django import forms

from .models import Service


class OrderDetailsForm(forms.Form):
    Type = forms.ModelChoiceField(
        initial='Service Type',
        queryset=Service.objects.values_list('service_type', flat=True).distinct())
    name = forms.ModelChoiceField(queryset=Service.objects.values_list('service_name', flat=True))
    quantity = forms.FloatField()
    street = forms.CharField(max_length=50)
    city = forms.CharField(max_length=50)
    state = forms.CharField(max_length=50)
    zipcode = forms.FloatField()
    pickup_time = forms.TimeField()
    streetD = forms.CharField(max_length=50)
    cityD = forms.CharField(max_length=50)
    stateD = forms.CharField(max_length=50)
    zipcodeD = forms.FloatField()
    dropoff_time = forms.TimeField()
