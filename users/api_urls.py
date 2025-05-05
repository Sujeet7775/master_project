from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import UserViewSet
from .views import assign_model_permissions, user_permissions

router = DefaultRouter()
router.register(r'users', UserViewSet)

urlpatterns = router.urls

urlpatterns = [
    path('', include(router.urls)),
    path('my-permissions/', user_permissions),  # <- Add this line
    # path('assign-permissions/', assign_permissions),
    path('assign-model-permissions/', assign_model_permissions),
]