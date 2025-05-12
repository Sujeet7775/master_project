"""
URL configuration for OrgMaster project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.contrib import admin
from django.urls import path, include
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularSwaggerView,
    SpectacularRedocView,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('', include('users.urls')),  # Home or public routes

    # App-specific routes
    path('organization/', include('organizations.urls')),
    path('department/', include('departments.urls')),
    path('teams/', include('teams.urls')),
    # path('permissions/', include('permissions.urls')),
    # path('tasks/', include('tasks.urls')),
    
    # API routes
    path('api/organization/', include('organizations.api_urls')),
    path('api/department/', include('departments.api_urls')),
    path('api/teams/', include('teams.api_urls')),
    path('api/users/', include('users.api_urls')),
    path('api/modulemaster/', include('modulemaster.api_urls')),
    path('api/permissions/', include('permissions.api_urls')),
    path('api/package/', include('package.api_urls')),
    path('api/district/', include('district.api_urls')),
    path('api/block/', include('block.api_urls')),
    path('api/gp_master/', include('gp_master.api_urls')),
    path('api/category/', include('category.api_urls')),
    path('api/subcategory/', include('subcategory.api_urls')),
    path('api/uom/', include('uom.api_urls')),
    path('api/gst/', include('gst.api_urls')),
    path('api/hsn/', include('hsn.api_urls')),
    path('api/material/', include('material.api_urls')),
    path('api/warehouse/', include('warehouse.api_urls')),

    # 🔍 Swagger / API documentation
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/schema/swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('api/schema/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),  
]
