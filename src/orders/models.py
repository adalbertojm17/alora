from django.db import models

from accounts.models import Account


class Service(models.Model):
    serviceType = models.CharField(max_length=50)
    serviceCost = models.FloatField()
    serviceName = models.CharField(max_length=50)

    def __str__(self):
        return self.serviceName


class Order(models.Model):
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    pickupTime = models.TimeField()
    dropoffTime = models.TimeField()
    dateCreated= models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return str(self.account)

class OrderDetails(models.Model):
    order = models.ForeignKey(Order,on_delete=models.CASCADE)
    service = models.ForeignKey(Service,on_delete=models.CASCADE)
    quantity =  models.FloatField()
    def __str__(self):
        return str(self.service)

class Status(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    currentStatus = models.BooleanField(default=False)
    deliveryStatus = models.BooleanField(default=False)
    pickupStatus = models.BooleanField(default=False)
    paymentStatus = models.BooleanField(default=False)

    def __str__(self):
        return str(self.id)



class Adress(models.Model):
    order = models.ForeignKey(Order,on_delete=models.CASCADE)
    street = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    zipcode = models.IntegerField()

class Item(models.Model):
    Order = models.ForeignKey(Order, on_delete=models.CASCADE)
    service = models.ForeignKey(Service,on_delete=models.CASCADE)
    pickupDate = models.DateTimeField()
    dropoffDate = models.DateTimeField()

    def __str__(self):
        return self.service
