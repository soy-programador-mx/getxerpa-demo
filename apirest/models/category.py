from django.db import models
import uuid

# Category model
class Category(models.Model):
    """
    Model representing a category.
    """

    class CategoryType(models.TextChoices):
        INCOME = 'IN', 'Income'
        EXPENSE = 'EX', 'Expense'

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.TextField(max_length=255, null=False, blank=False)
    type = models.CharField(max_length=2, choices=CategoryType.choices, null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name