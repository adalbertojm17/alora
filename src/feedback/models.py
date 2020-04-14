# noinspection PyUnresolvedReferences
from business.models import Store
from django.db import models

# noinspection PyUnresolvedReferences
from alora import settings


class Feedback(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)
    store = models.ForeignKey(Store, on_delete=models.SET_NULL, null=True)
    subject = models.CharField(max_length=250)
    content = models.TextField(max_length=500)

    class Meta:
        verbose_name_plural = 'Feedback'

    REQUIRED_FIELDS = ['subject' 'content']
