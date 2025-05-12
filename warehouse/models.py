from django.db import models
from core.models import BaseModel
from district.models import District
from warehouse import WAREHOUSE_TYPE_CHOICES, ZONE_TYPE_CHOICES

class Warehouse(BaseModel):
    id = models.AutoField(primary_key=True)
    warehouse_name = models.CharField(max_length=255)
    warehouse_type = models.CharField(max_length=20, choices=WAREHOUSE_TYPE_CHOICES)
    zone_type = models.CharField(max_length=20, choices=ZONE_TYPE_CHOICES)
    assigned_user = models.CharField(max_length=255)
    state = models.CharField(max_length=100)
    district = models.ForeignKey(District, on_delete=models.SET_NULL, null=True)
    location = models.TextField()
    pincode = models.CharField(max_length=6)
    contact_persons = models.JSONField(default=list)
    contact_no = models.CharField(max_length=10)
    email_id = models.EmailField(blank=True, null=True)
    capacity = models.CharField(max_length=50)
    gps_coordinates = models.JSONField(blank=True, null=True)

    def __str__(self):
        return self.warehouse_name
    
    class Meta:
        verbose_name = 'Warehouse'
        ordering = ['warehouse_name']
        unique_together = ('warehouse_name', 'warehouse_type')