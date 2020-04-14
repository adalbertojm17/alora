# noinspection PyUnresolvedReferences
from accounts.models import Account
# noinspection PyUnresolvedReferences,PyPackageRequirements
from addresses.models import Address
# noinspection PyUnresolvedReferences
from business.models import Service
# noinspection PyUnresolvedReferences
from business.models import Store
# noinspection PyUnresolvedReferences
from django.db import models
# noinspection PyUnresolvedReferences
from django.urls import reverse

# tuple of possible statuses of an order
# emulates a static table
STATUS_CHOICES = (
    ('P', 'Processed'),
    ('PU', 'Picked up'),
    ('CL', 'Cleaning'),
    ('CP', 'Complete'),
    ('ER', 'Enroute'),
    ('D', 'Delivered'),
    ('C', 'Completed')
)


# model for a single product item (e.g. clothing or a bag)
class Item(models.Model):
    name = models.CharField(max_length=100)
    services = models.ForeignKey(Service, on_delete=models.SET_NULL, null=True)
    price = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return self.name

    def get_item_price(self):
        return self.price

    def get_add_to_order_url(self):
        return reverse('core:add-to-order', kwargs={
            'id': self.id
        })


# model for a complete customer order
class Order(models.Model):
    user = models.ForeignKey(Account, on_delete=models.SET_NULL, null=True)
    store = models.ForeignKey(Store, on_delete=models.SET_NULL, null=True)
    pickup_location = models.ForeignKey(Address, on_delete=models.SET_NULL, null=True)
    dropoff_location = models.ForeignKey(Address, related_name='+', on_delete=models.SET_NULL, null=True)
    pickup_at = models.DateTimeField()
    dropoff_at = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    current_status = models.CharField(choices=STATUS_CHOICES, max_length=2, default='P')

    def __str__(self):
        return self.user.username

    def get_status(self):
        return self.current_status


# model for a single item in an order
# encapsulates a single product in an order
class OrderItem(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE, null=True)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return f"{self.quantity} of {self.item.name}"

    class Meta:
        verbose_name_plural = 'Order Items'
