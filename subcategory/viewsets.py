from rest_framework import viewsets
from .models import SubCategory
from .serializers import SubCategorySerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets, filters
from drf_spectacular.utils import extend_schema

@extend_schema(tags=["Subcategory"])
class SubCategoryViewSet(viewsets.ModelViewSet):
    queryset = SubCategory.objects.all()
    serializer_class = SubCategorySerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['sub_category_name']  
    permission_classes = [IsAuthenticated]
    model = SubCategory