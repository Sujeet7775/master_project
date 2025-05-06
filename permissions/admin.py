from django.contrib import admin
from .models import User_Permission

@admin.register(User_Permission)
class User_PermissionAdmin(admin.ModelAdmin):
    list_display = ('user', 'module', 'permissions')
    list_filter = ('module',)
    search_fields = ('user__username', 'module')
    ordering = ('user', 'module')