from rest_framework import viewsets
from .models import Department
from .serializers import DepartmentSerializer
from drf_spectacular.utils import extend_schema

@extend_schema(tags=["Department"])
class DepartmentViewSet(viewsets.ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer
    lookup_field = 'department_id'