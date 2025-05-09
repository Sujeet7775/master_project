from rest_framework import viewsets, permissions
from .models import District
from .serializers import DistrictAdminSerializer
from drf_spectacular.utils import extend_schema

@extend_schema(tags=["District"])
class DistrictAdminViewSet(viewsets.ModelViewSet):
    queryset = District.objects.all()
    serializer_class = DistrictAdminSerializer
    permission_classes = [permissions.IsAdminUser]  # Only admin users can access this
    search_fields = ['district_name', 'district_code']  # Add any other fields you want to search on    
    filterset_fields = ['package']  # Allows filtering by package
    ordering_fields = ['district_name', 'district_code']  # Allows ordering by these fields
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