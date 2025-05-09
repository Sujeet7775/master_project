from django.urls import path
from rest_framework.routers import DefaultRouter
from .viewsets import DistrictAdminViewSet

router = DefaultRouter()
router.register(r'districts', DistrictAdminViewSet, basename='district')

urlpatterns = router.urls
