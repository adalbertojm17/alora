from django.contrib import admin
from django.utils.html import format_html

from .models import Order, OrderItem, Item


class ItemAdmin(admin.ModelAdmin):
    search_fields = ('id', 'name'),

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
        return format_html('<a class="btn" href="/admin/core/order/{}/delete/">Delete</a>', obj.id)

    delete_button.allow_tags = Item
    delete_button.short_description = 'Delete Account'
    list_display = ('id', 'name', 'price', 'delete_button')


class OrderAdmin(admin.ModelAdmin):
    search_fields = ('id', 'account', 'store' 'created_at', 'current_status'),
    readonly_fields = ('id', 'account', 'created_at')

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
        return format_html('<a class="btn" href="/admin/accounts/core/orderitem/{}/delete/">Delete</a>', obj.id)

    delete_button.allow_tags = True
    delete_button.short_description = 'Delete Order'
    list_display = ('id', 'account', 'created_at', 'current_status', 'delete_button')


class OrderItemAdmin(admin.ModelAdmin):
    search_fields = ('item', 'order'),
    readonly_fields = ('id',)

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
        return format_html('<a class="btn" href="/admin/accounts/customeraccount/{}/delete/">Delete</a>', obj.id)

    delete_button.allow_tags = True
    delete_button.short_description = 'Delete Order Item'
    list_display = ('item', 'order', 'quantity', 'delete_button')


admin.site.register(Item, ItemAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(OrderItem, OrderItemAdmin)
