from django.contrib import admin

# Register your models here.
from webapp.models import Guest


class TaskAdmin(admin.ModelAdmin):
    list_display = ['id', 'text', 'status', 'created_at', 'author']
    list_display_links = ['author']
    list_filter = ['created_at']
    search_fields = ['created_at']
    fields = ['text', 'status', 'created_at', 'author']
    readonly_fields = []


admin.site.register(Guest, TaskAdmin)