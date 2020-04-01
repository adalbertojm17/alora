# noinspection PyUnresolvedReferences
from accounts.models import Account
# noinspection PyUnresolvedReferences,PyPackageRequirements
from address.models import Address
# noinspection PyUnresolvedReferences
from business.models import Store
# noinspection PyUnresolvedReferences
from clothes.models import ClothingItem
from django.db import models


class Service(models.Model):
    store = models.OneToOneField(Store, on_delete=models.CASCADE)
    service_type = models.CharField(max_length=50)
    service_cost = models.FloatField()
    service_name = models.CharField(max_length=50)


class OrderItem(models.Model):
    service = models.OneToOneField(Service, on_delete=models.SET_NULL, null=True)
    quantity = models.IntegerField()
    pickup_date_time = models.DateTimeField()
    dropoff_date_time = models.DateTimeField()


class Order(models.Model):
    account = models.ForeignKey(Account, on_delete=models.SET_NULL, null=True)
    pickup_location = models.ForeignKey(Address, on_delete=models.SET_NULL, null=True)
    dropoff_location = models.ForeignKey(Address, related_name='+', on_delete=models.SET_NULL, null=True)
    pickup_date_time = models.DateTimeField()
    dropoff_date_time = models.DateTimeField()
    date_created = models.DateTimeField(auto_now_add=True)
