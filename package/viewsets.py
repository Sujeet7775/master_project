# views.py
from rest_framework import viewsets, filters, permissions
from drf_spectacular.utils import extend_schema
from .models import Package
from .serializers import PackageSerializer

@extend_schema(tags=["Package"])
class PackageViewSet(viewsets.ModelViewSet):
    queryset = Package.objects.all()
    serializer_class = PackageSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [filters.SearchFilter]
    search_fields = ['package_name', 'state_name', 'package_code']
    model = Package
    
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
