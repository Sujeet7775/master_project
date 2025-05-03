from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
def user_list(request):
    return JsonResponse({'message': 'List of users'})


from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Organization, Permission
from .serializers import UserSerializer, PermissionSerializer
from .permissions import HasModelPermission

class OrganizationViewSet(viewsets.ModelViewSet):
    queryset = Organization.objects.all()
    serializer_class = UserSerializer  # Replace if you have OrgSerializer
    permission_classes = [IsAuthenticated, HasModelPermission]
    model_name = 'organization'

class MyPermissionsView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        permissions = request.user.permissions.all()
        data = {}
        for perm in permissions:
            data[perm.model_name] = {
                'view': perm.can_view,
                'create': perm.can_create,
                'edit': perm.can_edit,
                'delete': perm.can_delete,
            }
        return Response({'permissions': data})
