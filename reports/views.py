from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from reports.models import *
from reports.serializers import *

class MobilePspCustomerInfoViewSet(viewsets.ModelViewSet):
    queryset = MobilePspCustomerInfo.objects.all()
    serializer_class = MobilePspCustomerInfoSerializer
    
class MobilePspTransactionCategorizationViewSet(viewsets.ModelViewSet):
    queryset = MobilePspTransactionCategorization.objects.all()
    serializer_class = MobilePspTransactionCategorizationSerializer
