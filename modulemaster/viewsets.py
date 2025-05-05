
    
from rest_framework import viewsets
from drf_spectacular.utils import extend_schema
from modulemaster.models import ModuleMaster
from modulemaster.serializers import ModuleMasterSerializer

@extend_schema(tags=["ModuleMaster"])
class ModuleMasterViewSet(viewsets.ModelViewSet):
    queryset = ModuleMaster.objects.all()
    serializer_class = ModuleMasterSerializer
