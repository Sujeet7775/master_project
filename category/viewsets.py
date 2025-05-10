from rest_framework import viewsets
from .models import Category
from .serializers import CategorySerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets, filters
from drf_spectacular.utils import extend_schema

@extend_schema(tags=["Category"])
class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['category_name']  
    permission_classes = [IsAuthenticated]
    model = Category
    
    
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