from rest_framework import viewsets
from .models import Organization
from .serializers import OrganizationSerializer
from drf_spectacular.utils import extend_schema
from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from .models import Organization
from .serializers import OrganizationSerializer
from rest_framework.permissions import IsAuthenticated
from permissions.permissions import HasModulePermission
from rest_framework.authentication import TokenAuthentication


@extend_schema(tags=["Organization"])
class OrganizationViewSet(viewsets.ModelViewSet):
    queryset = Organization.objects.all()
    serializer_class = OrganizationSerializer
    permission_classes = [IsAuthenticated, HasModulePermission]
    # authentication_classes = [TokenAuthentication]  # Only Token-based auth is allowed
    module_name = "Organization"

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






