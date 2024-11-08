from django.db import models
from .choice_fields import *


# Create your models here.
class psp_customer_info(models.Model):
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
    
class psp_transac_categorization_info(models.Model):
    row_id= models.AutoField(primary_key=True)
    psp_id = models.CharField(max_length=25, choices=PSP_ID_OTHER_CHOICES)
    reporting_date = models.CharField(max_length=15)
    sub_transaction_code = models.CharField(max_length=10, choices=SUB_TRANSACTION_CHOICES)
    band_code = models.CharField(max_length=25, choices=BAND_CHOICES)
    volume_of_transactions = models.PositiveIntegerField()
    value_of_transactions = models.DecimalField(max_digits=12, decimal_places=2)

class interoperability_data(models.Model):
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

class trust_account_info(models.Model):
    row_id= models.AutoField(primary_key=True)
    psp_id = models.CharField(max_length=25, choices=PSP_ID_OTHER_CHOICES)
    reporting_date = models.CharField(max_length=15)
    trust_fund_placement = models.CharField(max_length=25)
    trust_fund_inv_maturity_date = models.DateField()
    cat_trust_fund_invested_amt = models.DecimalField(max_digits=12, decimal_places=2)
    interest_amt_per_category = models.DecimalField(max_digits=12, decimal_places=2)

class psp_agents_info(models.Model):
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

class psp_tariffs_info(models.Model):
    psp_id = models.CharField(max_length=25, choices=PSP_ID_OTHER_CHOICES)
    reporting_date = models.CharField(max_length=20)
    band_code = models.CharField(max_length=10,choices=BAND_CHOICES)
    p2p_on_net_registered_wallet = models.PositiveIntegerField()
    p2p_on_net_non_reg_wallet = models.PositiveIntegerField()
    p2p_off_net_registered_wallet = models.PositiveIntegerField()
    p2p_off_net_non_reg_wallet = models.PositiveIntegerField()
    cash_withdrawals_mob_money_agent = models.PositiveIntegerField()
    cash_withdrawals_bank_ATMs = models.PositiveIntegerField()
    agent_com_cash_out_reg_cust = models.PositiveIntegerField()
    agent_com_cash_out_non_reg_cust = models.PositiveIntegerField()
    agent_commision_for_cash_in = models.PositiveIntegerField()
    ATM_commision_for_cash_out = models.PositiveIntegerField()
    ATM_commision_for_cash_in = models.PositiveIntegerField()
    B2C_paybill_type1_customer = models
    B2C_payments_paybill_type2_cust = models.PositiveIntegerField()
    B2C_payments_paybill_type2_bus = models.PositiveIntegerField()
    B2C_payments_paybill_type3_bus = models.PositiveIntegerField()
    C2B_payments_paybill_type1_customer = models.PositiveIntegerField()
    C2B_payments_paybill_type2_cust = models.PositiveIntegerField()
    C2B_payments_paybill_type2_bus = models.PositiveIntegerField()
    C2B_payments_paybill_type3_bus = models.PositiveIntegerField()
    B2B_payments_paybill_type1_customer = models.PositiveIntegerField()
    B2B_payments_paybill_type2_cust = models.PositiveIntegerField()
    B2B_payments_paybill_type2_bus = models.PositiveIntegerField()
    B2B_payments_paybill_type3 = models.PositiveIntegerField()
    B2C_payments_payments_bank_aggreg_codes = models.PositiveIntegerField()
    C2B_payments_bank_aggreg_codes = models.PositiveIntegerField()
    till_number_payments = models.PositiveIntegerField()
    cross_border_Int_mny_trans_out = models.PositiveIntegerField()
    cross_border_int_mny_trans_in = models.PositiveIntegerField()
    P2P_outgoing_reg_partner_net = models.PositiveIntegerField()

