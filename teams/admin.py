from django.contrib import admin
from .models import Team

@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ('team_name', 'team_lead', 'department')
    list_filter = ('department',)
    search_fields = ('team_name', 'team_lead')
    ordering = ('team_name',)