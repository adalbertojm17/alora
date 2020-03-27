from django.contrib import admin
from .models import Service, Order, Adress,OrderDetails,Status


class OrderAdmin(admin.ModelAdmin):
    list_display = ('name', 'pickup_Location', 'dropoff_Location', 'pickup_Time', 'dropoff_Time')
    search_fields = ('name', 'pickup_Location', 'dropoff_Location'),
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


class ServiceAdmin(admin.ModelAdmin):
    list_display = ('service_Name', 'service_Type', 'service_Cost')
    search_fields = ('service_Name', 'service_Type', 'service_Cost'),
    readonly_fields = ('service_Name', 'service_Type', 'service_Cost')

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()

    def has_add_permission(self, request, obj=None):
        return request.user.is_superuser

    def has_change_permission(self, request, obj=None):
        return request.user.is_superuser

    def has_delete_permission(self, request, obj=None):
        return request.user.is_superuser


class OrderAddressAdmin(admin.ModelAdmin):
    list_display = ('type', 'street', 'city', 'state', 'zipcode')
    search_fields = ('type', 'city', 'state', 'zipcode'),
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


admin.site.register(Service)
admin.site.register(Order)
admin.site.register(Adress)
admin.site.register(OrderDetails)
admin.site.register(Status)