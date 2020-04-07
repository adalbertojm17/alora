from django.db import models

# noinspection PyUnresolvedReferences
from business.models import Store


class Feedback(models.Model):
    store = models.CharField(max_length=150, choices=[(
        store.id,
        store.name,
    )
        for store in Store.objects.all()
    ], null=True, blank=True)
    subject = models.CharField(max_length=250)
    content = models.TextField(max_length=500)

    class Meta:
        verbose_name_plural = 'Feedback'

    REQUIRED_FIELDS = ['subject' 'content']
