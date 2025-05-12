from rest_framework.routers import DefaultRouter
from .viewsets import HSNCodeViewSet

router = DefaultRouter()
router.register(r'', HSNCodeViewSet)

urlpatterns = router.urls