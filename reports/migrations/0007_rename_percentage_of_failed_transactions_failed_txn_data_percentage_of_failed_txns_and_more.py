# Generated by Django 5.1.1 on 2024-11-26 06:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0006_rename_sub_county_code_psp_customer_info_sub_country_code'),
    ]

    operations = [
        migrations.RenameField(
            model_name='failed_txn_data',
            old_name='percentage_of_failed_transactions',
            new_name='percentage_of_failed_txns',
        ),
        migrations.RenameField(
            model_name='incidents_data',
            old_name='reporting_date',
            new_name='report_date',
        ),
        migrations.RenameField(
            model_name='merchant_transaction_info',
            old_name='merchant_status_code',
            new_name='merchant_status',
        ),
        migrations.RenameField(
            model_name='psp_tariffs_info',
            old_name='ATM_commision_for_cash_in',
            new_name='agent_com_cash_out_unreg_cust',
        ),
        migrations.RenameField(
            model_name='psp_tariffs_info',
            old_name='ATM_commision_for_cash_out',
            new_name='agents_commission_for_cash_in',
        ),
        migrations.RenameField(
            model_name='psp_tariffs_info',
            old_name='B2B_payments_paybill_type1_customer',
            new_name='atm_commission_for_cash_in',
        ),
        migrations.RenameField(
            model_name='psp_tariffs_info',
            old_name='B2B_payments_paybill_type2_bus',
            new_name='atm_commission_for_cash_out',
        ),
        migrations.RenameField(
            model_name='psp_tariffs_info',
            old_name='B2B_payments_paybill_type2_cust',
            new_name='b2b_pay_bill_type_1_customer',
        ),
        migrations.RenameField(
            model_name='psp_tariffs_info',
            old_name='B2B_payments_paybill_type3',
            new_name='b2b_payment_p_bill_type_2_bus',
        ),
        migrations.RenameField(
            model_name='psp_tariffs_info',
            old_name='B2C_payments_paybill_type2_bus',
            new_name='b2b_payment_pay_bill_type_3',
        ),
        migrations.RenameField(
            model_name='psp_tariffs_info',
            old_name='B2C_payments_paybill_type2_cust',
            new_name='b2b_payment_pbill_type_2_cust',
        ),
        migrations.RenameField(
            model_name='psp_tariffs_info',
            old_name='B2C_payments_paybill_type3_bus',
            new_name='b2c_pay_bill_type_1_customer',
        ),
        migrations.RenameField(
            model_name='psp_tariffs_info',
            old_name='B2C_payments_payments_bank_aggreg_codes',
            new_name='b2c_payment_bank_aggreg_code',
        ),
        migrations.RenameField(
            model_name='psp_tariffs_info',
            old_name='C2B_payments_bank_aggreg_codes',
            new_name='b2c_payment_pbill_type_2_bus',
        ),
        migrations.RenameField(
            model_name='psp_tariffs_info',
            old_name='C2B_payments_paybill_type1_customer',
            new_name='b2c_payment_pbill_type_2_cust',
        ),
        migrations.RenameField(
            model_name='psp_tariffs_info',
            old_name='C2B_payments_paybill_type2_bus',
            new_name='b2c_payment_pbill_type_3_bus',
        ),
        migrations.RenameField(
            model_name='psp_tariffs_info',
            old_name='C2B_payments_paybill_type2_cust',
            new_name='c2b_pay_bill_type_1_customer',
        ),
        migrations.RenameField(
            model_name='psp_tariffs_info',
            old_name='C2B_payments_paybill_type3_bus',
            new_name='c2b_payment_bank_aggreg_code',
        ),
        migrations.RenameField(
            model_name='psp_tariffs_info',
            old_name='P2P_outgoing_reg_partner_net',
            new_name='c2b_payment_pbill_type_2_bus',
        ),
        migrations.RenameField(
            model_name='psp_tariffs_info',
            old_name='agent_com_cash_out_non_reg_cust',
            new_name='c2b_payment_pbill_type_2_cust',
        ),
        migrations.RenameField(
            model_name='psp_tariffs_info',
            old_name='agent_commision_for_cash_in',
            new_name='c2b_payment_pbill_type_3_bus',
        ),
        migrations.RenameField(
            model_name='psp_tariffs_info',
            old_name='cash_withdrawals_bank_ATMs',
            new_name='cash_withdrawal_mob_money_agent',
        ),
        migrations.RenameField(
            model_name='psp_tariffs_info',
            old_name='cash_withdrawals_mob_money_agent',
            new_name='cash_withdrawals_bank_atms',
        ),
        migrations.RenameField(
            model_name='psp_tariffs_info',
            old_name='cross_border_Int_mny_trans_out',
            new_name='cross_border_int_mny_trans_out',
        ),
        migrations.RenameField(
            model_name='sch_sy_stabil_srvce_int',
            old_name='service_interruption_cause_code',
            new_name='service_interruption_cause_cod',
        ),
        migrations.RenameField(
            model_name='sch_sy_stabil_srvce_int',
            old_name='system_unavailability_type_code',
            new_name='system_unavailability_type_cod',
        ),
        migrations.RenameField(
            model_name='system_activity_info',
            old_name='no_of_transactions_per_hr',
            new_name='no_of_transactions_per_hour',
        ),
        migrations.RenameField(
            model_name='trustaccount_data',
            old_name='org_recieving_donations',
            new_name='org_receiving_donations',
        ),
        migrations.RenameField(
            model_name='trustaccount_data',
            old_name='trust_account_debit_types_code',
            new_name='trust_acc_dr_type_code',
        ),
        migrations.RenameField(
            model_name='wallet_to_wallet',
            old_name='busines_size_code',
            new_name='business_size_code',
        ),
        migrations.RemoveField(
            model_name='system_activity_info',
            name='hour_of_day',
        ),
        migrations.AddField(
            model_name='psp_tariffs_info',
            name='p2p_outgoing_reg_partner_net',
            field=models.PositiveIntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='sch_sy_stabil_srvce_int',
            name='psp_id',
            field=models.CharField(choices=[('0800001', 'Safaricom Plc'), ('0800002', 'Airtel Money Kenya Limited'), ('0800003', 'Telkom Kenya Limited'), ('0800004', 'Mobile Pay Limited'), ('0800005', 'Kenswitch Limited'), ('0800006', 'Interswitch East Africa (K) Limited'), ('0800007', 'Integrated Payment Services Limited'), ('0800008', 'Viewtech Limited'), ('0800009', 'Web Tribe Limited'), ('0800010', 'Finserve Africa Limited'), ('0800011', 'Cellulant Kenya Limited'), ('0800012', 'Pesapal Limited'), ('0800013', 'Fivespot Limited'), ('0800014', 'Craft Silicon Limited'), ('0800015', 'Virtual Pay International Limited'), ('0800016', 'Direct Pay Limited'), ('0800017', 'Pesawise Services Limited'), ('0800018', 'Paystack Payments Kenya Limited'), ('0800019', 'Wakandi Kenya Limited'), ('0800020', 'Kenya Airports Parking Services (KAPS) Limited'), ('0800021', 'Loop Payco Limited'), ('0800022', 'DLocal Payments Kenya Limited'), ('0800023', 'Pesaflow Limited'), ('0800024', 'Kenya Commerce Exchange Service Bureau Limited'), ('0800025', 'PayU Kenya Limited'), ('0800026', 'Dolcepay Kenya Limited'), ('0800027', 'Unlimint Kenya Limited'), ('0800028', 'Gladys Technologies Limited'), ('0800029', 'Mamlaka Hub and Spoke Limited'), ('0800030', 'Eclectics International Limited'), ('0800031', 'Jumia Payment Services Kenya Limited'), ('0800032', 'Amsuka Capital Limited'), ('0800033', 'Sky World Limited'), ('0800034', 'Kashia Services Limited'), ('0800035', 'Data Integrated Limited'), ('0800036', 'Tanda Agent Limited')], default=1, max_length=25),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='system_activity_info',
            name='hour_of_the_day',
            field=models.CharField(choices=[('HH01', '00:00 - 00:59'), ('HH02', '01:00 - 01:59'), ('HH03', '02:00 - 02:59'), ('HH04', '03:00 - 03:59'), ('HH05', '04:00 - 04:59'), ('HH06', '05:00 - 05:59'), ('HH07', '06:00 - 06:59'), ('HH08', '07:00 - 07:59'), ('HH09', '08:00 - 08:59'), ('HH10', '09:00 - 09:59'), ('HH11', '10:00 - 10:59'), ('HH12', '11:00 - 11:59'), ('HH13', '12:00 - 12:59'), ('HH14', '13:00 - 13:59'), ('HH15', '14:00 - 14:59'), ('HH16', '15:00 - 15:59'), ('HH17', '16:00 - 16:59'), ('HH18', '17:00 - 17:59'), ('HH19', '18:00 - 18:59'), ('HH20', '19:00 - 19:59'), ('HH21', '20:00 - 20:59'), ('HH22', '21:00 - 21:59'), ('HH23', '22:00 - 22:59'), ('HH24', '23:00 - 23:59')], default=1, max_length=10),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='counterfeit_transactions',
            name='date_confiscated',
            field=models.CharField(max_length=15),
        ),
        migrations.AlterField(
            model_name='incidents_data',
            name='date_of_occurence',
            field=models.CharField(max_length=15),
        ),
        migrations.AlterField(
            model_name='incidents_data',
            name='fraud_category_flag',
            field=models.CharField(choices=[('FCT01', 'Actual'), ('FCT02', 'Attempted')], max_length=10),
        ),
        migrations.AlterField(
            model_name='incidents_data',
            name='sub_county_code',
            field=models.CharField(choices=[('101', 'CHANGAMWE'), ('102', 'JOMVU'), ('103', 'KISAUNI'), ('104', 'LIKONI'), ('105', 'MVITA'), ('106', 'NYALI'), ('201', 'KINANGO'), ('202', 'LUNGA LUNGA'), ('203', 'MATUGA'), ('204', 'MSAMBWENI'), ('205', 'SAMBURU'), ('301', 'CHONYI'), ('302', 'GANZE'), ('303', 'KALOLENI'), ('304', 'KAUMA'), ('305', 'KILIFI NORTH'), ('306', 'KILIFI SOUTH'), ('307', 'MAGARINI'), ('308', 'MALINDI'), ('309', 'RABAI'), ('401', 'TANA DELTA'), ('402', 'TANA NORTH'), ('403', 'TANA RIVER'), ('501', 'LAMU EAST'), ('502', 'LAMU WEST'), ('601', 'MWATATE'), ('602', 'TAITA'), ('603', 'TAVETA'), ('604', 'VOI'), ('701', 'BALAMBALA'), ('702', 'DADAAB'), ('703', 'FAFI'), ('704', 'GARISSA'), ('705', 'HULUGHO'), ('706', 'IJARA'), ('707', 'LAGDERA'), ('801', 'BUNA'), ('802', 'ELDAS'), ('803', 'HABASWEIN'), ('804', 'TARBAJ'), ('805', 'WAJIR EAST'), ('806', 'WAJIR NORTH'), ('807', 'WAJIR SOUTH'), ('808', 'WAJIR WEST'), ('901', 'MANDERA WEST'), ('902', 'BANISA'), ('903', 'KOTULO'), ('904', 'LAFEY'), ('905', 'MANDERA CENTRAL'), ('906', 'MANDERA EAST'), ('907', 'MANDERA NORTH'), ('1001', 'LOIYANGALANI'), ('1002', 'MARSABIT CENTRAL'), ('1003', 'MARSABIT NORTH'), ('1004', 'MARSABIT SOUTH'), ('1005', 'MOYALE'), ('1006', 'NORTH HORR'), ('1007', 'SOLOLO'), ('1101', 'GARBATULLA'), ('1102', 'ISIOLO'), ('1103', 'MERTI'), ('1202', 'BUURI WEST'), ('1203', 'IGEMBE CENTRAL'), ('1204', 'IGEMBE NORTH'), ('1205', 'IGEMBE SOUTH'), ('1206', 'IMENTI NORTH'), ('1207', 'IMENTI SOUTH'), ('1208', 'MERU CENTRAL'), ('1209', 'TIGANIA CENTRAL'), ('1210', 'TIGANIA EAST'), ('1211', 'TIGANIA WEST'), ('1301', "IGAMBANG'OMBE"), ('1302', 'MAARA'), ('1303', 'MERU SOUTH'), ('1304', 'THARAKA NORTH'), ('1305', 'THARAKA SOUTH'), ('1401', 'EMBU EAST'), ('1402', 'EMBU NORTH'), ('1403', 'EMBU WEST'), ('1404', 'MBEERE SOUTH'), ('1405', 'MBEERE NORTH'), ('1501', 'IKUTHA'), ('1502', 'KATULANI'), ('1503', 'KISASI'), ('1504', 'KITUI CENTRAL'), ('1505', 'KITUI WEST'), ('1506', 'KYUSO'), ('1507', 'LOWER YATTA'), ('1508', 'MATINYANI'), ('1509', 'MIGWANI'), ('1510', 'MUMONI'), ('1511', 'MUTITU'), ('1512', 'MUTITU NORTH'), ('1513', 'MUTOMO'), ('1514', 'MWINGI CENTRAL'), ('1515', 'MWINGI EAST'), ('1516', 'NZAMBANI'), ('1517', 'THAGICU'), ('1518', 'TSEIKURU'), ('1601', 'ATHI RIVER'), ('1602', 'KALAMA'), ('1603', 'KANGUNDO'), ('1604', 'KATHIANI'), ('1605', 'MACHAKOS'), ('1606', 'MASINGA'), ('1607', 'MATUNGULU'), ('1608', 'MWALA'), ('1609', 'YATTA'), ('1701', 'KATHONZWENI'), ('1702', 'KIBWEZI'), ('1703', 'KILUNGU'), ('1704', 'MAKINDU'), ('1705', 'MAKUENI'), ('1706', 'MBOONI EAST'), ('1707', 'MBOONI WEST'), ('1708', 'MUKAA'), ('1709', 'NZAUI'), ('1801', 'KINANGOP'), ('1802', 'NYANDARUA SOUTH'), ('1803', 'MIRANGINE'), ('1804', 'KIPIPIRI'), ('1805', 'NYANDARUA CENTRAL'), ('1806', 'NYANDARUA WEST'), ('1807', 'NYANDARUA NORTH'), ('1901', 'TETU'), ('1902', 'KIENI EAST'), ('1903', 'KIENI WEST'), ('1904', 'MATHIRA EAST'), ('1905', 'MATHIRA WEST'), ('1906', 'NYERI SOUTH'), ('1907', 'MUKURWE-INI'), ('1908', 'NYERI CENTRAL'), ('2001', 'KIRINYAGA CENTRAL'), ('2002', 'KIRINYAGA EAST'), ('2003', 'KIRINYAGA WEST'), ('2004', 'MWEA EAST'), ('2005', 'MWEA WEST'), ('2101', "MURANG'A EAST"), ('2102', 'KANGEMA'), ('2103', 'MATHIOYA'), ('2104', 'KAHURO'), ('2105', "MURANG'A SOUTH"), ('2106', 'GATANGA'), ('2107', 'KIGUMO'), ('2108', 'KANDARA'), ('2201', 'GATUNDU NORTH'), ('2202', 'GATUNDU SOUTH'), ('2203', 'GITHUNGURI'), ('2204', 'JUJA'), ('2205', 'KABETE'), ('2206', 'KIAMBAA'), ('2207', 'KIAMBU'), ('2208', 'KIKUYU'), ('2209', 'LARI'), ('2210', 'LIMURU'), ('2211', 'RUIRU'), ('2212', 'THIKA EAST'), ('2213', 'THIKA WEST'), ('2301', 'KIBISH'), ('2302', 'LOIMA'), ('2303', 'TURKANA CENTRAL'), ('2304', 'TURKANA EAST'), ('2305', 'TURKANA NORTH'), ('2306', 'TURKANA SOUTH'), ('2307', 'TURKANA WEST'), ('2401', 'KIPKOMO'), ('2402', 'POKOT CENTRAL'), ('2403', 'POKOT NORTH'), ('2404', 'POKOT SOUTH'), ('2405', 'WEST POKOT'), ('2501', 'SAMBURU CENTRAL'), ('2502', 'SAMBURU EAST'), ('2503', 'SAMBURU NORTH'), ('2601', 'TRANS NZOIA WEST'), ('2602', 'TRANS NZOIA EAST'), ('2603', 'KWANZA'), ('2604', 'ENDEBESS'), ('2605', 'KIMININI'), ('2701', 'AINABKOI'), ('2702', 'KAPSERET'), ('2703', 'KESSES'), ('2704', 'MOIBEN'), ('2705', 'SOY'), ('2706', 'TURBO'), ('2801', 'KEIYO NORTH'), ('2802', 'KEIYO SOUTH'), ('2803', 'MARAKWET EAST'), ('2804', 'MARAKWET WEST'), ('2901', 'CHESUMEI'), ('2902', 'NANDI CENTRAL'), ('2903', 'NANDI EAST'), ('2904', 'NANDI NORTH'), ('2905', 'NANDI SOUTH'), ('2906', 'TINDERET'), ('3001', 'BARINGO CENTRAL'), ('3002', 'BARINGO NORTH'), ('3003', 'EAST POKOT'), ('3004', 'KOIBATEK'), ('3005', 'MARIGAT'), ('3006', 'MOGOTIO'), ('3007', 'TIATY EAST'), ('3008', 'LAKE BARINGO'), ('3101', 'LAIKIPIA CENTRAL'), ('3102', 'LAIKIPIA EAST'), ('3103', 'LAIKIPIA NORTH'), ('3104', 'LAIKIPIA WEST'), ('3105', 'NYAHURURU'), ('3201', 'GILGIL'), ('3202', 'KURESOI NORTH'), ('3203', 'KURESOI SOUTH'), ('3204', 'MOLO'), ('3205', 'NAIVASHA'), ('3206', 'NAKURU EAST'), ('3207', 'NAKURU NORTH'), ('3208', 'NAKURU WEST'), ('3209', 'NJORO'), ('3210', 'RONGAI'), ('3211', 'SUBUKIA'), ('3301', 'NAROK EAST'), ('3302', 'NAROK NORTH'), ('3303', 'NAROK SOUTH'), ('3304', 'NAROK WEST'), ('3305', 'TRANS MARA EAST'), ('3306', 'TRANS MARA WEST'), ('3401', 'ISINYA'), ('3402', 'KAJIADO CENTRAL'), ('3403', 'KAJIADO NORTH'), ('3404', 'KAJIADO WEST'), ('3405', 'LOITOKITOK'), ('3406', 'MASHUURU'), ('3501', 'BELGUT'), ('3502', 'BURETI'), ('3503', 'KERICHO EAST'), ('3504', 'KIPKELION'), ('3505', 'LONDIANI'), ('3506', 'SOIN SIGOWET'), ('3601', 'BOMET EAST'), ('3602', 'CHEPALUNGU'), ('3603', 'KONOIN'), ('3604', 'SOTIK'), ('3605', 'BOMET CENTRAL'), ('3701', 'BUTERE'), ('3702', 'KAKAMEGA CENTRAL'), ('3703', 'KAKAMEGA EAST'), ('3704', 'KAKAMEGA NORTH'), ('3705', 'KAKAMEGA SOUTH'), ('3706', 'KHWISERO'), ('3707', 'LIKUYANI'), ('3708', 'LUGARI'), ('3709', 'MATETE'), ('3710', 'MATUNGU'), ('3711', 'MUMIAS EAST'), ('3712', 'MUMIAS WEST'), ('3713', 'NAVAKHOLO'), ('3801', 'EMUHAYA'), ('3802', 'VIHIGA'), ('3803', 'SABATIA'), ('3804', 'LUANDA'), ('3805', 'HAMISI'), ('3901', 'BUMULA'), ('3902', 'BUNGOMA CENTRAL'), ('3903', 'BUNGOMA EAST'), ('3904', 'BUNGOMA NORTH'), ('3905', 'BUNGOMA SOUTH'), ('3906', 'CHEPTAIS'), ('3907', 'KIMILILI'), ('3909', 'BUNGOMA WEST'), ('3910', 'TONGAREN'), ('3911', 'WEBUYE WEST'), ('3912', 'MT ELGON FOREST'), ('4001', 'BUNYALA'), ('4002', 'BUSIA'), ('4003', 'BUTULA'), ('4004', 'NAMBALE'), ('4005', 'SAMIA'), ('4006', 'TESO NORTH'), ('4007', 'TESO SOUTH'), ('4101', 'SIAYA'), ('4102', 'GEM'), ('4103', 'UGENYA'), ('4104', 'UGUNJA'), ('4105', 'BONDO'), ('4106', 'RARIEDA'), ('4201', 'KISUMU EAST'), ('4202', 'KISUMU CENTRAL'), ('4203', 'KISUMU WEST'), ('4204', 'SEME'), ('4205', 'MUHORONI'), ('4206', 'NYANDO'), ('4207', 'NYAKACH'), ('4301', 'HOMA BAY'), ('4302', 'NDHIWA'), ('4303', 'RACHUONYO NORTH'), ('4304', 'RACHUONYO EAST'), ('4305', 'RACHUONYO SOUTH'), ('4306', 'RANGWE'), ('4307', 'SUBA NORTH'), ('4308', 'SUBA SOUTH'), ('4401', 'AWENDO'), ('4402', 'KURIA EAST'), ('4403', 'KURIA WEST'), ('4404', 'NYATIKE'), ('4405', 'RONGO'), ('4406', 'SUNA EAST'), ('4407', 'SUNA WEST'), ('4408', 'URIRI'), ('4501', 'ETAGO'), ('4502', 'GUCHA'), ('4503', 'GUCHA SOUTH'), ('4504', 'KENYENYA'), ('4505', 'KISII CENTRAL'), ('4506', 'KISII SOUTH'), ('4507', 'KITUTU CENTRAL'), ('4508', 'MARANI'), ('4509', 'MASABA SOUTH'), ('4510', 'NYAMACHE'), ('4511', 'SAMETA'), ('4601', 'BORABU'), ('4602', 'MANGA'), ('4603', 'MASABA NORTH'), ('4604', 'NYAMIRA NORTH'), ('4605', 'NYAMIRA SOUTH'), ('4701', 'DAGORETTI'), ('4702', 'EMBAKASI'), ('4703', 'KAMUKUNJI'), ('4704', 'KASARANI'), ('4705', 'KIBRA'), ('4706', "LANG'ATA"), ('4707', 'MAKADARA'), ('4708', 'MATHARE'), ('4709', 'NJIRU'), ('4710', 'STAREHE'), ('4711', 'WESTLANDS')], max_length=6),
        ),
        migrations.AlterField(
            model_name='incidents_data',
            name='sub_fraud_code',
            field=models.CharField(choices=[('IC01', 'Wallet to wallet registered to registered'), ('IC02', 'Wallet to wallet registered to unregistered'), ('IC03', 'wallet to wallet unregistered to registered'), ('IC04', 'Cross-network wallet to mobile number ( Interop)'), ('IC05', 'Local mobile wallet to international mobile money wallet'), ('IC06', 'Bulk payment from business mobile money wallet to personal mobile money wallet'), ('IC07', 'Bank account to mobile money wallet'), ('IC08', 'Mobile money wallet to bank account'), ('IC09', 'Agent cash and float'), ('IC10', 'Deposit at branch or super agent'), ('IC11', 'Withdrawal at branch or super agent'), ('IC12', 'Float transfer to other agent'), ('IC13', 'Mobile money wallet to merchant or business paybill'), ('IC14', 'Mobile money wallet to till'), ('IC99', 'Any other instrument type'), ('SG01', 'P2P - Person to Person'), ('SG02', 'P2B - Person to Business'), ('SG03', 'P2G - Person to Government'), ('SG04', 'B2P - Business to Person'), ('SG05', 'B2B - Business to Business'), ('SG06', 'B2G - Business to Government'), ('SG07', 'G2P - Government to Person'), ('SG08', 'G2G - Government to Business'), ('SG09', 'G2B - Government to Government'), ('I', 'Individual'), ('B', 'Business'), ('G', 'Government/ Public entity'), ('SS', 'Sim swap'), ('CONSEND', 'Individuals conned into sending money'), ('CONPIN', 'PIN theft'), ('CONIDEN', 'Identity theft'), ('CONIMPER', 'Impersonification'), ('I', 'Individual'), ('B', 'Business'), ('G', 'Government/ Public entity'), ('I', 'Individual'), ('B', 'Business'), ('G', 'Government/ Public entity'), ('ATM', 'ATM'), ('AG', 'Agent')], max_length=10),
        ),
        migrations.AlterField(
            model_name='interoperability_data',
            name='reporting_date',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='new_mobile_agents',
            name='agent_status',
            field=models.CharField(choices=[('ACT30', 'Active 30 Days'), ('DRMNT', 'Dormant'), ('SUS', 'Suspended'), ('TER', 'Terminated'), ('ACT60', 'Active 60 Days'), ('ACT90', 'Active 90 Days'), ('INACT', 'Inactive'), ('REG', 'Registered'), ('UNREG', 'Unregistered')], max_length=10),
        ),
        migrations.AlterField(
            model_name='new_mobile_agents',
            name='date_of_onboarding',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='new_mobile_agents',
            name='suspension_termination_date',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='psp_agents_info',
            name='agent_status',
            field=models.CharField(choices=[('ACT30', 'Active 30 Days'), ('DRMNT', 'Dormant'), ('SUS', 'Suspended'), ('TER', 'Terminated'), ('ACT60', 'Active 60 Days'), ('ACT90', 'Active 90 Days'), ('INACT', 'Inactive'), ('REG', 'Registered'), ('UNREG', 'Unregistered')], max_length=25),
        ),
        migrations.AlterField(
            model_name='psp_agents_info',
            name='reporting_date',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='psp_customer_complaints',
            name='date_of_occurence',
            field=models.CharField(max_length=15),
        ),
        migrations.AlterField(
            model_name='psp_customer_complaints',
            name='date_reported_to_the_institution',
            field=models.CharField(max_length=15),
        ),
        migrations.AlterField(
            model_name='psp_customer_complaints',
            name='date_resolved',
            field=models.CharField(max_length=15),
        ),
        migrations.AlterField(
            model_name='psp_customer_info',
            name='psp_id',
            field=models.CharField(choices=[('0800001', 'Safaricom Plc'), ('0800002', 'Airtel Money Kenya Limited'), ('0800003', 'Telkom Kenya Limited'), ('0800004', 'Mobile Pay Limited'), ('0800005', 'Kenswitch Limited'), ('0800006', 'Interswitch East Africa (K) Limited'), ('0800007', 'Integrated Payment Services Limited'), ('0800008', 'Viewtech Limited'), ('0800009', 'Web Tribe Limited'), ('0800010', 'Finserve Africa Limited'), ('0800011', 'Cellulant Kenya Limited'), ('0800012', 'Pesapal Limited'), ('0800013', 'Fivespot Limited'), ('0800014', 'Craft Silicon Limited'), ('0800015', 'Virtual Pay International Limited'), ('0800016', 'Direct Pay Limited'), ('0800017', 'Pesawise Services Limited'), ('0800018', 'Paystack Payments Kenya Limited'), ('0800019', 'Wakandi Kenya Limited'), ('0800020', 'Kenya Airports Parking Services (KAPS) Limited'), ('0800021', 'Loop Payco Limited'), ('0800022', 'DLocal Payments Kenya Limited'), ('0800023', 'Pesaflow Limited'), ('0800024', 'Kenya Commerce Exchange Service Bureau Limited'), ('0800025', 'PayU Kenya Limited'), ('0800026', 'Dolcepay Kenya Limited'), ('0800027', 'Unlimint Kenya Limited'), ('0800028', 'Gladys Technologies Limited'), ('0800029', 'Mamlaka Hub and Spoke Limited'), ('0800030', 'Eclectics International Limited'), ('0800031', 'Jumia Payment Services Kenya Limited'), ('0800032', 'Amsuka Capital Limited'), ('0800033', 'Sky World Limited'), ('0800034', 'Kashia Services Limited'), ('0800035', 'Data Integrated Limited'), ('0800036', 'Tanda Agent Limited')], default='0800009', max_length=25, null=True),
        ),
        migrations.AlterField(
            model_name='psp_customer_info',
            name='reporting_date',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='psp_cybersecurity_incident_record',
            name='date_and_time_of_incident_happened',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='psp_cybersecurity_incident_record',
            name='date_and_time_of_the_incident_resolution',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='psp_transac_categorization_info',
            name='reporting_date',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='pymt_gw_card_brands',
            name='bank_id',
            field=models.CharField(choices=[('0000001', 'KCB Bank Kenya Limited'), ('0000002', 'Standard Chartered Bank Kenya Limited'), ('0000003', 'ABSA Bank Kenya PLC'), ('0000005', 'Bank of India'), ('0000006', 'Bank of Baroda (Kenya) Ltd'), ('0000007', 'NCBA Kenya PLC'), ('0000010', 'Prime Bank Ltd'), ('0000011', 'Co-operative Bank of Kenya Limited'), ('0000012', 'National Bank of Kenya Ltd'), ('0000014', 'M-Oriental Bank Limited'), ('0000016', 'Citibank N.A. Kenya'), ('0000017', 'Habib Bank AG Zurich'), ('0000018', 'Middle East Bank Kenya Limited'), ('0000019', 'Bank of Africa Kenya Limited'), ('0000023', 'Consolidated Bank of Kenya Ltd'), ('0000025', 'Credit Bank Limited'), ('0000026', 'Access Bank (Kenya) Limited'), ('0000030', 'Chase Bank (K) Limited'), ('0000031', 'Stanbic Bank Kenya Limited'), ('0000035', 'African Banking Corporation Limited'), ('0000039', 'Imperial Bank Ltd'), ('0000043', 'Ecobank Kenya Limited'), ('0000049', 'Spire Bank Ltd'), ('0000050', 'Paramount Bank Limited'), ('0000051', 'Kingdom Bank Limited'), ('0000053', 'Guaranty Trust Bank (Kenya) Limited'), ('0000054', 'Victoria Commercial Bank Limited'), ('0000055', 'Guardian Bank Limited'), ('0000057', 'I&M Bank Ltd'), ('0000059', 'Development Bank of Kenya Ltd'), ('0000060', 'SBM Bank (Kenya) Limited'), ('0000063', 'Diamond Trust Bank (K) Limited'), ('0000064', 'Charterhouse Bank Ltd'), ('0000065', 'Mayfair CIB Bank Limited'), ('0000066', 'Sidian Bank Limited'), ('0000068', 'Equity Bank Kenya Limited'), ('0000070', 'Family Bank Limited'), ('0000072', 'Gulf African Bank Limited'), ('0000074', 'First Community Bank Ltd'), ('0000075', 'DIB Bank Kenya Limited'), ('0000076', 'UBA Kenya Bank Limited'), ('0000083', 'HFC Limited'), ('0500001', 'Faulu Microfinance Bank Limited'), ('0500002', 'Kenya Women Microfinance Bank PLC'), ('0500003', 'SMEP Microfinance Bank Limited'), ('0500004', 'Key Microfinance Bank Limited'), ('0500005', 'Rafiki Microfinance Bank Limited'), ('0500006', 'Century Microfinance Bank Limited'), ('0500007', 'Sumac Microfinance Bank Limited'), ('0500008', 'U & I Microfinance Bank Limited'), ('0500011', 'Daraja Microfinance Bank Limited'), ('0500012', 'Caritas Microfinance Bank Limited'), ('0500013', 'Maisha Microfinance Bank Limited'), ('0500014', 'UWEZO Microfinance Bank Limited'), ('0500202', 'Choice Microfinance Bank Limited'), ('0500016', 'Muungano Microfinance Bank Limited'), ('0300003', 'Alpha Forex Bureau Ltd'), ('0300009', 'Aristocrats Forex Bureau Ltd'), ('0300010', 'Bamburi Forex Bureau Ltd'), ('0300011', 'Bay Forex Bureau (Nairobi) Ltd'), ('0300014', 'Muthaiga-ABC Forex Bureau Ltd'), ('0300020', 'Central Forex Bureau Ltd'), ('0300023', 'Classic Forex Bureau Limited'), ('0300025', 'Commercial Forex Bureau Limited'), ('0300026', 'Conference Forex Bureau Company Limited'), ('0300028', 'Continental Forex Bureau Ltd'), ('0300029', 'Cosmos Forex Bureau Ltd'), ('0300042', 'Forex Bureau Afro Ltd'), ('0300045', 'Gateway Forex Bureau Ltd'), ('0300046', 'Giant Forex Bureau de Change Ltd'), ('0300048', 'Give and Take Forex Bureau Ltd'), ('0300050', 'Glory Forex Bureau Ltd'), ('0300051', 'GNK Forex Bureau Ltd'), ('0300056', 'Industrial Area Forex Bureau Ltd'), ('0300057', 'Island Forex Bureau Ltd'), ('0300059', 'Junction Forex Bureau Limited'), ('0300062', 'Kenza Exchange Bureau Ltd'), ('0300063', 'La’che Forex Bureau Ltd'), ('0300066', 'Leo Forex Bureau Ltd'), ('0300067', 'Link Forex Bureau Ltd'), ('0300070', 'Maritime Forex Bureau Ltd'), ('0300074', 'Middletown Forex Bureau Ltd'), ('0300076', 'Mona Bureau De Change Ltd'), ('0300077', 'Moneypoint Forex Bureau Ltd'), ('0300078', 'Morgan Forex Bureau De Change Ltd'), ('0300079', 'Mustaqbal Forex Bureau Ltd'), ('0300081', 'Nairobi Bureau De Change Ltd'), ('0300083', 'Namanga Forex Bureau Ltd'), ('0300085', 'Nawal Forex Bureau Ltd'), ('0300087', 'Offshore Forex Bureau Limited'), ('0300089', 'Pacific Forex Bureau Limited'), ('0300090', 'Peaktop Bureau De Change Ltd'), ('0300091', 'Pearl Forex Bureau Ltd'), ('0300092', 'Pel Forex Bureau Ltd'), ('0300096', 'Pwani Forex Bureau Ltd'), ('0300097', 'Avenue Forex Bureau Limited'), ('0300099', 'Regional Forex Bureau Limited'), ('0300100', 'Rift Valley Forex Bureau Ltd'), ('0300102', 'Satellite Forex Bureau Ltd'), ('0300104', 'Simba Forex Bureau Limited'), ('0300105', 'Sky Forex Bureau Limited'), ('0300106', 'Solid Exchange Bureau Ltd'), ('0300108', 'Sterling Forex Bureau Ltd'), ('0300109', 'Sunny Forex Bureau Limited'), ('0300111', 'Taipan Forex Bureau Ltd'), ('0300113', 'Trade Bureau De Change Ltd'), ('0300114', 'Travel Point Forex Bureau Limited'), ('0300115', 'Travellers Forex Bureau Ltd'), ('0300117', 'Union Forex Bureau Ltd'), ('0300118', 'Victoria Forex Bureau De Change Ltd'), ('0300120', 'Wallstreet Bureau De Change Ltd'), ('0300122', 'Westlands Forex Bureau Ltd'), ('0300123', 'Yaya Centre Exchange Bureau Ltd'), ('0300128', 'Green Exchange Forex Bureau Limited'), ('0300129', 'CBD Forex Bureau Limited'), ('0300131', 'Magnum Forex Bureau De Change Ltd'), ('0300135', 'Gala Forex Bureau Ltd'), ('0300142', 'Sisi Forex Bureau Limited'), ('0300143', 'Rand Forex Bureau Limited'), ('0300146', 'Boston Forex Bureau Limited'), ('0300148', 'Southend Forex Bureau Ltd'), ('0300149', 'Springs Forex Bureau Limited'), ('0600001', 'Credit Reference Bureau Africa Limited'), ('0600002', 'Metropol Credit Reference Bureau Limited'), ('0600003', 'Creditinfo Credit Reference Bureau Kenya Limited'), ('0700001', 'Dahabshiil Money Transfer Company Limited'), ('0700005', 'Amal Express Money Transfer Limited'), ('0700006', 'Iftin Express Money Transfer Limited'), ('0700007', 'Juba Express Money Transfer Limited'), ('0700009', 'Kaah Express Money Transfer Limited'), ('0700010', 'Amana Money Transfer Ltd'), ('0700011', 'Bakaal Express Money Transfer Ltd'), ('0700012', 'Safaricom Money Transfer Services Limited'), ('0700013', 'Hodan Global Money Remittance and Exchange Limited'), ('0700014', 'Tawakal Money Transfer Limited'), ('0700016', 'Flex Money Transfer Limited'), ('0700017', 'Taaj Money Transfer Limited'), ('0700018', 'Upesi Money Transfer Limited'), ('0700019', 'Real Value Money Transfer Limited'), ('0700020', 'PostBank Money Transfer Services Limited'), ('0700021', 'Postal Corporation of Kenya Money Transfer Services'), ('0700023', 'Airtel Money Transfer Limited'), ('0700024', 'Mobex Money Transfer Services Ltd'), ('0700026', 'Mukuru Money Transfer Limited'), ('0000066 NOHC', 'Bakki Holdco Limited (Centum Group)'), ('0000068 NOHC', 'Equity Group Holdings Limited'), ('0000083 NOHC', 'HF Group Limited'), ('0000057 NOHC', 'I&M Holdings Limited'), ('0000001 NOHC', 'KCB Group PLC'), ('0000014 NOHC', 'M Holdings Limited'), ('0000007 NOHC', 'NCBA Group PLC'), ('0000031 NOHC', 'Stanbic Holdings PLC'), ('1000001', 'Bank of China Limited - Kenya Representative Office'), ('1000002', 'Bank of Kigali Ltd - Kenya Representative Office'), ('1000003', 'FirstRand Bank limited - Kenya Representative Office'), ('1000004', 'HDFC Bank Limited - Kenya Representative Office'), ('1000005', 'Mauritius Commercial Bank Limited - Kenya Representative Office'), ('1000006', 'Nedbank Limited - Kenya Representative Office'), ('1000007', 'Co-operative Rabobank U.A - Kenya Representative Office'), ('1000008', 'Societe Generale - Kenya Representative Office'), ('1000009', 'BAHL - Kenya Representative Office'), ('100-CBK', 'Central Bank of Kenya'), ('101-SACCO', 'Sacco'), ('102-FIN', 'Fintechs'), ('103-OTH', 'Anyother')], max_length=25),
        ),
        migrations.AlterField(
            model_name='sch_sy_stabil_srvce_int',
            name='third_party_name',
            field=models.CharField(max_length=25),
        ),
        migrations.AlterField(
            model_name='sched_of_dir',
            name='date_of_appointment',
            field=models.CharField(max_length=15),
        ),
        migrations.AlterField(
            model_name='sched_of_dir',
            name='date_of_retirement',
            field=models.CharField(max_length=15),
        ),
        migrations.AlterField(
            model_name='sched_of_dir',
            name='dob',
            field=models.CharField(max_length=15),
        ),
        migrations.AlterField(
            model_name='sched_of_share_hldrs',
            name='dob_or_reg_date',
            field=models.CharField(max_length=15),
        ),
        migrations.AlterField(
            model_name='sched_of_share_hldrs',
            name='onboarding_date',
            field=models.CharField(max_length=15),
        ),
        migrations.AlterField(
            model_name='sched_of_trustees',
            name='dob',
            field=models.CharField(max_length=15),
        ),
        migrations.AlterField(
            model_name='senior_mngt_schedule',
            name='date_of_emp',
            field=models.CharField(max_length=15),
        ),
        migrations.AlterField(
            model_name='senior_mngt_schedule',
            name='dob',
            field=models.CharField(max_length=15),
        ),
        migrations.AlterField(
            model_name='senior_mngt_schedule',
            name='retirement_date',
            field=models.CharField(max_length=15),
        ),
        migrations.AlterField(
            model_name='trust_account_info',
            name='reporting_date',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='trust_account_info',
            name='trust_fund_inv_maturity_date',
            field=models.CharField(max_length=25),
        ),
        migrations.AlterField(
            model_name='trust_account_info',
            name='trust_fund_placement',
            field=models.CharField(choices=[('TFP01', 'Cash holdings (Fixed Deposit)'), ('TFP02', 'Cash holdings (Current)'), ('TFP03', 'Cash holdings (Fixed Deposit) in foreign currency account'), ('TFP04', 'Cash holdings (Current) in foreign currency account'), ('TFP05', 'Treasury bills'), ('TFP06', 'Treasury bonds'), ('TFP99', 'Any other')], max_length=25),
        ),
        migrations.AlterField(
            model_name='trustaccount_data',
            name='trust_acc_int_utilized_details',
            field=models.CharField(choices=[('DBT01', 'Banks charges'), ('DBT02', 'Management fees'), ('DBT03', 'Stamp duty'), ('DBT04', 'Donations'), ('DBT05', 'Custody fees'), ('DBT06', 'Audit fees'), ('DBT07', 'Withholding taxes'), ('DBT08', 'Field not applicable'), ('DBT99', 'Any others debit type')], max_length=100),
        ),
    ]