# noinspection PyUnresolvedReferences
from accounts.models import Account
# noinspection PyUnresolvedReferences,PyPackageRequirements
from addresses.models import Address
# noinspection PyUnresolvedReferences
from business.models import Store
# noinspection PyUnresolvedReferences
from django.db import models
# noinspection PyUnresolvedReferences
from products.models import Product, Service

# tuple of possible statuses of an order
# emulates a static table
STATUS_CHOICES = (
    ('P', 'Processed'),
    ('PU', 'Picked up'),
    ('CL', 'Cleaning'),
    ('CP', 'Complete'),
    ('ER', 'Enroute'),
    ('D', 'Delivered'),
)


# model for a complete customer order
class Order(models.Model):
    account = models.ForeignKey(Account, on_delete=models.SET_NULL, null=True)
    store = models.ForeignKey(Store, on_delete=models.SET_NULL, null=True)
    pickup_location = models.ForeignKey(Address, on_delete=models.SET_NULL, null=True)
    dropoff_location = models.ForeignKey(Address, related_name='+', on_delete=models.SET_NULL, null=True)
    pickup_at = models.DateTimeField()
    dropoff_at = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    currentstatus = models.CharField(choices=STATUS_CHOICES, max_length=2)

    def __str__(self):
        return str(self.account)

    def get_status(self):
        return self.get_status()


# model for a single item in an order
# encapsulates a single product in an order
class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.OneToOneField(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return self.service.service_name + " - " + self.quantity.__str__()

    class Meta:
        verbose_name_plural = 'Order Items'
