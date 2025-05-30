from django.db import models
from core.models import BaseModel
import uuid


class Organization(BaseModel):
    organisation_id = models.UUIDField(default=uuid.uuid4, unique=True, editable=False)
    organisation_name = models.CharField(max_length=255)
    address = models.TextField()
    industry_type = models.CharField(max_length=100)

    def __str__(self):
        return str(self.organisation_id)
    
    class Meta:
        verbose_name_plural = "1. Organizations"
        permissions = [
            ("can_read_organization", "Can read organization"),
            ("can_create_organization", "Can create organization"),
            ("can_update_organization", "Can update organization"),
            ("can_delete_organization", "Can delete organization"),
        ]
        
        
