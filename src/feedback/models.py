from django.db import models


class Feedback(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=254, verbose_name="email")
    services = models.CharField(max_length=2)
    content = models.TextField(max_length=500)

    class Meta:
        verbose_name_plural = 'Feedback'

    REQUIRED_FIELDS = ['first_name', 'last_name', 'email', 'services', 'content']
