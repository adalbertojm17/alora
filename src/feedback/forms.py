# noinspection PyUnresolvedReferences
from business.models import Store
from django import forms
from .models import Feedback
# noinspection PyUnresolvedReferences
from accounts.models import Account


class FeedBackForm(forms.ModelForm):

    store = forms.ModelChoiceField(
        empty_label='Choose a Store (Optional)',
        label='',
        required=False,
        queryset=Store.objects.all()
    )

    content = forms.CharField(
        min_length=20,
        max_length=500,
        label='',
        widget=forms.Textarea(attrs={
            'placeholder': 'We welcome your feedback. '
                           '(20-100 characters)',
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
        fields = ['user','store', 'subject', 'content']

    def __init__(self, user, *args, **kwargs):
        super(FeedBackForm, self).__init__(*args, **kwargs)
        self.fields['user'] = forms.ModelChoiceField(label='', queryset=Account.objects.all().filter(id=user),
                                                    widget=forms.HiddenInput(), initial=user)




