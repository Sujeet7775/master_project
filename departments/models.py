from django.db import models
from core.models import BaseModel
from organizations.models import Organization


class Department(BaseModel):
    department_id = models.CharField(max_length=100, unique=True)
    organisation = models.ForeignKey(Organization, on_delete=models.CASCADE, related_name='departments')
    department_name = models.CharField(max_length=255)
    head_of_department = models.CharField(max_length=255)

    def __str__(self):
        return self.department_name
