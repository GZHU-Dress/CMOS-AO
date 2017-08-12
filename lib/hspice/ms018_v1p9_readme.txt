*** SMIC SPICE model for 0.18um Mixed Signal 1.8V/3.3V 1P6M process ***
*** For HSPICE only ***

1. Update History:

           V0.1: Initiate
           V0.2: a. All MOS (1.8V N/P & 3.3V N/P & native 1.8V/3.3V) parameters were re-extracted due to minor process change. 
                 b. Revise interconnect table in section 7.6
                 c. Revise resistor model.
                 d. Revise BJT & diode model.
                 e. Re-new all of content
           V1.0: Add Technology Develop Revision 1.0
           V1.1: a. Add 1.8V and 3.3V thin_oxide medium device model to 7.2.2 E, F and 7.8.2 E, F and 7.8.3 A, B, C, D, E 
                    and 7.8.5 A3 and update the model card.          
                 b. Add 3.3V BJT model cards and update BJT model at 7.3.1, add 3.3V BJT GDS files in attachment files. 
                 c. Revise all the .txt, .mdl and .lib files in attachment.
           V1.2: a. Add noise model parameter table for 1.8V/3.3V native MOSFETs in section 7.2.4E page 55.
                 b. Revised resistor macro model parameters table in section 7.6 page 65,which include jc1a,
                    jc1b, jc2a, jc2b, rint1, rinttc1, rinttc2, rintjc1a, rintjc1b, rintjc2a and rintjc2b,
                    to provide more accurate resistor model.
                 Attachment files change description:
                 a. Revised "MS018_fit_C.doc", "MS018_fit_D.doc", "MS018_fit_G.doc" for native diode model,
                    resistor macro model, and native MOS 1/f noise model, respectively.
                 b. Updated "MS018_v1p2_res.mdl", "MS018_v1p2_res.ckt", "MS018_v1p2_res_spe.mdl",
                    "MS018_v1p2_res_spe.ckt" for resistor and MIM capacitor model.
                 c. Add "res.def" for resistor simulation by Spectre.
                 d. Revised "MS018_v1p2.mdl" and "MS018_v1p2_spe.mdl" for native diode  and 1/f native MOS model.
                 e. Revised "MS018_v1p2.lib", "MS018_v1p2_spe.lib" and separated into four model files
                    ("MS018_v1p2.mdl" and "MS018_v1p2_res.mdl" for HSPICE, "MS018_v1p2_spe.mdl" and 
                    "MS018_v1p2_res_spe.mdl" for Spectre, respectively ) to provide the individual corner model
                    for MOSFETs and resistors.
                 f. Revised readme file for model card usage.
           V1.3: a. Added non-standard (with LDD) SAB resistor model in section7.6.
                 b. Added Isub parameters for all types MOSFETs in MOS model.
                 c. NLEV=3 replaced NLEV=2 in HSPICE format for 1/f MOS noise model.
                 d. Separated MIM capacitance model from resistor model, and generated "ms018_v1p3_mim.mdl" 
                    and "ms018_v1p3_mim_spe.mdl" for MIM.
                 e. Revised 3.3V PNP BJT model parameters in BJT model.
                 f. Added BJT corner model in section7.3.2 and revised BJT model format, please
                    refer to "ms018_v1p3_bjt.mdl" for HSPICE, "ms018_v1p3_bjt_spe.mdl" for Spectre, respectively.
                 g. Updated fitting plots "MS018_fit_B1.doc" and "MS018_fit_D.doc" for BJT and resistor model.
                 h. Revised PNP BJT gds files.
                 i. Revised readme files for model card usage.
           V1.4: Slightly modified a few parameters to fix MOIN warning message for 1.8V and 3.3V NMOS, 1.8V and 
                 3.3V native MOS, 1.8V and 3.3V medium NMOS model, so we have revised section 7.2.3, section 7.8.2, 
                 section 7.8.3 and section 7.8.4.
           V1.5: Add thin oxide N+poly/NW MOS varactor model.
           V1.6: Updated RC_N+, RC_P+, RC_N+Poly, RC_P+Poly and RC_Via PCM SPEC in document file Resistance Table (section 7.6) .
           V1.7: Main document file change description:
                 a. Updated corner table in the section 7.2.2.
                 b. Updated noise model in the section 7.2.4.
                 c. Updated resistance table in the section 7.6.
                 d. Updated pcm spec comparison table in the section 7.9.3.
                 Attachment files change description:
                 a. Centered the model of N18, P18, N33, P33, NT18, NT33, NMVT18, PMVT18 and NMVT33 to match the PCM SPEC in í—ms018_v1p7.mdlí˜.
                 b. Revised the corner for N18, P18, N33, P33, NT18, NT33, NMVT18, PMVT18 and NMVT33 to match the PCM SPEC in í—ms018_v1p7.libí˜. 
                 c. Updated N18, P18, N33, P33, NNT18, NNT33 HSPICE noise parameter to BSIM noise parameter in í—ms018_v1p7.mdlí˜.
                 d. Added 3T poly resistor model and centered the resistor model to match the PCM SPEC in í—ms018_v1p7_res.mdlí˜, í—ms018_v1p7_res.cktí˜.
                 e. Revised the corner for the resistor model to match the PCM SPEC in í—ms018_v1p7.libí˜.
                 f. Added Eldo format model card.
                 g. Updated í—MS018_fit_A1.docí˜, í—MS018_fit_D.docí˜, í—MS018_fit_F.docí˜, and  í—MS018_fit_G.docí˜.
           V1.8: Main document file change description:
                 a. Updated the typical values of contact and via's resistance in section 7.6.
                 b. Updated 1.8V N+poly/NW MOS varactor model in section 7.8.1.
                 c. Added 3.3V N+poly/NW MOS varactor model in section 7.8.2.
                 d. Added reference documents in page.6.
                 Attachment files change description:
                 a. Revised N+poly/NW MOS varactor model in the files of "ms018_v1p8_res.ckt","ms018_v1p8_res_spe.ckt"and "ms018_v1p8_res_eldo.ckt".
                 b. Revised the parameters of CJC and CJE in the files "ms018_v1p8_bjt.mdl", "ms018_v1p8_bjt_spe.mdl" and "ms018_v1p8_bjt_eldo.mdl".
                 c. Revised the corner parameters of DCJC and DCJE inthe files "ms018_v1p8.lib", "ms018_v1p8_spe.lib" and "ms018_v1p8_eldo.lib".
                 d. Added N+poly/NW MOS varactor corner model in the files of "ms018_v1p8.lib", "ms018_v1p8_spe.lib" and "ms018_v1p8_eldo.lib".
                 e. Revised the readme files of "ms018_v1p8_readme.txt", "ms018_v1p8_readme_spe.txt"and"ms018_v1p8_readme_eldo.txt".
                 f. Changed resistors macro model 'res.def' to 'res.va'.
                 g. Revised the parameter definition of í—temperí˜ to directly expression to avoid the limitation of simulator in the files í—ms018_v1p8_res.cktí˜ and í—ms018_v1p8_res_eldo.cktí˜.
                 h. Revised all model card files to version 1.8.

           V1.9: a.Revised all model card files to version 1.9.
                 b.Included Monte Carlo statistical model for MOSFETs SPICE model by modifying í«ms018_v1p9.lib'
		 c.Added Monte Carlo Statistical model in section 7.2.3 of the main document.
		 d.Included Monte Carlo model uses in the read me files í«ms018_v1p9_readme.txt'
