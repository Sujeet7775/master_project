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
from rest_framework.permissions import IsAdminUser

@extend_schema(tags=["Organization"])
class OrganizationViewSet(viewsets.ModelViewSet):
    queryset = Organization.objects.all()
    serializer_class = OrganizationSerializer
    lookup_field = 'organisation_id'
    permission_classes = [IsAuthenticated, IsAdminUser]

    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            self.permission_classes = [IsAuthenticated]
        return super().get_permissions()



