from django.urls import path, include
from rest_framework.routers import DefaultRouter
from reports.views import *

router = DefaultRouter()
router.register(r'mobile-psp-customer-info', MobilePspCustomerInfoViewSet)
router.register(r'mobile-transac-categ', MobilePspTransactionCategorizationViewSet)
router.register(r'mobile-psp-interoperability', MobilePspInteroperabilityViewSet )
router.register(r'mobile-psp-trust-placement', PspTrustAccountPlacementViewSet )
router.register(r'mobile-psp-agent-info', MobilePspAgentsInformationViewSet )

urlpatterns = [
    path('', include(router.urls)),
]
