from django.contrib import admin
from .models import SubCategory

# Register your models here.
@admin.register(SubCategory)
class SubCategoryAdmin(admin.ModelAdmin):
    list_display = ('sub_category_name', 'category', 'created_at', 'updated_at')
    search_fields = ('sub_category_name',)
    readonly_fields = ['created_by', 'updated_by', 'created_at', 'updated_at']
    ordering = ('-created_at',)
