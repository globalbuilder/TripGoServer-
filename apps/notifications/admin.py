# apps/notifications/admin.py

from django.contrib import admin
from .models import Notification

@admin.register(Notification)
class NotificationAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'is_broadcast', 'user', 'created_at')
    list_filter = ('is_broadcast', 'user')
    search_fields = ('title', 'message', 'user__username')
    ordering = ('-created_at',)
