from rest_framework import serializers
from reports.models import *

class MobilePspCustomerInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = psp_customer_info
        fields = '__all__'


class MobilePspTransactionCategorizationSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = psp_transac_categorization_info
        fields = '__all__'

class MobilePspInteroperabilitySerializer(serializers.ModelSerializer):
    class Meta:
        model = interoperability_data
        fields = '__all__'

class PspTrustAccountPlacementSerializer(serializers.ModelSerializer):
    class Meta:
        model = trust_account_info
        fields = "__all__"
        
class MobilePspAgentsInformationSerializer(serializers.ModelSerializer):
    class Meta:
        model = psp_agents_info
        fields = "__all__"