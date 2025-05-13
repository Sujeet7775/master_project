from core.serializers import BaseAuditSerializer
from .models import Supplier

class SupplierSerializer(BaseAuditSerializer):
    class Meta:
        model = Supplier
        fields = '__all__'
        read_only_fields = ['created_by', 'updated_by', 'created_at', 'updated_at']