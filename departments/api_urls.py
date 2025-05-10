from rest_framework.routers import DefaultRouter
from .viewsets import DepartmentViewSet

router = DefaultRouter()
router.register(r'', DepartmentViewSet)  # <--- this adds '/department/'

urlpatterns = router.urls
