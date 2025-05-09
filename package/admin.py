from django.contrib import admin

# Register your models here.
# admin.py
from django.contrib import admin
from .models import Package

@admin.register(Package)
class PackageAdmin(admin.ModelAdmin):
    list_display = ('package_name', 'package_code')
    search_fields = ('package_name', 'package_code', 'state_name')
    list_filter = ('created_at', 'updated_at')
    readonly_fields = ('created_at', 'updated_at', 'created_by', 'updated_by')
