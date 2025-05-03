from rest_framework.routers import DefaultRouter
from .viewsets import DepartmentViewSet

router = DefaultRouter()
router.register(r'department', DepartmentViewSet)  # <--- this adds '/department/'

urlpatterns = router.urls
