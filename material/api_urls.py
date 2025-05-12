from rest_framework.routers import DefaultRouter
from .viewsets import MaterialViewSet

router = DefaultRouter()
router.register(r'', MaterialViewSet)

urlpatterns = router.urls