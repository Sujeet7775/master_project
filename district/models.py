import uuid
from django.db import models
from django.contrib.auth import get_user_model
from package.models import Package
from core.models import BaseModel

User = get_user_model()


class District(BaseModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    package = models.ForeignKey(Package, on_delete=models.CASCADE, related_name='districts')
    district_name = models.CharField(max_length=255)
    district_code = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return str(self.id)
    class Meta: 
        ordering = ['-created_at']
        