2. Files:

      	      	ms018_v1p9_readme.txt             	.... This file!
      	      	ms018_v1p9.mdl                    	.... Model parameters file for N/PMOS and diode
  	      	ms018_v1p9.lib                    	.... Corner values for N/PMOS, BJT, resistors, MIM capacitors and varactor
      	      	ms018_v1p9_res.mdl                	.... Model parameters file for resistors       
	      	ms018_v1p9_res.ckt                	.... Resistor, MIM capacitor and varactor macro model
	      	ms018_v1p9_bjt.mdl                	.... Model parameters file BJT
	      	ms018_v1p9_mim.mdl                	.... Model parameters file MIM capacitors
	      	ms018_v1p9_interconnect_struct_1.txt    .... Interconnect tables for structure-1 (Parallel lines above a bottom plate)
	      	ms018_v1p9_interconnect_struct_2.txt    .... Interconnect tables for structure-2 (Parallel lines between two plates)
	      	MS018_fit_A1.pdf                  	.... Section A1 of the fitting plots for 0.18um Mixed Signal model
	      	MS018_fit_A2.pdf                  	.... Section A2 of the fitting plots for 0.18um Mixed Signal model
	      	MS018_fit_A3.pdf                  	.... Section A3 of the fitting plots for 0.18um Mixed Signal model
	      	MS018_fit_B1.pdf                  	.... Section B1 of the fitting plots for 0.18um Mixed Signal model
	      	MS018_fit_B2.pdf                  	.... Section B2 of the fitting plots for 0.18um Mixed Signal model
	      	MS018_fit_C.pdf                   	.... Section C of the fitting plots for 0.18um Mixed Signal model
	      	MS018_fit_D.pdf                   	.... Section D of the fitting plots for 0.18um Mixed Signal model
	      	MS018_fit_E.pdf                   	.... Section E of the fitting plots for 0.18um Mixed Signal model
	      	MS018_fit_F.pdf                   	.... Section F of the fitting plots for 0.18um Mixed Signal model
	      	MS018_fit_G.pdf                   	.... Section G of the fitting plots for 0.18um Mixed Signal model
	      	MS018_layer.map                  	.... GDSII layers definition file
	      	PNP18a100.gds                     	.... GDSII file for 1.8V BJT PNP 10X10
	      	PNP18a25.gds                      	.... GDSII file for 1.8V BJT PNP 5X5
	      	PNP18a4.gds                       	.... GDSII file for 1.8V BJT PNP 2X2
	      	PNP33a100.gds                     	.... GDSII file for 3.3V BJT PNP 10X10
	      	PNP33a25.gds                      	.... GDSII file for 3.3V BJT PNP 5X5
	      	PNP33a4.gds                       	.... GDSII file for 3.3V BJT PNP 2X2
	     	NPN18a100.gds                     	.... GDSII file for 1.8V BJT NPN 10X10
	      	NPN18a25.gds                      	.... GDSII file for 1.8V BJT NPN 5X5
	      	NPN18a4.gds                      	.... GDSII file for 1.8V BJT NPN 2X2
	      	NPN33a100.gds                     	.... GDSII file for 3.3V BJT NPN 10X10
	      	NPN33a25.gds                      	.... GDSII file for 3.3V BJT NPN 5X5
	      	NPN33a4.gds                       	.... GDSII file for 3.3V BJT NPN 2X2
	      	DIO_NPW18.gds                     	.... GDSII file for 1.8V Diode N+/Pwell
	      	DIO_PNW18.gds                     	.... GDSII file for 1.8V Diode P+/Nwell
	      	DIO_NPW33.gds                     	.... GDSII file for 3.3V Diode N+/Pwell
	      	DIO_PNW33.gds                     	.... GDSII file for 3.3V Diode P+/Nwell
	      	DIO_NWPW.gds                      	.... GDSII file for Diode Nwell/Pwell
	      	DIO_NNPW18.gds                    	.... GDSII file for 1.8V Native Diode N+/Pwell
	      	DIO_NNPW33.gds                    	.... GDSII file for 3.3V Native Diode N+/Pwell
	      	DIO_BPWDNW.gds                    	.... GDSII file for Diode Buried Pwell/Deep Nwell
	
