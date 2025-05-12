from rest_framework import viewsets
from .models import Material
from .serializers import MaterialSerializer 
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets, filters
from drf_spectacular.utils import extend_schema

@extend_schema(tags=["Material"])
class MaterialViewSet(viewsets.ModelViewSet):
    queryset = Material.objects.all()
    serializer_class = MaterialSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['material_name', 'material_code']
    permission_classes = [IsAuthenticated]
    model = Material


    # def get_permissions(self):
    #     # Map DRF actions to permission names
    #     action_map = {
    #         "create": "create",
    #         "list": "read",
    #         "retrieve": "view",
    #         "update": "update",
    #         "partial_update": "update",
    #         "destroy": "delete",
    #     }

    #     self.required_permission = action_map.get(self.action)
    #     return [permission() for permission in self.permission_classes]