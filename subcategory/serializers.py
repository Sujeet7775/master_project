from core.serializers import BaseAuditSerializer
from .models import SubCategory


class SubCategorySerializer(BaseAuditSerializer):
    class Meta:
        model = SubCategory
        fields = '__all__'
        read_only_fields = ['created_by', 'updated_by', 'created_at', 'updated_at']