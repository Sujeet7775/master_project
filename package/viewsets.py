from rest_framework import viewsets, filters, permissions
from drf_spectacular.utils import extend_schema
from .models import Package
from .serializers import PackageSerializer
from rest_framework.response import Response
from rest_framework import status

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

    # Override the create method to handle bulk creation
    def create(self, request, *args, **kwargs):
        if isinstance(request.data, list):
            # Bulk insert
            serializer = self.get_serializer(data=request.data, many=True)
            serializer.is_valid(raise_exception=True)
            self.perform_bulk_create(serializer)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            # Single object fallback
            return super().create(request, *args, **kwargs)

    def perform_bulk_create(self, serializer):
        self.get_queryset().model.objects.bulk_create([
            self.get_serializer().Meta.model(**item) for item in serializer.validated_data
        ])