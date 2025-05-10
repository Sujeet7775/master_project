from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import UserViewSet

router = DefaultRouter()
router.register(r'', UserViewSet)

urlpatterns = router.urls

<<<<<<< HEAD
urlpatterns = [
    path('', include(router.urls)),
]
=======
>>>>>>> bb6ef40a6ebaa4bd7e1b546f1653e32200497a9c
