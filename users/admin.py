from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django import forms
from .models import User

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
                'mobile_number','user_type',
                'state', 'city', 'country', 'pincode',
                'approval_1', 'approval_2',
                
            )
        }),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
        ('Status', {'fields': ('is_active', 'is_superuser')}),
    )
    list_display = ('username', 'email', 'first_name', 'last_name', 'organization', 'user_type', 'is_active')
    list_filter = ('organization', 'department', 'team', 'is_active', 'is_superuser', 'user_type')
    search_fields = ('username', 'email', 'first_name', 'last_name', 'mobile_number')
    ordering = ('username',)


