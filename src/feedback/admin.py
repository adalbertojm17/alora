from django.contrib import admin
from django.utils.html import format_html

from .models import Feedback


class FeedbackAdmin(admin.ModelAdmin):
    def delete_button(self, obj):
        return format_html('<a class="btn" href="/admin/feedback/feedback/{}/delete/">Delete</a>', obj.id)

    delete_button.allow_tags = True
    delete_button.short_description = 'Delete Feedback'

    list_display = ('id', 'store', 'subject', 'delete_button')
    search_fields = ('store', 'subject'),
    readonly_fields = ()

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()

    def get_readonly_fields(self, request, obj=None):
        if obj:
            return self.readonly_fields + ('store', 'subject', 'content')
        return self.readonly_fields

    def has_add_permission(self, request, obj=None):
        return request.user.is_superuser

    def has_change_permission(self, request, obj=None):
        return request.user.is_superuser

    def has_delete_permission(self, request, obj=None):
        return request.user.is_superuser


admin.site.register(Feedback, FeedbackAdmin)
