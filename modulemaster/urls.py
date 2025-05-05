from django.urls import path
from .viewsets import ModuleMasterCreateView

urlpatterns = [
    path('', ModuleMasterCreateView.as_view(), name='modulemaster-create'),
]
