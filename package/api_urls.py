<<<<<<< HEAD
=======
# urls.py
>>>>>>> bb6ef40a6ebaa4bd7e1b546f1653e32200497a9c
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import PackageViewSet

router = DefaultRouter()
<<<<<<< HEAD
router.register(r'packages', PackageViewSet, basename='package')
=======
router.register(r'', PackageViewSet, basename='package')
>>>>>>> bb6ef40a6ebaa4bd7e1b546f1653e32200497a9c

urlpatterns = router.urls