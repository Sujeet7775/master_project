from django.db import models
from core.models import BaseModel
from organizations.models import Organization
from departments.models import Department
from teams.models import Team
from django.contrib.auth.models import AbstractUser
import uuid
from django.db import models

class Permission(models.Model):
    MODEL_CHOICES = [
        ('organization', 'Organization'),
        ('department', 'Department'),
        ('team', 'Team'),
        # Add more models as needed
    ]

    model_name = models.CharField(max_length=100, choices=MODEL_CHOICES)
    can_view = models.BooleanField(default=False)
    can_create = models.BooleanField(default=False)
    can_edit = models.BooleanField(default=False)
    can_delete = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.model_name} perms"
    class Meta:
        verbose_name_plural = "5. Permission"
    
class User(AbstractUser,BaseModel):
    user_id = models.UUIDField(default=uuid.uuid4, unique=True, editable=False)
    
    organization = models.ForeignKey(Organization, on_delete=models.SET_NULL, null=True, related_name='users')
    department = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True, related_name='users')
    team = models.ForeignKey(Team, on_delete=models.SET_NULL, null=True, related_name='users')

    mobile_number = models.CharField(max_length=20)
    role = models.CharField(max_length=100)

    state = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    pincode = models.CharField(max_length=20)

    approval_1 = models.CharField(max_length=100, null=True, blank=True)
    approval_2 = models.CharField(max_length=100, null=True, blank=True)
    
    permissions = models.ManyToManyField('Permission', blank=True, related_name='users')


    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
    class Meta:
        verbose_name_plural = "4. Users"
    