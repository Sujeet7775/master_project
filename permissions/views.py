from rest_framework import viewsets
from drf_spectacular.utils import extend_schema
from .models import User_Permission
from .serializers import PermissionSerializer
from rest_framework.permissions import IsAuthenticated
from drf_spectacular.utils import extend_schema
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework import status
from rest_framework.exceptions import PermissionDenied
from django.contrib.auth.models import User
from .models import User_Permission
from .serializers import PermissionSerializer 

@extend_schema(tags=["Permissions"])
class PermissionViewSet(viewsets.ModelViewSet):     
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




class VerifyTokenView(APIView):
    """
    View to verify the token and check if it's valid.
    """

    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        """
        Verifies the token and returns the user data.
        """
        user = request.user  # request.user will automatically be populated from the token

        return Response(
            {
                "message": "Token is valid",
                "user_id": user.id,
                "username": user.username,
                "permissions": self.get_user_permissions(user),
            }
        )

    def get_user_permissions(self, user):
        """
        Fetches permissions for the respective user.
        """
        # Assuming the permissions are stored in a model `UserPermissions` as a relationship to modules
        permissions = User_Permission.objects.filter(user=user)
        permission_data = PermissionSerializer(permissions, many=True).data
        return permission_data


class UserPermissionsView(APIView):
    """
    View to fetch the user permissions for each module.
    """

    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        """
        Fetches the permissions for the logged-in user.
        """
        user = request.user  # request.user will automatically be populated from the token

        # Fetch user permissions (assumes you have a model named UserPermissions)
        permissions = User_Permission.objects.filter(user=user)

        if not permissions:
            raise PermissionDenied("No permissions found for this user.")
        
        return Response(
            {
                "message": "User permissions fetched successfully.",
                "permissions": permissions,
            }
        )