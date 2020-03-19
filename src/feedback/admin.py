from django.contrib import admin
from .models import Feedback


class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'services', 'content')
    search_fields = ('first_name', 'last_name', 'email', 'services'),
    readonly_fields = list_display

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()

    def has_add_permission(self, request, obj=None):
        return request.user.is_superuser

    def has_change_permission(self, request, obj=None):
        return request.user.is_superuser

    def has_delete_permission(self, request, obj=None):
        return request.user.is_superuser


admin.site.register(Feedback, FeedbackAdmin)
