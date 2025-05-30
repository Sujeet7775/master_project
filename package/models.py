import uuid
from django.db import models
from django.contrib.auth import get_user_model
from core.models import BaseModel

User = get_user_model()

class Package(BaseModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    package_name = models.CharField(max_length=255)
    state_name = models.TextField()  # assuming a comma-separated list, or use JSON if needed
    package_code = models.CharField(max_length=100, unique=True)
    

    def __str__(self):
        return str(self.id)
    class Meta:
            ordering = ['-created_at']