from rest_framework.routers import DefaultRouter
from .viewsets import UOMViewSet

router = DefaultRouter()
router.register(r'', UOMViewSet)

urlpatterns = router.urls