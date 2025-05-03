from rest_framework import viewsets
from .models import Organization
from .serializers import OrganizationSerializer
from drf_spectacular.utils import extend_schema
from django.contrib.auth.models import Permission
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.contenttypes.models import ContentType
from users.models import User  # your custom User model

@extend_schema(tags=["Organization"])
class OrganizationViewSet(viewsets.ModelViewSet):
    queryset = Organization.objects.all()
    serializer_class = OrganizationSerializer
    lookup_field = 'organisation_id'

# class AssignOrgPermissionsView(APIView):
#     def post(self, request, user_id):
#         permissions = request.data.get("permissions", [])
#         try:
#             user = User.objects.get(id=user_id)
#         except User.DoesNotExist:
#             return Response({"error": "User not found"}, status=404)

#         # Clear existing org permissions
#         content_type = ContentType.objects.get(app_label='organizations', model='organization')
#         org_permissions = Permission.objects.filter(content_type=content_type)
#         user.user_permissions.remove(*org_permissions)

#         # Assign new ones
#         for codename in permissions:
#             try:
#                 perm = Permission.objects.get(codename=codename)
#                 user.user_permissions.add(perm)
#             except Permission.DoesNotExist:
#                 continue

#         return Response({"status": "Permissions updated successfully"}, status=200)