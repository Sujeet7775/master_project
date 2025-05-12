from django.db import models
from core.models import BaseModel

class GST(BaseModel):
    gst_percentage = models.DecimalField(max_digits=5, decimal_places=2)
    
    class Meta:
        unique_together = ('gst_percentage',)
        ordering = ['gst_percentage']
        
    def __str__(self):
        return f"{self.gst_percentage}%"
