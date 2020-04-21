__author__ = 'dkarchmer@gmail.com'

from django.conf import settings
from django.core.management.base import BaseCommand

from ...models import Account


class Command(BaseCommand):

    def handle(self, *args, **options):
        if Account.objects.count() == 0:
            for user in settings.ADMINS:
                username = user[0].replace(' ', '')
                email = user[1]
                first_name = user[2]
                last_name = user[1]
                password = 'admin'
                print('Creating account for %s (%s) with the default password "%s"' % (username, email, password))
                admin = Account.objects.create_superuser(
                    email=email,
                    username=username,
                    password=password,
                    first_name=first_name,
                    last_name=last_name
                )
                admin.is_active = True
                admin.is_admin = True
                admin.save()
        else:
            print('Admin accounts can only be initialized if no Accounts exist')
