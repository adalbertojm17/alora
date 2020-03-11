import re

from django import forms
from .backends import authenticate
from django.contrib.auth.forms import UserCreationForm
from django.utils.safestring import mark_safe

from .models import Account

EMAIL_REGEX = r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"


class RegistrationForm(UserCreationForm):
    first_name = forms.CharField(
        max_length=50,
        label='',
        widget=forms.TextInput(attrs={'placeholder': 'First name*'}),
    )

    last_name = forms.CharField(
        max_length=100,
        label='',
        widget=forms.TextInput(attrs={'placeholder': 'Last name*'}),

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
        widget=forms.EmailInput(attrs={'placeholder': 'Email*'})

    )

    username = forms.CharField(
        max_length=35,
        label='',
        widget=forms.TextInput(attrs={'placeholder': 'Username*', 'pattern': '[0-9A-Za-z ]+', 'title': ' alphanumeric '
                                                                                                       'characters '
                                                                                                       'only '
                                                                                                       'please'})
    )

    password1 = forms.CharField(
        label='',
        strip=False,
        max_length=32,
        widget=forms.PasswordInput(attrs={'placeholder': 'Password*'})
    )

    password2 = forms.CharField(
        label='',
        strip=False,
        max_length=32,
        widget=forms.PasswordInput(attrs={'placeholder': 'Confirm password*'})
    )

    class Meta:
        model = Account
        fields = ('first_name', 'last_name', 'phone', 'email', 'username')

    def clean_phone(self):
        return self.cleaned_data['phone'] or None


class AccountAuthenticationForm(forms.ModelForm):
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
        if not authenticate(username=username, password=password):
            raise forms.ValidationError("Invalid login")


class EditAccountForm(forms.ModelForm):
    required_css_class = 'required'
    first_name = forms.CharField(
        max_length=50,
        label=mark_safe('First Name<br />'),
        label_suffix='',
        widget=forms.TextInput(attrs={'placeholder': 'First name', 'class': 'toggleenabled'}),
    )

    last_name = forms.CharField(
        max_length=100,
        label=mark_safe('Last Name<br />'),
        label_suffix='',
        widget=forms.TextInput(attrs={'placeholder': 'Last name', 'class': 'toggleenabled'}),

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
        label=mark_safe('Username<br />'),
        label_suffix='',
        widget=forms.TextInput(attrs={'placeholder': 'Username', 'class': 'toggleenabled', 'pattern': '[0-9A-Za-z ]+',
                                      'title': ' alphanumeric '
                                               'characters only '
                                               'please'})
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
