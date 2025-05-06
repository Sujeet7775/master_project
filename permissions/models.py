from django.db import models
from django.contrib.auth import get_user_model
import json

User = get_user_model()

class User_Permission(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='permission_snapshots')
    module = models.CharField(max_length=100)
    permissions = models.JSONField()  # Stores key-value pairs like {"User create": true, "Role create": false}

    def __str__(self):
        return f"Snapshot for {self.user.username} on {self.module}"
