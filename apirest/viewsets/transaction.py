from ..serializers.transaction import TransactionSerializer
from ..models import Transaction
from rest_framework import viewsets, permissions

class TransactionViewSet(viewsets.ModelViewSet):
    queryset = Transaction.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = TransactionSerializer