from django.contrib import admin
from .models import HSNCode

@admin.register(HSNCode)
class HSNCodeAdmin(admin.ModelAdmin):
    list_display = ('hsn_code', 'gst_percentage', 'created_at', 'updated_at')
    search_fields = ('hsn_code',)
    readonly_fields = ['created_by', 'updated_by', 'created_at', 'updated_at']
    ordering = ('-created_at',)