EESchema Schematic File Version 2
LIBS:power
LIBS:device
LIBS:transistors
LIBS:conn
LIBS:linear
LIBS:regul
LIBS:74xx
LIBS:cmos4000
LIBS:adc-dac
LIBS:memory
LIBS:xilinx
LIBS:microcontrollers
LIBS:dsp
LIBS:microchip
LIBS:analog_switches
LIBS:motorola
LIBS:texas
LIBS:intel
LIBS:audio
LIBS:interface
LIBS:digital-audio
LIBS:philips
LIBS:display
LIBS:cypress
LIBS:siliconi
LIBS:opto
LIBS:atmel
LIBS:contrib
LIBS:valves
LIBS:stm32
LIBS:maxim
LIBS:lm75
LIBS:tpd4s012
LIBS:ap1509
LIBS:device_big
LIBS:SeeedOPL-Resistor-2016
LIBS:SeeedOPL-Connector-2016
LIBS:SeeedOPL-Inductor-2016
LIBS:SeeedOPL-Display-2016
LIBS:interface-cache
EELAYER 25 0
EELAYER END
$Descr A4 11693 8268
encoding utf-8
Sheet 2 7
Title ""
Date ""
Rev ""
Comp ""
Comment1 ""
Comment2 ""
Comment3 ""
Comment4 ""
$EndDescr
$Comp
L GND #PWR01
U 1 1 59C40584
P 6600 4750
F 0 "#PWR01" H 6600 4500 50  0001 C CNN
F 1 "GND" H 6600 4600 50  0000 C CNN
F 2 "" H 6600 4750 50  0000 C CNN
F 3 "" H 6600 4750 50  0000 C CNN
	1    6600 4750
	1    0    0    -1  
$EndComp
Wire Wire Line
	6600 2000 6600 3450
$Comp
L +3.3V #PWR02
U 1 1 59C4084E
P 6600 2000
F 0 "#PWR02" H 6600 1850 50  0001 C CNN
F 1 "+3.3V" H 6600 2140 50  0000 C CNN
F 2 "" H 6600 2000 50  0000 C CNN
F 3 "" H 6600 2000 50  0000 C CNN
	1    6600 2000
	1    0    0    -1  
$EndComp
$Comp
L C C1
U 1 1 59C40861
P 6950 2200
F 0 "C1" H 6975 2300 50  0000 L CNN
F 1 "0.1uF" H 6975 2100 50  0000 L CNN
F 2 "Capacitors_SMD:C_0402" H 6988 2050 50  0001 C CNN
F 3 "" H 6950 2200 50  0000 C CNN
	1    6950 2200
	0    1    1    0   
$EndComp
Wire Wire Line
	6600 2200 6800 2200
Connection ~ 6600 2200
Wire Wire Line
	7100 2200 7350 2200
Wire Wire Line
	7350 2200 7350 2400
$Comp
L GND #PWR03
U 1 1 59C408FB
P 7350 2400
F 0 "#PWR03" H 7350 2150 50  0001 C CNN
F 1 "GND" H 7350 2250 50  0000 C CNN
F 2 "" H 7350 2400 50  0000 C CNN
F 3 "" H 7350 2400 50  0000 C CNN
	1    7350 2400
	1    0    0    -1  
$EndComp
Wire Wire Line
	3600 3350 4750 3350
Wire Wire Line
	3600 3550 5150 3550
Wire Wire Line
	3600 3750 4750 3750
Text HLabel 3600 3250 0    59   Input ~ 0
SD_SPI_CS
Text HLabel 3600 3350 0    59   Input ~ 0
SD_SPI_MOSI
Text HLabel 3600 3550 0    59   Input ~ 0
SD_SPI_SCK
Text HLabel 3600 3750 0    59   Output ~ 0
SD_SPI_MISO
Text Notes 7150 6800 0    118  ~ 0
Sodalord Interface - SD Card
$Comp
L TEST_1P W1
U 1 1 59C77C66
P 3800 2750
F 0 "W1" H 3800 3020 50  0000 C CNN
F 1 "CS" H 3800 2950 50  0000 C CNN
F 2 "" H 4000 2750 50  0001 C CNN
F 3 "" H 4000 2750 50  0000 C CNN
	1    3800 2750
	1    0    0    -1  
$EndComp
$Comp
L TEST_1P W2
U 1 1 59C77CEC
P 4000 2750
F 0 "W2" H 4000 3020 50  0000 C CNN
F 1 "MOSI" H 4000 2950 50  0000 C CNN
F 2 "" H 4200 2750 50  0001 C CNN
F 3 "" H 4200 2750 50  0000 C CNN
	1    4000 2750
	1    0    0    -1  
