from django.urls import path
from . import views
# from .viewsets import AssignOrgPermissionsView


urlpatterns = [
    path('', views.organization_list, name='organization-list'),

]
