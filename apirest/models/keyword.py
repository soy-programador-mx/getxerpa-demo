from django.db import models
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
    merchant_id = models.OneToOneField(
        'Merchant',
        on_delete=models.RESTRICT,
        on_update=models.CASCADE,
        null=False,
        blank=False
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.keyword