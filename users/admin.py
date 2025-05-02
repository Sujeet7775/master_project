from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from users.models import User

@admin.register(User)
class CustomUserAdmin(UserAdmin):
    model = User
    list_display = ('username', 'email', 'first_name', 'last_name', 'organization', 'department', 'team', 'role', 'is_active')
    list_filter = ('organization', 'department', 'team', 'is_active', 'is_staff', 'is_superuser')
    search_fields = ('username', 'email', 'first_name', 'last_name', 'mobile_number')
    ordering = ('username',)

    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal Info', {'fields': ('first_name', 'last_name', 'email', 'mobile_number', 'role')}),
        ('Organization Info', {'fields': ('organization', 'department', 'team')}),
        ('Address', {'fields': ('state', 'city', 'country', 'pincode')}),
        ('Approvals', {'fields': ('approval_1', 'approval_2')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important Dates', {'fields': ('last_login', 'date_joined')}),
    )