from django.db import models


class Order(models.Model):
    name = models.CharField(max_length= 300)
    pickup_Location = models.IntegerField()
    dropoff_Location = models.IntegerField()
    pickup_Time = models.TimeField()
    dropoff_Time = models.TimeField()
    def __str__(self):
        return self.id


class Service(models.Model):
    service_Type = models.CharField(max_length=35)
    service_Cost= models.FloatField()
    service_Name = models.CharField(max_length=35)
    def __str__(self):
        return self.service_Name

class Order_Adress(models.Model):
    adress_order = models.ForeignKey(Order, on_delete=models.CASCADE())
    type = models.Choices("Dropoff","Pickup")
    street = models.CharField(max_length=30)
    city = models.CharField(max_length=30)
    state= models.CharField(max_length=30)
    zipcode=models.IntegerField(max_length=6)


class Status(models.Model):
    status_Order = models.ForeignKey(Order, on_delete=models.CASCADE())
    current_Status = models.Choices()
    delivery_Status =  models.BooleanField()
    pickup_Status = models.NullBooleanField()
    payment_Status =  models.BooleanField()

    def __str__(self):
        return self.current_status


class FeedBack(models.Model):
    feedback_Order = models.ForeignKey(Order, on_delete=models.CASCADE())
    feedback_text = models.CharField(max_length=300)
    def __str__(self):
        return self.id


class Item(models.Model):
    item_Order = models.ForeignKey(Order,on_delete=models.CASCADE())
    item_Weigth =models.FloatField(default=0)
    item_Type=models.CharField()
    item_Cost= models.FloatField()
    def __str__(self):
        return self.item_Type

