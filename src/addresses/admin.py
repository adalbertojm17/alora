from django.contrib import admin
from django.utils.html import format_html

from .models import Address


class AddressAdmin(admin.ModelAdmin):
    search_fields = ('street', 'city', 'state', 'zip_code'),
    readonly_fields = ()

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()

    def has_add_permission(self, request, obj=None):
        return request.user.is_superuser

    def has_change_permission(self, request, obj=None):
        return request.user.is_superuser

    def has_delete_permission(self, request, obj=None):
        return request.user.is_superuser

    def delete_button(self, obj):
        return format_html('<a class="btn" href="/admin/addresses/address/{}/delete/">Delete</a>', obj.id)

    delete_button.allow_tags = True
    delete_button.short_description = 'Delete Address'
    list_display = ('street', 'city', 'state', 'zip_code', 'delete_button')


admin.site.register(Address, AddressAdmin)
