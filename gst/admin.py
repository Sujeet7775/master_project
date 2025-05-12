from django.contrib import admin
from .models import GST

@admin.register(GST)
class GSTAdmin(admin.ModelAdmin):
    list_display = ('gst_percentage', 'created_at', 'updated_at')
    search_fields = ('gst_percentage',)
    readonly_fields = ['created_by', 'updated_by', 'created_at', 'updated_at']
    ordering = ('-created_at',)