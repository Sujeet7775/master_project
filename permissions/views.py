from rest_framework import viewsets
from drf_spectacular.utils import extend_schema
from .models import User_Permission
from .serializers import PermissionSerializer
from rest_framework.permissions import IsAuthenticated
from drf_spectacular.utils import extend_schema

@extend_schema(tags=["Permissions"])
class PermissionViewSet(viewsets.ModelViewSet):
    # '''
    # ViewSet for managing user permissions.
    # Allows listing, creating, updating, and deleting permissions.
    # '''
    # queryset = User_Permission.objects.all()
    # # print("🔍 Permissions Queryset:", queryset)
    # serializer_class = PermissionSerializer
    # permission_classes = [IsAuthenticated]

    # def list(self, request, *args, **kwargs):
    #     # You can filter for current user if needed:
    #     if not request.user.is_superuser:
    #         self.queryset = self.queryset.filter(user=request.user)
    #         print(f"🔍 Filtered Queryset for user {request.user}: {self.queryset}")
    #     else:
    #         print("🔍 Superuser access, no filtering applied.")
            
    #     response = super().list(request, *args, **kwargs)

    #     print("🔍 Permissions List Requested:")
    #     for item in response.data:
    #         print(item)

    #     return response
    
    """
    ViewSet for managing user permissions.
    Shows permissions for the authenticated user.
    """
    queryset = User_Permission.objects.all()
    serializer_class = PermissionSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        if self.request.user.is_superuser:
            return User_Permission.objects.all()
        return User_Permission.objects.filter(user=self.request.user)
