# noinspection PyUnresolvedReferences
from accounts.models import Account
# noinspection PyUnresolvedReferences,PyPackageRequirements
from addresses.models import Address
# noinspection PyUnresolvedReferences
from business.models import Store
# noinspection PyUnresolvedReferences
from django.db import models


class Service(models.Model):
    store = models.ForeignKey(Store, on_delete=models.CASCADE)
    service_type = models.CharField(max_length=50)
    service_cost = models.FloatField(blank=True)
    service_name = models.CharField(max_length=50)

    def __str__(self):
        return self.service_name


class Status(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Statuses'


class Order(models.Model):
    account = models.ForeignKey(Account, on_delete=models.SET_NULL, null=True)
    Store = models.ForeignKey(Store,on_delete=models.SET_NULL, null=True)
    pickup_location = models.ForeignKey(Address, on_delete=models.SET_NULL, null=True)
    dropoff_location = models.ForeignKey(Address, related_name='+', on_delete=models.SET_NULL, null=True)
    pickup_at = models.DateTimeField()
    dropoff_at = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.ForeignKey(Status,on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return str(self.account)


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    service = models.ForeignKey(Service, on_delete=models.SET_NULL, null=True)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return self.service.service_name + " - " + self.quantity.__str__()

    def get_service_price(self):
        return self.service.service_cost

    class Meta:
        verbose_name_plural = 'Order Items'
