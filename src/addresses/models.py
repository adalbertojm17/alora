from django.db import models
from localflavor.us.models import USStateField, USZipCodeField
from localflavor.us.us_states import STATE_CHOICES


class Address(models.Model):
    street = models.CharField(max_length=120)
    apt = models.CharField(max_length=50, null=True, blank=True)
    city = models.CharField(max_length=120)
    state = USStateField(choices=STATE_CHOICES)
    zip_code = USZipCodeField()

    def __str__(self):
        return self.street + ', ' + self.city + ', ' + self.state + ' ' + self.zip_code

    class Meta:
        verbose_name_plural = 'Addresses'
