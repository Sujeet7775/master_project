import uuid
from django.db import models
from django.contrib.auth import get_user_model
from core.models import BaseModel
from package.models import Package
from district.models import District

User = get_user_model()

class Block(BaseModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    package = models.ForeignKey(Package, on_delete=models.CASCADE, related_name='blocks')
    district = models.ForeignKey(District, on_delete=models.CASCADE, related_name='blocks')
    block_name = models.CharField(max_length=255)
    block_code = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return str(self.id)
