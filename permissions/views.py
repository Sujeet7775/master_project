from rest_framework import viewsets
from .models import User_Permission
from drf_spectacular.utils import extend_schema
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from .models import User_Permission
from .serializers import PermissionSerializer 

@extend_schema(tags=["Permissions"],responses=PermissionSerializer)
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