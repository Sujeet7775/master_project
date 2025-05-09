from rest_framework import serializers
from .models import User_Permission

class PermissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = User_Permission
        fields = ['id', 'user', 'module', 'permissions']
        read_only_fields = ['id']

    def validate_permissions(self, value):
        # Optional: define which keys are required
        required_keys = {'create', 'update', 'view'}
        missing = required_keys - value.keys()
        if missing:
            raise serializers.ValidationError(f"Missing required keys: {missing}")
        
        for key, val in value.items():
            if not isinstance(val, bool):
                raise serializers.ValidationError(f"Permission '{key}' must be a boolean.")

        return value