3. How to use SMIC SPICE models in HSPICE:

      Add the following statements to HSPICE netlist.
      
      a. Specify MOS, BJT, diode, resistor, MIM corner and model by the '.lib' statement;

         .lib '/xxx/xxx/ms018_v1p9.lib' TT
                                        ^^ mos model corner

         .lib '/xxx/xxx/ms018_v1p9.lib' MC
                                        ^^ mos monte carlo statistical model


         .lib '/xxx/xxx/ms018_v1p9.lib' BJT_TT
                                            ^^ bjt model corner

         .lib '/xxx/xxx/ms018_v1p9.lib' RES_TT
                                            ^^ resistor model corner

         .lib '/xxx/xxx/ms018_v1p9.lib' MIM_TT
                                            ^^ mim model corner

      b. Call resistor and MIM macro model subcircuit by the following statement;

         .include '/xxx/xxx/ms018_v1p9_res.ckt'
         
         .lib '/xxx/xxx/ms018_v1p9.lib' TT
                                        ^^ mos model corner

         .lib '/xxx/xxx/ms018_v1p9.lib' RES_TT
                                            ^^ resistor model corner

         .lib '/xxx/xxx/ms018_v1p9.lib' MIM_TT
                                            ^^ mim model corner

          
         then add the following statement in your netlist to define subcircuit condition 
         you want to simulate. 
         e.g. 
             * nwell resistor under STI        
               X1  rnw_ckt w=1u l=1u
             * mim capacitor
               X2  mim_ckt w=30u l=30u

         Note: For metal resistor, don't need to use the subcircuit file 
               '/xxx/xxx/ms018_v1p9_res.ckt'.
                      
         Where /xxx/xxx is the directory where mdl and lib files are located.
         
      c. Call N+poly/NW MOS varactor model by the following statement;

         .include '/xxx/xxx/ms018_v1p9_res.ckt'
         
         .lib '/xxx/xxx/ms018_v1p9.lib' VAR_TT
                                            ^^ varactor model corner
         
         then add the following statement in your netlist to define subcircuit condition
         you want to simulate.
         
         e.g. XCKT 1 2 pvar18_ckt lr=1u wr=10u nf=10 
  
