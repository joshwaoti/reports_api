from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from reports.models import *
from reports.serializers import *

class MobilePspCustomerInfoViewSet(viewsets.ModelViewSet):
    queryset = psp_customer_info.objects.all()
    serializer_class = MobilePspCustomerInfoSerializer
    
class MobilePspTransactionCategorizationViewSet(viewsets.ModelViewSet):
    queryset = psp_transac_categorization_info.objects.all()
    serializer_class = MobilePspTransactionCategorizationSerializer
    
class MobilePspInteroperabilityViewSet(viewsets.ModelViewSet):
    queryset = interoperability_data.objects.all()
    serializer_class = MobilePspInteroperabilitySerializer
    
class PspTrustAccountPlacementViewSet(viewsets.ModelViewSet):
    queryset = trust_account_info.objects.all()
    serializer_class = PspTrustAccountPlacementSerializer

class MobilePspAgentsInformationViewSet(viewsets.ModelViewSet):
    queryset = psp_agents_info.objects.all()
    serializer_class = MobilePspAgentsInformationSerializer
    

