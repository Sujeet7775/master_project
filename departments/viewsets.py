# from rest_framework import viewsets

# from drf_spectacular.utils import extend_schema

# @extend_schema(tags=["Department"])
# class DepartmentViewSet(viewsets.ModelViewSet):
#     queryset = Department.objects.all()
#     serializer_class = DepartmentSerializer
#     lookup_field = 'department_id'
    
    
from rest_framework import viewsets
from drf_spectacular.utils import extend_schema
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.permissions import IsAuthenticated
from permissions.permissions import HasModulePermission
from .models import Department
from .serializers import DepartmentSerializer


@extend_schema(tags=["Department"])
class DepartmentViewSet(viewsets.ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer
    lookup_field = 'department_id'
    permission_classes = [IsAuthenticated, HasModulePermission]
    module_name = "Department"

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

















