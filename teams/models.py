from django.db import models
from core.models import BaseModel
from departments.models import Department
import uuid


class Team(BaseModel):
    team_id = models.UUIDField(default=uuid.uuid4, unique=True, editable=False)
    department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name='teams')
    team_name = models.CharField(max_length=255)
    team_lead = models.CharField(max_length=255)

    def __str__(self):
        return self.team_name
    
    class Meta:
        verbose_name_plural = "3. Teams"
