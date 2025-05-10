from core.serializers import BaseAuditSerializer
from .models import Category

class CategorySerializer(BaseAuditSerializer):
    class Meta:
        model = Category
        fields = '__all__'
        read_only_fields = ['created_by', 'updated_by', 'created_at', 'updated_at']