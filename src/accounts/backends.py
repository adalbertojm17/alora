from django.conf import settings
from .models import Account


def authenticate(username=None, password=None):
    if '@' in username:
        kwargs = {'email': username}
    else:
        kwargs = {'username': username}
    try:
        user = Account.objects.get(**kwargs)
        if user.check_password(password):
            return user
    except Account.DoesNotExist:
        return None


def get_user(user_id):
    try:
        return Account.objects.get(pk=user_id)
    except Account.DoesNotExist:
        return None


class EmailOrUsernameModelBackend(object):
    def authenticate(self, username=None, password=None):
        if '@' in username:
            kwargs = {'email': username}
        else:
            kwargs = {'username': username}
        try:
            user = Account.objects.get(**kwargs)
            if user.check_password(password):
                return user
        except Account.DoesNotExist:
            return None

    def get_user(self, user_id):
        try:
            return Account.objects.get(pk=user_id)
        except Account.DoesNotExist:
            return None
