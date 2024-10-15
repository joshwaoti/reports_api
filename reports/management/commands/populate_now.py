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
                reporting_date="14-Oct-2024",
                psp_id=random.choice([choice[0] for choice in PSP_ID_OTHER_CHOICES]),
                sub_county_code=random.choice([choice[0] for choice in SUB_COUNTY_CHOICES]),
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
                reporting_date="14-Oct-2024",
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
                reporting_date="14-Oct-2024",
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
                reporting_date="14-Oct-2024",
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
                reporting_date="14-Oct-2024",
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