from core.serializers import BaseAuditSerializer
from .models import Warehouse

class WarehouseSerializer(BaseAuditSerializer):
    class Meta:
        model = Warehouse
        fields = '__all__'
        read_only_fields = ['created_by', 'updated_by', 'created_at', 'updated_at']