# urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import PackageViewSet

router = DefaultRouter()
router.register(r'', PackageViewSet, basename='package')

urlpatterns = router.urls