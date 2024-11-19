from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from reports.models import *
from reports.serializers import *

class MobilePspCustomerInfoViewSet(viewsets.ModelViewSet):
    queryset = psp_customer_info.objects.all()
    serializer_class = MobilePspCustomerInfoSerializer
    
class MobilePspTariffsInformationViewSet(viewsets.ModelViewSet):
    queryset = psp_tariffs_info.objects.all()
    serializer_class = MobilePspTariffsInformationSerializer

class MobilePspMerchantCustomerBalanceViewSet(viewsets.ModelViewSet):
    queryset = merchant_cust_balance_info.objects.all()
    serializer_class = MobilePspMerchantCustomerBalanceSerializer

class MobilePspMerchantTransactionsViewSet(viewsets.ModelViewSet):
    queryset = merchant_transaction_info.objects.all()
    serializer_class = MobilePspMerchantTransactionsSerializer

class MobilePspFailedTransactionsViewSet(viewsets.ModelViewSet):
    queryset = failed_txn_data.objects.all()
    serializer_class = MobilePspFailedTransactionsSerializer

class MobilePspEnlistingNewAgentsViewSet(viewsets.ModelViewSet):
    queryset = new_mobile_agents.objects.all()
    serializer_class = MobilePspEnlistingNewAgentsAndAgentsOperatingSerializer

class MobilePspCounterfeitViewSet(viewsets.ModelViewSet):
    queryset = counterfeit_transactions.objects.all()
    serializer_class = MobilePspCounterfeitCurrencyFraudSerializer

class MobilePspWalletToWalletViewSet(viewsets.ModelViewSet):
    queryset = wallet_to_wallet.objects.all()
    serializer_class = MobilePspWallettoWalletSerializer

class PspCardBrandsViewSet(viewsets.ModelViewSet):
    queryset = pymt_gw_card_brands.objects.all()
    serializer_class = PspPaymentGtwyCardBrandsSerializer

class CardSwitchInfoViewSet(viewsets.ModelViewSet):
    queryset = card_switch_info.objects.all()
    serializer_class = CardSwitchInfoSerializer

class P2pSwitchInfoViewSet(viewsets.ModelViewSet):
    queryset = p2p_switch_info.objects.all()
    serializer_class = P2pSwitchInfoSerializer

class PspProductsViewSet(viewsets.ModelViewSet):
    queryset = psp_products_info.objects.all()
    serializer_class = PspProductsSerializer

class PspTrustAccountDetailsViewSet(viewsets.ModelViewSet):
    queryset = trustaccount_data.objects.all()
    serializer_class = PspTrustAccountDetailsSerializer

class IncidentsDataViewSet(viewsets.ModelViewSet):
    queryset = incidents_data.objects.all()
    serializer_class = IncidentsDataSerializer

class SystemActivityInfoViewSet(viewsets.ModelViewSet):
    queryset = system_activity_info.objects.all()
    serializer_class = SystemActivityInfoSerializer

class PspCustomerComplaintsViewSet(viewsets.ModelViewSet):
    queryset = psp_customer_complaints.objects.all()
    serializer_class = PspCustomerComplaintsSerializer

class SchSyStabilServceInfoViewSet(viewsets.ModelViewSet):
    queryset = sch_sy_stabil_srvce_int.objects.all()
    serializer_class = SchSyStabilServceInfoSerializer

class PspCyberSecurityIncidentRecordViewSet(viewsets.ModelViewSet):
    queryset = psp_cybersecurity_incident_record.objects.all()
    serializer_class = PspCyberSecurityIncidentRecordSerializer

class FailedRejectedTrxInfoViewSet(viewsets.ModelViewSet):
    queryset = failed_rejected_trx_info.objects.all()
    serializer_class = FailedRejectedTrxInfoSerializer

class PaymentGatewayTransactionsTarrifsViewSet(viewsets.ModelViewSet):
    queryset = payment_gateway_tariffs.objects.all()
    serializer_class = PaymentGatewayTransactionsTarrifsSerializer

class PaymentGatewayTransactionsDetailsViewSet(viewsets.ModelViewSet):
    queryset = payment_gateway_transactions_details.objects.all()
    serializer_class = PaymentGatewayTransactionsDetailsSerializer

class PaymentGatewayBillingTemplateViewSet(viewsets.ModelViewSet):
    queryset = pay_gtway_bill_temp.objects.all()
    serializer_class = PaymentGatewayBillingTemplateSerializer

class PaymentGatewayCardBrandsViewSet(viewsets.ModelViewSet):
    queryset = pymt_gw_card_brands.objects.all()
    serializer_class = paymentGatewayCardBrandsSerializer

class PspScheduleOfDirectorsViewSet(viewsets.ModelViewSet):
    queryset = sched_of_dir.objects.all()
    serializer_class = PspScheduleOfDirectorsSerializer

class PspScheduleOfSeniorManagementViewSet(viewsets.ModelViewSet):
    queryset = senior_mngt_schedule.objects.all()
    serializer_class = PspScheduleOfSeniorManagementSerializer

class PspScheduleOfShareholdersViewSet(viewsets.ModelViewSet):
    queryset = sched_of_share_hldrs.objects.all()
    serializer_class = PspScheduleOfShareholdersSerializer

class PspScheduleOfTrusteesViewSet(viewsets.ModelViewSet):
    queryset = sched_of_trustees.objects.all()
    serializer_class = pspScheduleOfTrusteesSerializer

class MobilePspInteroperabilityViewSet(viewsets.ModelViewSet):
    queryset = interoperability_data.objects.all()
    serializer_class = MobilePspInteroperabilitySerializer

class PspTrustAccountPlacementViewSet(viewsets.ModelViewSet):
    queryset = trust_account_info.objects.all()
    serializer_class = PspTrustAccountPlacementSerializer

class MobilePspAgentsInformationViewSet(viewsets.ModelViewSet):
    queryset = psp_agents_info.objects.all()
    serializer_class = MobilePspAgentsInformationSerializer

# class MerchantTransactionInfoViewSet(viewsets.ModelViewSet):
#     queryset = merchant_transaction_info.objects.all()
#     serializer_class = MerchantTransactionInfoSerializer

class MobilePspTransactionCategorizationViewSet(viewsets.ModelViewSet):
    queryset = psp_transac_categorization_info.objects.all()
    serializer_class = MobilePspTransactionCategorizationSerializer

