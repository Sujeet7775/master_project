from rest_framework.permissions import BasePermission, IsAuthenticated
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from permissions.serializers import PermissionSerializer
from .models import User_Permission
from drf_spectacular.utils import extend_schema
from django.contrib.auth import get_user_model

User = get_user_model()

class CreateSomethingView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, user_id):
        if str(request.user.id) != str(user_id):
            return Response({"detail": "You are not authorized for this user."}, status=status.HTTP_403_FORBIDDEN)

        # Proceed with creation
        return Response({"message": "Authorized and created."})

class HasModulePermission(BasePermission):
    def has_permission(self, request, view):
        print("Authenticated user:", request.user)  # This should be Ram_123, not admin

        print(f"🧪 Checking permission for: {request.user}")
        print(f"➡️  Action: {view.action}")
        
        if not request.user or not request.user.is_authenticated:
            print("❌ User is not authenticated")
            return False

        module = getattr(view, "module_name", None)
        action = getattr(view, "required_permission", None)

        print(f"📦 Module: {module}, 🔐 Action: {action}")

        if not module or not action:
            print("❌ Module or action not defined")
            return False

        perms = User_Permission.objects.filter(user=request.user, module__iexact=module)
        print(f"🔍 Found permissions: {perms}")

        for perm in perms:
            print(f"➡️  Permissions object: {perm.permissions}")
            if perm.permissions.get(action.lower(), False):
                print("✅ Permission granted")
                return True

        print("❌ Permission denied")
        return False
    
from rest_framework.authentication import TokenAuthentication


@extend_schema(tags=["Authentication & Permissions"])
class MyPermissionsView(APIView):
    authentication_classes = [TokenAuthentication]

    permission_classes = [IsAuthenticated]
    
    def get(self, request, user_id):
        try:
            User.objects.get(id=user_id)
        except User.DoesNotExist:
            return Response({"detail": "User not found"}, status=404)

        permissions = User_Permission.objects.filter(user_id=user_id)
        serializer = PermissionSerializer(permissions, many=True)
        return Response(serializer.data)