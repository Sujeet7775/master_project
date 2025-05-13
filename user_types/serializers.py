from core.serializers import BaseAuditSerializer
from .models import UserProfile

class UserProfileSerializer(BaseAuditSerializer):
    class Meta:
        model = UserProfile
        fields = '__all__'
        read_only_fields = ['created_by', 'updated_by', 'created_at', 'updated_at']