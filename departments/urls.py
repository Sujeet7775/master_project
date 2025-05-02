from django.urls import path
from . import views

urlpatterns = [
    path('', views.department_list, name='department-list'),
    path('<str:pk>/', views.department_detail, name='department-detail'),
]