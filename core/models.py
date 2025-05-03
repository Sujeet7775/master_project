from django.db import models
from threading import local

_user = local()

def get_current_user():
    return getattr(_user, 'value', None)

class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.CharField(max_length=100)
    updated_by = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)

    class Meta:
        abstract = True

    
    def save(self, *args, **kwargs):
        user = get_current_user()
        if user:
            username = str(user.username)
            if not self.pk and not self.created_by:
                self.created_by = username
            self.updated_by = username
        super().save(*args, **kwargs)