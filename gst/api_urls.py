from rest_framework.routers import DefaultRouter
from .viewsets import GSTViewSet

router = DefaultRouter()
router.register(r'', GSTViewSet)

urlpatterns = router.urls