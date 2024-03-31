from django.contrib import admin

from app_users.models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('pk', 'phone', 'phone_verify', 'email', 'invite_code', 'active_invite_code')
