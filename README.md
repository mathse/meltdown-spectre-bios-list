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
| B9940UA | 308 | 2017/11/09 | no |
| Prime Z370-A | 0606 | ? | yes |
| Prime Z370-P | 0606 | ? | yes |
| ROG Maximus X Apex | follows | ? | |
| ROG Maximus X Code | follows | ? | |
| ROG Maximus X Formula | follows | ? | |
| ROG Maximus X Hero | follows | ? | |
| ROG Maximus X Hero (Wi-Fi AC) | follows | ? | |
| ROG Strix Z370-E Gaming | 0606 | ? | yes |
| ROG Strix Z370-F Gaming | 0606 | ? | yes |
| ROG Strix Z370-G Gaming | 0606 | ? | yes |
| ROG Strix Z370-G Gaming (Wi-Fi AC) | 0606 | ? | yes |
| ROG Strix Z370-H Gaming | follows | ? | |
| ROG Strix Z370-I Gaming | 0606 | ? | yes |
| TUF Z370-Plus Gaming | 0606 | ? | yes |
| TUF Z370-Pro Gaming | follows | ? | |

# Dell
| model | latest BIOS | release date | vulnerabilities mitigated ? |
| --- | --- | --- | --- |
| Alienware 13 R2 | follows | 1/19/2018 |
| Alienware 13 R3 | 1.2.3 | ? | yes
| Alienware 15 R2 | follows | 1/19/2018
| Alienware 15 R3 | 1.2.3 | ? | yes
| Alienware 17 R2 | follows | 1/19/2018
| Alienware 17 R4 | 1.2.3 | ? | yes
| Alienware Area-51 R2 | follows | ? |
| Alienware Area-51 R4 | follows | 1/19/2018
| Alienware Area-51 R5 | follows | 1/19/2018
| Alienware Aurora R5 | follows | 1/19/2018
| Alienware Aurora R6 | 1.0.12 | ? | yes
| Alienware Aurora R7 | follows | 1/31/2018
| Alienware Steam Machine 200 | 2.0.10
| Alienware Steam Machine 201 | 1.0.11
| Alienware X51 R3 | 1.0.11 | ? | yes
| ChengMing 3967 | 1.2.2 | ? | yes
| ChengMing 3977 | 1.3.2 | ? | yes
| Dell Embedded Box PC 3000 | follows | In Process
| Edge Gateway 3000 series | follows | In Process
| Edge Gateway 5000 (Commercial) | follows | In Process
| Edge Gateway 5100 (Industrial) | follows | In Process
| Embedded Box PC 5000 | 1.4.2 | ? | yes
| Enterprise Server T20 | A15 | ? | yes
| Enterprise Server T30 | 1.0.12 | ? | yes
| Inspiron 11 (3137) SFX Platform  | follows | In Process
| Inspiron 11 (3153) | 1.18.2 | ? | yes
| Inspiron 11 (3158) | 1.18.2 | ? | yes
| Inspiron 11 (3162)  | follows | In Process
| Inspiron 11 (3164) | follows | In Process
| Inspiron 11 (3168) | follows | In Process
| Inspiron 13 2-in-1 (5368) | 1.15.2 | ? | yes
| Inspiron 13 2-in-1 (5378) | 1.22.3 | ? | yes
| Inspiron 13 2-in-1 (5379) | 1.3.2 | ? | yes
| Inspiron 13 2-in-1 (7378) | 1.22.3 | ? | yes
| Inspiron 14 (3467) | 2.1.3 | ? | yes
| Inspiron 14 (5439) | follows | In Process
| Inspiron 14 (3468) | 1.8.3 | ? | yes
| Inspiron 14 (5468) | 1.4.2 | ? | yes
| Inspiron 14 (7437) | follows | In Process
| Inspiron 14 (7460) | 1.4.2 | ? | yes
| Inspiron 14 (7466) | 1.2.1 | ? | yes
| Inspiron 14 (7467) | 1.4.0 | ? | yes
| Inspiron 15 (3567) | 2.1.3 | ? | yes
| Inspiron 15 (3568) | 1.8.3 | ? | yes
| Inspiron 15 (5566) | 1.4.2 | ? | yes
| Inspiron 15 (5567) | 1.1.9 | ? | yes
| Inspiron 15 (7537) | follows | In Process
| Inspiron 15 (7560) | 1.4.2 | ? | yes
| Inspiron 15 (7566) | 1.2.1 | ? | yes
| Inspiron 15 (7567) | 1.4.0 | ? | yes
| Inspiron 15 2-in-1 (5568) | 1.15.2 | ? | yes
| Inspiron 15 2-in-1 (5578) | 1.22.3 | ? | yes
| Inspiron 15 2-in-1 (5579) | 1.3.2 | ? | yes
| Inspiron 15 2-in-1 (7569) | 1.15.2 | ? | yes
| Inspiron 15 2-in-1 (7579) | 1.22.3 | ? | yes
| Inspiron 15R (5537) | follows | In Process
| Inspiron 17 (5767) | 1.1.9 | ? | yes
| Inspiron 17 (7737) | follows | In Process
| Inspiron 17 2-in-1 (7773) | 1.3.2 | ? | yes
| Inspiron 17 2-in-1 (7778) | 1.15.2 | ? | yes
| Inspiron 17 2-in-1 (7779) | 1.22.3 | ? | yes
| Inspiron 17R (5737) | follows | In Process
| Inspiron 20 (3064) | 2.2.2 | ? | yes
| Inspiron 20 AIO (3059) | follows | 1/19/2018
| Inspiron 22 (3263) | 1.7.0 | ? | yes
| Inspiron 22 AIO (3263) | 1.7.0 | ? | yes
| Inspiron 22 AIO (3264) | 2.2.2 | ? | yes
| Inspiron 23 (5348) | A09 | ? | yes
| Inspiron 2350 | follows | In Process
| Inspiron 24 (3459) | follows | 1/19/2018
| Inspiron 24 AIO (3464) | 2.2.2 | ? | yes
| Inspiron 24 AIO (5459) | 2.8.0 | ? | yes
| Inspiron 24 AIO (5488) | 2.4.2 | ? | yes
| Inspiron 3052 | follows | In Process
| Inspiron 3147 | follows | In Process
| Inspiron 3148 | follows | In Process
| Inspiron 3169 | 1.4.0 | ? | yes
| Inspiron 3179 | 1.3.3 | ? | yes
| Inspiron 3250 | 3.5.2 | ? | yes
| Inspiron 3252 | follows | In Process
| Inspiron 3268 | 1.6.0 | ? | yes
| Inspiron 3452 | follows | In Process
| Inspiron 3458 | follows | In Process
| Inspiron 3459 | 1.5.3 | ? | yes
| Inspiron 3462 | follows | 1/19/2018
| Inspiron 3476 | follows | 1/19/2018
| Inspiron 3537 | follows | In Process
| Inspiron 3558 | follows | In Process
| Inspiron 3559 | 1.5.3 | ? | yes
| Inspiron 3576 | follows | 1/19/2018
| Inspiron 3650 | 3.5.2 | ? | yes
| Inspiron 3662 | 2.5.0 | ? | yes
| Inspiron 3668 | 1.6.0 | ? | yes
| Inspiron 3737 | follows | In Process
| Inspiron 5370 | 1.3.1 | ? | yes
| Inspiron 5442 | follows | In Process
| Inspiron 5447 | follows | In Process
| Inspiron 5452 | follows | In Process
| Inspiron 5457 | 1.3.2 | ? | yes
| Inspiron 5458 | follows | In Process
| Inspiron 5459 | 1.4.1 | ? | yes
| Inspiron 5542 | follows | In Process
| Inspiron 5547 | follows | In Process
| Inspiron 5552 | follows | In Process
| Inspiron 5557 | 1.3.2 | ? | yes
| Inspiron 5558 | follows | In Process
| Inspiron 5559 | 1.4.1 | ? | yes
| Inspiron 5570 | 1.0.9 | ? | yes
| Inspiron 5577 | 1.0.8 | ? | yes
| Inspiron 5758 | follows | In Process
| Inspiron 5759 | 1.4.1 | ? | yes
| Inspiron 5770 | 1.0.9 | ? | yes
| Inspiron 7347 | follows | In Process
| Inspiron 7348 2-in-1 | follows | In Process
| Inspiron 7353 | 1.18.2 | ? | yes
| Inspiron 7359 | 1.18.2 | ? | yes
| Inspiron 7370 | 1.5.4 | ? | yes
| Inspiron 7373 | 1.5.4 | ? | yes
| Inspiron 7459 | 1.7.1 | ? | yes
| Inspiron 7472 | 1.1.0 | ? | yes
| Inspiron 7559 | 1.2.7 | ? | yes
| Inspiron 7568 | 1.18.2 | ? | yes
| Inspiron 7570 | 1.5.4 | ? | yes
| Inspiron 7572 | 1.1.0 | ? | yes
| Inspiron 7573 | 1.5.4 | ? | yes
| Inspiron 7577 | 1.3.2 | ? | yes
| Latitude 3150 | follows | In Process
| Latitude 3160 | follows | In Process
| Latitude 3180 | follows | 1/18/2018
| Latitude 3189 | follows | 1/18/2018
| Latitude 3330 | follows | In Process
| Latitude 3340 | A15 | 1/12/2018 | yes
| Latitude 3350 | A12 | ? | yes
| Latitude 3379 | 1.0.21 | ? | yes
| Latitude 3380 | 1.3.5 | ? | yes
| Latitude 3390 2-in-1 | follows | 1/18/2018
| Latitude 3450 | A15 | ? | yes
| Latitude 3460 | A12 | ? | yes
| Latitude 3470 | 1.10.1 | ? | yes
| Latitude 3480 | 1.5.5 | ? | yes
| Latitude 3490 | follows | 1/19/2018
| Latitude 3540 | follows | In Process
| Latitude 3550 | A15 | ? | yes
| Latitude 3560 | A12 | ? | yes
| Latitude 3570 | 1.10.1 | ? | yes
| Latitude 3580 | 1.5.5 | ? | yes
| Latitude 3590 | follows | 1/19/2018
| Latitude 5175 | 1.0.29 | ? | yes
| Latitude 5179 | 1.0.29 | ? | yes
| Latitude 5280 | 1.8.1 | ? | yes
| Latitude 5285 | 1.3.1 | ? | yes
| Latitude 5288 | 1.8.1 | ? | yes
| Latitude 5289 | 1.10.1 | ? | yes
| Latitude 5290 | 1.1.7 | ? | yes
| Latitude 5290 2-in-1 | 1.1.0 | ? | yes
| Latitude 5404 | follows | 1/19/2018
| Latitude 5414 | 1.15.0 | ? | yes
| Latitude 5480 | 1.8.1 | ? | yes
| Latitude 5488 | 1.8.1 | ? | yes
| Latitude 5490 | 1.1.7 | ? | yes
| Latitude 5580 | 1.8.1 | ? | yes
| Latitude 5590 | 1.1.7 | ? | yes
| Latitude 7202 | follows | 1/19/2018
| Latitude 7204 | follows | 1/19/2018
| Latitude 7212 | 1.7.0 | ? | yes
| Latitude 7214 | 1.15.0 | ? | yes
| Latitude 7275 | 1.1.34 | ? | yes
| Latitude 7280 | 1.8.1 | ? | yes
| Latitude 7285 | 1.1.0 | ? | yes
| Latitude 7290 | 1.2.6 | ? | yes
| Latitude 7350 | A14 | ? | yes
| Latitude 7370 | 1.15.3 | ? | yes
| Latitude 7380 | 1.8.1 | ? | yes
| Latitude 7389 | 1.10.1 | ? | yes
| Latitude 7390 | 1.2.6 | ? | yes
| Latitude 7390 2-in-1 | 1.1.3 | ? | yes
| Latitude 7404 | follows | 1/19/2018
| Latitude 7414 | 1.15.0 | ? | yes
| Latitude 7480 | 1.8.1 | ? | yes
| Latitude 7490 | 1.2.6 | ? | yes
| Latitude E5250 | A18 | ? | yes
| Latitude E5270 | 1.18.6 | ? | yes
| Latitude E5430 | follows | 2/7/2018
| Latitude E5430 vPro | follows | 2/7/2018
| Latitude E5440 | A19 | ? | yes
| Latitude E5450 | A18 | ? | yes
| Latitude E5470 | 1.18.6 | ? | yes
| Latitude E5530 | follows | 2/7/2018
| Latitude E5530 vPro | follows | 2/7/2018
| Latitude E5540 | A19 | ? | yes
| Latitude E5550 | A18 | ? | yes
| Latitude E5570 | 1.18.6 | ? | yes
| Latitude E6230 | follows | 2/7/2018
| Latitude E6330 | follows | 2/7/2018
| Latitude E6430 | follows | 2/7/2018
| Latitude E6430 ATG | follows | 2/7/2018
| Latitude E6430S | follows | 2/7/2018
| Latitude E6430U | follows | 2/7/2018
| Latitude E6440 | A19 | ? | yes
| Latitude E6440 ATG | follows | 1/31/2018
| Latitude E6530 | follows | 2/7/2018
| Latitude E6540 | A22 | ? | yes
| Latitude E7240 | A23 | ? | yes
| Latitude E7250 | A18 | ? | yes
| Latitude E7270 | 1.18.5 | ? | yes
| Latitude E7440 | A23 | ? | yes
| Latitude E7450 | A18 | ? | yes
| Latitude E7470 | 1.18.5 | ? | yes
| OptiPlex 3010 | follows | 1/19/2018
| OptiPlex 3011 AIO | follows | 1/19/2018
| OptiPlex 3020 | A16 | 1/11/2018 | yes (verified)
| OptiPlex 3020M | A11 | ? | yes
| OptiPlex 3030 | follows | 1/19/2018
| OptiPlex 3040 | 1.6.1 | 2018/01/09 | yes |
| OptiPlex 3046 | 1.3.1 | ? | yes
| OptiPlex 3050 | 1.7.7 | ? | yes
| OptiPlex 3050 AIO | 1.8.1 | ? | yes
| OptiPlex 3240 AIO | 1.5.21 | ? | yes
| OptiPlex 5040 | 1.8.1 | ? | yes
| OptiPlex 5050 | 1.7.7 | ? | yes
| OptiPlex 5250 | 1.8.1 | ? | yes
| OptiPlex 7010 | A26 | 2018/01/09 | not verified |
| OptiPlex 7020 | A14 | ? | yes
| OptiPlex 7040 | 1.8.1 | ? | yes
| OptiPlex 7050 | 1.7.7 | 1/9/2018 | yes (verified)
| OptiPlex 7440 AIO | 1.8.6 | ? | yes
| OptiPlex 7450 | 1.8.1 | ? | yes
| OptiPlex 9010 | A27 | ? | yes
| OptiPlex 9010 AIO | follows | 1/19/2018
| OptiPlex 9020 | A21 | ? | yes
| OptiPlex 9020 AIO | A16 | ? | yes
| OptiPlex 9020M | A15 | ? | yes
| OptiPlex 9030 | follows | 1/19/2018
| OptiPlex XE2 | A21 | ? | yes
| Precision 3420 Tower | 2.6.1 | ? | yes
| Precision 3510 | 1.18.6 | ? | yes
| Precision 3520 | 1.8.1 | ? | yes
| Precision 3620 Tower | 2.6.1 | ? | yes
| Precision 5510 | 1.6.1 | ? | yes
| Precision 5520 | 1.7.0 | ? | yes
| Precision 5720 AIO | 2.3.3 | ? | yes
| Precision 5810 Tower | A24 | ? | yes
| Precision 5810 XL Tower | A24 | ? | yes
| Precision 5820 XL Tower | 1.2.1 | ? | yes
| Precision 7510 | 1.15.3 | ? | yes
| Precision 7520 | 1.9.0 | ? | yes
| Precision 7710 | 1.15.3 | ? | yes
| Precision 7720 | 1.9.0 | ? | yes
| Precision 7810 Tower | A24 | ? | yes
| Precision 7810 XL Tower | A24 | ? | yes
| Precision 7820 Tower | 1.2.2 | ? | yes
| Precision 7910 Tower | A24 | ? | yes
| Precision 7910 XL Tower | A24 | ? | yes
| Precision 7920 Tower | 1.2.2 | ? | yes
| Precision M2800 | A12 | ? | yes
| Precision M4700 | follows | 2/7/2018
| Precision M4800 | A21 | ? | yes
| Precision M6700 | follows | 2/7/2018
| Precision M6800 | A21 | ? | yes
| Precision R7610 | A15 | ? | yes
| Precision Rack 7910 | 2.7.0 | ? | yes
| Precision T1650 | A25 | ? | yes
| Precision T1700 | A24 | ? | yes
| Precision T3610 | A15 | ? | yes
| Precision T5610 | A15 | ? | yes
| Precision T7610 | A15 | ? | yes
| Venue 11 Pro (5130-32Bit) | follows | In Process
| Venue 11 Pro (5130-64Bit) | follows | In Process
| Venue 11 Pro (7130) | A24 | ? | yes
| Venue 11 Pro (7130) MS | follows | In Process
| Venue 11 Pro (7140) | A14 | ? | yes
| Vostro 14 (3459) | 1.3.1 | ? | yes
| Vostro 14 (3468) | 2.1.5 | ? | yes
| Vostro 14 (5468) | 1.4.2 | ? | yes
| Vostro 14 (5470) | follows | In Process
| Vostro 15 (3559) | 1.3.1 | ? | yes
| Vostro 15 (3568) | 2.1.5 | ? | yes
| Vostro 15 (5568) | 1.4.2 | ? | yes
| Vostro 23 (3340) | A07 | ? | yes
| Vostro 24 (5450) | 2.8.0 | ? | yes
| Vostro 24 (5460 Kaby Lake) | 2.4.2
| Vostro 24 (5460) | 1.4.0 | ? | yes
| Vostro 3052 | follows | In Process
| Vostro 3250 | 3.5.2 | ? | yes
| Vostro 3252 | follows | In Process
| Vostro 3267 | 1.6.0 | ? | yes
| Vostro 3268 | 1.6.0 | ? | yes
| Vostro 3458 | follows | In Process
| Vostro 3558 | follows | In Process
| Vostro 3562 | follows | 1/19/2018
| Vostro 3650 | 3.5.2 | ? | yes
| Vostro 3653 | 3.5.2 | ? | yes
| Vostro 3660 | 1.6.0 | ? | yes
| Vostro 3667 | 1.6.0 | ? | yes
| Vostro 3668 | 1.6.0 | ? | yes
| Vostro 3669 | 1.6.0 | ? | yes
| Vostro 5370 | 1.3.1 | ? | yes
| Vostro 5459 | 1.1.3 | ? | yes
| Vostro 5471 | 1.3.1 | ? | yes
| Vostro 5560 | follows | In Process
| Vostro 7570 | 1.3.2 | ? | yes
| XPS 12 (9250) | 1.1.34 | ? | yes
| XPS 13 (9343) | follows | 1/19/2018
| XPS 13 (9350) | 1.6.1 | ? | yes
| XPS 13 (9360) | 2.5.0 | ? | yes
| XPS 13 (9370) | 1.1.3 | ? | yes
| XPS 13 2-in-1 (9365) | 1.2.1 | ? | yes
| XPS 15 (9550) | 1.6.1 | ? | yes
| XPS 15 (9560) | 1.7.0 | ? | yes
| XPS 27 AIO (7760) | 2.3.3 | ? | yes
| XPS 8900 | 2.2.1 | ? | yes
| XPS 8910 | follows | 1/19/2018
| XPS 8920 | 1.0.12 | ? | yes
| XPS 8930 | follows | 1/31/2018

