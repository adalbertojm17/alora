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
