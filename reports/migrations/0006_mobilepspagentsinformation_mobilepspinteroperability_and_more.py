# Generated by Django 5.0.4 on 2024-09-25 12:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0005_mobilepsptransactioncategorization'),
    ]

    operations = [
        migrations.CreateModel(
            name='MobilePspAgentsInformation',
            fields=[
                ('row_id', models.AutoField(primary_key=True, serialize=False)),
                ('psp_id', models.CharField(choices=[('0800001', 'Safaricom Plc'), ('0800002', 'Airtel Money Kenya Limited'), ('0800003', 'Telkom Kenya Limited'), ('0800004', 'Mobile Pay Limited'), ('0800005', 'Kenswitch Limited'), ('0800006', 'Interswitch East Africa (K) Limited'), ('0800007', 'Integrated Payment Services Limited'), ('0800008', 'Viewtech Limited'), ('0800009', 'Web Tribe Limited'), ('0800010', 'Finserve Africa Limited'), ('0800011', 'Cellulant Kenya Limited'), ('0800012', 'Pesapal Limited'), ('0800013', 'Fivespot Limited'), ('0800014', 'Craft Silicon Limited'), ('0800015', 'Virtual Pay International Limited'), ('0800016', 'Direct Pay Limited'), ('0800017', 'Pesawise Services Limited'), ('0800018', 'Paystack Payments Kenya Limited'), ('0800019', 'Wakandi Kenya Limited'), ('0800020', 'Kenya Airports Parking Services (KAPS) Limited'), ('0800021', 'Loop Payco Limited'), ('0800022', 'DLocal Payments Kenya Limited'), ('0800023', 'Pesaflow Limited'), ('0800024', 'Kenya Commerce Exchange Service Bureau Limited'), ('0800025', 'PayU Kenya Limited'), ('0800026', 'Dolcepay Kenya Limited'), ('0800027', 'Unlimint Kenya Limited'), ('0800028', 'Gladys Technologies Limited'), ('0800029', 'Mamlaka Hub and Spoke Limited'), ('0800030', 'Eclectics International Limited'), ('0800031', 'Jumia Payment Services Kenya Limited'), ('0800032', 'Amsuka Capital Limited'), ('0800033', 'Sky World Limited'), ('0800034', 'Kashia Services Limited'), ('0800035', 'Data Integrated Limited'), ('0800036', 'Tanda Agent Limited')], max_length=25)),
                ('reporting_date', models.DateField()),
                ('agent_type_code', models.CharField(choices=[('SUPAG', 'Super Agent'), ('AG', 'Agent')], max_length=10)),
                ('agents_id', models.CharField(max_length=10)),
                ('gps_cordinates', models.CharField(max_length=10)),
                ('sub_county_code', models.CharField(choices=[('101', 'CHANGAMWE'), ('102', 'JOMVU'), ('103', 'KISAUNI'), ('104', 'LIKONI'), ('105', 'MVITA'), ('106', 'NYALI'), ('201', 'KINANGO'), ('202', 'LUNGA LUNGA'), ('203', 'MATUGA'), ('204', 'MSAMBWENI'), ('205', 'SAMBURU'), ('301', 'CHONYI'), ('302', 'GANZE'), ('303', 'KALOLENI'), ('304', 'KAUMA'), ('305', 'KILIFI NORTH'), ('306', 'KILIFI SOUTH'), ('307', 'MAGARINI'), ('308', 'MALINDI'), ('309', 'RABAI'), ('401', 'TANA DELTA'), ('402', 'TANA NORTH'), ('403', 'TANA RIVER'), ('501', 'LAMU EAST'), ('502', 'LAMU WEST'), ('601', 'MWATATE'), ('602', 'TAITA'), ('603', 'TAVETA'), ('604', 'VOI'), ('701', 'BALAMBALA'), ('702', 'DADAAB'), ('703', 'FAFI'), ('704', 'GARISSA'), ('705', 'HULUGHO'), ('706', 'IJARA'), ('707', 'LAGDERA'), ('801', 'BUNA'), ('802', 'ELDAS'), ('803', 'HABASWEIN'), ('804', 'TARBAJ'), ('805', 'WAJIR EAST'), ('806', 'WAJIR NORTH'), ('807', 'WAJIR SOUTH'), ('808', 'WAJIR WEST'), ('901', 'MANDERA WEST'), ('902', 'BANISA'), ('903', 'KOTULO'), ('904', 'LAFEY'), ('905', 'MANDERA CENTRAL'), ('906', 'MANDERA EAST'), ('907', 'MANDERA NORTH'), ('1001', 'LOIYANGALANI'), ('1002', 'MARSABIT CENTRAL'), ('1003', 'MARSABIT NORTH'), ('1004', 'MARSABIT SOUTH'), ('1005', 'MOYALE'), ('1006', 'NORTH HORR'), ('1007', 'SOLOLO'), ('1101', 'GARBATULLA'), ('1102', 'ISIOLO'), ('1103', 'MERTI'), ('1202', 'BUURI WEST'), ('1203', 'IGEMBE CENTRAL'), ('1204', 'IGEMBE NORTH'), ('1205', 'IGEMBE SOUTH'), ('1206', 'IMENTI NORTH'), ('1207', 'IMENTI SOUTH'), ('1208', 'MERU CENTRAL'), ('1209', 'TIGANIA CENTRAL'), ('1210', 'TIGANIA EAST'), ('1211', 'TIGANIA WEST'), ('1301', "IGAMBANG'OMBE"), ('1302', 'MAARA'), ('1303', 'MERU SOUTH'), ('1304', 'THARAKA NORTH'), ('1305', 'THARAKA SOUTH'), ('1401', 'EMBU EAST'), ('1402', 'EMBU NORTH'), ('1403', 'EMBU WEST'), ('1404', 'MBEERE SOUTH'), ('1405', 'MBEERE NORTH'), ('1501', 'IKUTHA'), ('1502', 'KATULANI'), ('1503', 'KISASI'), ('1504', 'KITUI CENTRAL'), ('1505', 'KITUI WEST'), ('1506', 'KYUSO'), ('1507', 'LOWER YATTA'), ('1508', 'MATINYANI'), ('1509', 'MIGWANI'), ('1510', 'MUMONI'), ('1511', 'MUTITU'), ('1512', 'MUTITU NORTH'), ('1513', 'MUTOMO'), ('1514', 'MWINGI CENTRAL'), ('1515', 'MWINGI EAST'), ('1516', 'NZAMBANI'), ('1517', 'THAGICU'), ('1518', 'TSEIKURU'), ('1601', 'ATHI RIVER'), ('1602', 'KALAMA'), ('1603', 'KANGUNDO'), ('1604', 'KATHIANI'), ('1605', 'MACHAKOS'), ('1606', 'MASINGA'), ('1607', 'MATUNGULU'), ('1608', 'MWALA'), ('1609', 'YATTA'), ('1701', 'KATHONZWENI'), ('1702', 'KIBWEZI'), ('1703', 'KILUNGU'), ('1704', 'MAKINDU'), ('1705', 'MAKUENI'), ('1706', 'MBOONI EAST'), ('1707', 'MBOONI WEST'), ('1708', 'MUKAA'), ('1709', 'NZAUI'), ('1801', 'KINANGOP'), ('1802', 'NYANDARUA SOUTH'), ('1803', 'MIRANGINE'), ('1804', 'KIPIPIRI'), ('1805', 'NYANDARUA CENTRAL'), ('1806', 'NYANDARUA WEST'), ('1807', 'NYANDARUA NORTH'), ('1901', 'TETU'), ('1902', 'KIENI EAST'), ('1903', 'KIENI WEST'), ('1904', 'MATHIRA EAST'), ('1905', 'MATHIRA WEST'), ('1906', 'NYERI SOUTH'), ('1907', 'MUKURWE-INI'), ('1908', 'NYERI CENTRAL'), ('2001', 'KIRINYAGA CENTRAL'), ('2002', 'KIRINYAGA EAST'), ('2003', 'KIRINYAGA WEST'), ('2004', 'MWEA EAST'), ('2005', 'MWEA WEST'), ('2101', "MURANG'A EAST"), ('2102', 'KANGEMA'), ('2103', 'MATHIOYA'), ('2104', 'KAHURO'), ('2105', "MURANG'A SOUTH"), ('2106', 'GATANGA'), ('2107', 'KIGUMO'), ('2108', 'KANDARA'), ('2201', 'GATUNDU NORTH'), ('2202', 'GATUNDU SOUTH'), ('2203', 'GITHUNGURI'), ('2204', 'JUJA'), ('2205', 'KABETE'), ('2206', 'KIAMBAA'), ('2207', 'KIAMBU'), ('2208', 'KIKUYU'), ('2209', 'LARI'), ('2210', 'LIMURU'), ('2211', 'RUIRU'), ('2212', 'THIKA EAST'), ('2213', 'THIKA WEST'), ('2301', 'KIBISH'), ('2302', 'LOIMA'), ('2303', 'TURKANA CENTRAL'), ('2304', 'TURKANA EAST'), ('2305', 'TURKANA NORTH'), ('2306', 'TURKANA SOUTH'), ('2307', 'TURKANA WEST'), ('2401', 'KIPKOMO'), ('2402', 'POKOT CENTRAL'), ('2403', 'POKOT NORTH'), ('2404', 'POKOT SOUTH'), ('2405', 'WEST POKOT'), ('2501', 'SAMBURU CENTRAL'), ('2502', 'SAMBURU EAST'), ('2503', 'SAMBURU NORTH'), ('2601', 'TRANS NZOIA WEST'), ('2602', 'TRANS NZOIA EAST'), ('2603', 'KWANZA'), ('2604', 'ENDEBESS'), ('2605', 'KIMININI'), ('2701', 'AINABKOI'), ('2702', 'KAPSERET'), ('2703', 'KESSES'), ('2704', 'MOIBEN'), ('2705', 'SOY'), ('2706', 'TURBO'), ('2801', 'KEIYO NORTH'), ('2802', 'KEIYO SOUTH'), ('2803', 'MARAKWET EAST'), ('2804', 'MARAKWET WEST'), ('2901', 'CHESUMEI'), ('2902', 'NANDI CENTRAL'), ('2903', 'NANDI EAST'), ('2904', 'NANDI NORTH'), ('2905', 'NANDI SOUTH'), ('2906', 'TINDERET'), ('3001', 'BARINGO CENTRAL'), ('3002', 'BARINGO NORTH'), ('3003', 'EAST POKOT'), ('3004', 'KOIBATEK'), ('3005', 'MARIGAT'), ('3006', 'MOGOTIO'), ('3007', 'TIATY EAST'), ('3008', 'LAKE BARINGO'), ('3101', 'LAIKIPIA CENTRAL'), ('3102', 'LAIKIPIA EAST'), ('3103', 'LAIKIPIA NORTH'), ('3104', 'LAIKIPIA WEST'), ('3105', 'NYAHURURU'), ('3201', 'GILGIL'), ('3202', 'KURESOI NORTH'), ('3203', 'KURESOI SOUTH'), ('3204', 'MOLO'), ('3205', 'NAIVASHA'), ('3206', 'NAKURU EAST'), ('3207', 'NAKURU NORTH'), ('3208', 'NAKURU WEST'), ('3209', 'NJORO'), ('3210', 'RONGAI'), ('3211', 'SUBUKIA'), ('3301', 'NAROK EAST'), ('3302', 'NAROK NORTH'), ('3303', 'NAROK SOUTH'), ('3304', 'NAROK WEST'), ('3305', 'TRANS MARA EAST'), ('3306', 'TRANS MARA WEST'), ('3401', 'ISINYA'), ('3402', 'KAJIADO CENTRAL'), ('3403', 'KAJIADO NORTH'), ('3404', 'KAJIADO WEST'), ('3405', 'LOITOKITOK'), ('3406', 'MASHUURU'), ('3501', 'BELGUT'), ('3502', 'BURETI'), ('3503', 'KERICHO EAST'), ('3504', 'KIPKELION'), ('3505', 'LONDIANI'), ('3506', 'SOIN SIGOWET'), ('3601', 'BOMET EAST'), ('3602', 'CHEPALUNGU'), ('3603', 'KONOIN'), ('3604', 'SOTIK'), ('3605', 'BOMET CENTRAL'), ('3701', 'BUTERE'), ('3702', 'KAKAMEGA CENTRAL'), ('3703', 'KAKAMEGA EAST'), ('3704', 'KAKAMEGA NORTH'), ('3705', 'KAKAMEGA SOUTH'), ('3706', 'KHWISERO'), ('3707', 'LIKUYANI'), ('3708', 'LUGARI'), ('3709', 'MATETE'), ('3710', 'MATUNGU'), ('3711', 'MUMIAS EAST'), ('3712', 'MUMIAS WEST'), ('3713', 'NAVAKHOLO'), ('3801', 'EMUHAYA'), ('3802', 'VIHIGA'), ('3803', 'SABATIA'), ('3804', 'LUANDA'), ('3805', 'HAMISI'), ('3901', 'BUMULA'), ('3902', 'BUNGOMA CENTRAL'), ('3903', 'BUNGOMA EAST'), ('3904', 'BUNGOMA NORTH'), ('3905', 'BUNGOMA SOUTH'), ('3906', 'CHEPTAIS'), ('3907', 'KIMILILI'), ('3909', 'BUNGOMA WEST'), ('3910', 'TONGAREN'), ('3911', 'WEBUYE WEST'), ('3912', 'MT ELGON FOREST'), ('4001', 'BUNYALA'), ('4002', 'BUSIA'), ('4003', 'BUTULA'), ('4004', 'NAMBALE'), ('4005', 'SAMIA'), ('4006', 'TESO NORTH'), ('4007', 'TESO SOUTH'), ('4101', 'SIAYA'), ('4102', 'GEM'), ('4103', 'UGENYA'), ('4104', 'UGUNJA'), ('4105', 'BONDO'), ('4106', 'RARIEDA'), ('4201', 'KISUMU EAST'), ('4202', 'KISUMU CENTRAL'), ('4203', 'KISUMU WEST'), ('4204', 'SEME'), ('4205', 'MUHORONI'), ('4206', 'NYANDO'), ('4207', 'NYAKACH'), ('4301', 'HOMA BAY'), ('4302', 'NDHIWA'), ('4303', 'RACHUONYO NORTH'), ('4304', 'RACHUONYO EAST'), ('4305', 'RACHUONYO SOUTH'), ('4306', 'RANGWE'), ('4307', 'SUBA NORTH'), ('4308', 'SUBA SOUTH'), ('4401', 'AWENDO'), ('4402', 'KURIA EAST'), ('4403', 'KURIA WEST'), ('4404', 'NYATIKE'), ('4405', 'RONGO'), ('4406', 'SUNA EAST'), ('4407', 'SUNA WEST'), ('4408', 'URIRI'), ('4501', 'ETAGO'), ('4502', 'GUCHA'), ('4503', 'GUCHA SOUTH'), ('4504', 'KENYENYA'), ('4505', 'KISII CENTRAL'), ('4506', 'KISII SOUTH'), ('4507', 'KITUTU CENTRAL'), ('4508', 'MARANI'), ('4509', 'MASABA SOUTH'), ('4510', 'NYAMACHE'), ('4511', 'SAMETA'), ('4601', 'BORABU'), ('4602', 'MANGA'), ('4603', 'MASABA NORTH'), ('4604', 'NYAMIRA NORTH'), ('4605', 'NYAMIRA SOUTH'), ('4701', 'DAGORETTI'), ('4702', 'EMBAKASI'), ('4703', 'KAMUKUNJI'), ('4704', 'KASARANI'), ('4705', 'KIBRA'), ('4706', "LANG'ATA"), ('4707', 'MAKADARA'), ('4708', 'MATHARE'), ('4709', 'NJIRU'), ('4710', 'STAREHE'), ('4711', 'WESTLANDS')], max_length=4)),
                ('agent_status', models.CharField(choices=[('ACT30', 'Active 30 Days'), ('DRMNT', 'Dormant'), ('SUS', 'Suspended'), ('TER', 'Terminated')], max_length=25)),
                ('band_code', models.CharField(choices=[('BNC01', '1 - 49'), ('BNC02', '50 - 100'), ('BNC03', '101 - 500'), ('BNC04', '501 - 1000'), ('BNC05', '1001 - 1500'), ('BNC06', '1501 - 2500'), ('BNC07', '2501 - 3500'), ('BNC08', '3501 - 5000'), ('BNC9', '5001 - 7500'), ('BNC10', '7501 - 10000'), ('BNC11', '10001 - 15000'), ('BNC12', '15001 - 20000'), ('BNC13', '20001 - 25000'), ('BNC14', '25001 - 30000'), ('BNC15', '30001 - 35000'), ('BNC16', '35001 - 40000'), ('BNC17', '40001 - 45000'), ('BNC18', '45001 - 50000'), ('BNC19', '50001 - 70000'), ('BNC20', '70001 - 150000'), ('BNC21', '150001-250000'), ('BNC22', 'Any other band')], max_length=25)),
                ('volume_cash_in_at_agents', models.PositiveIntegerField()),
                ('value_cash_in_at_agents', models.DecimalField(decimal_places=2, max_digits=12)),
                ('volume_of_cash_out_at_agents', models.PositiveIntegerField()),
                ('value_of_cash_out_at_agents', models.DecimalField(decimal_places=2, max_digits=12)),
                ('amount_of_eFloat_mobile_agents', models.DecimalField(decimal_places=2, max_digits=12)),
                ('number_of_agent_cash_dep_banks', models.PositiveIntegerField()),
                ('value_of_agent_cash_dep_banks', models.DecimalField(decimal_places=2, max_digits=12)),
                ('no_of_agent_cash_withd_banks', models.PositiveIntegerField()),
                ('value_of_agent_cash_withd_banks', models.DecimalField(decimal_places=2, max_digits=12)),
            ],
        ),
        migrations.CreateModel(
            name='MobilePspInteroperability',
            fields=[
                ('row_id', models.AutoField(primary_key=True, serialize=False)),
                ('psp_id', models.CharField(choices=[('0800001', 'Safaricom Plc'), ('0800002', 'Airtel Money Kenya Limited'), ('0800003', 'Telkom Kenya Limited'), ('0800004', 'Mobile Pay Limited'), ('0800005', 'Kenswitch Limited'), ('0800006', 'Interswitch East Africa (K) Limited'), ('0800007', 'Integrated Payment Services Limited'), ('0800008', 'Viewtech Limited'), ('0800009', 'Web Tribe Limited'), ('0800010', 'Finserve Africa Limited'), ('0800011', 'Cellulant Kenya Limited'), ('0800012', 'Pesapal Limited'), ('0800013', 'Fivespot Limited'), ('0800014', 'Craft Silicon Limited'), ('0800015', 'Virtual Pay International Limited'), ('0800016', 'Direct Pay Limited'), ('0800017', 'Pesawise Services Limited'), ('0800018', 'Paystack Payments Kenya Limited'), ('0800019', 'Wakandi Kenya Limited'), ('0800020', 'Kenya Airports Parking Services (KAPS) Limited'), ('0800021', 'Loop Payco Limited'), ('0800022', 'DLocal Payments Kenya Limited'), ('0800023', 'Pesaflow Limited'), ('0800024', 'Kenya Commerce Exchange Service Bureau Limited'), ('0800025', 'PayU Kenya Limited'), ('0800026', 'Dolcepay Kenya Limited'), ('0800027', 'Unlimint Kenya Limited'), ('0800028', 'Gladys Technologies Limited'), ('0800029', 'Mamlaka Hub and Spoke Limited'), ('0800030', 'Eclectics International Limited'), ('0800031', 'Jumia Payment Services Kenya Limited'), ('0800032', 'Amsuka Capital Limited'), ('0800033', 'Sky World Limited'), ('0800034', 'Kashia Services Limited'), ('0800035', 'Data Integrated Limited'), ('0800036', 'Tanda Agent Limited')], max_length=25)),
                ('reporting_date', models.DateField()),
                ('band_code', models.CharField(choices=[('BNC01', '1 - 49'), ('BNC02', '50 - 100'), ('BNC03', '101 - 500'), ('BNC04', '501 - 1000'), ('BNC05', '1001 - 1500'), ('BNC06', '1501 - 2500'), ('BNC07', '2501 - 3500'), ('BNC08', '3501 - 5000'), ('BNC9', '5001 - 7500'), ('BNC10', '7501 - 10000'), ('BNC11', '10001 - 15000'), ('BNC12', '15001 - 20000'), ('BNC13', '20001 - 25000'), ('BNC14', '25001 - 30000'), ('BNC15', '30001 - 35000'), ('BNC16', '35001 - 40000'), ('BNC17', '40001 - 45000'), ('BNC18', '45001 - 50000'), ('BNC19', '50001 - 70000'), ('BNC20', '70001 - 150000'), ('BNC21', '150001-250000'), ('BNC22', 'Any other band')], max_length=25)),
                ('psp_id_other', models.CharField(choices=[('0800001', 'Safaricom Plc'), ('0800002', 'Airtel Money Kenya Limited'), ('0800003', 'Telkom Kenya Limited'), ('0800004', 'Mobile Pay Limited'), ('0800005', 'Kenswitch Limited'), ('0800006', 'Interswitch East Africa (K) Limited'), ('0800007', 'Integrated Payment Services Limited'), ('0800008', 'Viewtech Limited'), ('0800009', 'Web Tribe Limited'), ('0800010', 'Finserve Africa Limited'), ('0800011', 'Cellulant Kenya Limited'), ('0800012', 'Pesapal Limited'), ('0800013', 'Fivespot Limited'), ('0800014', 'Craft Silicon Limited'), ('0800015', 'Virtual Pay International Limited'), ('0800016', 'Direct Pay Limited'), ('0800017', 'Pesawise Services Limited'), ('0800018', 'Paystack Payments Kenya Limited'), ('0800019', 'Wakandi Kenya Limited'), ('0800020', 'Kenya Airports Parking Services (KAPS) Limited'), ('0800021', 'Loop Payco Limited'), ('0800022', 'DLocal Payments Kenya Limited'), ('0800023', 'Pesaflow Limited'), ('0800024', 'Kenya Commerce Exchange Service Bureau Limited'), ('0800025', 'PayU Kenya Limited'), ('0800026', 'Dolcepay Kenya Limited'), ('0800027', 'Unlimint Kenya Limited'), ('0800028', 'Gladys Technologies Limited'), ('0800029', 'Mamlaka Hub and Spoke Limited'), ('0800030', 'Eclectics International Limited'), ('0800031', 'Jumia Payment Services Kenya Limited'), ('0800032', 'Amsuka Capital Limited'), ('0800033', 'Sky World Limited'), ('0800034', 'Kashia Services Limited'), ('0800035', 'Data Integrated Limited'), ('0800036', 'Tanda Agent Limited')], max_length=50)),
                ('interoperability_code', models.CharField(choices=[('OIT01', 'P2P transactions'), ('OIT02', 'Agent to agent wallet'), ('OIT03', 'Till transactions to another network'), ('OIT04', 'Paybill transactions to another network'), ('OIT05', 'B2P wallet to another network'), ('OIT99', 'Other interoperability payment (specify)')], max_length=25)),
                ('incoming_transaction_volume', models.PositiveIntegerField()),
                ('incoming_transaction_value', models.DecimalField(decimal_places=2, max_digits=12)),
                ('outgoing_transaction_volume', models.PositiveIntegerField()),
                ('outgoing_transaction_value', models.DecimalField(decimal_places=2, max_digits=12)),
            ],
        ),
        migrations.CreateModel(
            name='PspTrustAccountPlacement',
            fields=[
                ('row_id', models.AutoField(primary_key=True, serialize=False)),
                ('psp_id', models.CharField(choices=[('0800001', 'Safaricom Plc'), ('0800002', 'Airtel Money Kenya Limited'), ('0800003', 'Telkom Kenya Limited'), ('0800004', 'Mobile Pay Limited'), ('0800005', 'Kenswitch Limited'), ('0800006', 'Interswitch East Africa (K) Limited'), ('0800007', 'Integrated Payment Services Limited'), ('0800008', 'Viewtech Limited'), ('0800009', 'Web Tribe Limited'), ('0800010', 'Finserve Africa Limited'), ('0800011', 'Cellulant Kenya Limited'), ('0800012', 'Pesapal Limited'), ('0800013', 'Fivespot Limited'), ('0800014', 'Craft Silicon Limited'), ('0800015', 'Virtual Pay International Limited'), ('0800016', 'Direct Pay Limited'), ('0800017', 'Pesawise Services Limited'), ('0800018', 'Paystack Payments Kenya Limited'), ('0800019', 'Wakandi Kenya Limited'), ('0800020', 'Kenya Airports Parking Services (KAPS) Limited'), ('0800021', 'Loop Payco Limited'), ('0800022', 'DLocal Payments Kenya Limited'), ('0800023', 'Pesaflow Limited'), ('0800024', 'Kenya Commerce Exchange Service Bureau Limited'), ('0800025', 'PayU Kenya Limited'), ('0800026', 'Dolcepay Kenya Limited'), ('0800027', 'Unlimint Kenya Limited'), ('0800028', 'Gladys Technologies Limited'), ('0800029', 'Mamlaka Hub and Spoke Limited'), ('0800030', 'Eclectics International Limited'), ('0800031', 'Jumia Payment Services Kenya Limited'), ('0800032', 'Amsuka Capital Limited'), ('0800033', 'Sky World Limited'), ('0800034', 'Kashia Services Limited'), ('0800035', 'Data Integrated Limited'), ('0800036', 'Tanda Agent Limited')], max_length=25)),
                ('reporting_date', models.DateField()),
                ('trust_fund_placement', models.CharField(max_length=25)),
                ('trust_fund_inv_maturity_date', models.DateField()),
                ('cat_trust_fund_invested_amt', models.DecimalField(decimal_places=2, max_digits=12)),
                ('interest_amt_per_category', models.DecimalField(decimal_places=2, max_digits=12)),
            ],
        ),
    ]
