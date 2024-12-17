from django.db import models
import uuid

# Transaction model
class Transaction(models.Model):
    """
    Model representing a transaction.
    """

    id = models.UUIDField(
        primary_key=True, 
        editable=False, 
        default=uuid.uuid4
    )
    description = models.TextField( null=False, blank=False)
    amount = models.DecimalField(max_digits=10, decimal_places=2, null=False, blank=False)
    date = models.DateTimeField(null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.description