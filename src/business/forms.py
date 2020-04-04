from django import forms
from .models import Service
from business.models import Store

class ServiceCreationForm(forms.ModelForm):

    name = forms.CharField(
        max_length=50,
        label='name',)

    store = forms.ModelChoiceField(
        queryset= Store.objects.all(),
        label = 'store',
    )
    price = forms.DecimalField(
        max_digits=5,
        decimal_places=2,
        label= 'price'
    )

    class Meta:
        model = Service
        fields = ('name','store','price')

    def clean_name(self):
        if self.is_valid():
            name = self.cleaned_data["name"]
            try:
                Service.objects.get(name=name)
            except Service.DoesNotExist:
                return name
            raise forms.ValidationError('name "%s" is already in use.' % name)
