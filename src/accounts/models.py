from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


# Create your models here.
class User(AbstractBaseUser):
    email = models.EmailField()


