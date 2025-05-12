from django.contrib import admin
from .models import UOM

@admin.register(UOM)
class UOMAdmin(admin.ModelAdmin):
    list_display = ('uom_name', 'created_at', 'updated_at')
    search_fields = ('uom_name',)
    readonly_fields = ['created_by', 'updated_by', 'created_at', 'updated_at']
    ordering = ('-created_at',)