from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from reports.models import *
from reports.serializers import *

class MobilePspCustomerInfoViewSet(viewsets.ModelViewSet):
    queryset = Psp_Customer.objects.all()
    serializer_class = MobilePspCustomerInfoSerializer
    
class MobilePspTransactionCategorizationViewSet(viewsets.ModelViewSet):
    queryset = Psp_Transac_Categorization.objects.all()
    serializer_class = MobilePspTransactionCategorizationSerializer
    
class MobilePspInteroperabilityViewSet(viewsets.ModelViewSet):
    queryset = MobilePspInteroperability.objects.all()
    serializer_class = MobilePspInteroperabilitySerializer
    
class PspTrustAccountPlacementViewSet(viewsets.ModelViewSet):
    queryset = PspTrustAccountPlacement.objects.all()
    serializer_class = PspTrustAccountPlacementSerializer

class MobilePspAgentsInformationViewSet(viewsets.ModelViewSet):
    queryset = MobilePspAgentsInformation.objects.all()
    serializer_class = MobilePspAgentsInformationSerializer
    