class merchant_cust_balance_info(models.Model):
    psp_id = models.CharField(max_length=25, choices=PSP_ID_OTHER_CHOICES)
    reporting_date = models.CharField(max_length=20)
    merchant_id = models.CharField(max_length=10)
    merchant_type_code = models.CharField(max_length=10, choices=MERCHANT_TYPE_CHOICES)
    merchant_name = models.CharField(max_length=100)
    company_name = models.CharField(max_length=100)
    merchant_classification_code = models.CharField(max_length=10, choices=MERCHANT_CLASSIFICATION_CODE_CHOICES)
    sub_county_code = models.CharField(max_length=4, choices=SUB_COUNTY_CHOICES)
    merchant_status_code = models.CharField(max_length=25, choices=MERCHANT_STATUS_CHOICES)
    no_of_customers = models.PositiveIntegerField()
    eod_balances = models.DecimalField(max_digits=12, decimal_places=2)

class merchant_transaction_info(models.Model):      #in SOAP UI this is listed under gateways
    psp_id = models.CharField(max_length=25, choices=PSP_ID_OTHER_CHOICES)
    reporting_date = models.CharField(max_length=20)
    merchant_id = models.CharField(max_length=10)
    merchant_type_code = models.CharField(max_length=10, choices=MERCHANT_TYPE_CHOICES)
    merchant_name = models.CharField(max_length=100)
    company_name = models.CharField(max_length=100)
    merchant_classification_code = models.CharField(max_length=10, choices=MERCHANT_CLASSIFICATION_CODE_CHOICES)
    sub_county_code = models.CharField(max_length=4, choices=SUB_COUNTY_CHOICES)
    merchant_status_code = models.CharField(max_length=25, choices=MERCHANT_STATUS_CHOICES)
    band_code = models.CharField(max_length=25, choices=BAND_CHOICES)
    deposit_transactions_vol = models.PositiveIntegerField()
    deposit_transactions_value = models.DecimalField(max_digits=12, decimal_places=2)
    no_of_withdrawal_transactions = models.PositiveIntegerField()
    withdrawal_transactions_value = models.DecimalField(max_digits=12, decimal_places=2)

class failed_txn_data(models.Model):
    row_id= models.AutoField(primary_key=True)
    psp_id = models.CharField(max_length=25, choices=PSP_ID_OTHER_CHOICES)
    reporting_date = models.CharField(max_length=20)
    failed_transaction_code = models.CharField(max_length=8, choices=FAILED_TRANSACTION_CODE_CHOICES)
    band_code = models.CharField(max_length=25, choices=BAND_CHOICES)
    volume_of_transactions = models.PositiveIntegerField()
    value_of_transactions = models.DecimalField(max_digits=12, decimal_places=2)
    percentage_of_failed_transactions = models.PositiveIntegerField()

class new_mobile_agents(models.Model):
    row_id= models.AutoField(primary_key=True)      # reporting date of this must be the end of the month date either 28th, 29th, 30th or 31st
    psp_id = models.CharField(max_length=25, choices=PSP_ID_OTHER_CHOICES)
    reporting_date = models.CharField(max_length=20)
    sub_county_code=models.CharField(max_length=4, choices=SUB_COUNTY_CHOICES)
    agent_id=models.CharField(max_length=10)
    store_number=models.CharField(max_length=10)
    agent_name=models.CharField(max_length=100)
    agent_type=models.CharField(max_length=10, choices=AGENT_TYPE_CHOICES)
    agent_status=models.CharField(max_length=10, choices=AGENT_STATUS_CHOICES)
    physical_address=models.CharField(max_length=100)
    postal_address=models.CharField(max_length=100)
    date_of_onboarding=models.DateField()
    contact_number=models.CharField(max_length=15)
    name_of_owner=models.CharField(max_length=100)
    contact_of_owner=models.CharField(max_length=100)
    main_commercial_activity=models.CharField(max_length=100)
    num_trainings_conducted = models.CharField(max_length=100)
    suspension_termination_date=models.DateField()
    suspension_termination_reason=models.CharField(max_length=100)

class counterfeit_transactions(models.Model):
    row_id= models.AutoField(primary_key=True)  #frequency must be end of week
    psp_id = models.CharField(max_length=25, choices=PSP_ID_OTHER_CHOICES)
    reporting_date = models.CharField(max_length=20)
    sub_county_code=models.CharField(max_length=4, choices=SUB_COUNTY_CHOICES)
    agent_id=models.CharField(max_length=10)
    denomination_code=models.CharField(max_length=10, choices=DENOMINATION_CODE_CHOICES)
    serial_number=models.CharField(max_length=10)
    depositors_name=models.CharField(max_length=100)
    tellers_name=models.CharField(max_length=100)
    date_confiscated=models.DateField()
    remarks=models.CharField(max_length=100)
    number_of_pieces=models.PositiveIntegerField()

