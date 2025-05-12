from core.serializers import BaseAuditSerializer
from .models import UOM

class UOMSerializer(BaseAuditSerializer):
    class Meta:
        model = UOM
        fields = '__all__'
        read_only_fields = ['created_by', 'updated_by', 'created_at', 'updated_at']