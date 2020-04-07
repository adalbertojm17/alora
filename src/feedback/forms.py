# noinspection PyUnresolvedReferences
from business.models import Store
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
    MODDED_STORE_CHOICES = list([(
        store.id,
        store.name,
    )
        for store in Store.objects.all()
    ])
    MODDED_STORE_CHOICES.insert(0, ('', 'Choose a Store'))
    store = forms.ChoiceField(
        label='',
        required=False,
        choices=MODDED_STORE_CHOICES
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

    def __init__(self, *args, **kwargs):
        super(FeedBackForm, self).__init__(*args, **kwargs)
        self.fields['store'].choices = self.MODDED_STORE_CHOICES
