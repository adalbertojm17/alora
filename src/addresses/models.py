from django.db import models


class Address(models.Model):
    street = models.CharField(max_length=120)
    city = models.CharField(max_length=120)
    state = models.CharField(max_length=120)
    country = models.CharField(max_length=120)
    zip_code = models.CharField()

    def __str__(self):
        return self.street + self.city
