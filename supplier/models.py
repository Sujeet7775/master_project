from django.db import models
from core.models import BaseModel

class Supplier(BaseModel):
    company_name = models.CharField(max_length=255)
    onboarding_date = models.DateField()
    pan_no = models.CharField(max_length=20)
    gst_no = models.CharField(max_length=20)
    email = models.EmailField()
    phone = models.CharField(max_length=10)
    contact_info = models.TextField(blank=True, null=True)
    kyc_complaints = models.TextField(blank=True, null=True)
    branch_details = models.TextField(blank=True, null=True)
    material_details = models.TextField(blank=True, null=True)
    pan_file = models.FileField(upload_to='uploads/pan_files/', blank=True, null=True)
    gst_file = models.FileField(upload_to='uploads/gst_files/', blank=True, null=True)  
    
    def __str__(self):
        return self.company_name
    class Meta:
        verbose_name_plural = "1. Suppliers"
        ordering = ['-created_at']