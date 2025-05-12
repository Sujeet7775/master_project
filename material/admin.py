from django.contrib import admin

from material.models import Material

# Register your models here.
@admin.register(Material)
class MaterialAdmin(admin.ModelAdmin):
    list_display = ('material_name', 'material_code', 'material_type')
    search_fields = ('material_name', 'material_code')
    readonly_fields = ['created_by', 'updated_by', 'created_at', 'updated_at']
    ordering = ('-created_at',)