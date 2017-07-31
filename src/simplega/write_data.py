# coding=utf-8

import os
import re
import time


root = os.getcwd()
path = root + '/src/simplega/'

title = """************************************************************************
* auCdl Netlist:
*
* Library Name: ZX_LDO
* Top Cell Name: opamp2_LDO_3
* View Name: schematic
* Netlisted on: %s
************************************************************************

*.EQUATION
*.SCALE METER
*.MEGA
.PARAM



************************************************************************
* Library Name: ZX_LDO
* Cell Name: opamp2_LDO_Cq
* View Name: schematic
************************************************************************

.SUBCKT opamp2_LDO_Cq_mf GND IB VDD VOUT VREF VT VAC
*.PININFO VREF:I VOUT:O GND:B IB:B VDD:B VT:B
CCq VG net29 .6p
CCm net21 VOUT 1.p
CCL VOUT GND 100p
RR1 net49 GND 50k
RR0 VOUT net49 60k
*CC VG GND -1.9p
*CC1 VDD VG 10P
*CC2 VDD VOUT -20.5p""" % time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

end = '.ENDS'


data = [['MPM5', 100.0, 2.0],
        ['*MNMF', 3.0, 1.0],
        ['MPM6', 4.0, 1.0],
        ['MPM0', 18.0, 1.0],
        ['MPM2', 4.0, 1.0],
        ['MPM1', 4.0, 1.0],
        ['MNM1', 2.0, 7.0],
        ['MNM0', 2.0, 7.0],
        ['MNM3', 6.0, 2.0],
        ['MNM2', 3.0, 2.0],
        ['MPM4', 20.0, 1.0],
        ['MPM3', 5.0, 1.0]]  # test

example = """MPM5 VOUT VG VDD VDD p18 W=%su L=.2u M=35
*MNMF VOUT net21 GND GND n18 W=3u L=1u M=1
MPM6 IB IB VDD VDD p18 W=4u L=1u M=1
MPM0 net52 IB VDD VDD p18 W=18u L=1u M=1

MPM2 net29 net49 net52 net52 p18 W=4u L=1u M=1
MPM1 net21 VREF net52 net52 p18 W=4u L=1u M=1
MNM1 net29 net29 GND GND n18 W=2u L=7u M=1
MNM0 net21 net29 GND GND n18 W=2u L=7u M=1

MNM3 VG net29 GND GND n18 W=6u L=2u M=1
MNM2 net19 net21 GND GND n18 W=3u L=2.5u M=1
MPM4 VG net19 VDD VDD p18 W=20u L=1u M=1
MPM3 net19 net19 VDD VDD p18 W=5u L=1u M=1""" % data[0][1]

with open(path + 'testlist', 'w+') as f:
    f.write(title + '\n \n%s \n \n' % data + end)
    f.close()
