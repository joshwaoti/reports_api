from django.core.management.base import BaseCommand
from faker import Faker
from reports.models import *
from reports.choice_fields import *
import random
from datetime import datetime

class Command(BaseCommand):
    help = 'Populate MobilePspCustomerInfo with fake data'

    def handle(self, *args, **kwargs):
        today = datetime.now().strftime("%d-%m-%Y")
        faker = Faker()
        for _ in range(100):  # Adjust the range for the number of records you want to create
            psp_customer_info.objects.create(
                reporting_date="21-Nov-2024",
                psp_id=random.choice([choice[0] for choice in PSP_ID_OTHER_CHOICES]),
                sub_country_code=random.choice([choice[0] for choice in SUB_COUNTY_CHOICES]),
                gender=random.choice([choice[0] for choice in GENDER_CHOICES]),
                age_code=random.choice([choice[0] for choice in AGE_CHOICES]),
                wallet_code=random.choice([choice[0] for choice in WALLET_CHOICES]),
                no_of_customers_registered=faker.random_int(min=1, max=10000),
                no_of_customers_active=faker.random_int(min=1, max=10000),
                no_of_customers_inactive=faker.random_int(min=1, max=10000),
                no_of_customers_dormant=faker.random_int(min=1, max=10000),
                balances_in_customer_accts=faker.pydecimal(left_digits=10, right_digits=2, positive=True),
                volume_of_transactions=faker.random_int(min=1, max=10000),
                value_of_transactions=faker.pydecimal(left_digits=10, right_digits=2, positive=True),
            )
        self.stdout.write(self.style.SUCCESS('Successfully populated MobilePspCustomerInfo with fake data'))

        for _ in range(100):  # Adjust the range for the number of records you want to create
            psp_transac_categorization_info.objects.create(
                psp_id=random.choice([choice[0] for choice in PSP_ID_OTHER_CHOICES]),
                reporting_date="21-Nov-2024",
                sub_transaction_code=random.choice([choice[0] for choice in SUB_TRANSACTION_CHOICES]),
                band_code=random.choice([choice[0] for choice in BAND_CHOICES]),
                volume_of_transactions=faker.random_int(min=1, max=10000),
                value_of_transactions=faker.pydecimal(left_digits=10, right_digits=2, positive=True),
            )

        self.stdout.write(self.style.SUCCESS('Successfully populated MobilePspTransactionCategorization with fake data'))
        
        # Populate MobilePspInteroperability
        for _ in range(100):
            interoperability_data.objects.create(
                psp_id=random.choice([choice[0] for choice in PSP_ID_OTHER_CHOICES]),
                reporting_date="21-Nov-2024",
                band_code=random.choice([choice[0] for choice in BAND_CHOICES]),
                psp_id_other=random.choice([choice[0] for choice in PSP_ID_OTHER_CHOICES]),
                interoperability_code=random.choice([choice[0] for choice in INTEROP_CHOICES]),
                incoming_transaction_volume=faker.random_int(min=1, max=10000),
                incoming_transaction_value=faker.pydecimal(left_digits=10, right_digits=2, positive=True),
                outgoing_transaction_volume=faker.random_int(min=1, max=10000),
                outgoing_transaction_value=faker.pydecimal(left_digits=10, right_digits=2, positive=True),
            )
        self.stdout.write(self.style.SUCCESS('Successfully populated MobilePspInteroperability with fake data'))

        # Populate PspTrustAccountPlacement
        for _ in range(100):
            trust_account_info.objects.create(
                psp_id=random.choice([choice[0] for choice in PSP_ID_OTHER_CHOICES]),
                reporting_date="21-Nov-2024",
                trust_fund_placement=faker.word(),
                trust_fund_inv_maturity_date=faker.date(pattern='%Y-%m-%d', end_datetime=None),
                cat_trust_fund_invested_amt=faker.pydecimal(left_digits=10, right_digits=2, positive=True),
                interest_amt_per_category=faker.pydecimal(left_digits=10, right_digits=2, positive=True),
            )
        self.stdout.write(self.style.SUCCESS('Successfully populated PspTrustAccountPlacement with fake data'))

        # Populate MobilePspAgentsInformation
        for _ in range(100):
            psp_agents_info.objects.create(
                psp_id=random.choice([choice[0] for choice in PSP_ID_OTHER_CHOICES]),
                reporting_date="21-Nov-2024",
                agent_type_code=random.choice([choice[0] for choice in AGENT_TYPE_CHOICES]),
                agents_id=faker.lexify(text='??????????'),
                gps_cordinates=faker.lexify(text='??????????'),
                sub_county_code=random.choice([choice[0] for choice in SUB_COUNTY_CHOICES]),
                agent_status=random.choice([choice[0] for choice in AGENT_STATUS_CHOICES]),
                band_code=random.choice([choice[0] for choice in BAND_CHOICES]),
                volume_cash_in_at_agents=faker.random_int(min=1, max=10000),
                value_cash_in_at_agents=faker.pydecimal(left_digits=10, right_digits=2, positive=True),
                volume_of_cash_out_at_agents=faker.random_int(min=1, max=10000),
                value_of_cash_out_at_agents=faker.pydecimal(left_digits=10, right_digits=2, positive=True),
                amount_of_eFloat_mobile_agents=faker.pydecimal(left_digits=10, right_digits=2, positive=True),
                number_of_agent_cash_dep_banks=faker.random_int(min=1, max=10000),
                value_of_agent_cash_dep_banks=faker.pydecimal(left_digits=10, right_digits=2, positive=True),
                no_of_agent_cash_withd_banks=faker.random_int(min=1, max=10000),
                value_of_agent_cash_withd_banks=faker.pydecimal(left_digits=10, right_digits=2, positive=True),
            )
        self.stdout.write(self.style.SUCCESS('Successfully populated MobilePspAgentsInformation with fake data'))

        # Populate psp_tariffs_info
        for _ in range(100):
            psp_tariffs_info.objects.create(
                psp_id=random.choice([choice[0] for choice in PSP_ID_OTHER_CHOICES]),
                reporting_date="21-Nov-2024",
                band_code=random.choice([choice[0] for choice in BAND_CHOICES]),
                p2p_on_net_registered_wallet=faker.random_int(min=1, max=1000),
                p2p_on_net_non_reg_wallet=faker.random_int(min=1, max=1000),
                p2p_off_net_registered_wallet=faker.random_int(min=1, max=1000),
                p2p_off_net_non_reg_wallet=faker.random_int(min=1, max=1000),
                cash_withdrawals_mob_money_agent=faker.random_int(min=1, max=1000),
                cash_withdrawals_bank_ATMs=faker.random_int(min=1, max=1000),
                agent_com_cash_out_reg_cust=faker.random_int(min=1, max=1000),
                agent_com_cash_out_non_reg_cust=faker.random_int(min=1, max=1000),
                agent_commision_for_cash_in=faker.random_int(min=1, max=1000),
                ATM_commision_for_cash_out=faker.random_int(min=1, max=1000),
                ATM_commision_for_cash_in=faker.random_int(min=1, max=1000),
                # Commenting out the problematic field until we confirm the correct name
                # B2C_paybill_type1_customer=faker.random_int(min=1, max=1000),
                B2C_payments_paybill_type2_cust=faker.random_int(min=1, max=1000),
                B2C_payments_paybill_type2_bus=faker.random_int(min=1, max=1000),
                B2C_payments_paybill_type3_bus=faker.random_int(min=1, max=1000),
                C2B_payments_paybill_type1_customer=faker.random_int(min=1, max=1000),
                C2B_payments_paybill_type2_cust=faker.random_int(min=1, max=1000),
                C2B_payments_paybill_type2_bus=faker.random_int(min=1, max=1000),
                C2B_payments_paybill_type3_bus=faker.random_int(min=1, max=1000),
                B2B_payments_paybill_type1_customer=faker.random_int(min=1, max=1000),
                B2B_payments_paybill_type2_cust=faker.random_int(min=1, max=1000),
                B2B_payments_paybill_type2_bus=faker.random_int(min=1, max=1000),
                B2B_payments_paybill_type3=faker.random_int(min=1, max=1000),
                B2C_payments_payments_bank_aggreg_codes=faker.random_int(min=1, max=1000),
                C2B_payments_bank_aggreg_codes=faker.random_int(min=1, max=1000),
                till_number_payments=faker.random_int(min=1, max=1000),
                cross_border_Int_mny_trans_out=faker.random_int(min=1, max=1000),
                cross_border_int_mny_trans_in=faker.random_int(min=1, max=1000),
                P2P_outgoing_reg_partner_net=faker.random_int(min=1, max=1000)
            )
        self.stdout.write(self.style.SUCCESS('Successfully populated psp_tariffs_info'))

        # Populate merchant_cust_balance_info
        for _ in range(100):
            merchant_cust_balance_info.objects.create(
                psp_id=random.choice([choice[0] for choice in PSP_ID_OTHER_CHOICES]),
                reporting_date="21-Nov-2024",
                merchant_id=faker.lexify(text='??????????'),
                merchant_type_code=random.choice([choice[0] for choice in MERCHANT_TYPE_CHOICES]),
                merchant_name=faker.company(),
                company_name=faker.company(),
                merchant_classification_code=random.choice([choice[0] for choice in MERCHANT_CLASSIFICATION_CODE_CHOICES]),
                sub_county_code=random.choice([choice[0] for choice in SUB_COUNTY_CHOICES]),
                merchant_status_code=random.choice([choice[0] for choice in MERCHANT_STATUS_CHOICES]),
                no_of_customers=faker.random_int(min=1, max=10000),
                eod_balances=faker.pydecimal(left_digits=10, right_digits=2, positive=True)
            )
        self.stdout.write(self.style.SUCCESS('Successfully populated merchant_cust_balance_info'))

        # Populate failed_txn_data
        for _ in range(100):
            failed_txn_data.objects.create(
                psp_id=random.choice([choice[0] for choice in PSP_ID_OTHER_CHOICES]),
                reporting_date="21-Nov-2024",
                failed_transaction_code=random.choice([choice[0] for choice in FAILED_TRANSACTION_CODE_CHOICES]),
                band_code=random.choice([choice[0] for choice in BAND_CHOICES]),
                volume_of_transactions=faker.random_int(min=1, max=10000),
                value_of_transactions=faker.pydecimal(left_digits=10, right_digits=2, positive=True),
                percentage_of_failed_transactions=faker.random_int(min=1, max=100)
            )
        self.stdout.write(self.style.SUCCESS('Successfully populated failed_txn_data'))

        # Populate new_mobile_agents
        for _ in range(100):
            new_mobile_agents.objects.create(
                psp_id=random.choice([choice[0] for choice in PSP_ID_OTHER_CHOICES]),
                reporting_date="21-Nov-2024",
                sub_county_code=random.choice([choice[0] for choice in SUB_COUNTY_CHOICES]),
                agent_id=faker.lexify(text='??????????'),
                store_number=faker.lexify(text='??????????'),
                agent_name=faker.name(),
                agent_type=random.choice([choice[0] for choice in AGENT_TYPE_CHOICES]),
                agent_status=random.choice([choice[0] for choice in AGENT_STATUS_CHOICES]),
                physical_address=faker.address(),
                postal_address=faker.address(),
                date_of_onboarding=faker.date_between(start_date='-2y', end_date='today'),
                contact_number=faker.numerify(text='##########')[:15],
                name_of_owner=faker.name(),
                contact_of_owner=faker.phone_number(),
                main_commercial_activity=faker.company(),
                num_trainings_conducted=str(faker.random_int(min=1, max=10)),
                suspension_termination_date=faker.date_between(start_date='-1y', end_date='today'),
                suspension_termination_reason=faker.sentence()
            )
        self.stdout.write(self.style.SUCCESS('Successfully populated new_mobile_agents'))

        # Populate counterfeit_transactions
        for _ in range(100):
            counterfeit_transactions.objects.create(
                psp_id=random.choice([choice[0] for choice in PSP_ID_OTHER_CHOICES]),
                reporting_date="21-Nov-2024",
                sub_county_code=random.choice([choice[0] for choice in SUB_COUNTY_CHOICES]),
                agent_id=faker.lexify(text='??????????'),
                denomination_code=random.choice([choice[0] for choice in DENOMINATION_CODE_CHOICES]),
                serial_number=faker.lexify(text='??????????'),
                depositors_name=faker.name(),
                tellers_name=faker.name(),
                date_confiscated=faker.date_between(start_date='-1y', end_date='today'),
                remarks=faker.sentence(),
                number_of_pieces=faker.random_int(min=1, max=100)
            )
        self.stdout.write(self.style.SUCCESS('Successfully populated counterfeit_transactions'))

        # Populate wallet_to_wallet
        for _ in range(100):
            wallet_to_wallet.objects.create(
                psp_id=random.choice([choice[0] for choice in PSP_ID_OTHER_CHOICES]),
                reporting_date="21-Nov-2024",
                segmentation_code=random.choice([choice[0] for choice in SEGMENTATION_CODE_CHOICES]),
                busines_size_code=random.choice([choice[0] for choice in BUSINESS_SIZE_CODE_CHOICES]),
                volume_of_transactions=faker.random_int(min=1, max=10000),
                value_of_transactions=faker.pydecimal(left_digits=10, right_digits=2, positive=True)
            )
        self.stdout.write(self.style.SUCCESS('Successfully populated wallet_to_wallet'))

        # Populate pymt_gw_card_brands
        for _ in range(100):
            pymt_gw_card_brands.objects.create(
                reporting_date="21-Nov-2024",
                psp_id=random.choice([choice[0] for choice in PSP_ID_OTHER_CHOICES]),
                bank_id=faker.lexify(text='?????'),
                transaction_category=random.choice([choice[0] for choice in TRANSACTION_CATEGORY_CHOICES]),
                card_brand_type=random.choice([choice[0] for choice in CARD_BRAND_TYPE_CHOICES]),
                number_of_txns=faker.random_int(min=1, max=10000),
                value_of_txns=faker.pydecimal(left_digits=10, right_digits=2, positive=True)
            )
        self.stdout.write(self.style.SUCCESS('Successfully populated pymt_gw_card_brands'))

        # Populate card_switch_info
        for _ in range(100):
            card_switch_info.objects.create(
                psp_id=random.choice([choice[0] for choice in PSP_ID_OTHER_CHOICES]),
                reporting_date="21-Nov-2024",
                bank_code=faker.lexify(text='?????'),
                system_name=faker.company(),
                card_flag=random.choice([choice[0] for choice in CARD_FLAG_CHOICES]),
                card_type=random.choice([choice[0] for choice in CARD_TYPE_CHOICES]),
                no_of_cards=faker.random_int(min=1, max=10000),
                vol_of_transactions_DR=faker.random_int(min=1, max=10000),
                value_of_transaction_DR=faker.random_int(min=1, max=10000),
                vol_of_transactions_CR=faker.random_int(min=1, max=10000),
                value_of_transaction_CR=faker.random_int(min=1, max=10000),
                net_settlement_instruction_DR=faker.random_int(min=1, max=10000),
                net_settlement_instruction_CR=faker.random_int(min=1, max=10000)
            )
        self.stdout.write(self.style.SUCCESS('Successfully populated card_switch_info'))

        # Populate p2p_switch_info
        for _ in range(100):
            p2p_switch_info.objects.create(
                reporting_date="21-Nov-2024",
                bank_id=faker.lexify(text='?????')[:5],
                transcation_channel=faker.word()[:10],
                no_of_registered_customer=faker.random_int(min=1, max=10000),
                no_of_active_customer=faker.random_int(min=1, max=10000),
                no_of_transactions_outgoing=faker.random_int(min=1, max=10000),
                value_of_transactions_ongoing=faker.pydecimal(left_digits=10, right_digits=2, positive=True),
                no_of_transactions_incoming=faker.random_int(min=1, max=10000),
                value_of_transactions_incoming=faker.pydecimal(left_digits=10, right_digits=2, positive=True),
                net_settlement_instruction_dr=faker.pydecimal(left_digits=10, right_digits=2, positive=True)
            )
        self.stdout.write(self.style.SUCCESS('Successfully populated p2p_switch_info'))

        # Populate psp_products_info
        for _ in range(100):
            psp_products_info.objects.create(
                psp_id=random.choice([choice[0] for choice in PSP_ID_OTHER_CHOICES]),
                reporting_date="21-Nov-2024",
                product_ownership_flag=random.choice([choice[0] for choice in PRODUCT_CATEGORY_CHOICES]),
                product_ownership_category=random.choice([choice[0] for choice in PRODUCT_OWNERSHIP_CATEGORY_CHOICES]),
                product_partner_name=faker.company()[:25],
                product_transaction_code=random.choice([choice[0] for choice in PRODUCT_TRANSACTION_CODE_CHOICES]),
                product_name=faker.word()[:10],
                gender=random.choice([choice[0] for choice in GENDER_CHOICES]),
                status_code=random.choice([choice[0] for choice in STATUS_CODE_CHOICES]),
                band_code=random.choice([choice[0] for choice in BAND_CHOICES]),
                no_of_customers=faker.random_int(min=1, max=10000),
                no_of_transactions=faker.random_int(min=1, max=10000),
                value_of_transactions=faker.pydecimal(left_digits=10, right_digits=2, positive=True)
            )
        self.stdout.write(self.style.SUCCESS('Successfully populated psp_products_info'))

        # Populate trustaccount_data
        for _ in range(100):
            trustaccount_data.objects.create(
                psp_id=random.choice([choice[0] for choice in PSP_ID_OTHER_CHOICES]),
                reporting_date="21-Nov-2024",
                bank_id=random.choice([choice[0] for choice in BANK_ID_CHOICES]),
                bank_account_number=faker.random_int(min=1000, max=999999),
                trust_account_debit_types_code=random.choice([choice[0] for choice in DEBIT_TYPE_CODE_CHOICES]),
                org_recieving_donations=faker.company(),
                sector_code=random.choice([choice[0] for choice in SECTOR_CODE_CHOICES]),
                trust_acc_int_utilized_details=faker.sentence(),
                trust_acc_opening_balance=faker.pydecimal(left_digits=10, right_digits=2, positive=True),
                principal_amount=faker.pydecimal(left_digits=10, right_digits=2, positive=True),
                trust_acc_interest_earned=faker.pydecimal(left_digits=10, right_digits=2, positive=True),
                closing_balance=faker.pydecimal(left_digits=10, right_digits=2, positive=True),
                trust_acc_interest_utilized=faker.pydecimal(left_digits=10, right_digits=2, positive=True)
            )
        self.stdout.write(self.style.SUCCESS('Successfully populated trustaccount_data'))

        # Populate incidents_data
        for _ in range(100):
            incidents_data.objects.create(
                psp_id=random.choice([choice[0] for choice in PSP_ID_OTHER_CHOICES]),
                reporting_date="21-Nov-2024",
                sub_county_code=random.choice([choice[0] for choice in SUB_COUNTY_CHOICES]),
                sub_fraud_code=faker.lexify(text='????'),
                fraud_category_flag=faker.lexify(text='????'),
                victim_category=random.choice([choice[0] for choice in VICTIM_CATEGORY_CHOICES]),
                victim_information=random.choice([choice[0] for choice in VICTIM_INFORMATION_CHOICES]),
                date_of_occurence=faker.date_between(start_date='-1y', end_date='today'),
                number_of_incidences=faker.random_int(min=1, max=100),
                amount_involved=faker.pydecimal(left_digits=10, right_digits=2, positive=True),
                amount_lost=faker.pydecimal(left_digits=10, right_digits=2, positive=True),
                amount_recovered=faker.pydecimal(left_digits=10, right_digits=2, positive=True),
                action_taken=faker.sentence(),
                recovery_details=faker.sentence()
            )
        self.stdout.write(self.style.SUCCESS('Successfully populated incidents_data'))

        # Populate system_activity_info
        for _ in range(100):
            system_activity_info.objects.create(
                reporting_date="21-Nov-2024",
                psp_id=random.choice([choice[0] for choice in PSP_ID_OTHER_CHOICES]),
                hour_of_day=random.choice([choice[0] for choice in TIME_CHOICES]),
                no_of_transactions_per_sec=faker.random_int(min=1, max=1000),
                no_of_transactions_per_hr=faker.random_int(min=1, max=10000)
            )
        self.stdout.write(self.style.SUCCESS('Successfully populated system_activity_info'))

        # Populate psp_customer_complaints
        for _ in range(100):
            psp_customer_complaints.objects.create(
                reporting_date="21-Nov-2024",
                psp_id=random.choice([choice[0] for choice in PSP_ID_OTHER_CHOICES]),
                complaint_code=random.choice([choice[0] for choice in COMPLAINTS_CODE_CHOICES]),
                complainant_gender=random.choice([choice[0] for choice in GENDER_CHOICES]),
                complaint_frequency=random.choice([choice[0] for choice in COMPLAINTS_FREQUENCY_CODE_CHOICES]),
                complaint_name=faker.sentence(),
                complainant_age=random.choice([choice[0] for choice in AGE_CHOICES]),
                complainant_contact_number=faker.phone_number()[:10],
                complainant_sub_county_location=random.choice([choice[0] for choice in SUB_COUNTY_CHOICES]),
                complainant_education_level=random.choice([choice[0] for choice in EDUCATION_CHOICES]),
                other_complainant_details=faker.sentence(),
                agent_id=faker.lexify(text='??????????'),
                date_of_occurence=faker.date_between(start_date='-1y', end_date='today'),
                date_reported_to_the_institution=faker.date_between(start_date='-1y', end_date='today'),
                date_resolved=faker.date_between(start_date='-1y', end_date='today'),
                remedial_status=random.choice([choice[0] for choice in REMEDIAL_STATUS_CHOICES]),
                amount_lost=faker.pydecimal(left_digits=10, right_digits=2, positive=True),
                amount_recovered=faker.pydecimal(left_digits=10, right_digits=2, positive=True)
            )
        self.stdout.write(self.style.SUCCESS('Successfully populated psp_customer_complaints'))

        # Populate sch_sy_stabil_srvce_int
        for _ in range(100):
            sch_sy_stabil_srvce_int.objects.create(
                reporting_date="21-Nov-2024",
                sub_county_code=random.choice([choice[0] for choice in SUB_COUNTY_CHOICES]),
                system_owner_flag=random.choice([choice[0] for choice in SYSTEM_CATEGORY_OWNER_FLAG_CHOICES]),
                third_party_owned_category=random.choice([choice[0] for choice in THIRD_PARTY_OWNED_CATEGORY_CHOICES]),
                third_party_name=faker.company(),
                product_type=random.choice([choice[0] for choice in PRODUCT_TYPE_CHOICES]),
                system_unavailability_type_code=random.choice([choice[0] for choice in SYSTEM_UNAVAILABILITY_CHOICES]),
                third_party_system_affected=faker.sentence(),
                service_interruption_cause_code=random.choice([choice[0] for choice in INTERRUPTION_CODE_CHOICES]),
                severity_interruption_code=random.choice([choice[0] for choice in DISRUPTION_CODE_CHOICES]),
                recovery_time_code=random.choice([choice[0] for choice in RECOVERY_TIME_CHOICES]),
                remedial_status_code=random.choice([choice[0] for choice in REMEDIAL_STATUS_CHOICES]),
                system_uptime_percentage=faker.pydecimal(left_digits=2, right_digits=2, positive=True)
            )
        self.stdout.write(self.style.SUCCESS('Successfully populated sch_sy_stabil_srvce_int'))

        # Populate psp_cybersecurity_incident_record
        for _ in range(100):
            psp_cybersecurity_incident_record.objects.create(
                reporting_date="21-Nov-2024",
                psp_id=random.choice([choice[0] for choice in PSP_ID_OTHER_CHOICES]),
                incident_number=faker.lexify(text='INC??????'),
                location_of_attacker=random.choice([choice[0] for choice in COUNTRY_CODE_CHOICES]),
                incident_mode=random.choice([choice[0] for choice in INCIDENT_MODE_CHOICES]),
                date_and_time_of_incident_happened=faker.date_time_this_year(),
                loss_type=random.choice([choice[0] for choice in LOSS_TYPE_CHOICES]),
                details_of_the_incident=faker.sentence(),
                action_taken_to_manage_the_incident=faker.sentence(),
                date_and_time_of_the_incident_resolution=faker.date_time_this_year(),
                action_taken_to_mitigate_future_incidents=faker.sentence(),
                amount_involved=faker.pydecimal(left_digits=10, right_digits=2, positive=True),
                amount_lost=faker.pydecimal(left_digits=10, right_digits=2, positive=True)
            )
        self.stdout.write(self.style.SUCCESS('Successfully populated psp_cybersecurity_incident_record'))

        # Populate sched_of_dir
        for _ in range(100):
            sched_of_dir.objects.create(
                reporting_date="21-Nov-2024",
                psp_id=random.choice([choice[0] for choice in PSP_ID_OTHER_CHOICES]),
                director_names=faker.name(),
                director_gender=random.choice([choice[0] for choice in GENDER_CHOICES]),
                type_of_director=random.choice([choice[0] for choice in TYPE_OF_DIRECTOR_CHOICES]),
                dob=faker.date_of_birth(minimum_age=30, maximum_age=70),
                nationality=random.choice([choice[0] for choice in COUNTRY_CODE_CHOICES]),
                resident_country=random.choice([choice[0] for choice in COUNTRY_CODE_CHOICES]),
                id_no_passport=faker.lexify(text='????????'),
                pin=faker.lexify(text='??????'),
                contact_number=faker.phone_number()[:10],
                qualifications=faker.sentence(),
                other_directorships=faker.sentence(),
                date_of_appointment=faker.date_between(start_date='-5y', end_date='today'),
                date_of_retirement=faker.date_between(start_date='today', end_date='+10y'),
                retirement_reason=faker.sentence(),
                disclosures=faker.sentence()
            )
        self.stdout.write(self.style.SUCCESS('Successfully populated sched_of_dir'))

        # Populate senior_mngt_schedule
        for _ in range(100):
            senior_mngt_schedule.objects.create(
                reporting_date="21-Nov-2024",
                psp_id=random.choice([choice[0] for choice in PSP_ID_OTHER_CHOICES]),
                officer_names=faker.name(),
                gender=random.choice([choice[0] for choice in GENDER_CHOICES]),
                designation=random.choice([choice[0] for choice in DESIGNATION_CHOICES]),
                dob=faker.date_of_birth(minimum_age=25, maximum_age=65),
                nationality=random.choice([choice[0] for choice in COUNTRY_CODE_CHOICES]),
                id_no=faker.lexify(text='????????'),
                tax_id=faker.lexify(text='??????'),
                qualification=faker.sentence(),
                date_of_emp=faker.date_between(start_date='-10y', end_date='today'),
                retirement_date=faker.date_between(start_date='today', end_date='+15y'),
                external_affiliates=faker.sentence(),
                other_disclosure=faker.sentence()
            )
        self.stdout.write(self.style.SUCCESS('Successfully populated senior_mngt_schedule'))

        # Populate sched_of_share_hldrs
        for _ in range(100):
            sched_of_share_hldrs.objects.create(
                reporting_date="21-Nov-2024",
                psp_id=random.choice([choice[0] for choice in PSP_ID_OTHER_CHOICES]),
                shareholder_name=faker.name(),
                shareholder_gender=random.choice([choice[0] for choice in GENDER_CHOICES]),
                shareholder_type=random.choice([choice[0] for choice in SHAREHOLDER_TYPE_CHOICES]),
                dob_or_reg_date=faker.date_of_birth(minimum_age=18, maximum_age=80),
                nationality=random.choice([choice[0] for choice in COUNTRY_CODE_CHOICES]),
                resident_country=random.choice([choice[0] for choice in COUNTRY_CODE_CHOICES]),
                id_no_passport=faker.lexify(text='????????'),
                pin=faker.lexify(text='??????'),
                contact_number=faker.phone_number()[:10],
                qualifications=faker.sentence(),
                previous_employment=faker.company(),
                onboarding_date=faker.date_between(start_date='-5y', end_date='today'),
                no_of_shares_held=faker.random_int(min=100, max=10000),
                share_value=faker.pydecimal(left_digits=6, right_digits=2, positive=True),
                percentage_of_share=faker.pydecimal(left_digits=2, right_digits=2, positive=True)
            )
        self.stdout.write(self.style.SUCCESS('Successfully populated sched_of_share_hldrs'))

        # Populate sched_of_trustees
        for _ in range(100):
            sched_of_trustees.objects.create(
                reporting_date="21-Nov-2024",
                psp_id=random.choice([choice[0] for choice in PSP_ID_OTHER_CHOICES]),
                trust_comp_name=faker.company(),
                directors_trust_comp=faker.name(),
                trustee_names=faker.name(),
                trustee_gender=random.choice([choice[0] for choice in GENDER_CHOICES]),
                dob=faker.date_of_birth(minimum_age=30, maximum_age=70),
                nationality=random.choice([choice[0] for choice in COUNTRY_CODE_CHOICES]),
                resident_country=random.choice([choice[0] for choice in COUNTRY_CODE_CHOICES]),
                id_no_passport=faker.lexify(text='????????'),
                pin=faker.lexify(text='??????'),
                contact_number=faker.phone_number()[:10],
                qualifications=faker.sentence(),
                other_trusteeships=faker.sentence(),
                disclosures=faker.sentence(),
                shareholders=faker.name(),
                shareholding_percentage=faker.pydecimal(left_digits=2, right_digits=2, positive=True)
            )
        self.stdout.write(self.style.SUCCESS('Successfully populated sched_of_trustees'))

        # Populate Gateway Models
        # Populate FailedRejectedTrxInfo
        for _ in range(100):
            failed_rejected_trx_info.objects.create(
                psp_id=random.choice([choice[0] for choice in PSP_ID_OTHER_CHOICES]),
                bank_id=random.choice([choice[0] for choice in BANK_ID_CHOICES]),
                reporting_date=faker.date_this_year(),
                customer_account_number=faker.lexify(text='????????'),
                channel_of_settlement=random.choice([choice[0] for choice in CHANNEL_SETTLEMENT_CHOICES]),
                merchant_id=faker.lexify(text='????????'),
                email=faker.email(),
                rejection_failure_reason=random.choice([choice[0] for choice in REJECTIONS_CHOICES]),
                number_of_transactions=faker.random_int(min=1, max=10000),
                value_of_transactions=faker.pydecimal(left_digits=10, right_digits=2, positive=True)
            )
        self.stdout.write(self.style.SUCCESS('Successfully populated FailedRejectedTrxInfo'))

        # Populate PaymentGatewayTransactionsTarrifs
        for _ in range(100):
            payment_gateway_tariffs.objects.create(
                reporting_date=faker.date_this_year(),
                psp_id=random.choice([choice[0] for choice in PSP_ID_OTHER_CHOICES]),
                channel_used=faker.word()[:10],
                channel_partner_name=faker.company()[:10],
                charge_description=faker.sentence(nb_words=3)[:10],
                percentage_transaction_cost=faker.pydecimal(left_digits=2, right_digits=2, positive=True),
                absolute_transaction_cost=faker.pydecimal(left_digits=4, right_digits=2, positive=True)
            )
        self.stdout.write(self.style.SUCCESS('Successfully populated PaymentGatewayTransactionsTarrifs'))

        # Populate PaymentGatewayTransactionsDetails
        for _ in range(100):
            payment_gateway_transactions_details.objects.create(
                reporting_date=faker.date_this_year(),
                psp_id=random.choice([choice[0] for choice in PSP_ID_OTHER_CHOICES]),
                card_brand_type=random.choice([choice[0] for choice in CARD_BRAND_TYPE_CHOICES]),
                card_type=random.choice([choice[0] for choice in CARD_TYPE_CHOICES]),
                card_class_type=random.choice([choice[0] for choice in CLASS_CARD_TYPE_CHOICES]),
                mobile_money_partner_id=faker.lexify(text='????????'),
                mobile_banking_partner_id=faker.lexify(text='????????'),
                transaction_category_type=random.choice([choice[0] for choice in TRANSACTION_CATEGORY_CHOICES]),
                channel_type=random.choice([choice[0] for choice in CHANNEL_TYPE_CHOICES]),
                total_number_of_transactions_done=faker.random_int(min=1, max=10000),
                total_value_of_transactions_done=faker.pydecimal(left_digits=10, right_digits=2, positive=True)
            )
        self.stdout.write(self.style.SUCCESS('Successfully populated PaymentGatewayTransactionsDetails'))

        # Populate PaymentGatewayBillingTemplate
        for _ in range(100):
            pay_gtway_bill_temp.objects.create(
                reporting_date=faker.date_this_year(),
                psp_id=random.choice([choice[0] for choice in PSP_ID_OTHER_CHOICES]),
                bill_classification_code=random.choice([choice[0] for choice in BILL_CLASSIFICATION_CODE]),
                number_of_transactions=faker.random_int(min=1, max=10000),
                value_of_transactions=faker.pydecimal(left_digits=10, right_digits=2, positive=True)
            )
        self.stdout.write(self.style.SUCCESS('Successfully populated PaymentGatewayBillingTemplate'))

        # Populate paymentGatewayCardBrands
        # for _ in range(100):
        #     pymt_gw_card_brands.objects.create(
        #         reporting_date=faker.date_this_year(),
        #         psp_id=random.choice([choice[0] for choice in PSP_ID_OTHER_CHOICES]),
        #         bank_id=random.choice([choice[0] for choice in BANK_ID_CHOICES]),
        #         card_flag=random.choice([choice[0] for choice in CARD_FLAG_CHOICES]),
        #         card_brand_type=random.choice([choice[0] for choice in CARD_BRAND_TYPE_CHOICES]),
        #         number_of_transactions=faker.random_int(min=1, max=10000),
        #         value_of_transactions=faker.pydecimal(left_digits=10, right_digits=2, positive=True)
        #     )
        # self.stdout.write(self.style.SUCCESS('Successfully populated paymentGatewayCardBrands'))
        
        for _ in range(100):
            merchant_transaction_info.objects.create(
                psp_id=random.choice([choice[0] for choice in PSP_ID_OTHER_CHOICES]),
                reporting_date=datetime.now().strftime("%d-%b-%Y"),
                merchant_id=faker.lexify(text='?????'),  # Random 5-character string
                merchant_type_code=random.choice([choice[0] for choice in MERCHANT_TYPE_CHOICES]),
                merchant_name=faker.company(),
                company_name=faker.company(),
                merchant_classification_code=random.choice([choice[0] for choice in MERCHANT_CLASSIFICATION_CODE_CHOICES]),
                sub_county_code=random.choice([choice[0] for choice in SUB_COUNTY_CHOICES]),
                merchant_status_code=random.choice([choice[0] for choice in MERCHANT_STATUS_CHOICES]),
                band_code=random.choice([choice[0] for choice in BAND_CHOICES]),
                deposit_transactions_vol=faker.random_int(min=1, max=10000),
                deposit_transactions_value=faker.pydecimal(left_digits=8, right_digits=2, positive=True),
                no_of_withdrawal_transactions=faker.random_int(min=1, max=10000),
                withdrawal_transactions_value=faker.pydecimal(left_digits=8, right_digits=2, positive=True)
            )

        self.stdout.write(self.style.SUCCESS('Successfully populated merchant_transaction_info with fake data'))