class wallet_to_wallet(models.Model):
    row_id= models.AutoField(primary_key=True)
    psp_id = models.CharField(max_length=25, choices=PSP_ID_OTHER_CHOICES)
    reporting_date = models.CharField(max_length=20)
    segmentation_code=models.CharField(max_length=10, choices=SEGMENTATION_CODE_CHOICES)
    busines_size_code=models.CharField(max_length=10, choices=BUSINESS_SIZE_CODE_CHOICES)
    volume_of_transactions=models.PositiveIntegerField()
    value_of_transactions=models.DecimalField(max_digits=12, decimal_places=2)
    
class pymt_gw_card_brands(models.Model):
    row_id= models.AutoField(primary_key=True)
    reporting_date = models.CharField(max_length=20)
    psp_id = models.CharField(max_length=25, choices=PSP_ID_OTHER_CHOICES)
    bank_id = models.CharField(max_length=5)
    transaction_category = models.CharField(max_length=10, choices=TRANSACTION_CATEGORY_CHOICES)
    card_brand_type = models.CharField(max_length=10, choices=CARD_BRAND_TYPE_CHOICES)
    number_of_txns = models.PositiveIntegerField()
    value_of_txns = models.DecimalField(max_digits=12, decimal_places=2)


class card_switch_info(models.Model):
    row_id= models.AutoField(primary_key=True)
    psp_id = models.CharField(max_length=25, choices=PSP_ID_OTHER_CHOICES)
    reporting_date = models.CharField(max_length=20)
    bank_code = models.CharField(max_length=10,)
    system_name = models.CharField(max_length=100)
    card_flag = models.CharField(max_length=10,choices=CARD_FLAG_CHOICES)
    card_type = models.CharField(max_length=10,choices=CARD_TYPE_CHOICES)
    no_of_cards = models.PositiveIntegerField()
    vol_of_transactions_DR = models.PositiveIntegerField()
    value_of_transaction_DR = models.PositiveIntegerField()
    vol_of_transactions_CR = models.PositiveIntegerField()
    value_of_transaction_CR = models.PositiveIntegerField()
    net_settlement_instruction_DR = models.PositiveIntegerField()
    net_settlement_instruction_CR = models.PositiveIntegerField()

class p2p_switch_info(models.Model):
    # Switches - P2P switch
    # not in template
    row_id= models.AutoField(primary_key=True)
    reporting_date = models.CharField(max_length=20)    
    bank_id = models.CharField(max_length=5)
    transcation_channel = models.CharField(max_length=10)
    no_of_registered_customer = models.PositiveIntegerField()
    no_of_active_customer = models.PositiveIntegerField()
    no_of_transactions_outgoing = models.PositiveIntegerField()
    value_of_transactions_ongoing = models.DecimalField(max_digits=12, decimal_places=2)
    no_of_transactions_incoming = models.PositiveIntegerField()
    value_of_transactions_incoming = models.DecimalField(max_digits=12, decimal_places=2)
    net_settlement_instruction_dr = models.DecimalField(max_digits=12, decimal_places=2)
    net_settlement_instruction_dr = models.DecimalField(max_digits=12, decimal_places=2)


# currently not in GDI phase 2
class psp_products_info(models.Model):
    row_id= models.AutoField(primary_key=True)  # not in GDI User Guide phase 2
    reporting_date = models.CharField(max_length=20)
    product_ownership_flag = models.CharField(max_length=10, choices=PRODUCT_CATEGORY_CHOICES)
    product_ownership_category = models.CharField(max_length=25, choices=PRODUCT_OWNERSHIP_CATEGORY_CHOICES)
    product_partner_name = models.CharField(max_length=25)
    product_transaction_code = models.CharField(max_length=10, choices=PRODUCT_TRANSACTION_CODE_CHOICES)
    product_name = models.CharField(max_length=10)
    gender = models.CharField(max_length=15, choices=GENDER_CHOICES) # male, female choices
    status_code = models.CharField(max_length=15, choices=STATUS_CODE_CHOICES)
    band_code = models.CharField(max_length=25, choices=BAND_CHOICES)
    no_of_customers = models.PositiveIntegerField()
    no_of_transactions = models.PositiveIntegerField()
    value_of_transactions = models.DecimalField(max_digits=12, decimal_places=2)

