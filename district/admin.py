from django.contrib import admin
from .models import District

@admin.register(District)
class DistrictAdmin(admin.ModelAdmin):
    list_display = ('district_name', 'district_code', 'package', 'created_at')
    search_fields = ('district_name', 'district_code')
    list_filter = ('package', 'created_at')
    readonly_fields = ['created_by', 'updated_by', 'created_at', 'updated_at']
    ordering = ('-created_at',)
