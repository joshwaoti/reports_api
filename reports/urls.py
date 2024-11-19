from django.urls import path, include
from rest_framework.routers import DefaultRouter
from reports.views import *

router = DefaultRouter()

# Existing routes
router.register(r'mobile-psp-customer-info', MobilePspCustomerInfoViewSet)
router.register(r'mobile-transac-categ', MobilePspTransactionCategorizationViewSet)
router.register(r'mobile-psp-interoperability', MobilePspInteroperabilityViewSet)
router.register(r'mobile-psp-trust-placement', PspTrustAccountPlacementViewSet)
router.register(r'mobile-psp-agent-info', MobilePspAgentsInformationViewSet)

# New routes
router.register(r'mobile-psp-tarrifs-info', MobilePspTariffsInformationViewSet)
router.register(r'mobile-psp-merchant-balance', MobilePspMerchantCustomerBalanceViewSet)
router.register(r'mobile-psp-merchant-trans', MobilePspMerchantTransactionsViewSet)
router.register(r'mobile-psp-failed-trans', MobilePspFailedTransactionsViewSet)
router.register(r'mobile-psp-enlist-new-agents', MobilePspEnlistingNewAgentsViewSet)
router.register(r'mobile-psp-counterfeit', MobilePspCounterfeitViewSet)
router.register(r'mobile-psp-wallet-2-wallet', MobilePspWalletToWalletViewSet)
router.register(r'psp-card-brands', PspCardBrandsViewSet)
router.register(r'card-switch-info', CardSwitchInfoViewSet)
router.register(r'mobile-p2p-switch-info', P2pSwitchInfoViewSet)
router.register(r'mobile-psp-products', PspProductsViewSet)
router.register(r'mobile-psp-trust-account-details', PspTrustAccountDetailsViewSet)
router.register(r'mobile-incidents-data', IncidentsDataViewSet)
router.register(r'mobile-system-activity-info', SystemActivityInfoViewSet)
router.register(r'mobile-psp-customer-complaints', PspCustomerComplaintsViewSet)
router.register(r'mobile-stability-service-info', SchSyStabilServceInfoViewSet)
router.register(r'mobile-security-incident-record', PspCyberSecurityIncidentRecordViewSet)
router.register(r'gateway-failed-rejected-info', FailedRejectedTrxInfoViewSet)
router.register(r'gateway-transaction-tarrifs', PaymentGatewayTransactionsTarrifsViewSet)
router.register(r'gateway-transaction-details', PaymentGatewayTransactionsDetailsViewSet)
router.register(r'gateway-billing-template', PaymentGatewayBillingTemplateViewSet)
router.register(r'gateway-card-brands', PaymentGatewayCardBrandsViewSet, basename='card_brands_v1')
# router.register(r'merchant-transaction-info', MerchantTransactionInfoViewSet)
router.register(r'psp-schedule-of-directors', PspScheduleOfDirectorsViewSet)
router.register(r'psp-schedule-of-senior-management', PspScheduleOfSeniorManagementViewSet)
router.register(r'psp-schedule-of-shareholders', PspScheduleOfShareholdersViewSet)
router.register(r'psp-schedule-of-trustees', PspScheduleOfTrusteesViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
