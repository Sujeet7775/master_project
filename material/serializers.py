from core.serializers import BaseAuditSerializer
from .models import Material

class MaterialSerializer(BaseAuditSerializer):
    class Meta:
        model = Material
        fields = '__all__'
        read_only_fields = ['created_by', 'updated_by', 'created_at', 'updated_at']