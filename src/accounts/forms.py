import re

# noinspection PyUnresolvedReferences
from addresses.models import Address
from django import forms
from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from django.utils.safestring import mark_safe
from localflavor.us.forms import USStateField, USZipCodeField
from localflavor.us.us_states import STATE_CHOICES

from .backends import authenticate
from .models import Account

EMAIL_REGEX = r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"


class UserSignUpForm(UserCreationForm):
    first_name = forms.CharField(
        max_length=50,
        min_length=3,
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
        min_length=3,
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
        fields = ('first_name', 'last_name', 'phone', 'email', 'email2', 'username')

    def clean_phone(self):
        return self.cleaned_data['phone'] or None

    def clean_email2(self):
        email = self.cleaned_data.get('email')
        email2 = self.cleaned_data.get('email2')
        if email != email2:
            raise forms.ValidationError('Emails must match')


class UserAddressForm(forms.ModelForm):
    street = forms.CharField(
        label='',
        max_length=120,
        widget=forms.TextInput(attrs={'placeholder': 'Street*'})
    )
    apt = forms.CharField(
        label='',
        required=False,
        max_length=50,
        widget=forms.TextInput(attrs={'placeholder': 'APT/Suite', 'pattern': '[0-9A-Za-z ]+',
                                      'title': ' alphanumeric '
                                               'characters '
                                               'only '
                                               'please'})

    )
    city = forms.CharField(
        label='',
        max_length=120,
        widget=forms.TextInput(attrs={'placeholder': 'City*'})

    )
    MODDED_STATE_CHOICES = list(STATE_CHOICES)
    MODDED_STATE_CHOICES.insert(0, ('', 'Select a State (Optional)'))
    state = USStateField(
        label='',
        widget=forms.Select(choices=MODDED_STATE_CHOICES))

    zip_code = USZipCodeField(
        label='',
        widget=forms.TextInput(attrs={'placeholder': 'Zip Code*'})
    )

    class Meta:
        model = Address
        fields = '__all__'


class AccountAuthenticationForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        self.current_login = kwargs.pop('current_login')
        self.redirect = False
        super(AccountAuthenticationForm, self).__init__(*args, **kwargs)

    username = forms.CharField(
        max_length=35,
        label='',
        widget=forms.TextInput(attrs={'placeholder': 'Email or Username'})
    )

    password = forms.CharField(label='', widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))

    class Meta:
        model = Account
        fields = ('username', 'password')

    def clean(self):

        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        if not user:
            raise forms.ValidationError("Invalid login")
        if user.is_manager and self.current_login == 'customer-login':
            self.redirect = True
            raise forms.ValidationError("Please use the business login")


class AccountForm(forms.ModelForm):
    required_css_class = 'required',
    first_name = forms.CharField(
        min_length=3,
        max_length=50,
        label=mark_safe('First Name<br />'),
        label_suffix='',
        widget=forms.TextInput(attrs={
            'placeholder': 'First name',
            'class': 'toggleenabled',
            'pattern': '[A-Za-z ]+',
            'title': ' alphabetic '
                     'characters '
                     'only '
                     'please'
        }),
    )

    last_name = forms.CharField(
        min_length=3,
        max_length=100,
        label=mark_safe('Last Name<br />'),
        label_suffix='',
        widget=forms.TextInput(attrs={
            'placeholder': 'Last name',
            'class': 'toggleenabled',
            'pattern': '[A-Za-z ]+',
            'title': ' alphabetic '
                     'characters '
                     'only '
                     'please'
        }),

    )

    phone = forms.CharField(
        max_length=15,
        label=mark_safe('Phone number (Optional)<br />'),
        label_suffix='',
        required=False,
        widget=forms.TextInput(attrs={'placeholder': 'e.g. 999-999-9999', 'class': 'toggleenabled'}),
    )

    email = forms.EmailField(
        max_length=254,
        label=mark_safe('Email<br />'),
        label_suffix='',
        widget=forms.EmailInput(attrs={'placeholder': 'Email', 'class': 'toggleenabled'})

    )

    username = forms.CharField(
        max_length=35,
        min_length=5,
        label=mark_safe('Username<br />'),
        label_suffix='',
        widget=forms.TextInput(attrs={
            'placeholder': 'Username',
            'class': 'toggleenabled',
            'pattern': '[0-9A-Za-z ]+',
            'title': ' alphanumeric '
                     'characters '
                     'only '
                     'please'
        })
    )

    class Meta:
        model = Account
        fields = ("first_name", "last_name", 'phone', "email", "username")

    def clean_first_name(self):
        if self.is_valid():
            first_name = self.cleaned_data["first_name"]
            return first_name

    def clean_last_name(self):
        if self.is_valid():
            last_name = self.cleaned_data["last_name"]
            return last_name

    def clean_phone(self):
        if self.is_valid():
            phone = self.cleaned_data["phone"]
            try:
                Account.objects.exclude(pk=self.instance.pk).get(phone=phone)
            except Account.DoesNotExist:
                if phone == "":
                    phone = None
                return phone
            raise forms.ValidationError('Phone "%s" is already in use.' % phone)

    def clean_email(self):
        if self.is_valid():
            email = self.cleaned_data["email"]
            if email and not re.match(EMAIL_REGEX, email):
                raise forms.ValidationError('Invalid email format')
            try:
                Account.objects.exclude(pk=self.instance.pk).get(email=email)
            except Account.DoesNotExist:
                return email
            raise forms.ValidationError('Email "%s" is already in use.' % email)

    def clean_username(self):
        if self.is_valid():
            username = self.cleaned_data["username"]
            try:
                Account.objects.exclude(pk=self.instance.pk).get(username=username)
            except Account.DoesNotExist:
                return username
            raise forms.ValidationError('Username "%s" is already in use.' % username)

class EditAddressForm(forms.ModelForm):
    street = forms.CharField(
        label='Street',
        label_suffix='',
        max_length=120,
        widget=forms.TextInput(attrs={'placeholder': 'Street*'})
    )
    apt = forms.CharField(
        label='APT/Suite',
        label_suffix='',
        required=False,
        max_length=50,
        widget=forms.TextInput(attrs={'placeholder': 'APT/Suite', 'pattern': '[0-9A-Za-z ]+',
                                      'title': ' alphanumeric '
                                               'characters '
                                               'only '
                                               'please'})

    )
    city = forms.CharField(
        label='City',
        label_suffix='',
        max_length=120,
        widget=forms.TextInput(attrs={'placeholder': 'City*'})

    )
    MODDED_STATE_CHOICES = list(STATE_CHOICES)
    MODDED_STATE_CHOICES.insert(0, ('', 'Select a State (Optional)'))
    state = USStateField(
        label='State',
        label_suffix='',
        widget=forms.Select(choices=MODDED_STATE_CHOICES))

    zip_code = USZipCodeField(
        label='Zip Code',
        label_suffix='',
        widget=forms.TextInput(attrs={'placeholder': 'Zip Code*'})
    )
    class Meta:
        model = Address
        fields = '__all__'