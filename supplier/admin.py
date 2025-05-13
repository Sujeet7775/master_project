from django.contrib import admin
from .models import  Supplier

@admin.register(Supplier)
class SupplierAdmin(admin.ModelAdmin):
    list_display = ('company_name', 'created_at', 'updated_at')
    search_fields = ('company_name',)
    readonly_fields = ['created_by', 'updated_by', 'created_at', 'updated_at']
    ordering = ('-created_at',)