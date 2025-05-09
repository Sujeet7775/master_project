from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token
from .views import PermissionViewSet, VerifyTokenView
from permissions.permissions import MyPermissionsView

# DRF router for viewsets
router = DefaultRouter()
router.register(r'permission', PermissionViewSet, basename='permission')

urlpatterns = [
    # Include viewset routes (e.g., /permission/)
    path('', include(router.urls)),

    # Token authentication endpoint
    path('token/', obtain_auth_token, name='api_token_auth'),

    # Custom permission view for a specific user
    path('<int:user_id>/', MyPermissionsView.as_view(), name='my-permissions'),

    # Token verification endpoint
    path('verify_token/', VerifyTokenView.as_view(), name='verify_token'),
]
