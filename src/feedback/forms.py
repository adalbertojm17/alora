# noinspection PyUnresolvedReferences
from business.models import Store
from django import forms

from .models import Feedback


class FeedBackForm(forms.ModelForm):
    store = forms.ModelChoiceField(
        empty_label='Choose a Store (Optional)',
        label='',
        required=False,
        queryset=Store.objects.all()
    )

    content = forms.CharField(
        label='',
        widget=forms.Textarea(attrs={
            'placeholder': 'We welcome your feedback.',
            'rows': 5, 'cols': 20
        })
    )

    subject = forms.CharField(
        label='',
        max_length=250,
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Enter your subject.',
                'pattern': '[0-9A-Za-z ]+',
                'title': ' alphanumeric '
                         'characters '
                         'only '
                         'please'
            }
        )
    )

    class Meta:
        model = Feedback
        fields = ['store', 'subject', 'content']

