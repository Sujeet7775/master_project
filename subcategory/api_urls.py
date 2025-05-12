from rest_framework.routers import DefaultRouter
from .viewsets import SubCategoryViewSet

router = DefaultRouter()
router.register(r'', SubCategoryViewSet)

urlpatterns = router.urls