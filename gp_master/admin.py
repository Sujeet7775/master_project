from django.contrib import admin
from .models import GPMaster

@admin.register(GPMaster)
class GPMasterAdmin(admin.ModelAdmin):
    list_display = ('gp_name', 'lgd_code', 'district', 'block', 'package', 'covered', 'gp_status', 'sr_status')
    search_fields = ('gp_name', 'lgd_code')
    list_filter = ('district', 'block', 'package', 'covered', 'gp_status', 'sr_status')
    readonly_fields = ('created_at', 'updated_at', 'created_by', 'updated_by')
    