class trustaccount_data(models.Model):
    row_id= models.AutoField(primary_key=True)# not in GDI User Guide phase 2
    reporting_date = models.CharField(max_length=20)
    bank_id = models.CharField(max_length=15,choices=BANK_ID_CHOICES)
    bank_account_number = models.IntegerField()
    trust_account_debit_types_code = models.CharField(max_length=100, choices=DEBIT_TYPE_CODE_CHOICES)
    org_recieving_donations = models.CharField(max_length=100)
    sector_code = models.CharField(max_length=100, choices=SECTOR_CODE_CHOICES)
    trust_acc_int_utilized_details = models.CharField(max_length=100)
    trust_acc_opening_balance = models.DecimalField(max_digits=12, decimal_places=2)
    principal_amount = models.DecimalField(max_digits=12, decimal_places=2)
    trust_acc_interest_earned = models.DecimalField(max_digits=12, decimal_places=2)
    closing_balance = models.DecimalField(max_digits=12, decimal_places=2)
    trust_acc_interest_utilized = models.DecimalField(max_digits=12, decimal_places=2)

class incidents_data(models.Model): # not in GDI User Guide phase 2
    # PSP Incidents of fraud theft robbery
    row_id= models.AutoField(primary_key=True)
    reporting_date = models.CharField(max_length=20)
    sub_county_code = models.CharField(max_length=4)
    sub_fraud_code = models.CharField(max_length=10)
    fraud_category_flag = models.CharField(max_length=10)
    victim_category = models.CharField(max_length=10,choices=VICTIM_CATEGORY_CHOICES)
    victim_information = models.CharField(max_length=100,choices=VICTIM_INFORMATION_CHOICES)
    date_of_occurence = models.DateField()
    number_of_incidences = models.PositiveIntegerField()
    amount_involved = models.DecimalField(max_digits=12, decimal_places=2)
    amount_lost = models.DecimalField(max_digits=12, decimal_places=2)
    amount_recovered = models.DecimalField(max_digits=12, decimal_places=2)
    action_taken = models.CharField(max_length=100)
    recovery_details = models.CharField(max_length=100)

class system_activity_info(models.Model): # not in GDI User Guide phase 2
    # PSP System Activity
    row_id= models.AutoField(primary_key=True)
    reporting_date = models.CharField(max_length=20)
    hour_of_day = models.CharField(max_length=6, choices=TIME_CHOICES)
    no_of_transactions_per_sec = models.PositiveIntegerField()
    no_of_transactions_per_hr = models.PositiveIntegerField()


class psp_customer_complaints(models.Model):
    row_id= models.AutoField(primary_key=True) # psp schedule customer complaints & remedial actions
    reporting_date = models.CharField(max_length=20)
    complaint_code = models.CharField(max_length=10,choices=COMPLAINTS_CODE_CHOICES)
    complainant_gender = models.CharField(max_length=10,choices=GENDER_CHOICES)
    complaint_frequency = models.CharField(max_length=10,choices=COMPLAINTS_FREQUENCY_CODE_CHOICES)
    complaint_name = models.CharField(max_length=100)
    complainant_age = models.PositiveIntegerField(choices=AGE_CHOICES)
    complainant_contact_number = models.CharField(max_length=10)
    complainant_sub_county_location = models.CharField(max_length=10,choices=SUB_COUNTY_CHOICES)
    complainant_education_level = models.CharField(max_length=10,choices=EDUCATION_CHOICES)
    other_complainant_details = models.CharField(max_length=100)
    agent_id = models.CharField(max_length=10)
    date_of_occurence = models.DateField()
    date_reported_to_the_institution = models.DateField()
    date_resolved = models.DateField()
    remedial_status = models.CharField(max_length=10,choices=REMEDIAL_STATUS_CHOICES)
    amount_lost = models.DecimalField(max_digits=12, decimal_places=2)
    amount_recovered = models.DecimalField(max_digits=12, decimal_places=2)

