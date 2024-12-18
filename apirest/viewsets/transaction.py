
from rest_framework import viewsets, permissions, status
from rest_framework.response import Response
from ..serializers.transaction import TransactionSerializer

from ..models import Transaction

class TransactionViewSet(viewsets.ModelViewSet):
    queryset = Transaction.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = TransactionSerializer

    def rates_enrichment(self, data, rows_total):

        category_enrichment = 0
        merchant_enrichment = 0


        for row in data:
            if not row["enrichment"]["category"]:
                category_enrichment += 1
            if not row["enrichment"]["merchant"]:
                merchant_enrichment += 1

        return {
            'category': (category_enrichment * 100) / rows_total,
            'merchant': (merchant_enrichment * 100) / rows_total
        }

    def create(self, request, *args, **kwargs):

        serializer = self.get_serializer(data=request.data, many=isinstance(request.data,list))
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)

        rates = self.rates_enrichment(serializer.data, len(serializer.data))
        response_data = {
            'transactions_total': len(serializer.data),
            'category_enrichment_rate': rates["category"],
            'merchant_enrichment_rate': rates["merchant"],
            'data': serializer.data
        }
        
        headers = self.get_success_headers(response_data)
        return Response(response_data, status=status.HTTP_201_CREATED, headers=headers)