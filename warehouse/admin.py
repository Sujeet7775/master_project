from django.contrib import admin
from .models import Warehouse

@admin.register(Warehouse)
class WarehouseAdmin(admin.ModelAdmin):
    list_display = ('warehouse_name', 'warehouse_type', 'zone_type', 'assigned_user', 'state', 'district', 'location', 'pincode', 'contact_no', 'email_id', 'capacity')
    search_fields = ('warehouse_name',)
    readonly_fields = ['created_by', 'updated_by', 'created_at', 'updated_at']
    ordering = ('-created_at',)