from rest_framework import serializers
from ..models import Transaction
from ..models import Keyword

class TransactionSerializer(serializers.ModelSerializer):

    enrichment = serializers.SerializerMethodField()
    keywords = Keyword.objects.values_list('keyword', flat=True)

    class Meta:
        model = Transaction
        fields = '__all__'
        read_only_fields = ('id', 
                            'created_at', 
                            'updated_at',
                            )

    def enrichment_data(self, input):
        object = {'category': {}, 'merchant': {}}
        try:
            for keyword in self.keywords:
               if keyword in input.description.lower():
                    _row = Keyword.objects.select_related("merchant_id").get(keyword=keyword)
                    merchant = _row.merchant_id
                    object['merchant'] = {
                        "name": merchant.merchant_name,
                        "logo": merchant.merchant_logo
                    }

                    if merchant.category_id:

                        if (float(input.amount) < 0 and merchant.category_id.type == 'expense') or \
                                (float(input.amount) > 0 and merchant.category_id.type == 'income'):
                               object['category'] = {
                                "name": merchant.category_id.name,
                                "type": merchant.category_id.type
                            }

                    break

        except Keyword.DoesNotExist:
            pass
        
        return object
        
    def get_enrichment(self, obj):
        return self.enrichment_data(obj)
        
        