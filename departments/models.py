import uuid
from django.db import models
from core.models import BaseModel
from organizations.models import Organization

class Department(BaseModel):
    department_id = models.UUIDField(default=uuid.uuid4, unique=True, editable=False)
    organisation = models.ForeignKey(Organization, on_delete=models.CASCADE, related_name='departments')
    department_name = models.CharField(max_length=255)
    head_of_department = models.CharField(max_length=255)

    def __str__(self):
        return str(self.department_id)
    
    class Meta:
        verbose_name_plural = "2. Department"
