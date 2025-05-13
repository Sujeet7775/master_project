from rest_framework import viewsets
from .models import UserProfile
from .serializers import  UserProfileSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets, filters
from drf_spectacular.utils import extend_schema

@extend_schema(tags=["User Types"])
class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['user_type']
    permission_classes = [IsAuthenticated]
    model = UserProfile


    # def get_permissions(self):
    #     # Map DRF actions to permission names
    #     action_map = {
    #         "create": "create",
    #         "list": "read",
    #         "retrieve": "view",
    #         "update": "update",
    #         "partial_update": "update",
    #         "destroy": "delete",
    #     }

    #     self.required_permission = action_map.get(self.action)
    #     return [permission() for permission in self.permission_classes]