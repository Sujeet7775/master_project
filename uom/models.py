from django.db import models
from core.models import BaseModel
import uuid
    
# UOM (Unit of Measurement) model
class UOM(BaseModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    uom_name = models.CharField(max_length=100)
    
    class Meta:
        unique_together = ('uom_name',)
        
    def __str__(self):
        return str(self.id)