$EndComp
$Comp
L TEST_1P W3
U 1 1 59C77D12
P 4200 2750
F 0 "W3" H 4200 3020 50  0000 C CNN
F 1 "SCK" H 4200 2950 50  0000 C CNN
F 2 "" H 4400 2750 50  0001 C CNN
F 3 "" H 4400 2750 50  0000 C CNN
	1    4200 2750
	1    0    0    -1  
$EndComp
$Comp
L TEST_1P W4
U 1 1 59C77D3B
P 4400 2750
F 0 "W4" H 4400 3020 50  0000 C CNN
F 1 "MISO" H 4400 2950 50  0000 C CNN
F 2 "" H 4600 2750 50  0001 C CNN
F 3 "" H 4600 2750 50  0000 C CNN
	1    4400 2750
	1    0    0    -1  
$EndComp
Connection ~ 3800 3250
Wire Wire Line
	4000 2750 4000 3350
Connection ~ 4000 3350
Wire Wire Line
	4200 2750 4200 3550
Connection ~ 4200 3550
Wire Wire Line
	4400 2750 4400 3750
Connection ~ 4400 3750
$Comp
L R R4
U 1 1 59C78021
P 5300 3250
F 0 "R4" V 5380 3250 50  0000 C CNN
F 1 "22" V 5300 3250 50  0000 C CNN
F 2 "" V 5230 3250 50  0001 C CNN
F 3 "" H 5300 3250 50  0000 C CNN
	1    5300 3250
	0    1    1    0   
$EndComp
Wire Wire Line
	3600 3250 5150 3250
Wire Wire Line
	5450 3250 6900 3250
$Comp
L R R2
U 1 1 59C7824A
P 4900 3350
F 0 "R2" V 4980 3350 50  0000 C CNN
F 1 "22" V 4900 3350 50  0000 C CNN
F 2 "" V 4830 3350 50  0001 C CNN
F 3 "" H 4900 3350 50  0000 C CNN
	1    4900 3350
	0    1    1    0   
$EndComp
$Comp
L R R5
U 1 1 59C782AC
P 5300 3550
F 0 "R5" V 5380 3550 50  0000 C CNN
F 1 "22" V 5300 3550 50  0000 C CNN
F 2 "" V 5230 3550 50  0001 C CNN
F 3 "" H 5300 3550 50  0000 C CNN
	1    5300 3550
	0    1    1    0   
$EndComp
$Comp
L R R3
U 1 1 59C782F5
P 4900 3750
F 0 "R3" V 4980 3750 50  0000 C CNN
F 1 "22" V 4900 3750 50  0000 C CNN
F 2 "" V 4830 3750 50  0001 C CNN
F 3 "" H 4900 3750 50  0000 C CNN
	1    4900 3750
	0    1    1    0   
$EndComp
Wire Wire Line
	5050 3350 6900 3350
Wire Wire Line
	5450 3550 6900 3550
Wire Wire Line
	5050 3750 6900 3750
Wire Wire Line
	2300 6300 2800 6300
Wire Wire Line
	3800 2750 3800 3250
Text Label 2300 6300 0    59   ~ 0
SD_SPI_CS
$Comp
L GND #PWR04
U 1 1 59C789EB
P 3100 6600
F 0 "#PWR04" H 3100 6350 50  0001 C CNN
F 1 "GND" H 3100 6450 50  0000 C CNN
F 2 "" H 3100 6600 50  0000 C CNN
F 3 "" H 3100 6600 50  0000 C CNN
	1    3100 6600
	1    0    0    -1  
$EndComp
Wire Wire Line
	3100 6450 3100 6600
Wire Wire Line
	3100 6050 3100 6000
$Comp
L LED D1
U 1 1 59C78A89
P 3100 5800
F 0 "D1" H 3100 5900 50  0000 C CNN
F 1 "ACTIVITY" H 3100 5700 50  0000 C CNN
F 2 "LEDs:LED_0603" H 3100 5800 50  0001 C CNN
F 3 "" H 3100 5800 50  0000 C CNN
	1    3100 5800
	0    -1   -1   0   
$EndComp
$Comp
L R R1
U 1 1 59C78B1A
P 3100 5450
F 0 "R1" V 3180 5450 50  0000 C CNN
F 1 "330" V 3100 5450 50  0000 C CNN
F 2 "" V 3030 5450 50  0001 C CNN
F 3 "" H 3100 5450 50  0000 C CNN
	1    3100 5450
	-1   0    0    1   