class sch_sy_stabil_srvce_int(models.Model):
    row_id= models.AutoField(primary_key=True)  # not in GDI User Guide phase 2
    #  Scheduled System Stability Service Information
    reporting_date = models.CharField(max_length=20)
    sub_county_code = models.CharField(max_length=4,choices=SUB_COUNTY_CHOICES)
    system_owner_flag = models.CharField(max_length=10,choices=SYSTEM_CATEGORY_OWNER_FLAG_CHOICES)
    third_party_owned_category = models.CharField(max_length=10,choices=THIRD_PARTY_OWNED_CATEGORY_CHOICES)
    third_party_name = models.CharField(max_length=100)
    product_type = models.CharField(max_length=100,choices=PRODUCT_TYPE_CHOICES)
    system_unavailability_type_code = models.CharField(max_length=100,choices=SYSTEM_UNAVAILABILITY_CHOICES)
    third_party_system_affected = models.CharField(max_length=100)
    service_interruption_cause_code = models.CharField(max_length=100,choices=INTERRUPTION_CODE_CHOICES)
    severity_interruption_code = models.CharField(max_length=100,choices=DISRUPTION_CODE_CHOICES)
    recovery_time_code = models.CharField(max_length=100,choices=RECOVERY_TIME_CHOICES)
    remedial_status_code = models.CharField(max_length=100,choices=REMEDIAL_STATUS_CHOICES)
    system_uptime_percentage = models.DecimalField(max_digits=12, decimal_places=2)


class psp_cybersecurity_incident_record(models.Model):
    row_id= models.AutoField(primary_key=True)  # not in GDI User Guide phase 2
    reporting_date = models.CharField(max_length=20)
    incident_number = models.CharField(max_length=10)
    location_of_attacker = models.CharField(max_length=10,choices=COUNTRY_CODE_CHOICES)
    incident_mode = models.CharField(max_length=10,choices=INCIDENT_MODE_CHOICES)
    date_and_time_of_incident_happened = models.DateField()
    loss_type = models.CharField(max_length=10,choices=LOSS_TYPE_CHOICES)
    details_of_the_incident = models.CharField(max_length=100)
    action_taken_to_manage_the_incident = models.CharField(max_length=100)
    date_and_time_of_the_incident_resolution = models.DateField()
    action_taken_to_mitigate_future_incidents = models.CharField(max_length=100)
    amount_involved = models.DecimalField(max_digits=12, decimal_places=2)
    amount_lost = models.DecimalField(max_digits=12, decimal_places=2)

class sched_of_dir(models.Model):  # Psp schedule of directors
    row_id = models.AutoField(primary_key=True) 
    reporting_date = models.CharField(max_length=20)
    psp_id = models.CharField(max_length=10)
    director_names = models.CharField(max_length=100)
    director_gender = models.CharField(max_length=10,choices=GENDER_CHOICES)
    type_of_director = models.CharField(max_length=10,choices=TYPE_OF_DIRECTOR_CHOICES)
    dob = models.DateField()
    nationality = models.CharField(max_length=10,choices=COUNTRY_CODE_CHOICES)
    resident_country = models.CharField(max_length=10,choices=COUNTRY_CODE_CHOICES)
    id_no_passport = models.CharField(max_length=10)
    pin = models.CharField(max_length=10)
    contact_number = models.CharField(max_length=10)
    qualifications = models.CharField(max_length=100)
    other_directorships = models.CharField(max_length=100)
    date_of_appointment = models.DateField()
    date_of_retirement = models.DateField()
    retirement_reason = models.CharField(max_length=100)
    disclosures = models.CharField(max_length=100)

