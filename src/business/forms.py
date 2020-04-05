from django import forms
from .models import Service
from .models import Store
from core.models import OrderItem
from core.models import Item


class ServiceCreationForm(forms.ModelForm):

    name = forms.CharField(
        max_length=50,
        label='name',)

    store = forms.ModelChoiceField(
        queryset= Store.objects.all(),
        label = 'store',
    )

    class Meta:
        model = Service
        fields = ('name','store')

    def clean_name(self):
        if self.is_valid():
            name = self.cleaned_data["name"]
            try:
                Service.objects.get(name=name)
            except Service.DoesNotExist:
                return name
            raise forms.ValidationError('service "%s" is already in use.' % name)


class AddingOrderItemForm(forms.ModelForm):
    class Meta:
        model = OrderItem
        fields = '__all__'

   # def clean_item(self):
    #    if self.is_valid():
     #       item = self.cleaned_data["item"]
      #      try:
       #         OrderItem.objects.get(item=item)
         #   except Service.DoesNotExist:
          #      return item
           # raise forms.ValidationError('service "%s" is already in use.' % item)
