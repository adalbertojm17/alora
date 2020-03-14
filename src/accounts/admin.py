from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Account
from rest_framework.authtoken.admin import TokenAdmin


class AccountAdmin(UserAdmin):
    list_display = ('username', 'email', 'date_joined', 'last_login', 'is_admin', 'is_staff')
    search_fields = ('email', 'username',),
    readonly_fields = ('date_joined', 'last_login', 'is_superuser')

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()


TokenAdmin.raw_id_fields = ['user']

admin.site.register(Account, AccountAdmin)
