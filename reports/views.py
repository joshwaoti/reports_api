from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from reports.models import MobilePspCustomerInfo
from reports.serializers import MobilePspCustomerInfoSerializer

class MobilePspCustomerInfoViewSet(viewsets.ModelViewSet):
    queryset = MobilePspCustomerInfo.objects.all()
    serializer_class = MobilePspCustomerInfoSerializer
