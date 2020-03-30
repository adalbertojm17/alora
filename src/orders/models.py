# noinspection PyUnresolvedReferences
from accounts.models import Account
from django.db import models


class Service(models.Model):
    service_type = models.CharField(max_length=50)
    service_cost = models.FloatField()
    service_name = models.CharField(max_length=50)

    def __str__(self):
        return self.service_name


class Order(models.Model):
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    pickup_time = models.DateTimeField(null=False, blank=False)
    dropoff_time = models.DateTimeField(null=False, blank=False)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.account)


class OrderDetails(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    quantity = models.FloatField()

    class Meta:
        verbose_name_plural = "Order Details"

    def __str__(self):
        return str(self.service)


class Status(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    current_status = models.BooleanField(default=False)
    delivery_status = models.BooleanField(default=False)
    pickup_status = models.BooleanField(default=False)
    payment_status = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = "Status"

    def __str__(self):
        return str(self.id)


class Address(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    street = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    zipcode = models.IntegerField()


class Item(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    pickup_date = models.DateTimeField()
    dropoff_date = models.DateTimeField()

    def __str__(self):
        return self.service
