from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()
class User_Permission(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='permission_snapshots')
    module = models.CharField(max_length=100)
    permissions = models.JSONField()

    def __str__(self):
        unique_together = ('user', 'module')
        return f"{self.user.username} on {self.module}"

