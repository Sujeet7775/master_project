from rest_framework.routers import DefaultRouter
from .viewsets import UserProfileViewSet

router = DefaultRouter()
router.register(r'', UserProfileViewSet)

urlpatterns = router.urls