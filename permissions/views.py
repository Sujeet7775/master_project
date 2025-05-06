# views.py
from rest_framework import viewsets
from .models import User_Permission
from .serializers import PermissionSerializer
from drf_spectacular.utils import extend_schema


@extend_schema(tags=["Permissions"])
class PermissionViewSet(viewsets.ModelViewSet):
    queryset = User_Permission.objects.all()
    serializer_class = PermissionSerializer
