from rest_framework import viewsets
from .models import GST
from .serializers import GSTSerializer 
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets, filters
from drf_spectacular.utils import extend_schema

@extend_schema(tags=["GST"])
class GSTViewSet(viewsets.ModelViewSet):
    queryset = GST.objects.all()
    serializer_class = GSTSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['gst_percentage']
    permission_classes = [IsAuthenticated]
    model = GST