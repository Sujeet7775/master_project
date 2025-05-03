from rest_framework import serializers
from .models import User, Permission

class PermissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Permission
        fields = ['id', 'name', 'description']

class UserSerializer(serializers.ModelSerializer):
    permissions = PermissionSerializer(many=True, read_only=True)
    permission_ids = serializers.PrimaryKeyRelatedField(
        many=True, queryset=Permission.objects.all(), write_only=True, source='permissions'
    )

    class Meta:
        model = User
        fields = [
            'id', 'username', 'email', 'first_name', 'last_name',
            'user_id', 'organization', 'department', 'team',
            'mobile_number', 'role', 'state', 'city', 'country', 'pincode',
            'approval_1', 'approval_2', 'permissions', 'permission_ids',
        ]
