from django.contrib import admin
from teams.models import Team
from .models import Department

class TeamInline(admin.TabularInline):
    model = Team
    extra = 1
    fields = ('team_name', 'team_lead')
    show_change_link = True


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ( 'department_name', 'head_of_department', 'organisation')
    search_fields = ('department_name', 'head_of_department')
    list_filter = ('organisation',)
    inlines = [TeamInline]
