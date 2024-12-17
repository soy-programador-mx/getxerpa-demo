from ..serializers.merchant import MerchantSerializer
from ..models import Merchant
from rest_framework import viewsets, permissions

class MerchantViewSet(viewsets.ModelViewSet):
    queryset = Merchant.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = MerchantSerializer