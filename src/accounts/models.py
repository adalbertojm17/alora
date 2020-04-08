# noinspection PyUnresolvedReferences
from addresses.models import Address
from django.conf import settings
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from phonenumber_field.modelfields import PhoneNumberField
from rest_framework.authtoken.models import Token


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)


class AccountManager(BaseUserManager):
    def create_user(self, email, username, first_name, last_name, password=None):
        if not email:
            raise ValueError("Users must have an email addresses")
        if not username:
            raise ValueError("Users must have a username")
        if not first_name:
            raise ValueError("Users must have a first name")
        if not last_name:
            raise ValueError("Users must have a last name")

        user = self.model(
            email=self.normalize_email(email),
            username=username,
            first_name=first_name,
            last_name=last_name,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, first_name, last_name, password):
        user = self.create_user(
            email=self.normalize_email(email),
            password=password,
            username=username,
            first_name=first_name,
            last_name=last_name,
        )

        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class Account(AbstractBaseUser):
    email = models.EmailField(max_length=254, verbose_name="email", unique=True)
    username = models.CharField(max_length=35, unique=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=100)
    address = models.ForeignKey(Address, on_delete=models.SET_NULL, null=True)
    phone = PhoneNumberField(max_length=15, blank=True, null=True, unique=True)
    date_joined = models.DateField(verbose_name='date joined', auto_now_add=True)
    last_login = models.DateField(verbose_name='last login', auto_now=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_manager = models.BooleanField(default=False)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', 'first_name', 'last_name']

    objects = AccountManager()

    def __str__(self):
        return self.username

    def has_perm(self, perm, obj=None):
        return self.is_staff

    def has_module_perms(self, app_label):
        return True

    def get_related(self):
        qs = Account.objects.select_related()


class CustomerManager(models.Manager):
    def get_queryset(self):
        return super(CustomerManager, self).get_queryset().filter(is_staff=False, is_manager=False)


class BusinessOwnerManager(models.Manager):
    def get_queryset(self):
        return super(BusinessOwnerManager, self).get_queryset().filter(is_manager=True)


class StaffManager(models.Manager):
    def get_queryset(self):
        return super(StaffManager, self).get_queryset().filter(is_staff=True)


class CustomerAccount(Account):
    customer = CustomerManager()

    class Meta:
        verbose_name = 'Customer'
        proxy = True


class StaffAccount(Account):
    staff = StaffManager()

    class Meta:
        verbose_name_plural = 'Alora Staff'
        proxy = True


class ManagerAccount(Account):
    manager = BusinessOwnerManager()

    class Meta:
        verbose_name = 'Manager'
        proxy = True
