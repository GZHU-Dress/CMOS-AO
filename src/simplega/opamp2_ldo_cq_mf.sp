*title test

*.lib 'E:\PDK\smic18mmrf_1P6M_200902271315\models\hspice\ms018_v1p9.lib' mc
.lib 'E:\PDK\smic18mmrf_1P6M_200902271315\models\hspice\ms018_v1p9.lib' tt
.lib 'E:\PDK\smic18mmrf_1P6M_200902271315\models\hspice\ms018_v1p9.lib' bjt_tt
.lib 'E:\PDK\smic18mmrf_1P6M_200902271315\models\hspice\ms018_v1p9.lib' res_tt
.lib 'E:\PDK\smic18mmrf_1P6M_200902271315\models\hspice\ms018_v1p9.lib' mim_tt

.temp 27

.option node 
.option list
.option nomod
.option captab
*.options ITLPZ=200
.global GND VDD

.include "netlist"

xtest GND IB VDD VOUT VREF VT VAC opamp2_LDO_Cq_mf
.param IL=100u
VVDD VDD 0 1.2 ac 1
VGND GND 0 0
VVREF VREF 0 0.5 
IIB IB VDD 1u
*L VT VOUT 1G
*C VAC VT 1G
*VVAC VAC 0 ac 1

IIL VOUT GND IL
*IIL VOUT GND PWL(0u 0 10u 0 11u 100m 30u 100m 31u 0 40u 0)
.op

.ac dec 10 1 1000meg 
*SWEEP IIL POI 7 0m 10u 60u 100u 1m 10m 100m
*SWEEP IIL POI 7 0m 10u 100u 1m 10m 50m 100m
.print ac vdb(VOUT) vp(VOUT) i(*)
.pz V(VOUT) VVDD
.tran  0.1u 40u 
.print tran V(VOUT) i(*) ip(*)
.end  