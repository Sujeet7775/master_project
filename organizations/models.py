from django.db import models
from core.models import BaseModel


class Organization(BaseModel):
    organisation_id = models.CharField(max_length=100, unique=True)
    organisation_name = models.CharField(max_length=255)
    address = models.TextField()
    industry_type = models.CharField(max_length=100)

    def __str__(self):
        return self.organisation_name
