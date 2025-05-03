# teams/views.py
from rest_framework import viewsets
from .models import Team
from .serializers import TeamSerializer
from drf_spectacular.utils import extend_schema

@extend_schema(tags=["Team"])
class TeamViewSet(viewsets.ModelViewSet):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer
    lookup_field = 'team_id'