from django.contrib import admin

# Register your models here.
from webapp.models import Guest


class GuestAdmin(admin.ModelAdmin):
    list_display = ['id', 'text', 'status', 'created_at', 'author', 'updated_at']
    list_display_links = ['author']
    list_filter = ['created_at']
    search_fields = ['created_at']
    fields = ['text', 'status', 'created_at', 'author']
    readonly_fields = ['created_at', 'updated_at']


admin.site.register(Guest, GuestAdmin)
