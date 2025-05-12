from django.db import models
from core.models import BaseModel
from gst.models import GST

class HSNCode(BaseModel):
    hsn_code = models.CharField(max_length=50)
    gst_percentage = models.ForeignKey(GST, on_delete=models.CASCADE)

    def __str__(self):
        return self.hsn_code
