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
class MobilePspCustomerInfo(models.Model):
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
