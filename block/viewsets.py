from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Block
from .serializers import BlockSerializer
from drf_spectacular.utils import extend_schema
from rest_framework import viewsets, filters, permissions

@extend_schema(tags=["Block"])
class BlockViewSet(viewsets.ModelViewSet):
    queryset = Block.objects.all()
    serializer_class = BlockSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [filters.SearchFilter]
    search_fields = ['block_name', 'block_code']
    model = Block

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