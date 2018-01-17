# Meltdown/Spectre BIOS/Firmware Updates list

This is a list of all products an manufacturers which patched BIOS/Firmware addressing the Meltdown and Spectre vulnerabilities

If you have better info please send pull requests.

# Why I did this?
to have a parseable list for all my hardware

# Check your mainboard

## linux
```
curl -s https://raw.githubusercontent.com/mathse/meltdown-spectre-bios-list/master/README.md | grep "$(cat /sys/devices/virtual/dmi/id/board_name)"
```

## windows - powershell 3.0 or above
```
$model = (Get-WmiObject -Class Win32_ComputerSystem -ComputerName . | Select-Object -Property Model).Model
$mainboard = (Get-WmiObject Win32_BaseBoard | Select-Object Product).Product
$list = (Invoke-WebRequest https://raw.githubusercontent.com/mathse/meltdown-spectre-bios-list/master/README.md).content
$list.Split("`n") | Select-String "$model |$mainboard "
```

# ASUS
| model | latest BIOS | release date | vulnerabilities mitigated ? |
| --- | --- | --- | --- |
| B9440UA | ? | Jan/E, 2018 | |
| P2440UA | ? | Jan/E, 2018 | |
| P2440UQ | ? | Jan/E, 2018 | |
| P2540UV | ? | Jan/E, 2018 | |
| UX370UA | ? | Jan/E, 2018 | |
| UX461UA | ? | Jan/E, 2018 | |
| UX461UN | ? | Jan/E, 2018 | |
| UX561UA | ? | Jan/E, 2018 | |
| UX561UD | ? | Jan/E, 2018 | |
| UX561UN | ? | Jan/E, 2018 | |
| X510UA | ? | Jan/E, 2018 | |
| X510UAR | ? | Jan/E, 2018 | |
| X510UF | ? | Jan/E, 2018 | |
| X510UN | ? | Jan/E, 2018 | |
| X510UNR | ? | Jan/E, 2018 | |
| X510UQ | ? | Jan/E, 2018 | |
| X510UQR | ? | Jan/E, 2018 | |
| X510UR | ? | Jan/E, 2018 | |
| X510URR | ? | Jan/E, 2018 | |
| X580VD | ? | Jan/E, 2018 | |
| X580VN | ? | Jan/E, 2018 | |
| Prime Z370-A | 0606 | ? | no |
| Prime Z370-P | 0606 | ? | no |
| D630MT | ? | Jan/E, 2018 | |
| D630SF | ? | Jan/E, 2018 | |
| D631MT | ? | Jan/E, 2018 | |
| D830MT | ? | Jan/E, 2018 | |
| D830SF | ? | Jan/E, 2018 | |
| D831MT | ? | Jan/E, 2018 | |
| GR8 II | ? | Jan/E, 2018 | |
| E510 | ? | Jan/E, 2018 | |
| E810 | ? | Jan/E, 2018 | |
| E420 | ? | Jan/E, 2018 | |
| E520 | ? | Jan/E, 2018 | |
| VC65R | ? | Jan/E, 2018 | |
| VC65 | ? | Jan/E, 2018 | |
| VC66R | ? | Jan/E, 2018 | |
| VC66D | ? | Jan/E, 2018 | |
| VC66 | ? | Jan/E, 2018 | |
| VC68V | ? | Jan/E, 2018 | |
| VC68R | ? | Jan/E, 2018 | |
| VM45 | ? | Jan/E, 2018 | |
| VM65 | ? | Jan/E, 2018 | |
| VM65N | ? | Jan/E, 2018 | |
| VM65N | ? | Jan/E, 2018 | |
| VM65 | ? | Jan/E, 2018 | |
| UN65 | ? | Jan/E, 2018 | |
| UN65H | ? | Jan/E, 2018 | |
| UN65U | ? | Jan/E, 2018 | |
| UN68U | ? | Jan/E, 2018 | |
| ROG Maximus X Apex | follows | ? | |
| ROG Maximus X Code | follows | ? | |
| ROG Maximus X Formula | follows | ? | |
| ROG Maximus X Hero | follows | ? | |
| ROG Maximus X Hero (Wi-Fi AC) | follows | ? | |
| ROG Strix Z370-E Gaming | 0606 | ? | no |
| ROG Strix Z370-F Gaming | 0606 | ? | no |
| ROG Strix Z370-G Gaming | 0606 | ? | no |
| ROG Strix Z370-G Gaming (Wi-Fi AC) | 0606 | ? | no |
| ROG Strix Z370-H Gaming | follows | ? | |
| ROG Strix Z370-I Gaming | 0606 | ? | no |
| TUF Z370-Plus Gaming | 0606 | ? | no |
| TUF Z370-Pro Gaming | follows | ? | |

# Dell
| model | latest BIOS | release date | vulnerabilities mitigated ? |
| --- | --- | --- | --- |
| Alienware 13 R2 | follows | 1/19/2018 |
| Alienware 13 R3 | 1.2.3 | ? | no
| Alienware 15 R2 | follows | 1/19/2018
| Alienware 15 R3 | 1.2.3 | ? | no
| Alienware 17 R2 | follows | 1/19/2018
| Alienware 17 R4 | 1.2.3 | ? | no
| Alienware Area-51 R2 | follows | ? |
| Alienware Area-51 R4 | follows | 1/19/2018
| Alienware Area-51 R5 | follows | 1/19/2018
| Alienware Aurora R5 | follows | 1/19/2018
| Alienware Aurora R6 | 1.0.12 | ? | no
| Alienware Aurora R7 | follows | 1/31/2018
| Alienware Steam Machine 200 | 2.0.10
| Alienware Steam Machine 201 | 1.0.11
| Alienware X51 R3 | 1.0.11 | ? | no
| ChengMing 3967 | 1.2.2 | ? | no
| ChengMing 3977 | 1.3.2 | ? | no
| Dell Embedded Box PC 3000 | follows | In Process
| Edge Gateway 3000 series | follows | In Process
| Edge Gateway 5000 (Commercial) | follows | In Process
| Edge Gateway 5100 (Industrial) | follows | In Process
| Embedded Box PC 5000 | 1.4.2 | ? | no
| Enterprise Server T20 | A15 | ? | no
| Enterprise Server T30 | 1.0.12 | ? | no
| Inspiron 11 (3137) SFX Platform  | follows | In Process
| Inspiron 11 (3153) | 1.18.2 | ? | no
| Inspiron 11 (3158) | 1.18.2 | ? | no
| Inspiron 11 (3162)  | follows | In Process
| Inspiron 11 (3164) | follows | In Process
| Inspiron 11 (3168) | follows | In Process
| Inspiron 13 2-in-1 (5368) | 1.15.2 | ? | no
| Inspiron 13 2-in-1 (5378) | 1.22.3 | ? | no
| Inspiron 13 2-in-1 (5379) | 1.3.2 | ? | no
| Inspiron 13 2-in-1 (7378) | 1.22.3 | ? | no
| Inspiron 14 (3467) | 2.1.3 | ? | no
| Inspiron 14 (5439) | follows | In Process
| Inspiron 14 (3468) | 1.8.3 | ? | no
| Inspiron 14 (5468) | 1.4.2 | ? | no
| Inspiron 14 (7437) | follows | In Process
| Inspiron 14 (7460) | 1.4.2 | ? | no
| Inspiron 14 (7466) | 1.2.1 | ? | no
| Inspiron 14 (7467) | 1.4.0 | ? | no
| Inspiron 15 (3567) | 2.1.3 | ? | no
| Inspiron 15 (3568) | 1.8.3 | ? | no
| Inspiron 15 (5566) | 1.4.2 | ? | no
| Inspiron 15 (5567) | 1.1.9 | ? | no
| Inspiron 15 (7537) | follows | In Process
| Inspiron 15 (7560) | 1.4.2 | ? | no
| Inspiron 15 (7566) | 1.2.1 | ? | no
| Inspiron 15 (7567) | 1.4.0 | ? | no
| Inspiron 15 2-in-1 (5568) | 1.15.2 | ? | no
| Inspiron 15 2-in-1 (5578) | 1.22.3 | ? | no
| Inspiron 15 2-in-1 (5579) | 1.3.2 | ? | no
| Inspiron 15 2-in-1 (7569) | 1.15.2 | ? | no
| Inspiron 15 2-in-1 (7579) | 1.22.3 | ? | no
| Inspiron 15R (5537) | follows | In Process
| Inspiron 17 (5767) | 1.1.9 | ? | no
| Inspiron 17 (7737) | follows | In Process
| Inspiron 17 2-in-1 (7773) | 1.3.2 | ? | no
| Inspiron 17 2-in-1 (7778) | 1.15.2 | ? | no
| Inspiron 17 2-in-1 (7779) | 1.22.3 | ? | no
| Inspiron 17R (5737) | follows | In Process
| Inspiron 20 (3064) | 2.2.2 | ? | no
| Inspiron 20 AIO (3059) | follows | 1/19/2018
| Inspiron 22 (3263) | 1.7.0 | ? | no
| Inspiron 22 AIO (3263) | 1.7.0 | ? | no
| Inspiron 22 AIO (3264) | 2.2.2 | ? | no
| Inspiron 23 (5348) | A09 | ? | no
| Inspiron 2350 | follows | In Process
| Inspiron 24 (3459) | follows | 1/19/2018
| Inspiron 24 AIO (3464) | 2.2.2 | ? | no
| Inspiron 24 AIO (5459) | 2.8.0 | ? | no
| Inspiron 24 AIO (5488) | 2.4.2 | ? | no
| Inspiron 3052 | follows | In Process
| Inspiron 3147 | follows | In Process
| Inspiron 3148 | follows | In Process
| Inspiron 3169 | 1.4.0 | ? | no
| Inspiron 3179 | 1.3.3 | ? | no
| Inspiron 3250 | 3.5.2 | ? | no
| Inspiron 3252 | follows | In Process
| Inspiron 3268 | 1.6.0 | ? | no
| Inspiron 3452 | follows | In Process
| Inspiron 3458 | follows | In Process
| Inspiron 3459 | 1.5.3 | ? | no
| Inspiron 3462 | follows | 1/19/2018
| Inspiron 3476 | follows | 1/19/2018
| Inspiron 3537 | follows | In Process
| Inspiron 3558 | follows | In Process
| Inspiron 3559 | 1.5.3 | ? | no
| Inspiron 3576 | follows | 1/19/2018
| Inspiron 3650 | 3.5.2 | ? | no
| Inspiron 3662 | 2.5.0 | ? | no
| Inspiron 3668 | 1.6.0 | ? | no
| Inspiron 3737 | follows | In Process
| Inspiron 5370 | 1.3.1 | ? | no
| Inspiron 5442 | follows | In Process
| Inspiron 5447 | follows | In Process
| Inspiron 5452 | follows | In Process
| Inspiron 5457 | 1.3.2 | ? | no
| Inspiron 5458 | follows | In Process
| Inspiron 5459 | 1.4.1 | ? | no
| Inspiron 5542 | follows | In Process
| Inspiron 5547 | follows | In Process
| Inspiron 5552 | follows | In Process
| Inspiron 5557 | 1.3.2 | ? | no
| Inspiron 5558 | follows | In Process
| Inspiron 5559 | 1.4.1 | ? | no
| Inspiron 5570 | 1.0.9 | ? | no
| Inspiron 5577 | 1.0.8 | ? | no
| Inspiron 5758 | follows | In Process
| Inspiron 5759 | 1.4.1 | ? | no
| Inspiron 5770 | 1.0.9 | ? | no
| Inspiron 7347 | follows | In Process
| Inspiron 7348 2-in-1 | follows | In Process
| Inspiron 7353 | 1.18.2 | ? | no
| Inspiron 7359 | 1.18.2 | ? | no
| Inspiron 7370 | 1.5.4 | ? | no
| Inspiron 7373 | 1.5.4 | ? | no
| Inspiron 7459 | 1.7.1 | ? | no
| Inspiron 7472 | 1.1.0 | ? | no
| Inspiron 7559 | 1.2.7 | ? | no
| Inspiron 7568 | 1.18.2 | ? | no
| Inspiron 7570 | 1.5.4 | ? | no
| Inspiron 7572 | 1.1.0 | ? | no
| Inspiron 7573 | 1.5.4 | ? | no
| Inspiron 7577 | 1.3.2 | ? | no
| Latitude 3150 | follows | In Process
| Latitude 3160 | follows | In Process
| Latitude 3180 | follows | 1/18/2018
| Latitude 3189 | follows | 1/18/2018
| Latitude 3330 | follows | In Process
| Latitude 3340 | A15 | 1/12/2018 | yes
| Latitude 3350 | A12 | ? | no
| Latitude 3379 | 1.0.21 | ? | no
| Latitude 3380 | 1.3.5 | ? | no
| Latitude 3390 2-in-1 | follows | 1/18/2018
| Latitude 3450 | A15 | ? | no
| Latitude 3460 | A12 | ? | no
| Latitude 3470 | 1.10.1 | ? | no
| Latitude 3480 | 1.5.5 | ? | no
| Latitude 3490 | follows | 1/19/2018
| Latitude 3540 | follows | In Process
| Latitude 3550 | A15 | ? | no
| Latitude 3560 | A12 | ? | no
| Latitude 3570 | 1.10.1 | ? | no
| Latitude 3580 | 1.5.5 | ? | no
| Latitude 3590 | follows | 1/19/2018
| Latitude 5175 | 1.0.29 | ? | no
| Latitude 5179 | 1.0.29 | ? | no
| Latitude 5280 | 1.8.1 | ? | no
| Latitude 5285 | 1.3.1 | ? | no
| Latitude 5288 | 1.8.1 | ? | no
| Latitude 5289 | 1.10.1 | ? | no
| Latitude 5290 | 1.1.7 | ? | no
| Latitude 5290 2-in-1 | 1.1.0 | ? | no
| Latitude 5404 | follows | 1/19/2018
| Latitude 5414 | 1.15.0 | ? | no
| Latitude 5480 | 1.8.1 | ? | no
| Latitude 5488 | 1.8.1 | ? | no
| Latitude 5490 | 1.1.7 | ? | no
| Latitude 5580 | 1.8.1 | ? | no
| Latitude 5590 | 1.1.7 | ? | no
| Latitude 7202 | follows | 1/19/2018
| Latitude 7204 | follows | 1/19/2018
| Latitude 7212 | 1.7.0 | ? | no
| Latitude 7214 | 1.15.0 | ? | no
| Latitude 7275 | 1.1.34 | ? | no
| Latitude 7280 | 1.8.1 | ? | no
| Latitude 7285 | 1.1.0 | ? | no
| Latitude 7290 | 1.2.6 | ? | no
| Latitude 7350 | A14 | ? | no
| Latitude 7370 | 1.15.3 | ? | no
| Latitude 7380 | 1.8.1 | ? | no
| Latitude 7389 | 1.10.1 | ? | no
| Latitude 7390 | 1.2.6 | ? | no
| Latitude 7390 2-in-1 | 1.1.3 | ? | no
| Latitude 7404 | follows | 1/19/2018
| Latitude 7414 | 1.15.0 | ? | no
| Latitude 7480 | 1.8.1 | ? | no
| Latitude 7490 | 1.2.6 | ? | no
| Latitude E5250 | A18 | ? | no
| Latitude E5270 | 1.18.6 | ? | no
| Latitude E5430 | follows | 2/7/2018
| Latitude E5430 vPro | follows | 2/7/2018
| Latitude E5440 | A19 | ? | no
| Latitude E5450 | A18 | ? | no
| Latitude E5470 | 1.18.6 | ? | no
| Latitude E5530 | follows | 2/7/2018
| Latitude E5530 vPro | follows | 2/7/2018
| Latitude E5540 | A19 | ? | no
| Latitude E5550 | A18 | ? | no
| Latitude E5570 | 1.18.6 | ? | no
| Latitude E6230 | follows | 2/7/2018
| Latitude E6330 | follows | 2/7/2018
| Latitude E6430 | follows | 2/7/2018
| Latitude E6430 ATG | follows | 2/7/2018
| Latitude E6430S | follows | 2/7/2018
| Latitude E6430U | follows | 2/7/2018
| Latitude E6440 | A19 | ? | no
| Latitude E6440 ATG | follows | 1/31/2018
| Latitude E6530 | follows | 2/7/2018
| Latitude E6540 | A22 | ? | no
| Latitude E7240 | A23 | ? | no
| Latitude E7250 | A18 | ? | no
| Latitude E7270 | 1.18.5 | ? | no
| Latitude E7440 | A23 | ? | no
| Latitude E7450 | A18 | ? | no
| Latitude E7470 | 1.18.5 | ? | no
| OptiPlex 3010 | follows | 1/19/2018
| OptiPlex 3011 AIO | follows | 1/19/2018
| OptiPlex 3020 | A16 | 1/11/2018 | yes (verified)
| OptiPlex 3020M | A11 | ? | no
| OptiPlex 3030 | follows | 1/19/2018
| OptiPlex 3040 | 1.6.1 | 2018/01/09 | yes |
| OptiPlex 3046 | 1.3.1 | ? | no
| OptiPlex 3050 | 1.7.7 | ? | no
| OptiPlex 3050 AIO | 1.8.1 | ? | no
| OptiPlex 3240 AIO | 1.5.21 | ? | no
| OptiPlex 5040 | 1.8.1 | ? | no
| OptiPlex 5050 | 1.7.7 | ? | no
| OptiPlex 5250 | 1.8.1 | ? | no
| OptiPlex 7010 | A26 | 2018/01/09 | no |
| OptiPlex 7020 | A14 | ? | no
| OptiPlex 7040 | 1.8.1 | ? | no
| OptiPlex 7050 | 1.7.7 | 1/9/2018 | yes (verified)
| OptiPlex 7440 AIO | 1.8.6 | ? | no
| OptiPlex 7450 | 1.8.1 | ? | no
| OptiPlex 9010 | A27 | ? | no
| OptiPlex 9010 AIO | follows | 1/19/2018
| OptiPlex 9020 | A21 | ? | no
| OptiPlex 9020 AIO | A16 | ? | no
| OptiPlex 9020M | A15 | ? | no
| OptiPlex 9030 | follows | 1/19/2018
| OptiPlex XE2 | A21 | ? | no
| Precision 3420 Tower | 2.6.1 | ? | no
| Precision 3510 | 1.18.6 | ? | no
| Precision 3520 | 1.8.1 | ? | no
| Precision 3620 Tower | 2.6.1 | ? | no
| Precision 5510 | 1.6.1 | ? | no
| Precision 5520 | 1.7.0 | ? | no
| Precision 5720 AIO | 2.3.3 | ? | no
| Precision 5810 Tower | A24 | ? | no
| Precision 5810 XL Tower | A24 | ? | no
| Precision 5820 XL Tower | 1.2.1 | ? | no
| Precision 7510 | 1.15.3 | ? | no
| Precision 7520 | 1.9.0 | ? | no
| Precision 7710 | 1.15.3 | ? | no
| Precision 7720 | 1.9.0 | ? | no
| Precision 7810 Tower | A24 | ? | no
| Precision 7810 XL Tower | A24 | ? | no
| Precision 7820 Tower | 1.2.2 | ? | no
| Precision 7910 Tower | A24 | ? | no
| Precision 7910 XL Tower | A24 | ? | no
| Precision 7920 Tower | 1.2.2 | ? | no
| Precision M2800 | A12 | ? | no
| Precision M4700 | follows | 2/7/2018
| Precision M4800 | A21 | ? | no
| Precision M6700 | follows | 2/7/2018
| Precision M6800 | A21 | ? | no
| Precision R7610 | A15 | ? | no
| Precision Rack 7910 | 2.7.0 | ? | no
| Precision T1650 | A25 | ? | no
| Precision T1700 | A24 | ? | no
| Precision T3610 | A15 | ? | no
| Precision T5610 | A15 | ? | no
| Precision T7610 | A15 | ? | no
| Venue 11 Pro (5130-32Bit) | follows | In Process
| Venue 11 Pro (5130-64Bit) | follows | In Process
| Venue 11 Pro (7130) | A24 | ? | no
| Venue 11 Pro (7130) MS | follows | In Process
| Venue 11 Pro (7140) | A14 | ? | no
| Vostro 14 (3459) | 1.3.1 | ? | no
| Vostro 14 (3468) | 2.1.5 | ? | no
| Vostro 14 (5468) | 1.4.2 | ? | no
| Vostro 14 (5470) | follows | In Process
| Vostro 15 (3559) | 1.3.1 | ? | no
| Vostro 15 (3568) | 2.1.5 | ? | no
| Vostro 15 (5568) | 1.4.2 | ? | no
| Vostro 23 (3340) | A07 | ? | no
| Vostro 24 (5450) | 2.8.0 | ? | no
| Vostro 24 (5460 Kaby Lake) | 2.4.2
| Vostro 24 (5460) | 1.4.0 | ? | no
| Vostro 3052 | follows | In Process
| Vostro 3250 | 3.5.2 | ? | no
| Vostro 3252 | follows | In Process
| Vostro 3267 | 1.6.0 | ? | no
| Vostro 3268 | 1.6.0 | ? | no
| Vostro 3458 | follows | In Process
| Vostro 3558 | follows | In Process
| Vostro 3562 | follows | 1/19/2018
| Vostro 3650 | 3.5.2 | ? | no
| Vostro 3653 | 3.5.2 | ? | no
| Vostro 3660 | 1.6.0 | ? | no
| Vostro 3667 | 1.6.0 | ? | no
| Vostro 3668 | 1.6.0 | ? | no
| Vostro 3669 | 1.6.0 | ? | no
| Vostro 5370 | 1.3.1 | ? | no
| Vostro 5459 | 1.1.3 | ? | no
| Vostro 5471 | 1.3.1 | ? | no
| Vostro 5560 | follows | In Process
| Vostro 7570 | 1.3.2 | ? | no
| XPS 12 (9250) | 1.1.34 | ? | no
| XPS 13 (9343) | follows | 1/19/2018
| XPS 13 (9350) | 1.6.1 | ? | no
| XPS 13 (9360) | 2.5.0 | ? | no
| XPS 13 (9370) | 1.1.3 | ? | no
| XPS 13 2-in-1 (9365) | 1.2.1 | ? | no
| XPS 15 (9550) | 1.6.1 | ? | no
| XPS 15 (9560) | 1.7.0 | ? | no
| XPS 27 AIO (7760) | 2.3.3 | ? | no
| XPS 8900 | 2.2.1 | ? | no
| XPS 8910 | follows | 1/19/2018
| XPS 8920 | 1.0.12 | ? | no
| XPS 8930 | follows | 1/31/2018

# HP
| model | latest BIOS | release date | vulnerabilities mitigated ? |
| --- | --- | --- | --- |
| HP 21-h0xx PC | 80.18 | SP84417 |  | http://ftp.hp.com/pub/softpaq/sp84001-84500/sp84417.exe
| HP 23-g0xx PC | 80.18 | SP84417 |  | http://ftp.hp.com/pub/softpaq/sp84001-84500/sp84417.exe
| HP ENVY 15-q2xx | F.27 | SP84431 |  | http://ftp.hp.com/pub/softpaq/sp84001-84500/sp84431.exe
| HP ENVY 23-nxxx All-in-One PC Beats SE | 80.13 | SP84254 |  | http://ftp.hp.com/pub/softpaq/sp84001-84500/sp84254.exe
| HP ENVY 750-6xx | F.10 | SP84331 |  | http://ftp.hp.com/pub/softpaq/sp84001-84500/sp84331.exe
| HP ENVY Curved 34-a0xx All-in-One PC | A0.09 | SP84375 |  | http://ftp.hp.com/pub/softpaq/sp84001-84500/sp84375.exe
| HP ENVY Laptop 13-ad000 ~ 13-ad099 | F.19 | SP84431 |  | http://ftp.hp.com/pub/softpaq/sp84001-84500/sp84431.exe
| HP ENVY Laptop 13-ad1xx, 13t-ad100 | F.19 | SP84332 |  | http://ftp.hp.com/pub/softpaq/sp84001-84500/sp84332.exe
| HP ENVY Laptop 17-ae1xx, 17t-ae100, 17m-ae1xx | F.19 | SP84333 |  | http://ftp.hp.com/pub/softpaq/sp84001-84500/sp84333.exe
| HP ENVY Notebook 17-u2xx, 17t-u200 | F.11 | SP84207 |  | http://ftp.hp.com/pub/softpaq/sp84001-84500/sp84207.exe
| HP ENVY x360 Convertible 15-bp000 ~ 15-bp099 | F.33 | SP84242 |  | http://ftp.hp.com/pub/softpaq/sp84001-84500/sp84242.exe
| HP ENVY x360 Convertible 15m-bp000 ~ 15m-bp099 | F.33 | SP84242 |  | http://ftp.hp.com/pub/softpaq/sp84001-84500/sp84242.exe
| HP ENVY x360 Convertible 15-w200 ~ 15-w299 | F.31 | sp84223 |  | http://ftp.hp.com/pub/softpaq/sp84001-84500/sp84223.exe
| HP ENVY 750-4xx Desktop PC | F.40 | SP84196 |  | http://ftp.hp.com/pub/softpaq/sp84001-84500/sp84196.exe
| HP ENVY 750-5xxPC Desktop PC | F.21 | SP84435 |  | http://ftp.hp.com/pub/softpaq/sp84001-84500/sp84435.exe
| HP Notebook 13-s000 ~ 13-s099 | F.23 | SP84430 |  | http://ftp.hp.com/pub/softpaq/sp84001-84500/sp84430.exe
| HP Notebook PC 11-aa0XX | F.14 | SP84332 |  | http://ftp.hp.com/pub/softpaq/sp84001-84500/sp84332.exe
| HP Notebook PC 11-ab0XX | F.14 | SP84332 |  | http://ftp.hp.com/pub/softpaq/sp84001-84500/sp84332.exe
| HP Pavilion 13-a000 ~ 13-a099 x360 | F.38 | SP84429 |  | http://ftp.hp.com/pub/softpaq/sp84001-84500/sp84429.exe
| HP Pavilion 13-b000 ~ 13-b099 | F.38 | SP84429 |  | http://ftp.hp.com/pub/softpaq/sp84001-84500/sp84429.exe
| HP Pavilion 13t-a0XX x360 | F.38 | SP84429 |  | http://ftp.hp.com/pub/softpaq/sp84001-84500/sp84429.exe
| HP Pavilion 13t-b0XX | F.38 | SP84429 |  | http://ftp.hp.com/pub/softpaq/sp84001-84500/sp84429.exe
| HP Pavilion 23-p0xx All-in-One PC | 80.18 | SP84417 |  | http://ftp.hp.com/pub/softpaq/sp84001-84500/sp84417.exe
| HP Pavilion Laptop 14-bf0xx, 14t-bf000 | F.32 | SP84206 |  | http://ftp.hp.com/pub/softpaq/sp84001-84500/sp84206.exe
| HP Pavilion Laptop 15-ck0xx, 15t-ck000 | F.04 | SP84210 |  | http://ftp.hp.com/pub/softpaq/sp84001-84500/sp84210.exe
| HP Pavilion Notebook 15-bc200 ~ 15-bc299 | F.44 | SP84432 |  | http://ftp.hp.com/pub/softpaq/sp84001-84500/sp84432.exe
| HP Spectre Notebook 13-v100 ~ 13-v199 | F.38 | SP84333 |  | http://ftp.hp.com/pub/softpaq/sp84001-84500/sp84333.exe
| HP Spectre x2 Detachable 12-c000 ~ 12-c099 | F.12 | SP84208 |  | http://ftp.hp.com/pub/softpaq/sp84001-84500/sp84208.exe
| HP Spectre x360 Convertible 13-ae0xx, 13-ae5xx, 13t-ae000, 13t-ae500 | F.12 | SP84314 |  | http://ftp.hp.com/pub/softpaq/sp84001-84500/sp84314.exe
| HP Spectre x360 Convertible 15-bl1xx, 15t-bl100 | F.32 | SP84378 |  | http://ftp.hp.com/pub/softpaq/sp84001-84500/sp84378.exe
| OMEN by HP Laptop 17-an000 ~ 17-an099 | F.11 | sp84223 |  | http://ftp.hp.com/pub/softpaq/sp84001-84500/sp84223.exe
| OMEN X VR PC Pack | F.11 | SP84360 |  | http://ftp.hp.com/pub/softpaq/sp84001-84500/sp84360.exe
| Compaq 100-0xx Desktop PC | follows | Feb. 9 2018
| Compaq 14-s000 thru 14-s099 (Intel) | follows | Feb. 9 2018
| Compaq 14-s000 thru 14-s099 TouchSmart (Intel) | follows | Feb. 9 2018
| Compaq 14t-s000 (Intel) | follows | Feb. 9 2018
| Compaq 14t-s000 TouchSmart (Intel) | follows | Feb. 9 2018
| Compaq 15-s000 ~ 15-s099 (Intel) | follows | Feb. 9 2018
| Compaq 15-s000 ~ 15-s099 TouchSmart (Intel) | follows | Feb. 9 2018
| Compaq 15t-s000 (Intel) | follows | Feb. 9 2018
| Compaq 15t-s000 TouchSmart (Intel) | follows | Feb. 9 2018
| Compaq 18-40xx PC | follows | Feb. 9 2018
| Compaq 18-50xx PC | follows | Feb. 9 2018
| Compaq 19-20xx PC | follows | Feb. 9 2018
| Compaq Presario 45-900 ~ 45-999 | follows | Feb. 9 2018
| HP 1000-1300 ~ 1000-1399 | follows | Feb. 9 2018
| HP 10-pOXX | follows | Feb. 9 2018
| HP 110-axx Desktop PC | follows | Feb. 9 2018
| HP 14-r000 ~ HP14-r099 (Intel) | follows | Feb. 9 2018
| HP 14-r000 ~ HP14-r099 TouchSmart (Intel) | follows | Feb. 9 2018
| HP 14t-r000 (Intel) | follows | Feb. 9 2018
| HP 14t-r000 TouchSmart (Intel) | follows | Feb. 9 2018
| HP 15g-ad000 ~ ad099 Notebook PC | follows | Feb. 9 2018
| HP 15g-ad100 ~ ad199 Notebook PC | follows | Feb. 9 2018
| HP 15q-aj000 ~ aj099 Notebook PC | follows | Feb. 9 2018
| HP 15q-aj100 ~ aj199 Notebook PC | follows | Feb. 9 2018
| HP 15-r000 ~ HP15-r099 | follows | Feb. 9 2018
| HP 15-r000 ~ HP15-r099 TouchSmart | follows | Feb. 9 2018
| HP 15t-r000 | follows | Feb. 9 2018
| HP 15t-r000 Touchsmart | follows | Feb. 9 2018
| HP 18-50xx PC | follows | Feb. 9 2018
| HP 19-20xx PC | follows | Feb. 9 2018
| HP 20-20xx PC | follows | Feb. 9 2018
| HP 20-r0xx All-in-One PC | follows | Feb. 9 2018
| HP 22-20xx All-in-One PC | follows | Feb. 9 2018
| HP 22-30xx All-in-One PC | follows | Feb. 9 2018
| HP 23-r0xx All-in-One PC | follows | Feb. 9 2018
| HP 240 G3 Notebook PC | follows | Feb. 9 2018
| HP 240 G4 | follows | Feb. 9 2018
| HP 240 G5 | follows | Feb. 9 2018
| HP 240 g5 Notebook PC | follows | Feb. 9 2018
| HP 246 G3 Notebook PC | follows | Feb. 9 2018
| HP 246 G4 | follows | Feb. 9 2018
| HP 246 G5 | follows | Feb. 9 2018
| HP 246 G6 Notebook PC | follows | Feb. 9 2018
| HP 246 Notebook PC | follows | Feb. 9 2018
| HP 250 G1 Notebook PC | follows | Feb. 9 2018
| HP 250 G3 | follows | Feb. 9 2018
| HP 250 G4 | follows | Feb. 9 2018
| HP 250 g4 Notebook PC | follows | Feb. 9 2018
| HP 251-0xx Desktop PC | follows | Feb. 9 2018
| HP 251-axx Desktop PC | follows | Feb. 9 2018
| HP 256 G4 | follows | Feb. 9 2018
| HP 256 G6 Notebook PC | follows | Feb. 9 2018
| HP ENVY 12-g0xx | follows | Feb. 9 2018
| HP ENVY 13-d000 ~ 13-d099 | follows | Feb. 9 2018
| HP ENVY 13t-d000 ~ 13t-d099 | follows | Feb. 9 2018
| HP ENVY 14-j000 ~ 14-j099 | follows | Feb. 9 2018
| HP ENVY 14t | follows | Feb. 9 2018
| HP ENVY 14t-j000 | follows | Feb. 9 2018
| HP ENVY 14-u000 ~ 14-u099 | follows | Feb. 9 2018
| HP ENVY 15 Notebook PC 15-q1xx | follows | Feb. 9 2018
| HP ENVY 15-j000 ~ 15-j099; 15-j100 ~ 15-j199 | follows | Feb. 9 2018
| HP ENVY 15-k000 - 15-k099 | follows | Feb. 9 2018
| HP ENVY 15-p000 ~ 15-p099 | follows | Feb. 9 2018
| HP ENVY 15-q3xx | follows | Feb. 9 2018
| HP ENVY 15t-j000; 15t-j100 | follows | Feb. 9 2018
| HP ENVY 15t-k000 | follows | Feb. 9 2018
| HP ENVY 15t-p000 | follows | Feb. 9 2018
| HP ENVY 17-j000 ~ 17-j099 Leap Motion SE | follows | Feb. 9 2018
| HP ENVY 17-j000 ~ 17-j099 Leap Motion TS SE | follows | Feb. 9 2018
| HP ENVY 17-j000 ~ 17-j099; 17-j100 ~ 17-j199 | follows | Feb. 9 2018
| HP ENVY 17-j100 ~ 17-j199 Leap Motion SE | follows | Feb. 9 2018
| HP ENVY 17-j100 ~ 17-j199 Leap Motion TS SE | follows | Feb. 9 2018
| HP ENVY 17-n000 ~ 17-n099 | follows | Feb. 9 2018
| HP ENVY 17t-j000 Leap Motion SE | follows | Feb. 9 2018
| HP ENVY 17t-j000 Leap Motion TS SE | follows | Feb. 9 2018
| HP ENVY 17t-j000; 17t-j100 | follows | Feb. 9 2018
| HP ENVY 17t-j100 Leap Motion SE | follows | Feb. 9 2018
| HP ENVY 17t-j100 Leap Motion TS SE | follows | Feb. 9 2018
| HP ENVY 17t-n000 | follows | Feb. 9 2018
| HP ENVY 24-m0xx All-in-One PC (Bulldozer-4GL/Bulldozer-4GTHD/Bulldozer-4GT/ Intel) | follows | Feb. 9 2018
| HP ENVY 27-xxx Recline AIO PC | follows | Feb. 9 2018
| HP ENVY h8-XXXX Desktop | follows | Feb. 9 2018
| HP ENVY Laptop 17-ae000 ~ 17-ae099 | follows | Feb. 9 2018
| HP ENVY Laptop 17m-ae000 ~ 17m-ae099 | follows | Feb. 9 2018
| HP ENVY Notebook 13-ab000 ~ 13-ab099 | follows | Feb. 9 2018
| HP ENVY Notebook 15-q3xx | follows | Feb. 9 2018
| HP ENVY Notebook 15-q400~15-q499 | follows | Feb. 9 2018
| HP ENVY Phoenix 800-0xx PC | follows | Feb. 9 2018
| HP ENVY Phoenix 810-0xx PC | follows | Feb. 9 2018
| HP ENVY Phoenix 850-0xx Desktop PC | follows | Feb. 9 2018
| HP ENVY Recline 23-xxx All-in-One PC | follows | Feb. 9 2018
| HP ENVY Recline Pro 23 All-in-One Business PC | follows | Feb. 9 2018
| HP ENVY Recline Pro 27 All-in-One Business PC | follows | Feb. 9 2018
| HP ENVY TouchSmart 15t-j000; 15t-j100 | follows | Feb. 9 2018
| HP ENVY TouchSmart 17t-j000; 17t-j100 | follows | Feb. 9 2018
| HP ENVY TouchSmart m7t-j000; m7t-j100 | follows | Feb. 9 2018
| HP ENVY TS 15-j000 ~ 15-j099; 15-j100 ~ 15-j199 | follows | Feb. 9 2018
| HP ENVY TS 17-j000 ~ 17-j099; 17-j100 ~ 17-j199 | follows | Feb. 9 2018
| HP ENVY TS m7-j000 ~ m7-j099; m7-j100 ~ m7-j199 | follows | Feb. 9 2018
| HP ENVY x2 13t-j0xx | follows | Feb. 9 2018
| HP ENVY x2 15t-c0xx | follows | Feb. 9 2018
| HP ENVY x2 Detachable PC 13-j000 ~ j099 | follows | Feb. 9 2018
| HP ENVY x2 Detachable PC 15-c000 ~ c099 | follows | Feb. 9 2018
| HP ENVY x360 15-w000 ~ 15-w099 | follows | Feb. 9 2018
| HP ENVY x360 15-w1XX | follows | Feb. 9 2018
| HP ENVY x360 Convertible 13-y000 ~ 13-y099 | follows | Feb. 9 2018
| HP ENVY x360 Convertible 15-aq2xx, 15t-aq200 | follows | Feb. 9 2018
| HP ENVY x360 Convertible 15-bp1xx, 15t-bp100, 15m-bp1xx | follows | Feb. 9 2018
| HP ENVY x360 m6 Convertible PC | follows | Feb. 9 2018
| HP ENVY x360 m6-w1xx | follows | Feb. 9 2018
| HP Laptop 14-bp000 ~ 14-bp099 | follows | Feb. 9 2018
| HP Laptop 14-bp1xx, 14s-bp1xx, 14s-bc1xx, 14s-be1xx | follows | Feb. 9 2018
| HP Laptop 14-bs1xx, 14-bs6xx, 14t-bs100, 14t-bs600, 14g-br1xx, 14q-bu1xx | follows | Feb. 9 2018
| HP Laptop 14s-bc000 ~ 14s-bc099 | follows | Feb. 9 2018
| HP Laptop 14s-be000 ~ 14s-be099 | follows | Feb. 9 2018
| HP Laptop 14s-bp000 ~ 14s-bp099 | follows | Feb. 9 2018
| HP Laptop 15-bs0xx | follows | Feb. 9 2018
| HP Laptop 15-bs1xx, 15-bs7xx, 15t-bs100, 15t-bs700, 15g-br1xx, 15q-bu1xx | follows | Feb. 9 2018
| HP Laptop 17-bs000 ~ 17-bs099 | follows | Feb. 9 2018
| HP Laptop 17-bs1xx, 17t-bs100, 17g-br1xx, 17q-bu1xx | follows | Feb. 9 2018
| HP Laptop 17g-br000 ~ 17g-br099 | follows | Feb. 9 2018
| HP Laptop 17g-bu000 ~ 17g-bu099 | follows | Feb. 9 2018
| HP Notebook 11-f0XX | follows | Feb. 9 2018
| HP Notebook 11-f1XX | follows | Feb. 9 2018
| HP Notebook 14-w1xx | follows | Feb. 9 2018
| HP Notebook 14-y0xx | follows | Feb. 9 2018
| HP Notebook 15-f0xx | follows | Feb. 9 2018
| HP Notebook g14 | follows | Feb. 9 2018
| HP Notebook PC 15-f2xx | follows | Feb. 9 2018
| HP OMEN Notebook 15-5300 ~ 5399 | follows | Feb. 9 2018
| HP OMEN Notebook PC 15 | follows | Feb. 9 2018
| HP OMEN Pro 15 | follows | Feb. 9 2018
| HP Pavilion 11-n000 x360 ~ Pavilion 11-n099 x360 | follows | Feb. 9 2018
| HP Pavilion 11t x360 | follows | Feb. 9 2018
| HP Pavilion 14-al000~14-al099 | follows | Feb. 9 2018
| HP Pavilion 14t-al000 | follows | Feb. 9 2018
| HP Pavilion 14t-v000 | follows | Feb. 9 2018
| HP Pavilion 14-v000~14-v099 | follows | Feb. 9 2018
| HP Pavilion 15-au000~15-au099 | follows | Feb. 9 2018
| HP Pavilion 15-bc000~15-bc099 | follows | Feb. 9 2018
| HP Pavilion 15-n100~199 | follows | Feb. 9 2018
| HP Pavilion 15-p000~15-p099 | follows | Feb. 9 2018
| HP Pavilion 15t-au000 | follows | Feb. 9 2018
| HP Pavilion 15t-bc000 | follows | Feb. 9 2018
| HP Pavilion 15t-p000 | follows | Feb. 9 2018
| HP Pavilion 17-ab001~ 17-ab099 | follows | Feb. 9 2018
| HP Pavilion 17t-ab001 | follows | Feb. 9 2018
| HP Pavilion 17-x000~17-x099 | follows | Feb. 9 2018
| HP Pavilion 550-0xx Desktop PC | follows | Feb. 9 2018
| HP Pavilion All-in-One 24-qa0xx | follows | Feb. 9 2018
| HP Pavilion All-in-One 24-r0xx | follows | Feb. 9 2018
| HP Pavilion All-in-One 24-x0xx | follows | Feb. 9 2018
| HP Pavilion All-in-One 27-qa0xx | follows | Feb. 9 2018
| HP Pavilion All-in-One 27-r0xx | follows | Feb. 9 2018
| HP Pavilion HPE h8-1xxx PC | follows | Feb. 9 2018
| HP Pavilion HPE h9-1xxx Phoenix PC | follows | Feb. 9 2018
| HP Pavilion Laptop 14-bf1xx, 14t-bf100 | follows | Feb. 9 2018
| HP Pavilion Laptop 14-bk000 ~ 14-bk099 | follows | Feb. 9 2018
| HP Pavilion Laptop 14-bk1xx, 14t-bk100 | follows | Feb. 9 2018
| HP Pavilion Laptop 15-cc000 ~ 15-cc099 | follows | Feb. 9 2018
| HP Pavilion Laptop 15-cc1xx, 15t-cc100 | follows | Feb. 9 2018
| HP Pavilion Laptop 15-cc500 ~ 15-cc599 | follows | Feb. 9 2018
| HP Pavilion Laptop 15-cc6xx, 15t-cc600 | follows | Feb. 9 2018
| HP Pavilion Laptop 15-cc700 ~ 15-cc799 | follows | Feb. 9 2018
| HP Pavilion Mini Desktop 300-0xx | follows | Feb. 9 2018
| HP Pavilion Notebook 14-ab000~ab099 | follows | Feb. 9 2018
| HP Pavilion Notebook 14-ab100~ab199 | follows | Feb. 9 2018
| HP Pavilion Notebook 14t-ab000 | follows | Feb. 9 2018
| HP Pavilion Notebook 14t-ab100 | follows | Feb. 9 2018
| HP Pavilion Notebook 15-ab000~ab099 | follows | Feb. 9 2018
| HP Pavilion Notebook 15-ab100~ab199 | follows | Feb. 9 2018
| HP Pavilion Notebook 15-ab500~ab599 | follows | Feb. 9 2018
| HP Pavilion Notebook 15-bc3xx, 15t-bc300 | follows | Feb. 9 2018
| HP Pavilion Notebook 15t-ab000 | follows | Feb. 9 2018
| HP Pavilion Notebook 15t-ab200 | follows | Feb. 9 2018
| HP Pavilion Notebook 17-ab200 ~ 17-ab299 | follows | Feb. 9 2018
| HP Pavilion Notebook 17-ab3xx, 17t-ab300 | follows | Feb. 9 2018
| HP Pavilion Power Laptop 15-cb000 ~ 15-cb099 | follows | Feb. 9 2018
| HP Pavilion Power Laptop 15-cb500 ~ 15-cb599 | follows | Feb. 9 2018
| HP Pavilion x2 10-n1xx | follows | Feb. 9 2018
| HP Pavilion x2 10-n2XX | follows | Feb. 9 2018
| HP Pavilion x2 Detachable 12-b000 ~ 12-b099 (Intel) | follows | Feb. 9 2018
| HP Pavilion x2 Detachable 12-b100 ~ 12-b199 (Intel) | follows | Feb. 9 2018
| HP Pavilion x2 Detachable PC 10-j0xx (Intel) | follows | Feb. 9 2018
| HP Pavilion x2 Detachable PC 10-k0xx (Intel) | follows | Feb. 9 2018
| HP Pavilion x360 13-s100 ~13-s199 | follows | Feb. 9 2018
| HP Pavilion x360 15-bk000 ~ 15-bk099 | follows | Feb. 9 2018
| HP Pavilion x360 15-bk100 ~ 15-bk199 | follows | Feb. 9 2018
| HP Pavilion x360 Convertible 11 11-k000~11-k099 | follows | Feb. 9 2018
| HP Pavilion x360 Convertible 11-ad000 ~ 11-ad099 | follows | Feb. 9 2018
| HP Pavilion x360 Convertible 11m-ad000 ~ 11m-ad099 | follows | Feb. 9 2018
| HP Pavilion x360 Convertible 14-ba000 ~ 14-ba099 | follows | Feb. 9 2018
| HP Pavilion x360 Convertible 14-ba1xx, 14t-ba100, 14m-ba1xx, 14t-cc100, 14-cc1xx | follows | Feb. 9 2018
| HP Pavilion x360 Convertible 14-cc000 ~ 14-cc099 | follows | Feb. 9 2018
| HP Pavilion x360 Convertible 14m-ba000 ~ 14m-ba099 | follows | Feb. 9 2018
| HP Pavilion x360 Convertible 15-ba000 ~ 15-ba099 | follows | Feb. 9 2018
| HP Pavilion x360 Convertible 15-br000 ~ 15-br099 | follows | Feb. 9 2018
| HP Pavilion x360 Convertible 15-br1xx, 15t-br100 | follows | Feb. 9 2018
| HP Pavilion x360 m1 Convertible | follows | Feb. 9 2018
| HP Slimline 270-p0xx Desktop PC | follows | Feb. 9 2018
| HP Slimline 450-axx Desktop PC | follows | Feb. 9 2018
| HP Spectre 13-h200 ~ 13-h299 x2 | follows | Feb. 9 2018
| HP Spectre 13t-h200 | follows | Feb. 9 2018
| HP Spectre 15-ch0xx | follows | Feb. 9 2018
| HP Spectre Laptop 13-af0xx, 13-af5xx, 13t-af000, 13t-af500 | follows | Feb. 9 2018
| HP Spectre Notebook 13-v000 ~ 13-v099 | follows | Feb. 9 2018
| HP Spectre Pro x360 G2 | follows | Feb. 9 2018
| HP Spectre x2 Detachable Convertible | follows | Feb. 9 2018
| HP Spectre x360 Convertible 13 13-w000 ~ 13-w099 | follows | Feb. 9 2018
| HP Spectre x360 Convertible 13-4000 ~ 13-4099 (Intel) | follows | Feb. 9 2018
| HP Spectre x360 Convertible 13-ac000 ~ 13-ac099 | follows | Feb. 9 2018
| HP Spectre x360 Convertible 15-ap000 ~ 15-ap099 (Intel) | follows | Feb. 9 2018
| HP Spectre x360 Convertible 15-bl000 ~ 15-bl099 | follows | Feb. 9 2018
| HP Stream 11 Pro G4 EE | follows | Feb. 9 2018
| HP Stream 11-y0XX | follows | Feb. 9 2018
| HP Stream 14 Pro G3 | follows | Feb. 9 2018
| HP Stream 14-ax0XX | follows | Feb. 9 2018
| HP Stream Mini Desktop 200-0xx | follows | Feb. 9 2018
| HP TouchSmart 15-n100~199 | follows | Feb. 9 2018
| OMEN by HP Laptop 15-ax200 ~ 15-ax299 | follows | Feb. 9 2018
| OMEN by HP Laptop 15-ce000 ~ 15-ce099 | follows | Feb. 9 2018
| OMEN by HP Laptop 17-w200 ~ 17-w299 | follows | Feb. 9 2018
| OMEN X by HP 900-2xx | follows | Feb. 9 2018
| OMEN X by HP Laptop 17-ap000 ~ 17-ap099 | follows | Feb. 9 2018
| Star Wars™ Special Edition 15-an000-an099 | follows | Feb. 9 2018
| Star Wars™ Special Edition 15t-an000 | follows | Feb. 9 2018

# HPE
| model | latest BIOS | release date | vulnerabilities mitigated ? |
| --- | --- | --- | --- |
| ProLiant ML10 Gen8 server | follows | | |
| ProLiant ML310e Gen8 server | follows | | |
| ProLiant MicroServer Gen8 | J06 | 2015/02/11 | no |
| ProLiant XL260a Gen9 server | follows | | |
| HPE Synergy 620 Gen9 Compute Modules | follows | | |
| HPE Synergy 680 Gen9 Compute Modules | follows | | |
| ProLiant Thin Micro TM200 | follows | | |
| ProLiant m510 Server Cartridge | follows | | |
| ProLiant m300 Server Cartridge | follows | | |
| ProLiant m350 Server Cartridge | follows | | |
| ProLiant DL160 Gen8 | follows | | |
| ProLiant DL320e Gen8 | follows | | |
| ProLiant DL360e Gen8 | follows | | |
| ProLiant DL360p Gen8 | follows | | |
| ProLiant DL380e Gen8 | follows | | |
| ProLiant DL380p Gen8 | follows | | |
| ProLiant DL560 Gen8 | follows | | |
| ProLiant DL580 Gen8 | follows | | |
| ProLiant ML350e Gen8 | follows | | |
| ProLiant ML350p Gen8 | follows | | |
| ProLiant SL230s Gen8 | follows | | |
| ProLiant SL250s Gen8 | follows | | |
| ProLiant SL270s Gen8 | follows | | |
| ProLiant BL420c Gen8 | follows | | |
| ProLiant BL460c Gen8 | follows | | |
| ProLiant BL660c Gen8 | follows | | |
| ProLiant SL210t Gen8 | follows | | |
| ProLiant XL230a Gen9 | follows | | |
| ProLiant XL250a gen9 | follows | | |
| ProLiant XL170r Gen9 | follows | | |
| ProLiant XL190r Gen9 | follows | | |
| ProLiant DL60 Gen9 | follows | | |
| ProLiant DL80 Gen9 | follows | | |
| ProLiant XL730f Gen9 | follows | | |
| ProLiant XL740f Gen9 | follows | | |
| ProLiant XL750f Gen9 | follows | | |
| Apollo 4200 Gen9 | follows | | |
| ProLiant DL160 Gen9 | follows | | |
| ProLiant DL180 Gen9 | follows | | |
| ProLiant XL450 Gen9 | follows | | |
| ProLiant XL270d Accelerator Tray | follows | | |
| ProLiant DL560 Gen9 | follows | | |
| ProLiant DL120 Gen9 | follows | | |
| ProLiant DL360 Gen9 | follows | | |
| ProLiant DL380 Gen9 | follows | | |
| ProLiant ML350 Gen9 | follows | | |
| ProLiant ML150 Gen9 | follows | | |
| ProLiant m710 p server cartridge | follows | | |
| ProLiant m710 server cartridge | follows | | |
| ProLiant ML310e Gen8 server | follows | | |
| ProLiant DL320e Gen8 server | follows | | |
| ProLiant ML10 v2 | follows | | |
| ProLiant XL220a Gen8 v2 | follows | | |

# MSI
| model | latest BIOS | release date | vulnerabilities mitigated ? |
| --- | --- | --- | --- |
| Z270 PC MATE | E7a72IMS.180 | ? | yes (not verified) |
| Z370 Godlike Gaming | 7A98vA3 | ? | no |
| Z370 Gaming M5 | 7B58v12 | ? | no |
| Z370 Gaming Pro Carbon AC | 7B45vA3 | ? | no |
| Z370 Gaming Pro Carbon | 7B45vA3 | ? | no |
| Z370I Gaming Pro Carbon AC | 7B43v12 | ? | no |
| Z370 Krait Gaming | 7B46v12 | ? | no |
| Z370 Gaming Plus | 7B61v12 | ? | no |
| Z370 Tomahawk | 7B47v12 | ? | no |
| Z370M Gaming Pro AC | 7B44v12 | ? | no |
| Z370 SLI Plus | 7B46vA2 | ? | no |
| Z370 Godlike Gaming | 7A98vA3 | ? | no
| Z370 Gaming M5 | 7B58v12 | ? | no
| Z370 Gaming Pro Carbon AC | 7B45vA3 | ? | no
| Z370 Gaming Pro Carbon | 7B45vA3 | ? | no
| Z370I Gaming Pro Carbon AC | 7B43v12 | ? | no
| Z370 Krait Gaming | 7B46v12 | ? | no
| Z370 Gaming Plus | 7B61v12 | ? | no
| Z370 Tomahawk | 7B47v12 | ? | no
| Z370M Gaming Pro AC | 7B44v12 | ? | no
| Z370 SLI Plus | 7B46vA2 | ? | no
| Z370-A Pro | 7B48v23 | ? | no
| Z370 PC Pro | 7B49v12 | ? | no
| Z370-A Pro | 7B48v23 | ? | no |
| Z370 PC Pro | 7B49v12 | ? | no |
| Z77A-G43 (MS-7758) | 2.13 | 2014/05/01 | no |

# Vendor links

ASUS: https://www.asus.com/News/YQ3Cr4OYKdZTwnQK

Dell: http://www.dell.com/support/article/us/en/04/sln308587/microprocessor-side-channel-vulnerabilities-cve-2017-5715-cve-2017-5753-cve-2017-5754-impact-on-dell-products?lang=en#Dell_Products_Affected

HPE: https://support.hpe.com/hpsc/doc/public/display?docId=emr_na-a00039267en_us

HP: https://support.hp.com/us-en/document/c05869091

MSI: https://www.hardwareluxx.de/index.php/news/hardware/mainboards/45408-meltdown-asus-und-msi-stellen-bios-updates-fuer-z370-mainboards-bereit.html
