from django import forms
from .models import Feedback

LAUNDRY = 'LA'
DRY_CLEANING = 'DC'

SERVICE_CHOICES = (
    ('', 'Services'),
    (LAUNDRY, 'Laundry'),
    (DRY_CLEANING, 'Dry Cleaning')
)


class FeedBackForm(forms.ModelForm):
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

    services = forms.ChoiceField(
        label='',
        initial='',
        choices=SERVICE_CHOICES
    )

    content = forms.CharField(
        label='',
        widget=forms.Textarea(attrs={'placeholder': 'We welcome your feedback.', 'rows': 5, 'cols': 20})
    )

    class Meta:
        model = Feedback
        fields = ['first_name', 'last_name', 'email', 'services', 'content']
