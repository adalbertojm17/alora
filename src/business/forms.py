from django import forms
from .models import Service
from .models import Store
from core.models import OrderItem
from core.models import Item
from core.models import Order


class ServiceCreationForm(forms.ModelForm):
    def __init__(self,user,*args, **kwargs):
        self.user = user
        super(ServiceCreationForm, self).__init__(*args, **kwargs)
        self.fields['store']=forms.ModelChoiceField(queryset=Store.objects.all().filter(manager=user))

    name = forms.CharField(
        max_length=50,
        label='name',)

    class Meta:
        model = Service
        fields = ('name','store')

    def clean_name(self):
        if self.is_valid():
            name = self.cleaned_data["name"]
            try:
                Service.objects.get(store__manager=self.user, name=name)
            except Service.DoesNotExist:
                return name
            raise forms.ValidationError('service "%s" is already in use.' % name)


class AddingOrderItemForm(forms.ModelForm):
    def __init__(self,user,order,*args, **kwargs):
        super(AddingOrderItemForm, self).__init__(*args, **kwargs)
        self.fields['item']=forms.ModelChoiceField(queryset=Item.objects.all().filter(services__store__manager=user))
        self.fields['order']= forms.ModelChoiceField(queryset=Order.objects.all().filter(id=order.id))

    class Meta:
        model = OrderItem
        fields = '__all__'



class AddingItemForm(forms.ModelForm):
    def __init__(self,user,*args, **kwargs):
        self.user = user
        super(AddingItemForm, self).__init__(*args, **kwargs)
        self.fields['services']=forms.ModelChoiceField(queryset=Service.objects.all().filter(store__manager=user))
    class Meta:
        model = Item
        fields = '__all__'

    def clean_name(self):
        if self.is_valid():
            name = self.cleaned_data["name"]
            try:
                Item.objects.get(services__store__manager=self.user, name=name)
            except Item.DoesNotExist:
                return name
            raise forms.ValidationError('item "%s" is already in use.' % name)