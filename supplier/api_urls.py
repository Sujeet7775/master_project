from rest_framework.routers import DefaultRouter
from .viewsets import SupplierViewSet

router = DefaultRouter()
router.register(r'', SupplierViewSet)

urlpatterns = router.urls