class senior_mngt_schedule(models.Model): #psp schedule of senior management
    row_id = models.AutoField(primary_key=True)
    reporting_date = models.CharField(max_length=20)
    psp_id = models.CharField(max_length=10)
    officer_names = models.CharField(max_length=100)
    gender = models.CharField(max_length=10,choices=GENDER_CHOICES)
    designation = models.CharField(max_length=10,choices=DESIGNATION_CHOICES)
    dob = models.DateField()
    nationality = models.CharField(max_length=10,choices=COUNTRY_CODE_CHOICES)
    id_no = models.CharField(max_length=10)
    tax_id = models.CharField(max_length=10)
    qualification = models.CharField(max_length=100)
    date_of_emp = models.DateField()
    retirement_date = models.DateField()
    external_affiliates = models.CharField(max_length=100)
    other_disclosure = models.CharField(max_length=100)

class sched_of_share_hldrs(models.Model): #psp schedule of share holders
    row_id = models.AutoField(primary_key=True)
    reporting_date = models.CharField(max_length=20)
    psp_id = models.CharField(max_length=10)
    shareholder_name= models.CharField(max_length=100)
    shareholder_gender = models.CharField(max_length=10,choices=GENDER_CHOICES)
    shareholder_type = models.CharField(max_length=10,choices=SHAREHOLDER_TYPE_CHOICES)
    dob_or_reg_date= models.DateField()
    nationality = models.CharField(max_length=10,choices=COUNTRY_CODE_CHOICES)
    resident_country = models.CharField(max_length=10,choices=COUNTRY_CODE_CHOICES)
    id_no_passport = models.CharField(max_length=10)
    pin = models.CharField(max_length=10)
    contact_number = models.CharField(max_length=10)
    qualifications = models.CharField(max_length=100)
    previous_employment= models.CharField(max_length=100)
    onboarding_date = models.DateField()
    no_of_shares_held = models.IntegerField()
    share_value = models.DecimalField(max_digits=12, decimal_places=2)
    percentage_of_share = models.DecimalField(max_digits=12, decimal_places=2)

class sched_of_trustees(models.Model): #psp schedule of trustees
    row_id = models.AutoField(primary_key=True)
    reporting_date = models.CharField(max_length=20)
    psp_id = models.CharField(max_length=10)
    trust_comp_name = models.CharField(max_length=100)
    directors_trust_comp = models.CharField(max_length=100)
    trustee_names = models.CharField(max_length=100)
    trustee_gender = models.CharField(max_length=10,choices=GENDER_CHOICES)
    dob = models.DateField()
    nationality = models.CharField(max_length=10,choices=COUNTRY_CODE_CHOICES)
    resident_country = models.CharField(max_length=10,choices=COUNTRY_CODE_CHOICES)
    id_no_passport = models.CharField(max_length=10)
    pin = models.CharField(max_length=10)
    contact_number = models.CharField(max_length=10)
    qualifications = models.CharField(max_length=100)
    other_trusteeships = models.CharField(max_length=100)
    disclosures = models.CharField(max_length=100)
    shareholders = models.CharField(max_length=100)
    shareholding_percentage = models.DecimalField(max_digits=12, decimal_places=2)

class psp_customer_compaints(models.Model):
    row_id = models.AutoField(primary_key=True)
    reporting_date = models.CharField(max_length=20)
    psp_id = models.CharField(max_length=10)
    complaint_id = models.CharField(max_length=10)
    complaint_code = models.CharField(max_length=10)
    complainant_gender = models.CharField(max_length=10,choices=GENDER_CHOICES)
    complaint_frequency = models.CharField(max_length=10,choices=COMPLAINT_FREQUENCY_CHOICES)
    complainant_name = models.CharField(max_length=100)
    complainant_age = models.CharField(max_length=10)
    complainant_contact_number = models.CharField(max_length=10)
    complainant_sub_county_location = models.CharField(max_length=100)
    complainant_education_level = models.CharField(max_length=100)
    other_complainant_details = models.CharField(max_length=100)
    agent_id = models.CharField(max_length=10)
    date_of_occurence = models.DateField()
    date_reported_to_the_institution = models.DateField()
    date_resolved = models.DateField()
    remedial_status = models.CharField(max_length=10,choices=REMEDIAL_STATUS_CHOICES)
    amount_lost = models.DecimalField(max_digits=12, decimal_places=2)
    amount_recovered = models.DecimalField(max_digits=12, decimal_places=2)
    
    
    
    
    
    
    # GATEWAY MODELS
    
    
