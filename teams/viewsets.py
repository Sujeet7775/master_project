# teams/views.py
from rest_framework import viewsets
from .models import Team
from .serializers import TeamSerializer
from drf_spectacular.utils import extend_schema
from permissions.permissions import HasModulePermission
from rest_framework.permissions import IsAuthenticated

@extend_schema(tags=["Team"])
class TeamViewSet(viewsets.ModelViewSet):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer
    permission_classes = [IsAuthenticated, HasModulePermission]
    module_name = "Team"
    lookup_field = 'team_id'
    
    def get_permissions(self):
        # Map DRF actions to permission names
        action_map = {
            "create": "create",
            "list": "read",
            "retrieve": "view",
            "update": "update",
            "partial_update": "update",
            "destroy": "delete",
        }
        self.required_permission = action_map.get(self.action)
        return [permission() for permission in self.permission_classes]
  
