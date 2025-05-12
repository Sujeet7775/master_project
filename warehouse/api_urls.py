from rest_framework.routers import DefaultRouter
from .viewsets import WarehouseViewSet

router = DefaultRouter()
router.register(r'', WarehouseViewSet)

urlpatterns = router.urls