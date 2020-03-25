from django import forms
from .models import OrderDetails,Service


class OrderDetailsForm(forms.Form):

    Type = forms.ModelChoiceField(queryset=Service.objects.values_list('serviceType',flat=True).distinct())
    name = forms.ModelChoiceField(queryset=Service.objects.values_list('serviceName',flat=True))
    quantity = forms.FloatField()
    street =forms.CharField(max_length=50)
    city = forms.CharField(max_length=50)
    state = forms.CharField(max_length=50)
    zipcode = forms.FloatField()
    pickupTime = forms.TimeField()
    streetD = forms.CharField(max_length=50)
    cityD = forms.CharField(max_length=50)
    stateD = forms.CharField(max_length=50)
    zipcodeD = forms.FloatField()
    DropoffTime = forms.TimeField()