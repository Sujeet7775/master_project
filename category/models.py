import uuid
from warnings import filters
from django.db import models
from django.contrib.auth import get_user_model
from core.models import BaseModel

User = get_user_model()

class Category(BaseModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    category_name = models.CharField(max_length=255)
    
    
    class Meta:
        unique_together = ('category_name',)
    
    def __str__(self):
        return self.category_name