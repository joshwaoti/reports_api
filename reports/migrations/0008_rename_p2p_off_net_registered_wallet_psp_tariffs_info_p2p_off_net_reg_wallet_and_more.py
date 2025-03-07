# Generated by Django 5.1.1 on 2024-11-27 06:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0007_rename_percentage_of_failed_transactions_failed_txn_data_percentage_of_failed_txns_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='psp_tariffs_info',
            old_name='p2p_off_net_registered_wallet',
            new_name='p2p_off_net_reg_wallet',
        ),
        migrations.AlterField(
            model_name='sch_sy_stabil_srvce_int',
            name='system_uptime_percentage',
            field=models.DecimalField(decimal_places=2, max_digits=5),
        ),
    ]
