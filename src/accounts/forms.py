from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate

from accounts.models import Account


class RegistrationForm(UserCreationForm):
    first_name = forms.CharField(
        max_length=50,
        label='',
        widget=forms.TextInput(attrs={'placeholder': 'First Name'}),
    )
    last_name = forms.CharField(
        max_length=100,
        label='',
        widget=forms.TextInput(attrs={'placeholder': 'Last Name'}),

    )

    email = forms.EmailField(
        max_length=254,
        help_text="Required, Add a valid email address",
        label='',
        widget=forms.EmailInput(attrs={'placeholder': 'Email'})

    )

    username = forms.CharField(
        max_length=35,
        label='',
        widget=forms.TextInput(attrs={'placeholder': 'Username'})
    )

    password1 = forms.CharField(
        label='',
        strip=False,
        widget=forms.PasswordInput(attrs={'placeholder': 'Password'})
    )

    password2 = forms.CharField(
        label='',
        strip=False,
        widget=forms.PasswordInput(attrs={'placeholder': 'Confirm Password'})

    )

    class Meta:
        model = Account
        fields = ('first_name', 'last_name', 'email', 'username')


class AccountAuthenticationForm(forms.ModelForm):
    email = forms.EmailField(
        max_length=254,
        help_text="Required, Add a valid email address",
        label='',
        widget=forms.EmailInput(attrs={'placeholder': 'Email'})

    )
    password = forms.CharField(label='', widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))

    class Meta:
        model = Account
        fields = ('email', 'password')

    def clean(self):
        email = self.cleaned_data.get('email')
        password = self.cleaned_data.get('password')
        if not authenticate(email=email, password=password):
            raise forms.ValidationError("Invalid login")


class Edit_Account_Form(forms.ModelForm):
    class Meta:
        model = Account
        fields = ("email", "username","first_name","last_name")

    def clean_first_name(self):
        if self.is_valid():
            first_name = self.cleaned_data["first_name"]
            return first_name

    def clean_last_name(self):
        if self.is_valid():
            last_name = self.cleaned_data["last_name"]
            return last_name

    def clean_email(self):
        if self.is_valid():
            email = self.cleaned_data["email"]
            try:
                account = Account.objects.exclude(pk=self.instance.pk).get(email=email)
            except Account.DoesNotExist:
                return email
            raise forms.ValidationError('Email "%s"is already in use.' % account)

    def clean_username(self):
        if self.is_valid():
            username = self.cleaned_data["username"]
            try:
                account = Account.objects.exclude(pk=self.instance.pk).get(username=username)
            except Account.DoesNotExist:
                return username
            raise forms.ValidationError('Username "%s"is already in use.' % account)