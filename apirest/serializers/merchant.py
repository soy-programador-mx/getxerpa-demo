from rest_framework import serializers
from ..models.merchant import Merchant

class MerchantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Merchant
        fields = '__all__'
        read_only_fields = ('id', 'created_at', 'updated_at',)