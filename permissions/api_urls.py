# from django.urls import path
# from .views import UserPermissionView

# urlpatterns = [
#     path('user-permissions/<uuid:user_id>/', UserPermissionView.as_view(), name='user-permissions'),




# ]


# urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from permissions.permissions import MyPermissionsView
from .views import PermissionViewSet, UserPermissionsView, VerifyTokenView
from rest_framework.authtoken.views import obtain_auth_token


router = DefaultRouter()
router.register(r'permission', PermissionViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('token/', obtain_auth_token, name='api_token_auth'),
    path('my-permissions/<int:user_id>', MyPermissionsView.as_view(), name='my-permissions'),
    path('api/verify_token/', VerifyTokenView.as_view(), name='verify_token'),  # Verify the token
    path('api/user_permissions/', UserPermissionsView.as_view(), name='user_permissions'),  # Fetch user permissions

]



