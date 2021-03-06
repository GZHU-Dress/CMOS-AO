*A CMOS OPERATIONAL AMPLIFIER USED IN HIGH GAIN
M1  3  12  4  4  MOD1  W=214U  L=4U
M2  2  1  4  4  MOD1  W=214U  L=4U
M3  4  5  11  11  MOD1  W=52U  L=4U
M4  3  3  10  10  MOD2  W=104U  L=4U
M5  2  3  10  10  MOD2  W=104U  L=4U
M6  6  2  10  10  MOD2  W=50U  L=4U
M7  7  2  10  10  MOD2  W=384U  L=4U
M8  6  5  11  11  MOD1  W=30U  L=4U
M9  7  8  11  11  MOD1  W=66U  L=4U
M10  8  8  11  11  MOD1  W=20U  L=8U
M11  6  6  10  10  MOD2  W=50U  L=4U
M12  8  6  10  10  MOD2  W=50U  L=4U
M13  5  11  10  10  MOD3  W=4U  L=12U
M14  5  5  11  11  MOD1  W=16U  L=4U

.MODEL  MOD1  NMOS  LEVEL=2 VTO=0.8 NSUB=1.17E16 TOX=0.08U 
+CGSO=4E0-11CGDO=4E-11 CGBO=2E-10  UO=383  TPG=1 LAMBDA=0.03
.MODEL  MOD2  PMOS  LEVEL=2  VTO=-0.8  NSUB =6E14 TOX=0.08U 
+CGSO=4E-11 CGDO=4E –1 CGBO=2E- 10   UO=180   TPG= -1
.MODEL  MOD3  PMOS  LEVEL=2  VTO = -0.8   NSUB=6E14  TOX=0.08U 
+CGSO=4E–11 CGDO=4E-11 CGBO=2E-10 UO=180 TPG=-1 LAMBDA=0.02
C  2  7  7PF
VDD  10  0  DC  2.5
VSS  11  0  DC  -2.5
V1  1  12  0.66M
VIN  12  0  AC  0.1
.TF  V(7)  VIN
.AC  DEC  10  1  100MEG
.PRINT  AC  VM(7)
.OPTION  LIMPTS=1000
.END
