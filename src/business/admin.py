from django.contrib import admin
from django.utils.html import format_html

from .models import Service, Store,ServingAreas


class ServiceAdmin(admin.ModelAdmin):
    search_fields = ('id', 'name', 'store'),
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
        return format_html('<a class="btn" href="/admin/business/service/{}/delete/">Delete</a>', obj.id)

    delete_button.allow_tags = True
    delete_button.short_description = 'Delete Service'
    list_display = ('id', 'name', 'store', 'delete_button')


class StoreAdmin(admin.ModelAdmin):
    search_fields = ('id', 'name'),
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
        return format_html('<a class="btn" href="/admin/business/store/{}/delete/">Delete</a>', obj.id)

    delete_button.allow_tags = True
    delete_button.short_description = 'Delete Store'
    list_display = ('name', 'get_manager', 'address', 'delete_button')

    def get_manager(self, obj):
        return obj.manager.username

    get_manager.allow_tags = True
    get_manager.short_description = 'Manager'


admin.site.register(Service, ServiceAdmin)
admin.site.register(Store, StoreAdmin)
admin.site.register(ServingAreas)
