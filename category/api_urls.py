from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import CategoryViewSet

router = DefaultRouter()
router.register(r'', CategoryViewSet)

urlpatterns = router.urls