# teams/api_urls.py
from rest_framework.routers import DefaultRouter
from .viewsets import TeamViewSet

router = DefaultRouter()
router.register(r'', TeamViewSet)  # no extra path

urlpatterns = router.urls
