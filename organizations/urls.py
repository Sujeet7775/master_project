from django.urls import path
from . import views
# from .viewsets import AssignOrgPermissionsView


urlpatterns = [
    path('', views.organization_list, name='organization-list'),
    # path('users/<uuid:user_id>/permissions/', AssignOrgPermissionsView.as_view(), name='assign_org_permissions'),

]
