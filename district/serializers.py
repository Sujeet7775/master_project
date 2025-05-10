from .models import District
from core.serializers import BaseAuditSerializer  # ✅ Import from core
class DistrictAdminSerializer(BaseAuditSerializer):
    class Meta:
        model = District
        fields = ['id', 'package', 'district_name', 'district_code', 'created_by', 'updated_by', 'created_at', 'updated_at']
