# noinspection PyUnresolvedReferences
from accounts.models import Account
# noinspection PyUnresolvedReferences,PyPackageRequirements
from addresses.models import Address
# noinspection PyUnresolvedReferences
from business.models import Store
# noinspection PyUnresolvedReferences
from django.db import models


class Service(models.Model):
    store = models.OneToOneField(Store, on_delete=models.CASCADE)
    service_type = models.CharField(max_length=50)
    service_cost = models.FloatField()
    service_name = models.CharField(max_length=50)
    def __str__(self):
        return self.service_name

class Status(models.Model):
    name = models.CharField(max_length= 100)
    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = 'Statuses'

class Order(models.Model):
    account = models.ForeignKey(Account, on_delete=models.SET_NULL, null=True)
    pickup_location = models.ForeignKey(Address, on_delete=models.SET_NULL, null=True)
    dropoff_location = models.ForeignKey(Address, related_name='+', on_delete=models.SET_NULL, null=True)
    pickup_date_time = models.DateTimeField()
    dropoff_date_time = models.DateTimeField()
    date_created = models.DateTimeField(auto_now_add=True)
    status =  models.OneToOneField(Status,on_delete=models.CASCADE)
    def __str__(self):
        return self.account

class OrderItem(models.Model):
    order = models.ForeignKey(Order,on_delete=models.CASCADE)
    service = models.OneToOneField(Service, on_delete=models.SET_NULL, null=True)
    quantity = models.IntegerField()
    def __str__(self):
        return self.service + self.quantity
    class Meta:
        verbose_name_plural = 'Order Items'


