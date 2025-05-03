from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from users.models import User
from django.contrib import admin
from .models import Permission  # adjust the import if needed

# @admin.register(User)
# class CustomUserAdmin(UserAdmin):
#     model = User
#     list_display = ('username', 'email', 'first_name', 'last_name', 'organization', 'department', 'team', 'role', 'is_active')
#     list_filter = ('organization', 'department', 'team', 'is_active', 'is_staff', 'is_superuser')
#     search_fields = ('username', 'email', 'first_name', 'last_name', 'mobile_number')
#     ordering = ('username',)

#     fieldsets = UserAdmin.fieldsets + (
#         ("Custom Fields", {
#             "fields": (
#                 "organization", "department", "team",
#                 "mobile_number", "role",
#                 "state", "city", "country", "pincode",
#                 "approval_1", "approval_2",
#                 "permissions",  # this adds your custom permissions field
#             )
#         }),
#     )

#     filter_horizontal = ("permissions",)  # better UI for many-to-many fields   


# @admin.register(Permission)
# class PermissionAdmin(admin.ModelAdmin):
#     list_display = ('name', 'description')
#     search_fields = ('name',)


from django import forms
from .models import User, Permission

# Optional: create a custom form to remove user_permissions and groups
class CustomUserChangeForm(forms.ModelForm):
    class Meta:
        model = User
        exclude = ('user_permissions', 'groups')

@admin.register(User)
class UserAdmin(UserAdmin):
    form = CustomUserChangeForm

    # Define only the fields you want to show in admin
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'email')}),
        ('Organization Info', {
            'fields': (
                'organization', 'department', 'team',
                'mobile_number', 'role',
                'state', 'city', 'country', 'pincode',
                'approval_1', 'approval_2',
                'permissions',  # your custom permission model
            )
        }),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
        ('Status', {'fields': ('is_active', 'is_superuser')}),
        # Don't include 'is_staff', 'groups', or 'user_permissions' here
    )

    # Hide from the form widget layout
    filter_horizontal = ("permissions",)   # do NOT include user_permissions or groups

    list_display = ('username', 'email', 'first_name', 'last_name', 'is_superuser')
    search_fields = ('username', 'email', 'first_name', 'last_name')