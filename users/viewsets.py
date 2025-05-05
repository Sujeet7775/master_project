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
    
    