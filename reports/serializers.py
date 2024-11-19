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
        fields = '__all__'

class MobilePspAgentsInformationSerializer(serializers.ModelSerializer):
    class Meta:
        model = psp_agents_info
        fields = '__all__'

class MobilePspTariffsInformationSerializer(serializers.ModelSerializer):
    class Meta:
        model = psp_tariffs_info
        fields = '__all__'

class MobilePspMerchantCustomerBalanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = merchant_cust_balance_info
        fields = '__all__'

class MobilePspMerchantTransactionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = merchant_transaction_info
        fields = '__all__'

class MobilePspFailedTransactionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = failed_txn_data
        fields = '__all__'

class MobilePspEnlistingNewAgentsAndAgentsOperatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = new_mobile_agents
        fields = '__all__'

class MobilePspCounterfeitCurrencyFraudSerializer(serializers.ModelSerializer):
    class Meta:
        model = counterfeit_transactions
        fields = '__all__'

class MobilePspWallettoWalletSerializer(serializers.ModelSerializer):
    class Meta:
        model = wallet_to_wallet
        fields = '__all__'

class PspPaymentGtwyCardBrandsSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = pymt_gw_card_brands
        fields = '__all__'

class CardSwitchInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = card_switch_info
        fields = '__all__'

class P2pSwitchInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = p2p_switch_info
        fields = '__all__'

class PspProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model = psp_products_info
        fields = '__all__'

class PspTrustAccountDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = trustaccount_data
        fields = '__all__'

class IncidentsDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = incidents_data
        fields = '__all__'

class SystemActivityInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = system_activity_info
        fields = '__all__'

class PspCustomerComplaintsSerializer(serializers.ModelSerializer):
    class Meta:
        model = psp_customer_complaints
        fields = '__all__'

class SchSyStabilServceInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = sch_sy_stabil_srvce_int
        fields = '__all__'

class PspCyberSecurityIncidentRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = psp_cybersecurity_incident_record
        fields = '__all__'

class FailedRejectedTrxInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = failed_rejected_trx_info
        fields = '__all__'

class PaymentGatewayTransactionsTarrifsSerializer(serializers.ModelSerializer):
    class Meta:
        model = payment_gateway_tariffs
        fields = '__all__'

class PaymentGatewayTransactionsDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = payment_gateway_transactions_details
        fields = '__all__'

class PaymentGatewayBillingTemplateSerializer(serializers.ModelSerializer):
    class Meta:
        model = pay_gtway_bill_temp
        fields = '__all__'

class paymentGatewayCardBrandsSerializer(serializers.ModelSerializer):
    class Meta:
        model = pymt_gw_card_brands
        fields = '__all__'

class MerchantTransactionInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = merchant_transaction_info
        fields = '__all__'

class PspScheduleOfDirectorsSerializer(serializers.ModelSerializer):
    class Meta:
        model = sched_of_dir
        fields = '__all__'

class PspScheduleOfSeniorManagementSerializer(serializers.ModelSerializer):
    class Meta:
        model = senior_mngt_schedule
        fields = '__all__'

class PspScheduleOfShareholdersSerializer(serializers.ModelSerializer):
    class Meta:
        model = sched_of_share_hldrs
        fields = '__all__'

class pspScheduleOfTrusteesSerializer(serializers.ModelSerializer):
    class Meta:
        model = sched_of_trustees
        fields = '__all__'


class pspCustomerComplaintsSerializer(serializers.ModelSerializer):
    class Meta:
        model = psp_customer_complaints
        fields = '__all__'