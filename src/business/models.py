# noinspection PyUnresolvedReferences
# noinspection PyUnresolvedReferences
from accounts.models import Account
from addresses.models import Address
from django.db import models


# model to represent a physical store
class Store(models.Model):
    name = models.CharField(max_length=100)
    manager = models.ManyToManyField(Account)
    address = models.OneToOneField(Address, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name


# model for a service (e.g. Laundry, Dry Cleaning, etc.,)
class Service(models.Model):
    name = models.CharField(max_length=50)
    store = models.ForeignKey(Store, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return self.name
