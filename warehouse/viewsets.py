from rest_framework import viewsets
from .models import Warehouse
from .serializers import WarehouseSerializer 
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets, filters
from drf_spectacular.utils import extend_schema

@extend_schema(tags=["Warehouse"])
class WarehouseViewSet(viewsets.ModelViewSet):
    queryset = Warehouse.objects.all()
    serializer_class = WarehouseSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['warehouse_name']
    permission_classes = [IsAuthenticated]
    model = Warehouse


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