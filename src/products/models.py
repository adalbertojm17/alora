# noinspection PyUnresolvedReferences,PyPackageRequirements
from business.models import Store, Service
from django.db import models


# model for a single product item (e.g. clothing or a bag)
class Product(models.Model):
    name = models.CharField(max_length=100)
    service = models.OneToOneField(Service, on_delete=models.SET_NULL, null=True)
    price = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return self.name

    def get_item_price(self):
        return self.price
