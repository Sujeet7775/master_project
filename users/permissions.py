from rest_framework.permissions import BasePermission

# class HasModelPermission(BasePermission):
#     def has_permission(self, request, view):
#         action_map = {
#             'list': 'can_view',
#             'retrieve': 'can_view',
#             'create': 'can_create',
#             'update': 'can_edit',
#             'partial_update': 'can_edit',
#             'destroy': 'can_delete',
#         }

#         model_name = getattr(view, 'model_name', None)
#         required_perm = action_map.get(view.action)

#         if not model_name or not required_perm:
#             return False

#         perms = request.user.permissions.filter(model_name=model_name).first()
#         return getattr(perms, required_perm, False) if perms else False





from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User, Permission
from django.apps import apps

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def user_permissions(request):
    user = request.user
    user_perms = user.get_user_permissions()

    # Create a map of model → {CRUD: True/False}
    permissions_by_model = {}

    for perm in user_perms:
        # Format: "app_label.codename"
        app_label, codename = perm.split('.')
        parts = codename.split('_')  # e.g. ["can", "create", "book"]

        if len(parts) < 3:
            continue  # Skip unexpected formats

        action = parts[1].capitalize()  # e.g. "Create"
        model = parts[2].capitalize()   # e.g. "Book"

        # Initialize model entry if not present
        if model not in permissions_by_model:
            permissions_by_model[model] = {
                "Create": False,
                "Read": False,
                "Update": False,
                "Delete": False
            }

        # Set permission to True
        if action in permissions_by_model[model]:
            permissions_by_model[model][action] = True

    return Response({
        "username": user.username,
        "permissions": permissions_by_model
    })


@api_view(['POST', 'PUT'])
@permission_classes([IsAdminUser])
def assign_model_permissions(request):
    username = request.data.get('username')
    models = request.data.get('models')  # List
    actions = request.data.get('actions')  # List

    if not username or not models or not actions:
        return Response(
            {"error": "username, models, and actions are required."},
            status=status.HTTP_400_BAD_REQUEST
        )

    try:
        user = User.objects.get(username=username)
    except User.DoesNotExist:
        return Response({"error": "User not found."}, status=status.HTTP_404_NOT_FOUND)

    valid_actions = {"Create", "Read", "Update", "Delete"}
    invalid = [a for a in actions if a.capitalize() not in valid_actions]
    if invalid:
        return Response({"error": f"Invalid actions: {invalid}"}, status=400)

    all_possible_model_perms = []
    assigned_perms = []

    for model_name in models:
        model = model_name.lower()
        for action in valid_actions:
            all_possible_model_perms.append(f"can_{action.lower()}_{model}")  # For cleanup if PUT

        for action in actions:
            codename = f"can_{action.lower()}_{model}"
            perm = Permission.objects.filter(codename=codename).first()
            if perm:
                assigned_perms.append(perm)
            else:
                assigned_perms.append(f"{codename} (NOT FOUND)")

    # Handle PUT: Clear model-related permissions before assigning
    if request.method == 'PUT':
        existing_perms = Permission.objects.filter(codename__in=all_possible_model_perms)
        user.user_permissions.remove(*existing_perms)

    # Add only valid Permission objects
    for perm in assigned_perms:
        if isinstance(perm, Permission):
            user.user_permissions.add(perm)

    return Response({
        "message": f"{request.method} permissions updated for {username}.",
        "assigned_permissions": [p.codename if isinstance(p, Permission) else p for p in assigned_perms]
    })
