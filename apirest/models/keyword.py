from django.db import models
from .merchant import Merchant
import uuid

class Keyword (models.Model):
    """
    Model representing a keyword.
    """

    id = models.UUIDField(
        primary_key=True, 
        editable=False, 
        default=uuid.uuid4
    )
    keyword = models.CharField(max_length=100, null=False, blank=False)
    merchant_id = models.ForeignKey(
        Merchant,
        on_delete=models.RESTRICT,
        null=False,
        blank=False
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.keyword