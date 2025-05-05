from django.contrib import admin
from modulemaster.models import ModuleMaster

# Register your models here.
@admin.register(ModuleMaster)
class ModuleMasterAdmin(admin.ModelAdmin):
    list_display = ('module_name', 'app_name', 'actions')
    search_fields = ('module_name', 'app_name')
    list_filter = ('app_name',)
    ordering = ('module_name',)