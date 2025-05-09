from warnings import filters
from rest_framework import viewsets, permissions
from .models import District
from .serializers import DistrictAdminSerializer
from drf_spectacular.utils import extend_schema
from rest_framework import viewsets, filters, permissions

@extend_schema(tags=["District"])
class DistrictAdminViewSet(viewsets.ModelViewSet):
    queryset = District.objects.all()
    serializer_class = DistrictAdminSerializer
    permission_classes = [permissions.IsAuthenticated]
    search_fields = ['district_name', 'district_code']  # Add any other fields you want to search on    
    filter_backends = [filters.SearchFilter]
    model = District
    
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