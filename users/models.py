from django.db import models
from core.models import BaseModel
from organizations.models import Organization
from departments.models import Department
from teams.models import Team
from django.contrib.auth.models import AbstractUser
import uuid
from django.db import models

from user_types.models import UserProfile
    
class User(AbstractUser,BaseModel):
    user_id = models.UUIDField(default=uuid.uuid4, unique=True, editable=False)
    
    organization = models.ForeignKey(Organization, on_delete=models.SET_NULL, null=True, related_name='users')
    department = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True, related_name='users')
    team = models.ForeignKey(Team, on_delete=models.SET_NULL, null=True, related_name='users')

    mobile_number = models.CharField(max_length=20)
    user_type = models.ForeignKey(UserProfile, on_delete=models.SET_NULL, null=True, related_name='users')

    state = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    pincode = models.CharField(max_length=20)
    approval_1 = models.CharField(max_length=100, null=True, blank=True)
    approval_2 = models.CharField(max_length=100, null=True, blank=True)
    

    def __str__(self):
        return str(self.user_id)
    
    class Meta:
        verbose_name_plural = "4. Users"
    