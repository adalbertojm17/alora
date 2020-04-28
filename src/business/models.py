# noinspection PyUnresolvedReferences
from accounts.models import Account
# noinspection PyUnresolvedReferences
from addresses.models import Address
from django.db import models


# model to represent a physical store
class Store(models.Model):
    name = models.CharField(max_length=150)
    manager = models.ForeignKey(Account, on_delete=models.CASCADE)
    address = models.OneToOneField(Address, on_delete=models.SET_NULL, null=True)
    staff = models.ManyToManyField(Account, related_name='staff')

    def __str__(self):
        return self.name


# model for a service (e.g. Laundry, Dry Cleaning, etc.,)
class Service(models.Model):
    name = models.CharField(max_length=50)
    store = models.ForeignKey(Store, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
