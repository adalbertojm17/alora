from django.contrib import admin
from django.utils.html import format_html

from .models import Feedback


class FeedbackAdmin(admin.ModelAdmin):
    def delete_button(self, obj):
        return format_html('<a class="btn" href="/admin/accounts/customeraccount/{}/delete/">Delete</a>', obj.id)

    delete_button.allow_tags = True
    delete_button.short_description = 'Delete Feedback'

    list_display = ('store', 'subject', 'delete_button')
    search_fields = ('store', 'subject'),
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
