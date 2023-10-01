from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from users.models import CustomUser


@admin.register(CustomUser)
class UserAdmin(UserAdmin):
    list_display = ('username', 'email', 'user_type', 'is_superuser', 'is_staff')
    filter_horizontal = 'user_permissions',
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal info', {'fields': (
            'first_name', 'last_name', 'email', 'user_type', 'phone')}),
        ('Permissions', {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions'),
        }),
        ('Important dates', {'fields': ('last_login',)}),
    )
    user_fieldsets = (
        (None, {'fields': ('username', 'password', 'phone')}),
        ('Personal info', {'fields': (
            'first_name', 'last_name', 'email', 'user_type')}),
        ('Permissions', {
            'fields': ('is_active', 'is_staff'),
        }),
    )
