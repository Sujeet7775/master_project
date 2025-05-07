from rest_framework.permissions import BasePermission, IsAuthenticated
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from permissions.serializers import PermissionSerializer
from .models import User_Permission
from drf_spectacular.utils import extend_schema
from django.contrib.auth import get_user_model

User = get_user_model()

class HasModulePermission(BasePermission):
    def has_permission(self, request, view):
        if not request.user or not request.user.is_authenticated:
            print("❌ User is not authenticated")
            return False

        module = getattr(view, "module_name", None)
        action = getattr(view, "required_permission", None)

        print(f"🔐 Authenticated user: {request.user}")
        print(f"🔎 Checking module: {module}, required action: {action}")

        if not module or not action:
            return False

        perms = User_Permission.objects.filter(user=request.user, module__iexact=module)

        if not perms.exists():
            print(f"❌ No permissions found for user {request.user} in module '{module}'")
            return False

        for perm in perms:
            print(f"✅ Found permissions: {perm.permissions}")
            if perm.permissions.get(action.lower(), False):
                print("✅ Permission granted")
                return True

        print("❌ Permission denied")
        return False


@extend_schema(tags=["Authentication & Permissions"])
class MyPermissionsView(APIView):
    permission_classes = [IsAuthenticated]
    
    def get(self, request, user_id):
        try:
            User.objects.get(id=user_id)
        except User.DoesNotExist:
            return Response({"detail": "User not found"}, status=404)

        permissions = User_Permission.objects.filter(user_id=user_id)
        serializer = PermissionSerializer(permissions, many=True)
        return Response(serializer.data)

    # def get(self, request):
    #     user = request.user
    #     print(f"🔍 Request user: {user}, ID: {user.id}, Is superuser: {user.is_superuser}")

    #     user_permissions = User_Permission.objects.filter(user=user)
    #     print(f"🔍 User permissions for {user}: {user_permissions}")

    #     permissions_by_module = {}

    #     for perm in user_permissions:
    #         module = perm.module.strip().title()  # Normalize for output
    #         if module not in permissions_by_module:
    #             permissions_by_module[module] = perm.permissions.copy()
    #         else:
    #             for key, value in perm.permissions.items():
    #                 permissions_by_module[module][key] = (
    #                     permissions_by_module[module].get(key, False) or value
    #                 )

    #     return Response({
    #         "user": str(user),
    #         "permissions": permissions_by_module
    #     })
