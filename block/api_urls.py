from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import BlockViewSet

router = DefaultRouter()
router.register(r'', BlockViewSet)

urlpatterns = router.urls