# HP
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
| Z370 Godlike Gaming | 7A98vA3 | ? | yes |
| Z370 Gaming M5 | 7B58v12 | ? | yes |
| Z370 Gaming Pro Carbon AC | 7B45vA3 | ? | yes |
| Z370 Gaming Pro Carbon | 7B45vA3 | ? | yes |
| Z370I Gaming Pro Carbon AC | 7B43v12 | ? | yes |
| Z370 Krait Gaming | 7B46v12 | ? | yes |
| Z370 Gaming Plus | 7B61v12 | ? | yes |
| Z370 Tomahawk | 7B47v12 | ? | yes |
| Z370M Gaming Pro AC | 7B44v12 | ? | yes |
| Z370 SLI Plus | 7B46vA2 | ? | yes |
| Z370 Godlike Gaming | 7A98vA3 | ? | yes
| Z370 Gaming M5 | 7B58v12 | ? | yes
| Z370 Gaming Pro Carbon AC | 7B45vA3 | ? | yes
| Z370 Gaming Pro Carbon | 7B45vA3 | ? | yes
| Z370I Gaming Pro Carbon AC | 7B43v12 | ? | yes
| Z370 Krait Gaming | 7B46v12 | ? | yes
| Z370 Gaming Plus | 7B61v12 | ? | yes
| Z370 Tomahawk | 7B47v12 | ? | yes
| Z370M Gaming Pro AC | 7B44v12 | ? | yes
| Z370 SLI Plus | 7B46vA2 | ? | yes
| Z370-A Pro | 7B48v23 | ? | yes
| Z370 PC Pro | 7B49v12 | ? | yes
| Z370-A Pro | 7B48v23 | ? | yes |
| Z370 PC Pro | 7B49v12 | ? | yes |
| Z77A-G43 (MS-7758) | 2.13 | 2014/05/01 | no |

# Vendor links

ASUS: ?

Dell: http://www.dell.com/support/article/us/en/04/sln308587/microprocessor-side-channel-vulnerabilities-cve-2017-5715-cve-2017-5753-cve-2017-5754-impact-on-dell-products?lang=en#Dell_Products_Affected

HP: https://support.hpe.com/hpsc/doc/public/display?docId=emr_na-a00039267en_us

MSI: https://www.hardwareluxx.de/index.php/news/hardware/mainboards/45408-meltdown-asus-und-msi-stellen-bios-updates-fuer-z370-mainboards-bereit.html
