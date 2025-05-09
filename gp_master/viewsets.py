from rest_framework import viewsets, filters, permissions
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import GPMaster
from .serializers import GPMasterSerializer
from drf_spectacular.utils import extend_schema

@extend_schema(tags=["GP Master"])
class GPMasterViewSet(viewsets.ModelViewSet):
    queryset = GPMaster.objects.all()
    serializer_class = GPMasterSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [filters.SearchFilter]
    search_fields = ['gp_name', 'lgd_code', 'district__name', 'block__name', 'package__package_name']   
    model = GPMaster
    
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