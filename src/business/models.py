# noinspection PyUnresolvedReferences
from addresses.models import Address
from django.db import models


class Store(models.Model):
    name = models.CharField(max_length=100)
    address = models.OneToOneField(Address, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name