class FailedRejectedTrxInfo(models.Model):
    # Payment Gateway Failed and Rejected Transactions
    psp_id = models.CharField(max_length=25, choices=PSP_ID_OTHER_CHOICES)
    bank_id = models.CharField(max_length=14,blank=False,null=False,choices=BANK_ID_CHOICES)
    reporting_date = models.DateField()
    customer_account_number = models.CharField(max_length=10,blank=False,null=False)
    channel_of_settlement = models.CharField(max_length=100,blank=False,null=False,choices=CHANNEL_SETTLEMENT_CHOICES)
    merchant_id = models.CharField(max_length=10,blank=False,null=False)
    email = models.EmailField(blank=False,null=False)
    rejection_failure_reason = models.CharField(max_length=10,blank=False,null=False,choices=REJECTIONS_CHOICES)
    number_of_transactions = models.PositiveBigIntegerField()
    value_of_transactions = models.DecimalField(max_digits=12, decimal_places=2,blank=False,null=False)

class PaymentGatewayTransactionsTarrifs(models.Model):
    reporting_date = models.DateField()
    psp_id = models.CharField(max_length=25, choices=PSP_ID_OTHER_CHOICES)
    channel_used = models.CharField(max_length=10,blank=False,null=False)
    channel_partner_name = models.CharField(max_length=10,blank=False,null=False)
    charge_description = models.CharField(max_length=10,blank=False,null=False)
    percentage_transaction_cost = models.DecimalField(max_digits=12, decimal_places=2,blank=False,null=False)
    absolute_transaction_cost = models.DecimalField(max_digits=12, decimal_places=2,blank=False,null=False)

class PaymentGatewayTransactionsDetails(models.Model):
    reporting_date = models.DateField()
    psp_id = models.CharField(max_length=25, choices=PSP_ID_OTHER_CHOICES)
    card_brand_type = models.CharField(max_length=10,blank=False,null=False,choices=CARD_BRAND_TYPE_CHOICES)
    card_type = models.CharField(max_length=10,blank=False,null=False,choices=CARD_TYPE_CHOICES)
    card_class_type = models.CharField(max_length=10,blank=False,null=False,choices=CLASS_CARD_TYPE_CHOICES)
    mobile_money_partner_id = models.CharField(max_length=10,blank=False,null=False)
    mobile_banking_partner_id = models.CharField(max_length=10,blank=False,null=False)
    transaction_category_type = models.CharField(max_length=10,blank=False,null=False,choices=TRANSACTION_CATEGORY_CHOICES)
    channel_type = models.CharField(max_length=10,blank=False,null=False,choices=CHANNEL_TYPE_CHOICES)
    total_number_of_transactions_done = models.PositiveBigIntegerField()
    total_value_of_transactions_done = models.DecimalField(max_digits=12, decimal_places=2,blank=False,null=False)

class PaymentGatewayBillingTemplate(models.Model):
    reporting_date = models.DateField()
    psp_id = models.CharField(max_length=25, choices=PSP_ID_OTHER_CHOICES)
    bill_classification_code = models.CharField(max_length=10,blank=False,null=False,choices=BILL_CLASSIFICATION_CODE)
    number_of_transactions = models.PositiveBigIntegerField()
    value_of_transactions = models.DecimalField(max_digits=12, decimal_places=2,blank=False,null=False)

class paymentGatewayCardBrands(models.Model):
    reporting_date=models.DateField()
    psp_id = models.CharField(max_length=25, choices=PSP_ID_OTHER_CHOICES)
    bank_id = models.CharField(max_length=15,choices=BANK_ID_CHOICES)
    card_flag = models.CharField(max_length=10,choices=CARD_FLAG_CHOICES)
    card_brand_type=models.CharField(max_length=10,choices=CARD_BRAND_TYPE_CHOICES)
    number_of_transactions = models.PositiveBigIntegerField()
    value_of_transactions = models.DecimalField(max_digits=12, decimal_places=2,blank=False,null=False)


