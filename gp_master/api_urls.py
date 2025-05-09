from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import GPMasterViewSet

router = DefaultRouter()
router.register(r'gp-masters', GPMasterViewSet)

urlpatterns = router.urls