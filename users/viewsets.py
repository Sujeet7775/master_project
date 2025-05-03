from rest_framework import viewsets
from .models import User
from .serializers import UserSerializer
from rest_framework.permissions import IsAuthenticated  # optional
from drf_spectacular.utils import extend_schema
from rest_framework.permissions import BasePermission


@extend_schema(tags=["User"])
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]  # Optional: require login
    lookup_field = 'user_id'  # Use user_id as the lookup field instead of id
    
    

class HasModelPermission(BasePermission):
    def has_permission(self, request, view):
        model_name = view.model_name  # We'll set this on the ViewSet
        action_map = {
            'list': 'can_view',
            'retrieve': 'can_view',
            'create': 'can_create',
            'update': 'can_edit',
            'partial_update': 'can_edit',
            'destroy': 'can_delete',
        }
        required_perm = action_map.get(view.action)
        if not required_perm:
            return False

        user_perms = request.user.permissions.filter(model_name=model_name)
        if not user_perms.exists():
            return False

        return getattr(user_perms.first(), required_perm, False)