# Generated by Django 5.1.1 on 2024-11-27 11:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0009_rename_org_receiving_donations_trustaccount_data_org_receiving_donation'),
    ]

    operations = [
        migrations.AlterField(
            model_name='failed_rejected_trx_info',
            name='reporting_date',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='pay_gtway_bill_temp',
            name='reporting_date',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='payment_gateway_tariffs',
            name='reporting_date',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='payment_gateway_transactions_details',
            name='reporting_date',
            field=models.CharField(max_length=20),
        ),
    ]
