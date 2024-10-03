from django.db import models
from .choice_fields import (
    AGE_CHOICES,
    GENDER_CHOICES,
    BAND_CHOICES,
    WALLET_CHOICES,
    SUB_COUNTY_CHOICES,
    SUB_TRANSACTION_CHOICES,
    INTEROP_CHOICES,
    PSP_ID_OTHER_CHOICES,
    FAILED_TRANSACTION_CODE_CHOICES,
    MERCHANT_CLASSIFICATION_CODE_CHOICES,
    MERCHANT_TYPE_CHOICES,
    MERCHANT_STATUS_CHOICES,
    AGENT_TYPE_CHOICES,
    AGENT_STATUS_CHOICES,
    PRODUCT_CATEGORY_CHOICES,
    PRODUCT_OWNERSHIP_CATEGORY_CHOICES,
    PRODUCT_TRANSACTION_CODE_CHOICES,
    STATUS_CODE_CHOICES,
    DEBIT_TYPE_CODE_CHOICES,
    SECTOR_CODE_CHOICES,
    EDUCATION_CHOICES,
    VICTIM_CATEGORY_CHOICES,
    VICTIM_INFORMATION_CHOICES,
    COMPLAINTS_CODE_CHOICES,
    REMEDIAL_STATUS_CHOICES,
    COMPLAINTS_FREQUENCY_CODE_CHOICES,
    SYSTEM_CATEGORY_OWNER_FLAG_CHOICES,
    THIRD_PARTY_OWNED_CATEGORY_CHOICES,
    PRODUCT_TYPE_CHOICES,
    SYSTEM_UNAVAILABILITY_CHOICES,
    RECOVERY_TIME_CHOICES,
    DISRUPTION_CODE_CHOICES,
    INTERRUPTION_CODE_CHOICES,
    COUNTRY_CODE_CHOICES,
    INCIDENT_MODE_CHOICES,
    LOSS_TYPE_CHOICES,
    CARD_FLAG_CHOICES,
    CARD_TYPE_CHOICES,
    TIME_CHOICES,
    COMPUTATIONAL_TIME_CHOICES,
    COMPUTATION_FREQUENCY_CHOICES,
    SUBMISSION_FREQUENCY_CHOICES,
    BANK_ID_CHOICES,
    SEGMENTATION_CODE_CHOICES,
    BUSINESS_SIZE_CODE_CHOICES,
    DENOMINATION_CODE_CHOICES
)


# Create your models here.
class Psp_Customer(models.Model):
    row_id = models.AutoField(primary_key=True, unique=True)
    psp_id = models.CharField(max_length=25, choices=PSP_ID_OTHER_CHOICES)
    reporting_date = models.CharField(max_length=15)
    sub_county_code = models.CharField(max_length=4, choices=SUB_COUNTY_CHOICES)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    age_code = models.CharField(max_length=10,choices=AGE_CHOICES)
    wallet_code = models.CharField(max_length=3, choices=WALLET_CHOICES)
    no_of_customers_registered = models.PositiveIntegerField()
    no_of_customers_active = models.PositiveIntegerField()
    no_of_customers_inactive = models.PositiveIntegerField()
    no_of_customers_dormant = models.PositiveIntegerField()
    balances_in_customer_accts = models.DecimalField(max_digits=12, decimal_places=2)
    volume_of_transactions = models.PositiveIntegerField()
    value_of_transactions = models.DecimalField(max_digits=12, decimal_places=2)
    
class Psp_Transac_Categorization(models.Model):
    row_id= models.AutoField(primary_key=True)
    psp_id = models.CharField(max_length=25, choices=PSP_ID_OTHER_CHOICES)
    reporting_date = models.CharField(max_length=15)
    sub_transaction_code = models.CharField(max_length=10, choices=SUB_TRANSACTION_CHOICES)
    band_code = models.CharField(max_length=25, choices=BAND_CHOICES)
    volume_of_transactions = models.PositiveIntegerField()
    value_of_transactions = models.DecimalField(max_digits=12, decimal_places=2)

class MobilePspInteroperability(models.Model):
    row_id= models.AutoField(primary_key=True)
    psp_id = models.CharField(max_length=25, choices=PSP_ID_OTHER_CHOICES)
    reporting_date = models.CharField(max_length=15)
    band_code = models.CharField(max_length=25 ,choices=BAND_CHOICES)
    psp_id_other = models.CharField(max_length=50, choices=PSP_ID_OTHER_CHOICES)
    interoperability_code = models.CharField(max_length=25, choices=INTEROP_CHOICES)
    incoming_transaction_volume = models.PositiveIntegerField()
    incoming_transaction_value = models.DecimalField(max_digits=12, decimal_places=2)
    outgoing_transaction_volume = models.PositiveIntegerField()
    outgoing_transaction_value = models.DecimalField(max_digits=12, decimal_places=2)

class PspTrustAccountPlacement(models.Model):
    row_id= models.AutoField(primary_key=True)
    psp_id = models.CharField(max_length=25, choices=PSP_ID_OTHER_CHOICES)
    reporting_date = models.CharField(max_length=15)
    trust_fund_placement = models.CharField(max_length=25)
    trust_fund_inv_maturity_date = models.DateField()
    cat_trust_fund_invested_amt = models.DecimalField(max_digits=12, decimal_places=2)
    interest_amt_per_category = models.DecimalField(max_digits=12, decimal_places=2)

class MobilePspAgentsInformation(models.Model):
    row_id= models.AutoField(primary_key=True)
    psp_id = models.CharField(max_length=25, choices=PSP_ID_OTHER_CHOICES)
    reporting_date = models.CharField(max_length=15)
    agent_type_code = models.CharField(max_length=10, choices=AGENT_TYPE_CHOICES)
    agents_id = models.CharField(max_length=10)
    gps_cordinates = models.CharField(max_length=10) # gps coordinates/ favourite cell
    sub_county_code = models.CharField(max_length=4, choices=SUB_COUNTY_CHOICES)
    agent_status = models.CharField(max_length=25, choices=AGENT_STATUS_CHOICES)
    band_code = models.CharField(max_length=25, choices=BAND_CHOICES)
    volume_cash_in_at_agents = models.PositiveIntegerField()
    value_cash_in_at_agents = models.DecimalField(max_digits=12, decimal_places=2)
    volume_of_cash_out_at_agents = models.PositiveIntegerField()
    value_of_cash_out_at_agents = models.DecimalField(max_digits=12, decimal_places=2)
    amount_of_eFloat_mobile_agents = models.DecimalField(max_digits=12, decimal_places=2)
    number_of_agent_cash_dep_banks = models.PositiveIntegerField()
    value_of_agent_cash_dep_banks = models.DecimalField(max_digits=12, decimal_places=2)
    no_of_agent_cash_withd_banks = models.PositiveIntegerField()
    value_of_agent_cash_withd_banks = models.DecimalField(max_digits=12, decimal_places=2)