4. The Capability of Model

            a. MOS Model

            *-----------------------------------------------* 
            |     MOSFET type    |  name  |  Lmin  |  Wmin  |
            |--------------------------------------|--------|
            |       1.8V NMOS    |   n18  | 0.18um | 0.22um |
            *--------------------------------------*--------|
            |       1.8V PMOS    |   p18  | 0.18um | 0.22um |
            *--------------------------------------*--------|
            |  1.8V Native NMOS  |  nnt18 | 0.5um  | 0.22um |
            *--------------------------------------*--------|
            |  1.8V Medium NMOS  | nmvt18 | 0.3um  | 0.22um |
            *--------------------------------------*--------|
            |  1.8V Medium PMOS  | pmvt18 | 0.25um | 0.22um |
            *--------------------------------------*--------|
            |       3.3V NMOS    |   n33  | 0.35um | 0.22um |
            *--------------------------------------*--------|
            |       3.3V PMOS    |   p33  | 0.3um  | 0.22um |
            *--------------------------------------*--------|
            |  3.3V Native NMOS  |  nnt33 | 1.2um  | 0.22um |
            *--------------------------------------*--------|
            |  3.3V Medium NMOS  | nmvt33 | 0.6um  | 0.22um |
            *--------------------------------------*--------|
            temperature range:-40C~125C

            b. BJT Model

            *---------------------------------------------------* 
            |      BJT type     |     name      |  Emitter Area |
            |===================================================|
            |   1.8V PNP_10X10  |   pnp18a100   |   10*10 um^2  |
            *---------------------------------------------------*  
            |   1.8V PNP_5X5    |   pnp18a25    |   5*5 um^2    |
            *---------------------------------------------------* 
            |   1.8V PNP_2X2    |   pnp18a4     |   2*2 um^2    |
            *---------------------------------------------------* 
            |   1.8V NPN_10X10  |   NPN18a100   |   10*10 um^2  |
            *---------------------------------------------------*  
            |   1.8V NPN_5X5    |   NPN18a25    |   5*5 um^2    |
            *---------------------------------------------------* 
            |   1.8V NPN_2X2    |   NPN18a4     |   2*2 um^2    |
            *---------------------------------------------------* 
            |   3.3V PNP_10X10  |   pnp33a100   |   10*10 um^2  |
            *---------------------------------------------------*  
            |   3.3V PNP_5X5    |   pnp33a25    |   5*5 um^2    |
            *---------------------------------------------------* 
            |   3.3V PNP_2X2    |   pnp33a4     |   2*2 um^2    |
            *---------------------------------------------------* 
            |   3.3V NPN_10X10  |   NPN33a100   |   10*10 um^2  |
            *---------------------------------------------------*  
            |   3.3V NPN_5X5    |   NPN33a25    |   5*5 um^2    |
            *---------------------------------------------------* 
            |   3.3V NPN_2X2    |   NPN33a4     |   2*2 um^2    |
            *---------------------------------------------------* 
            temperature range:-40C~125C

           c. Diode Model
   
           *--------------------------------------------* 
           |   Diode type           |  name  |  Area    |
           |============================================| 
           |     1.8V  N+/PWELL     | ndio18 |60*60um^2 |
           |--------------------------------------------|
           |     1.8V  P+/NWELL     | pdio18 |60*60um^2 |
           |--------------------------------------------|
           |      NWELL/PSUB        | nwdio  |80*120um^2|
           |--------------------------------------------|      
           |  1.8V Native N+/PWELL  | nndio18|60*60um^2 |
           |--------------------------------------------|
           |     3.3V  N+/PWELL     | ndio33 |60*60um^2 |
           |--------------------------------------------|
           |     3.3V  P+/NWELL     | pdio33 |60*60um^2 |
           |--------------------------------------------|      
           |  3.3V Native N+/PWELL  | nndio33|60*60um^2 |
           |--------------------------------------------|
           | Buried PWELL/Deep NWELL| diobpw |80*120um^2|
           *--------------------------------------------*
           temperature range: -40C~125C

           d. Resistor Model

        *----------------------------------------------------------------------* 
        |             Resistor Type                            | 1.8V/3.3V     |
        |======================================================|===============|
        |        Silicide N+ Diffusion                         |    rndif      |
        |------------------------------------------------------|---------------| 
        |        Silicide P+ Diffusion                         |    rpdif      |
        |------------------------------------------------------|---------------| 
        |           Silicide N+ Poly                           |     rnpo      |
        |----------------------------------------------------  |---------------| 
        |           Silicide N+ Poly(three terminal)           |    rnpo_3t    |
        |------------------------------------------------------|---------------| 
        |           Silicide P+ Poly                           |     rppo      |
        |------------------------------------------------------|---------------| 
        |           Silicide P+ Poly(three terminal)           |    rppo_3t    |
        |------------------------------------------------------|---------------|
        |        Silicide Nwell under AA                       |    rnwaa      |
        |------------------------------------------------------|---------------| 
        |        Silicide Nwell under STI                      |    rnwsti     |
        |------------------------------------------------------|---------------|
        |        Non-Silicide N+ Diffusion                     |   rndifsab    |
        |------------------------------------------------------|---------------| 
        | Non-Silicide N+ Diffusion (non-standard)             | rndifsab_nstd | 
        |------------------------------------------------------|---------------| 
        |        Non-Silicide P+ Diffusion                     |   rpdifsab    |
        |------------------------------------------------------|---------------|
        | Non-Silicide P+ Diffusion (non-standard)             | rpdifsab_nstd | 
        |------------------------------------------------------|---------------| 
        |          Non-Silicide N+ Poly                        |   rnposab     |
        |------------------------------------------------------|---------------| 
        |          Non-Silicide N+ Poly(three terminal)        |   rnposab_3t  |
        |------------------------------------------------------|---------------|
        |   Non-Silicide N+ Poly (non-standard)                | rnposab_nstd  |
        |------------------------------------------------------|---------------|
        |   Non-Silicide N+ Poly (non-standard)(three terminal)|rnposab_nstd_3t|
        |------------------------------------------------------|---------------| 
        |          Non-Silicide P+ Poly                        |   rpposab     |
        |------------------------------------------------------|---------------| 
        |          Non-Silicide P+ Poly(three terminal)        |  rpposab_3t   |
        |------------------------------------------------------|---------------|
        |   Non-Silicide P+ Poly (non-standard)                | rpposab_nstd  |
        |------------------------------------------------------|---------------|
        |   Non-Silicide P+ Poly (non-standard)(three terminal)|rpposab_nstd_3t|  
        |------------------------------------------------------|---------------|
        |        High Resistance Poly                          |     rhrpo     |
        |------------------------------------------------------|---------------| 
        |        High Resistance Poly(three terminal)          |    rhrpo_3t   |
        |------------------------------------------------------|---------------| 
        |                  Metal 1                             |      rm1      |
        |------------------------------------------------------|---------------| 
        |                  Metal 2                             |      rm2      |
        |------------------------------------------------------|---------------| 
        |                  Metal 3                             |      rm3      |
        |------------------------------------------------------|---------------|  
        |                  Metal 4                             |      rm4      |
        |------------------------------------------------------|---------------| 
        |                  Metal 5                             |      rm5      |
        |------------------------------------------------------|---------------| 
        |                  Metal 6                             |      rm6      |
        *----------------------------------------------------------------------* 

           temperature range:-40C~125C
           For more detailed information, please refer to the main document in section 7.6.

           e. MIM capacitor Model
           capacitor name    : mim 
           temperature range : -55C~125C

           f. 1.8V and 3.3V N+poly/NW MOS varactor model
           temperature range:-40C~125C


