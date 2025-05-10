from django.contrib import admin
from .models import Block

@admin.register(Block)
class BlockAdmin(admin.ModelAdmin):
    list_display = ('block_name', 'block_code', 'district', 'package')
    search_fields = ('block_name', 'block_code')
    list_filter = ('district', 'package')
    readonly_fields = ['created_by', 'updated_by', 'created_at', 'updated_at']
    ordering = ('-created_at',)
