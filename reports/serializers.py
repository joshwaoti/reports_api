from rest_framework import serializers
from reports.models import MobilePspCustomerInfo, MobilePspTransactionCategorization

class MobilePspCustomerInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = MobilePspCustomerInfo
        fields = '__all__'


class MobilePspTransactionCategorizationSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = MobilePspTransactionCategorization
        fields = '__all__'