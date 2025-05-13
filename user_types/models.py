from django.db import models
from block.models import User
from core.models import BaseModel
from user_types import USER_TYPE_CHOICES

class UserProfile(BaseModel):
    user_type = models.CharField(max_length=20, choices=USER_TYPE_CHOICES)
    
    def __str__(self):
        return f"{self.user_type}"
    
    class Meta:
        unique_together = ('user_type',)
        verbose_name = 'User Profile'
        ordering = ['-created_at']