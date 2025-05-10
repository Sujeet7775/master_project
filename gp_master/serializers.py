
from core.serializers import BaseAuditSerializer
from .models import GPMaster

class GPMasterSerializer(BaseAuditSerializer):
    class Meta:
        model = GPMaster
        fields = '__all__'
