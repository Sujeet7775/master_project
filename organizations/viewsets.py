from rest_framework import viewsets
from .models import Organization
from .serializers import OrganizationSerializer
from drf_spectacular.utils import extend_schema
from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from .models import Organization
from .serializers import OrganizationSerializer
from .permissions import OrganizationCRUDPermissions
from rest_framework.permissions import IsAuthenticated
from rest_framework.permissions import IsAdminUser
from django.contrib.auth.models import User, Permission

@extend_schema(tags=["Organization"])
# class OrganizationViewSet(viewsets.ModelViewSet):
#     queryset = Organization.objects.all()
#     serializer_class = OrganizationSerializer
#     lookup_field = 'organisation_id'
    


# Create your views here.
class OrganizationViewSet(viewsets.ModelViewSet):
    queryset = Organization.objects.all()
    serializer_class = OrganizationSerializer
    lookup_field = 'organisation_id'
    permission_classes = [IsAuthenticated, IsAdminUser, OrganizationCRUDPermissions]
    # permission_classes = [OrganizationCRUDPermissions]

    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            self.permission_classes = [IsAuthenticated]
        return super().get_permissions()




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