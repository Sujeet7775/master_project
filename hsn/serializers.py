from core.serializers import BaseAuditSerializer
from .models import HSNCode


class HSNCodeSerializer(BaseAuditSerializer):
    class Meta:
        model = HSNCode
        fields = '__all__'
        read_only_fields = ['created_by', 'updated_by', 'created_at', 'updated_at']

