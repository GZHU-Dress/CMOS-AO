*title test

.lib '/home/axionl/Documents/CMOS-AO/lib/hspice/ms018_v1p9.lib' tt
.lib '/home/axionl/Documents/CMOS-AO/lib/hspice/ms018_v1p9.lib' bjt_tt
.lib '/home/axionl/Documents/CMOS-AO/lib/hspice/ms018_v1p9.lib' res_tt
.lib '/home/axionl/Documents/CMOS-AO/lib/hspice/ms018_v1p9.lib' mim_tt

.temp 27

.option node
.option list
.option nomod
.option captab
.global GND VDD

.include "netlist"

xtest GND IB VDD VOUT VREF VT VAC opamp2_LDO_Cq_mf
.param IL=100u
VVDD VDD 0 1.2 ac 1
VGND GND 0 0
VVREF VREF 0 0.5
IIB IB VDD 1u


IIL VOUT GND IL
.op

.ac dec 10 1 1000meg
.print ac vdb(VOUT) vp(VOUT) i(*)
* .pz V(VOUT) VVDD
.tran  0.1u 40u
.print tran V(VOUT) i(*) ip(*)
.end
