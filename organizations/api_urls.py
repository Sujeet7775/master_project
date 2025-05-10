from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import OrganizationViewSet

router = DefaultRouter()
router.register(r'', OrganizationViewSet, basename='organization')

urlpatterns = router.urls