from core.serializers import BaseAuditSerializer
from .models import GST

class GSTSerializer(BaseAuditSerializer):
    class Meta:
        model = GST
        fields = '__all__'
        read_only_fields = ['created_by', 'updated_by', 'created_at', 'updated_at']