from django.contrib import admin
from departments.models import Department
from organizations.models import Organization


class DepartmentInline(admin.TabularInline):
    model = Department
    extra = 1  # Number of blank forms to display
    fields = ('department_name', 'head_of_department')
    show_change_link = True


@admin.register(Organization)
class OrganizationAdmin(admin.ModelAdmin):
    list_display = ('organisation_name', 'address', "industry_type")
    search_fields = ('organisation_name', 'address', "industry_type")
    inlines = [DepartmentInline]
