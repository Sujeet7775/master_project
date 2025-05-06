from rest_framework import serializers
from .models import User

from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


# class UserSerializer(serializers.ModelSerializer):
#     # permissions = PermissionSerializer(many=True, read_only=True)
#     permission_ids = serializers.PrimaryKeyRelatedField(
#         many=True, queryset=Permission.objects.all(), write_only=True, source='permissions'
#     )

#     class Meta:
#         model = User
#         fields = [
#             'id', 'username', 'email', 'first_name', 'last_name',
#             'user_id', 'organization', 'department', 'team',
#             'mobile_number', 'role', 'state', 'city', 'country', 'pincode',
#             'approval_1', 'approval_2', 'permissions', 'permission_ids',
#         ]




# class UserSerializer(serializers.ModelSerializer):
#     permissions = PermissionSerializer(many=True, required=False)

#     class Meta:
#         model = User
#         fields = ('id', 'username', 'first_name', 'last_name', 'email', 'permissions')

#     def create(self, validated_data):
#         permissions_data = validated_data.pop('permissions', [])
#         user = User.objects.create(**validated_data)

#         for perm_data in permissions_data:
#             perm, _ = Permission.objects.get_or_create(**perm_data)
#             user.permissions.add(perm)

#         return user
