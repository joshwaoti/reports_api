from rest_framework import serializers
from reports.models import MobilePspCustomerInfo

class MobilePspCustomerInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = MobilePspCustomerInfo
        fields = '__all__'