$EndComp
$Comp
L +3.3V #PWR05
U 1 1 59C78BD3
P 3100 5300
F 0 "#PWR05" H 3100 5150 50  0001 C CNN
F 1 "+3.3V" H 3100 5440 50  0000 C CNN
F 2 "" H 3100 5300 50  0000 C CNN
F 3 "" H 3100 5300 50  0000 C CNN
	1    3100 5300
	1    0    0    -1  
$EndComp
$Comp
L MMBF170 Q1
U 1 1 59C7C007
P 3000 6250
F 0 "Q1" H 3200 6325 50  0000 L CNN
F 1 "MMBF170" H 3200 6250 50  0000 L CNN
F 2 "TO_SOT_Packages_SMD:SOT-23" H 3200 6175 50  0000 L CIN
F 3 "" H 3000 6250 50  0000 L CNN
	1    3000 6250
	1    0    0    -1  
$EndComp
$Comp
L MICRO-SD-CARD-SOCKET-9P_ST-TF-003A_ SD1
U 1 1 59C9BC84
P 7600 3550
F 0 "SD1" H 7050 4050 45  0000 L BNN
F 1 "MICRO_SD" H 7400 3000 45  0000 L BNN
F 2 "" H 7600 3550 79  0001 C CNN
F 3 "" H 7600 3550 79  0000 C CNN
F 4 "ST-TF-003A" H 7630 3700 20  0001 C CNN "MPN"
F 5 "320090000" H 7630 3700 20  0001 C CNN "SKU"
	1    7600 3550
	1    0    0    -1  
$EndComp
Text Notes 7050 4550 0    59   ~ 0
Seeed SKU 320090000
Wire Wire Line
	7900 4200 7900 4350
Wire Wire Line
	7900 4350 8400 4350
Wire Wire Line
	8000 4350 8000 4200
Wire Wire Line
	7900 2800 7900 2650
Wire Wire Line
	7900 2650 8400 2650
Wire Wire Line
	8000 2650 8000 2800
Wire Wire Line
	8400 2650 8400 4750
Connection ~ 8000 2650
Connection ~ 8400 4350
Connection ~ 8000 4350
$Comp
L GND #PWR06
U 1 1 59C9C2DA
P 8400 4750
F 0 "#PWR06" H 8400 4500 50  0001 C CNN
F 1 "GND" H 8400 4600 50  0000 C CNN
F 2 "" H 8400 4750 50  0000 C CNN
F 3 "" H 8400 4750 50  0000 C CNN
	1    8400 4750
	1    0    0    -1  
$EndComp
Wire Wire Line
	6900 3650 6600 3650
Wire Wire Line
	6600 3650 6600 4750
Wire Wire Line
	6600 3450 6900 3450
NoConn ~ 6900 3150
NoConn ~ 6900 3850
Wire Wire Line
	3600 3950 6900 3950
Text HLabel 3600 3950 0    59   Output ~ 0
SD_CARD_DET_L
$Comp
L R R6
U 1 1 59C9C9B8
P 6050 2500
F 0 "R6" V 6130 2500 50  0000 C CNN
F 1 "10K" V 6050 2500 50  0000 C CNN
F 2 "" V 5980 2500 50  0001 C CNN
F 3 "" H 6050 2500 50  0000 C CNN
	1    6050 2500
	-1   0    0    1   
$EndComp
Wire Wire Line
	6050 2650 6050 3950
Connection ~ 6050 3950
Wire Wire Line
	6050 2350 6050 2000
$Comp
L +3.3V #PWR07
U 1 1 59C9CAF7
P 6050 2000
F 0 "#PWR07" H 6050 1850 50  0001 C CNN
F 1 "+3.3V" H 6050 2140 50  0000 C CNN
F 2 "" H 6050 2000 50  0000 C CNN
F 3 "" H 6050 2000 50  0000 C CNN
	1    6050 2000
	1    0    0    -1  
$EndComp
$Comp
L TEST_1P W5
U 1 1 59C9CB5D
P 5600 2750
F 0 "W5" H 5600 3020 50  0000 C CNN
F 1 "CD" H 5600 2950 50  0000 C CNN
F 2 "" H 5800 2750 50  0001 C CNN
F 3 "" H 5800 2750 50  0000 C CNN
	1    5600 2750
	1    0    0    -1  
$EndComp
Wire Wire Line
	5600 2750 5600 2900
Wire Wire Line
	5600 2900 6050 2900
Connection ~ 6050 2900
$EndSCHEMATC
