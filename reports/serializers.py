from rest_framework import serializers
from reports.models import *

class MobilePspCustomerInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Psp_Customer
        fields = '__all__'


class MobilePspTransactionCategorizationSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Psp_Transac_Categorization
        fields = '__all__'

class MobilePspInteroperabilitySerializer(serializers.ModelSerializer):
    class Meta:
        model = MobilePspInteroperability
        fields = '__all__'

class PspTrustAccountPlacementSerializer(serializers.ModelSerializer):
    class Meta:
        model = PspTrustAccountPlacement
        fields = "__all__"
        
class MobilePspAgentsInformationSerializer(serializers.ModelSerializer):
    class Meta:
        model = MobilePspAgentsInformation
        fields = "__all__"