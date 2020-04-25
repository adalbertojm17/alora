from django import forms
from django.contrib.auth.forms import UserCreationForm

from .models import Service
from .models import Store
from core.models import OrderItem
from core.models import Item
from core.models import Order
from accounts.models import Account


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
        self.order = order
        super(AddingOrderItemForm, self).__init__(*args, **kwargs)
        self.fields['item']=forms.ModelChoiceField(queryset=Item.objects.all().filter(services__store__manager=user))
        self.fields['order']= forms.ModelChoiceField(queryset=Order.objects.all().filter(id=order.id))

    class Meta:
        model = OrderItem
        fields = '__all__'

    def clean_item(self):
        if self.is_valid():
            item = self.cleaned_data["item"]
            try:
                OrderItem.objects.get(order = self.order,item=item)
            except OrderItem.DoesNotExist:
                return item
            raise forms.ValidationError('item "%s" is already in the order.' % item)


class AddingItemForm(forms.ModelForm):
    def __init__(self,user,*args, **kwargs):
        self.user = user
        super(AddingItemForm, self).__init__(*args, **kwargs)
        self.fields['services']=forms.ModelChoiceField(queryset=Service.objects.all().filter(store__manager=user))
    class Meta:
        model = Item
        fields = '__all__'

    def clean(self):
        cleaned_data = super(AddingItemForm, self).clean()
        name = cleaned_data.get("name")
        service = cleaned_data.get("services")
        try:
             Item.objects.get(services__store__manager=self.user, name=name,services=service)
        except Item.DoesNotExist:
             return cleaned_data
        raise forms.ValidationError('item "%s" is already in use.' % name)


class StaffCreationForm(UserCreationForm):

    is_staff= forms.BooleanField(
        label='',
        widget=forms.HiddenInput(), initial=True)

    first_name = forms.CharField(
        max_length=50,
        label='',
        widget=forms.TextInput(attrs={
            'placeholder': 'First name*',
            'pattern': '[A-Za-z ]+',
            'title': ' alphabetic '
                     'characters '
                     'only '
                     'please'
        }),
    )

    last_name = forms.CharField(
        max_length=100,
        label='',
        widget=forms.TextInput(attrs={
            'placeholder': 'Last name*',
            'pattern': '[A-Za-z ]+',
            'title': 'alphabetic '
                     'characters '
                     'only '
                     'please'
        }),

    )

    phone = forms.CharField(
        max_length=12,
        label='',
        widget=forms.TextInput(attrs={'placeholder': 'Phone number (Optional)'}),
        help_text='Enter a valid phone number (e.g. 999-999-9999)',
        required=False
    )

    email = forms.EmailField(
        max_length=254,
        label='',
        widget=forms.EmailInput(attrs={'placeholder': 'Email addresses*'})

    )

    email2 = forms.EmailField(
        max_length=254,
        label='',
        widget=forms.EmailInput(attrs={'placeholder': 'Confirm Email*'})

    )

    username = forms.CharField(
        min_length=5,
        max_length=35,
        label='',
        widget=forms.TextInput(attrs={
            'placeholder': 'Username*',
            'pattern': '[0-9A-Za-z ]+',
            'title': ' alphanumeric '
                     'characters '
                     'only '
                     'please'
        })
    )

    password1 = forms.CharField(
        label='',
        strip=False,
        min_length=6,
        max_length=32,
        widget=forms.PasswordInput(attrs={
            'placeholder': 'Password*',
        })
    )

    password2 = forms.CharField(
        label='',
        strip=False,
        min_length=6,
        max_length=32,
        widget=forms.PasswordInput(attrs={'placeholder': 'Confirm password*'})
    )

    class Meta:
        model = Account
        fields = ('is_staff','first_name', 'last_name', 'phone', 'email', 'email2', 'username')

    def clean_phone(self):
        return self.cleaned_data['phone'] or None

    def clean_email2(self):
        email = self.cleaned_data.get('email')
        email2 = self.cleaned_data.get('email2')
        if email != email2:
            raise forms.ValidationError('Emails must match')
