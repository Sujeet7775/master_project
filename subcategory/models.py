from category.models import Category
from core.models import BaseModel
from django.db import models
import uuid


class SubCategory(BaseModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    sub_category_name = models.CharField(max_length=255)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='subcategories')

    class Meta:
        unique_together = ('sub_category_name', 'category')
        
    def __str__(self):
        return self.sub_category_name