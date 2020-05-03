from django.contrib import admin
from django.contrib.auth.admin import Group
from django.contrib.auth.admin import UserAdmin
from django.utils.html import format_html
from rest_framework.authtoken.admin import TokenAdmin
from rest_framework.authtoken.models import Token

from .models import CustomerAccount, StaffAccount, ManagerAccount, EmployeeAccount


class AccountAdmin(UserAdmin):
    list_display = ('username', 'email', 'date_joined', 'last_login', 'is_manager', 'is_staff')
    search_fields = ('email', 'username',),
    readonly_fields = ('date_joined', 'last_login', 'is_superuser')

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()

    def has_add_permission(self, request, obj=None):
        return request.user.is_superuser

    def has_change_permission(self, request, obj=None):
        return request.user.is_superuser

    def has_delete_permission(self, request, obj=None):
        return request.user.is_superuser


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

class EmployeeAdmin(AccountAdmin):
    def delete_button(self, obj):
        return format_html('<a class="btn" href="/admin/accounts/employeeaccount/{}/delete/">Delete</a>', obj.id)

    delete_button.allow_tags = True
    delete_button.short_description = 'Delete Account'
    list_display = ('username', 'email', 'date_joined', 'last_login', 'delete_button')


class StaffAdmin(AccountAdmin):
    def delete_button(self, obj):
        return format_html('<a class="btn" href="/admin/accounts/staffaccount/{}/delete/">Delete</a>', obj.id)

    delete_button.allow_tags = True
    delete_button.short_description = 'Delete Account'

    list_display = ('username', 'email', 'date_joined', 'last_login', 'is_superuser', 'delete_button')


class CustomTokenAdmin(TokenAdmin):
    def has_add_permission(self, request, obj=None):
        return request.user.is_superuser

    def has_change_permission(self, request, obj=None):
        return request.user.is_superuser

    def has_delete_permission(self, request, obj=None):
        return request.user.is_superuser


TokenAdmin.raw_id_fields = ['user']
TokenAdmin.readonly_fields = ['user']

admin.site.unregister(Group)
admin.site.register(CustomerAccount, CustomerAdmin)
admin.site.register(StaffAccount, StaffAdmin)
admin.site.register(ManagerAccount, ManagerAdmin)
admin.site.register(EmployeeAccount, EmployeeAdmin)
admin.site.unregister(Token)
admin.site.register(Token, CustomTokenAdmin)
