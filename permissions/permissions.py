from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import BasePermission, IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from drf_spectacular.utils import extend_schema
from django.contrib.auth import get_user_model
from permissions.serializers import PermissionSerializer
from .models import User_Permission
import logging

logger = logging.getLogger(__name__)
User = get_user_model()
class HasModulePermission(BasePermission):
    """
    Custom permission that checks whether the authenticated user has the required
    action permission for a specific module.
    """

    def has_permission(self, request, view):
        user = request.user

        if not user or not user.is_authenticated:
            logger.warning("User is not authenticated.")
            return False

        module = getattr(view, "module_name", None)
        required_action = getattr(view, "required_permission", None)

        if not module or not required_action:
            logger.warning("Module or required permission not specified on the view.")
            return False

        permissions_qs = User_Permission.objects.filter(user=user, module__iexact=module)
        logger.debug(f"User '{user}' has module permissions: {permissions_qs}")

        for perm in permissions_qs:
            if perm.permissions.get(required_action.lower(), False):
                logger.info(f"Permission granted for {user} on {module}:{required_action}")
                return True

        logger.warning(f"Permission denied for {user} on {module}:{required_action}")
        return False


@extend_schema(tags=["Authentication & Permissions"],responses=PermissionSerializer)
class MyPermissionsView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, user_id):
        try:
            User.objects.get(id=user_id)
        except User.DoesNotExist:
            return Response({"detail": "User not found."}, status=status.HTTP_404_NOT_FOUND)

        permissions = User_Permission.objects.filter(user_id=user_id)
        serializer = PermissionSerializer(permissions, many=True)
        return Response(serializer.data)
