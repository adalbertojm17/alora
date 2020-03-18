from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.html import format_html
from .models import CustomerAccount, StaffAccount, ManagerAccount
from rest_framework.authtoken.admin import TokenAdmin


class AccountAdmin(UserAdmin):
    list_display = ('username', 'email', 'date_joined', 'last_login', 'is_manager', 'is_staff')
    search_fields = ('email', 'username',),
    readonly_fields = ('date_joined', 'last_login', 'is_superuser')

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()


class CustomerAdmin(AccountAdmin):
    def delete_button(self, obj):
        return format_html('<a class="btn" href="/admin/accounts/customeraccount/{}/delete/">Delete</a>', obj.id)

    delete_button.allow_tags = True
    delete_button.short_description = 'Delete Account'
    list_display = ('username', 'email', 'date_joined', 'last_login', 'delete_button')


class ManagerAdmin(AccountAdmin):
    def delete_button(self, obj):
        return format_html('<a class="btn" href="/admin/accounts/manageraccount/{}/delete/">Delete</a>', obj.id)

    delete_button.allow_tags = True
    delete_button.short_description = 'Delete Account'

    list_display = ('username', 'email', 'date_joined', 'last_login', 'delete_button')


class StaffAdmin(AccountAdmin):
    def delete_button(self, obj):
        return format_html('<a class="btn" href="/admin/accounts/staffaccount/{}/delete/">Delete</a>', obj.id)

    delete_button.allow_tags = True
    delete_button.short_description = 'Delete Account'

    list_display = ('username', 'email', 'date_joined', 'last_login', 'is_superuser', 'delete_button')


TokenAdmin.raw_id_fields = ['user']

admin.site.register(CustomerAccount, CustomerAdmin)
admin.site.register(StaffAccount, StaffAdmin)
admin.site.register(ManagerAccount, ManagerAdmin)