5. Corner Model

   Five model corners are provided for MOSFETs, 
   three model corners are provided for BJT, 
   three model corners are provided for resistors, 
   three model corners are provided for MIM capacitors.
   three model corners are provided for varactor.

   They are

      ----------------------------------------------------
      MOS          name : corner
      ----------------------------------------------------
                     TT : Typical case 
                     SS : Slow case
                     FF : Fast case
                   SNFP : Slow N Fast P case 
                   FNSP : Fast N Slow P case 
      ----------------------------------------------------
      BJT          name : corner
      ----------------------------------------------------
                 BJT_TT : Typical case
                 BJT_SS : Slow case
                 BJT_FF : Fast case 
      ----------------------------------------------------
      Resistor     name : corner
      ----------------------------------------------------
                 RES_TT : Typical case
                 RES_SS : Slow case
                 RES_FF : Fast case 
      ----------------------------------------------------
      MIM          name : corner
      ----------------------------------------------------
                 MIM_TT : Typical case
                 MIM_SS : Slow case
                 MIM_FF : Fast case 
      ----------------------------------------------------
      Varactor     name : corner
      ----------------------------------------------------
                 VAR_TT : Typical case
                 VAR_SS : Slow case
                 VAR_FF : Fast case 
      ----------------------------------------------------
  
6. Monte Carlo Statistical model
   Demo netlist
------------------------------------------------------------
|*SMIC model verification
|.options itl5=0 measdgt=5 post=2 nomod ingold=2
|.lib 'ms018_v1p9.lib' mc
|.temp 25
|* assume source at 0
|vg1 g1 0 1.8
|vd1 d1 0 1.8
|vd2 d2 0 1.8
|vb b 0 0
|m1 d1 g1 0 b n18 w=10u l=0.18u
|.dc  sweep  monte=500
|.print dc  id1=i(vd1)
|.end
---------------------------------------------------------------
