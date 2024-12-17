from django.db import models
from .category import Category
import uuid

class Merchant(models.Model):
    """
    Model representing a merchant.
    """

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    merchant_name = models.CharField(max_length=255, null=False, blank=False)
    merchant_logo = models.CharField(max_length=255, null=True, blank=False)
    category = models.OneToOneField(Category, 
                                    on_delete=models.RESTRICT,
                                    null=False, 
                                    blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name