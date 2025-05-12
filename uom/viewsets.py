from rest_framework import viewsets
from .models import UOM
from .serializers import UOMSerializer 
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets, filters
from drf_spectacular.utils import extend_schema

@extend_schema(tags=["UOM"])
class UOMViewSet(viewsets.ModelViewSet):
    queryset = UOM.objects.all()
    serializer_class = UOMSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['uom_name']
    permission_classes = [IsAuthenticated]
    model = UOM


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