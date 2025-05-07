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

@extend_schema(tags=["Organization"])
class OrganizationViewSet(viewsets.ModelViewSet):
    queryset = Organization.objects.all()
    serializer_class = OrganizationSerializer
    permission_classes = [IsAuthenticated, HasModulePermission]
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
















# class OrganizationViewSet(viewsets.ModelViewSet):
#     queryset = Organization.objects.all()
#     serializer_class = OrganizationSerializer
#     lookup_field = 'organisation_id'
#     permission_classes = [IsAuthenticated, IsAdminUser]

#     def get_permissions(self):
#         if self.action in ['list', 'retrieve']:
#             self.permission_classes = [IsAuthenticated]
#         return super().get_permissions()







