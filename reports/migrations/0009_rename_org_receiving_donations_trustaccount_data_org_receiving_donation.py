# Generated by Django 5.1.1 on 2024-11-27 08:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0008_rename_p2p_off_net_registered_wallet_psp_tariffs_info_p2p_off_net_reg_wallet_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='trustaccount_data',
            old_name='org_receiving_donations',
            new_name='org_receiving_donation',
        ),
    ]
