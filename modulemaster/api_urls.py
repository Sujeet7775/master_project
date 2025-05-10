from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import ModuleMasterViewSet

router = DefaultRouter()
router.register(r'', ModuleMasterViewSet, basename='modulemaster')

urlpatterns = [
    path('', include(router.urls)),
]
