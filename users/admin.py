from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django import forms
from .models import User, Permission, Organization, Department, Team

class CustomUserChangeForm(forms.ModelForm):
    class Meta:
        model = User
        exclude = ('groups', 'user_permissions',)

@admin.register(User)
class CustomUserAdmin(BaseUserAdmin):
    form = CustomUserChangeForm

    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'email')}),
        ('Organization Info', {
            'fields': (
                'organization', 'department', 'team',
                'mobile_number', 'role',
                'state', 'city', 'country', 'pincode',
                'approval_1', 'approval_2',
                'permissions',
            )
        }),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
        ('Status', {'fields': ('is_active', 'is_superuser')}),
    )

    filter_horizontal = ('permissions',)
    list_display = ('username', 'email', 'first_name', 'last_name', 'organization', 'role', 'is_active')
    list_filter = ('organization', 'department', 'team', 'is_active', 'is_superuser')
    search_fields = ('username', 'email', 'first_name', 'last_name', 'mobile_number')
    ordering = ('username',)

@admin.register(Permission)
class PermissionAdmin(admin.ModelAdmin):
    list_display = ('model_name', 'can_view', 'can_create', 'can_edit', 'can_delete')
    search_fields = ('model_name',)


