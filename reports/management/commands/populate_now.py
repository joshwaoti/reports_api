from django.core.management.base import BaseCommand
from faker import Faker
from reports.models import *
from reports.choice_fields import *
import random

class Command(BaseCommand):
    help = 'Populate MobilePspCustomerInfo with fake data'

    def handle(self, *args, **kwargs):
        faker = Faker()
        for _ in range(100):  # Adjust the range for the number of records you want to create
            MobilePspCustomerInfo.objects.create(
                reporting_date=faker.date(pattern='%d-%b-%Y', end_datetime=None),
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
            MobilePspTransactionCategorization.objects.create(
                psp_id=random.choice([choice[0] for choice in PSP_ID_OTHER_CHOICES]),
                reporting_date=faker.date(pattern='%Y-%m-%d', end_datetime=None),
                sub_transaction_code=random.choice([choice[0] for choice in SUB_TRANSACTION_CHOICES]),
                band_code=random.choice([choice[0] for choice in BAND_CHOICES]),
                volume_of_transactions=faker.random_int(min=1, max=10000),
                value_of_transactions=faker.pydecimal(left_digits=10, right_digits=2, positive=True),
            )

        self.stdout.write(self.style.SUCCESS('Successfully populated MobilePspTransactionCategorization with fake data'))