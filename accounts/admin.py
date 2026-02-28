from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User


@admin.register(User)
class CustomUserAdmin(UserAdmin):
    # Add 'role' to the list view (the main table)
    list_display = ('username', 'email', 'role', 'is_staff')

    # Add 'role' to the filter sidebar
    list_filter = ('role', 'is_staff', 'is_superuser')

    # This adds the 'role' field to the User Edit/Add pages
    # We append it to the existing 'Personal info' section or create a new one
    fieldsets = UserAdmin.fieldsets + (
        ('Profile Role', {'fields': ('role',)}),
    )

    # This ensures the 'role' field is also there when creating a user
    add_fieldsets = UserAdmin.add_fieldsets + (
        ('Profile Role', {'fields': ('role',)}),
    )