from django.urls import path, include
from rest_framework.routers import DefaultRouter
from reports.views import *

router = DefaultRouter()
router.register(r'mobile-psp-customer-info', MobilePspCustomerInfoViewSet)
router.register(r'mobile-transac-categ', MobilePspTransactionCategorizationViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
