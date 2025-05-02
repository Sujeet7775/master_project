from django.db import models
from core.models import BaseModel
import uuid


class Organization(BaseModel):
    organisation_id = models.UUIDField(default=uuid.uuid4, unique=True, editable=False)
    organisation_name = models.CharField(max_length=255)
    address = models.TextField()
    industry_type = models.CharField(max_length=100)

    def __str__(self):
        return self.organisation_name
    
    class Meta:
        verbose_name_plural = "1. Organizations"
