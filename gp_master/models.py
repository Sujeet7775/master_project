import uuid
from django.db import models
from django.contrib.auth import get_user_model
from core.models import BaseModel
from package.models import Package
from district.models import District
from block.models import Block

User = get_user_model()

class GPMaster(BaseModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    package = models.ForeignKey(Package, on_delete=models.CASCADE, related_name='gps')
    district = models.ForeignKey(District, on_delete=models.CASCADE, related_name='gps')
    block = models.ForeignKey(Block, on_delete=models.CASCADE, related_name='gps')
    gp_name = models.CharField(max_length=255)
    lgd_code = models.CharField(max_length=100)
    phase = models.CharField(max_length=100)
    latitude = models.DecimalField(max_digits=10, decimal_places=6)
    longitude = models.DecimalField(max_digits=10, decimal_places=6)
    gp_status = models.CharField(max_length=100)
    covered = models.BooleanField(default=False)
    sr_status = models.CharField(max_length=100)
    

    def __str__(self):
        return self.gp_name
