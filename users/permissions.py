from rest_framework.permissions import BasePermission

class HasModelPermission(BasePermission):
    def has_permission(self, request, view):
        action_map = {
            'list': 'can_view',
            'retrieve': 'can_view',
            'create': 'can_create',
            'update': 'can_edit',
            'partial_update': 'can_edit',
            'destroy': 'can_delete',
        }

        model_name = getattr(view, 'model_name', None)
        required_perm = action_map.get(view.action)

        if not model_name or not required_perm:
            return False

        perms = request.user.permissions.filter(model_name=model_name).first()
        return getattr(perms, required_perm, False) if perms else False
