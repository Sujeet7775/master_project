from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import UserViewSet
from .views import MyPermissionsView

router = DefaultRouter()
router.register(r'users', UserViewSet)

urlpatterns = router.urls

urlpatterns = [
    path('', include(router.urls)),
    path('me/permissions/', MyPermissionsView.as_view(), name='my-permissions'),
]