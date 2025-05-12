from django.db import models
from core.models import BaseModel
from material import MATERIAL_TYPE_CHOICES
from django.utils.translation import gettext_lazy as _
from uom.models import UOM
from category.models import Category
from subcategory.models import SubCategory
from hsn.models import HSNCode

class Material(BaseModel):
    material_name = models.CharField(max_length=255, unique=True)
    material_code = models.CharField(max_length=255)
    material_type = models.CharField(max_length=16,
                                      choices=MATERIAL_TYPE_CHOICES)
    description = models.TextField(blank=True, null=True)
    category_id = models.ForeignKey(Category, on_delete=models.CASCADE)
    sub_category_id = models.ForeignKey(SubCategory, on_delete=models.CASCADE)
    uom_id = models.ForeignKey(UOM, on_delete=models.CASCADE)
    gst_hsn_code_id = models.ForeignKey(HSNCode, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('material_name', 'material_code')
        ordering = ['material_name']
        verbose_name = 'Material'

    def __str__(self):
        return self.material_name
