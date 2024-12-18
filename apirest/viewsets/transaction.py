
from rest_framework import viewsets, permissions, status
from rest_framework.response import Response
from ..serializers.transaction import TransactionSerializer
from django.core import serializers

from ..models import Transaction
from ..models import Keyword
from ..models import Merchant

class TransactionViewSet(viewsets.ModelViewSet):
    queryset = Transaction.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = TransactionSerializer

    def enrinchment(self, input):
        object = {'category': {}, 'merchant': {}}
        keywords = Keyword.objects.values_list('keyword', flat=True)

        try:
            for keyword in keywords:
               if keyword in input['description'].lower():
                    _row = Keyword.objects.select_related("merchant_id").get(keyword=keyword)
                    merchant = _row.merchant_id
                    object['merchant'] = {
                        "name": merchant.merchant_name,
                        "logo": merchant.merchant_logo
                    }

                    if merchant.category_id:

                        if (float(input['amount']) < 0 and merchant.category_id.type == 'expense') or \
                                (float(input['amount']) > 0 and merchant.category_id.type == 'income'):
                               object['category'] = {
                                "name": merchant.category_id.name,
                                "type": merchant.category_id.type
                            }

                    break

        except Keyword.DoesNotExist:
            pass
        
        return object

    def create(self, request, *args, **kwargs):

        if isinstance(request.data,list):
            for row in request.data:
                row['enrichment'] = self.enrinchment(row)
        else :
            request.data['enrichment'] = self.enrinchment(request.data)

        serializer = self.get_serializer(data=request.data, many=isinstance(request.data,list))
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)

        # serializer.data.append(request.data['enrichment'])
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)