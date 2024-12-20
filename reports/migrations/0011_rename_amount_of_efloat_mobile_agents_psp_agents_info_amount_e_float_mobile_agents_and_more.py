# Generated by Django 5.1.1 on 2024-11-28 06:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0010_alter_failed_rejected_trx_info_reporting_date_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='psp_agents_info',
            old_name='amount_of_eFloat_mobile_agents',
            new_name='amount_e_float_mobile_agents',
        ),
        migrations.RenameField(
            model_name='psp_agents_info',
            old_name='no_of_agent_cash_withd_banks',
            new_name='no_agent_cash_withd_banks',
        ),
        migrations.RenameField(
            model_name='psp_agents_info',
            old_name='number_of_agent_cash_dep_banks',
            new_name='number_agent_cash_dep_banks',
        ),
        migrations.RenameField(
            model_name='psp_agents_info',
            old_name='value_of_agent_cash_dep_banks',
            new_name='value_agent_cash_dep_banks',
        ),
        migrations.RenameField(
            model_name='psp_agents_info',
            old_name='value_of_agent_cash_withd_banks',
            new_name='value_agent_cash_withd_banks',
        ),
        migrations.RenameField(
            model_name='psp_agents_info',
            old_name='value_of_cash_out_at_agents',
            new_name='value_cash_out_at_agents',
        ),
        migrations.RenameField(
            model_name='psp_agents_info',
            old_name='volume_of_cash_out_at_agents',
            new_name='volume_cash_out_at_agents',
        ),
        migrations.RenameField(
            model_name='sch_sy_stabil_srvce_int',
            old_name='psp_id',
            new_name='psp_code',
        ),
    ]
