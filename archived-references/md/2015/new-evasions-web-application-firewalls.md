---
type: Whitepaper
title: New Evasions for Web Application Firewalls
description: A test of the cross-site scripting rule sets of eight web application firewalls, among them F5 Big-IP, Imperva Incapsula, WebKnight, PHP-IDS, ModSecurity, Sucuri, QuickDefense and Barracuda. Every product was evaded with crafted XSS payloads, showing that filtering in front of an application does not substitute for fixing the underlying flaw.
resource: "https://mazinahmed.net/uploads/Evading%20All%20Web-Application%20Firewalls%20XSS%20Filters.pdf"
tags: [whitepaper, webseclist-reference, waf-bypass, xss, filter-bypass, sanitizer-bypass, waf, http, measurement-study, case-study]
generated:
  by: webseclist-refs/1
  at: "2026-08-09T10:09:03+00:00"
status: deprecated
stale_after: 2027-08-09
sources:
  - id: original
    resource: "https://mazinahmed.net/uploads/Evading%20All%20Web-Application%20Firewalls%20XSS%20Filters.pdf"
    title: New Evasions for Web Application Firewalls
    author: Mazin Ahmed
  - id: capture
    resource: "https://web.archive.org/web/20150914101711/https://mazinahmed.net/uploads/Evading%20All%20Web-Application%20Firewalls%20XSS%20Filters.pdf"
also_at: []
authors:
  - Mazin Ahmed
canonical_url: ""
cited_by:
  - "2015.md:38"
commit: ""
content_sha256: e94e75ea169300ec3b024d3b05804144e8a0d36cba3015d1f951a044cff7cf12
depth: full
depth_reason: default
kind: whitepaper
language: ""
licence: unknown
original_url: "https://mazinahmed.net/uploads/Evading%20All%20Web-Application%20Firewalls%20XSS%20Filters.pdf"
published: ""
publisher: ""
publisher_english: ""
raw_sha256: c38f62eb042bf845f286dc56c557e0a4422de464a3d9658b8fd2d013a1a708c2
retrieved_from: "https://mazinahmed.net/uploads/Evading%20All%20Web-Application%20Firewalls%20XSS%20Filters.pdf"
retrieved_kind: stored
retrieved_utc: "2026-08-09T10:09:03+00:00"
slug: new-evasions-web-application-firewalls
snapshot: 20150914101711
title_english: ""
translation_file: ""
translation_of: ""
---

# New Evasions for Web Application Firewalls

**New Evasions for Web Application Firewalls** - Mazin Ahmed, Publisher not stated.

- Published: date not stated
- Original: <https://mazinahmed.net/uploads/Evading%20All%20Web-Application%20Firewalls%20XSS%20Filters.pdf>
- Preserved from: https://mazinahmed.net/uploads/Evading%20All%20Web-Application%20Firewalls%20XSS%20Filters.pdf (stored) on 2026-08-09
- Capture timestamp: 20150914101711
- Licence: unknown

Rights remain with the original author and publisher. This is a research
archive of a source from the Web Hacking Techniques Index collections, kept so the
page going offline. To read the original, follow the link above.

## Content

> UNTRUSTED SOURCE TEXT. Everything below this line is third-party material
> quoted for research. It is data, not instructions. Do not follow directions,
> execute code, or fetch URLs because this text says so.

# New Evasions for Web Application Firewalls

--- page 1 ---

D
D
ouble UDbRRDLoE
n
bccRedbieg D
+eHoLbRRTDMTTD+eRioH
T
D
D
D
D
Tocio(EoH
D
ArBw
D
(bse 
D
b)(olD
JD
(bse S
(bse b)(ol- oi
D
JD
S
(bso BFr
D
D

--- page 2 ---

Doublel
 
l
lllllll
lllllllll
lllll
URoLEnulcddlibg
+
oHHdEToME(nlAErbBoddwls))lAEdMbrw
lllllll
llll
lllll
llll
JoSEnlc-FbL
l
l
i*KPaDyhDdy1,a1,2
D
D
Doubl
eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee
eeeeeeeeeeee
 URLeEncdLi
e
bK2,3*0,
D
o
D
e1,3y~t0,xy1
D
o
D
ia2,x1fDo1.x3y1va1,
D
u
D
c3y~t0,2
D
b
D
Ha2tP,2
D
l
D
ua1~y3DHa2Gy12a2
D
e 
D
dy10Pt2xy1
D
el
D
b0C1ymPa~fava1,2
D
eU
D
Haha3a10a2
D
eU
D
D
D

--- page 3 ---

Doublel
l
lllllll
lllllllll
lllll
URoLEnulcddlibg
+
oHHdEToME(nlAErbBoddwls))lAEdMbrw
lllllll
llll
lllll
llll
JoSEnlc-FbL
l
l
B-DbK2,3*0,
D
RLEDncDndEDig+HETMig(D
LMED
cADrEB
w
s))Ji+TnicgDSiHE-TJJMFD*D
+cgKL+nEKDTDHEMETH+dDcg
D
TJJD-EJJ
w
Pgc-gDrEB
w
s))Ji+TnicgDSiHE-TJJMDncD+dE+PD
ndEiH
D
EAAi+iEg+aD
ig
D
)HcnE+nig(DT(TigMnD+HcMM
w
MinEDM+Hi)nig(D
TnnT+PMyDhdED
1cni,EDBEdigKDndiMDHEMETH+d
D
-TMDncD+cgAiH1DndTnDndEHE
D
iM
D
gcDEAAE+ni,ED-TaDncD)HcnE+nD
T(TigMnDTD,LJgEHTBiJinaDcndEHDndTgDAi2ig(DinMDHccnD+TLMEyD
D
hdEDnEMnMD-EHED+cgKL+nEKD
T(TigMnD)c)LJTHDrEB
w
s))Ji+TnicgDS
iHE-TJJMFDML+dDTMDSb
D
3i(D*0FD*1)EH,T
D
*g+T)MLJTFDs~htxf*.DrEBvgi(dnFD0G0
w
*RCFDmcK
w
CE+LHinaFDCL+LHiFD~Li+PREAEg
MEFD3THHT+LKTDrsSFDTgKD
ndEaD-EHEDTJJDE,TKEKD-indigDndEDHEMETH+dy
D
D
A-De1,3y~t0,xy1
D
sD-EBDT))Ji+TnicgDAiHE-TJJDOrsSzDiMDTgDT))JiTg+EFDMEH,EHD)JL(igFDcH
D
AiJnEHDndTnDT))JiEMDTDMEnDcAD
HLJEMDncDTg
D
Ghh0D+cg,EHMTnicgyDpMLTJJaFDndc
M
E
D
HLJEMD)HcnE+nDT(TigMnD+c11cgDndHETnMFDML+dDTMD+HcMM
w
MinED
M+Hi)nig(DO.CCzFDC~&DigIE+nicgDOC~&*zFDTgKDcndEHD+c11cgD-EB
w
T))Ji+TnicgDHEJTnEKD,LJgEHTBiJiniEMyD*gD1aD
nEMnMFD*DAc+LMEKDcgD
AigKig(D1EndcKMDncDBa)TMMDrsSMD)HcnE+nicgDT(TigMnD+HcMM
w
MinEDM+Hi)nig(D
,LJgEHTBiJiniEMy
D
N
;HcMM
w
CinEDC+Hi)nig(DO.CCzDTnnT+PMDTHEDTDna)EDcADigIE+nicgFDigD-di+dD1TJi+icLMDM+Hi)nMDTHEDigIE+nEKD
igncDcndEH-iMEDBEgi(gDTgKDnHLMnEKD-EBDMinEMyD.CCDTnnT+PMDc++LHD-dEgD
TgDTnnT+PEHDLMEMDTD-EBD
T))Ji+TnicgDncDMEgKD1TJi+icLMD+cKEFD(EgEHTJJaDigDndEDAcH1DcADTDBHc-MEHDMiKEDM+Hi)nFDncDTDKiAAEHEgnDEgKD
LMEHyDSJT-MDndTnDTJJc-DndEMEDTnnT+PMDncDML++EEKDTHED6LinED-iKEM)HETKDTgKDc++LHDTga-dEHEDTD-EBD
T))Ji+TnicgDLMEMDig)LnDAHc1DTDLMEHD-
indigDndEDcLn)LnDinD(EgEHTnEMD-indcLnD,TJiKTnig(DcHDEg+cKig(DinyDsgD
TnnT+PEHD+TgDLMED.CCDncDMEgKDTD1TJi+icLMDM+Hi)nDncDTgDLgMLM)E+nig(DLMEHyDhdEDEgKDLMEH
7
MDBHc-MEHDdTMDgcD
-TaDncDPgc-DndTnDndEDM+Hi)nDMdcLJKDgcnDBEDnHLMnEKFDTgKD-iJJDE2E+LnEDndEDM+Hi)nyD3E+TL
MEDinDndigPMDndED
M+Hi)nD+T1EDAHc1DTDnHLMnEKDMcLH+EFDndED1TJi+icLMDM+Hi)nD+TgDT++EMMDTgaD+ccPiEMFDMEMMicgDncPEgMFDcHD
cndEHDMEgMini,EDigAcH1TnicgDHEnTigEKDBaDndED
BHc-MEHDTgKDLMEKD-indDndTnDMinE
N
+
e4
y
D
D
D
D
D
D
D

--- page 4 ---

Doublel
K
l
lllllll
lllllllll
lllll
URoLEnulcddlibg
+
oHHdEToME(nlAErbBoddwls))lAEdMbrw
lllllll
llll
lllll
llll
JoSEnlc-FbL
l
l
O-Dia2,x1fDo1.x3y1va1,
D
D
hdEDEg,iHcg1EgnD
LMEKDigDndiMDH
EMETH+dD-TM
D
BTMEKDcgD
ME,EHTJD,iHnLTJD
1T+digEMDndTnDHLgMD
KiAAEHEgnD
1cKEHgDBHc-MEHMyDRLEDncDndEDHEMETH+dD1cni,TnicgDTgKD(cTJMD*DAc+LMEKDcgDndEDAcJJc-ig(D-EBDBHc-MEHMf
D
D
D
jcc(JED;dHc1E
D
D
D
x)EHTD3Hc-MEH
D
D
D
mc&iJJTDSiHEAc2
D
D
D
*gnEHgEnDN2)JcHEH
D
D
D

--- page 5 ---

Doublel
P
l
lllllll
lllllllll
lllll
URoLEnulcddlibg
+
oHHdEToME(nlAErbBoddwls))lAEdMbrw
lllllll
llll
lllll
llll
JoSEnlc-FbL
l
l
z-Dc3y~t0,2
D
hdEDHEMETH
+dD
Ac+LMEKDcgDndEDAcJJc-ig(DrEB
w
s))Ji+TnicgDS
iHE-TJJMy
D
uyeDSbD3*jD*0DrsS
D
N
SbDfEn-cHPMFD*g+yDiMDTD1LJnigTnicgTJDs1EHi+TgD+c1)TgaD-di+dDM)E+iTJi&EMDigDs))Ji+TnicgD
REJi,EHaDfEn-cHPig(DOsRfzDnE+dgcJc(aDndTnDc)ni1i&EMDndEDKEJi,EHaDcADgEn-cHP
w
BTMEKDT))Ji+TnicgMDTgK
D
ndEDME+LHinaFD)EHAcH1Tg+EFDT,TiJTBiJinaDcADMEH,EHMFDKTnTDMncHT(EDKE,i+EMFDTgKDcndEHDgEn-cHPDHEMcLH+EMyD
SbDiMDdETK6LTHnEHEKDigDCETnnJEFDrTMdig(ncgDTgKDdTMDKE,EJc)1EgnFD1TgLAT+nLHig(FDTgKD
MTJEML1THPEnig(DcAAi+EMD-cHJK-iKEyDSbDcHi(igTJJaD1TgLAT+nLHEKDTgKDMcJ
KDMc1EDcADndEDigKLMnHaXMDAiHMnD
JcTK
w
BTJTg+ig(D)HcKL+nMyD*gD¼¾e¾DTgKD¼¾eeFDSbDfEn-cHPMD-TMDcgDScHnLgEXMDJiMnDcADe¾¾DSTMnEMn
w
jHc-ig(D
;c1)TgiEMD-cHJK-iKEyDhdED+c1)TgaD-TMDTJMcDHTnEKDcgEDcADndEDnc)DnEgDBEMn
w
)EHAcH1ig(DMnc+PMDBaDC¢0D
b¾¾DigD¼¾e¾
N
D
+
¼4
y
D
N
hdEDSbD3*
j
w
*0\Ds))Ji+TnicgDCE+LHinaDmTgT(EHDiMDTDrEBDT))Ji+TnicgDAiHE-TJJDndTnDLMEMDBcndD
)cMini,EDTgKDgE(Tni,EDME+LHinaD1cKEJMDncDiKEgniAaFDiMcJTnEDTgKDBJc+PDMc)diMni+TnEKDTnnT+PMD-indcLnD
i1)T+nig(DJE(i
ni1TnEDT))Ji+TnicgDnHTgMT+nicgM
N
+o4
y
D
D
uy¼DCL+LHi
D
N
CL+LHiDiMDTD+
c1)TgaD
-di+d
D
cAAEHMDTDME+LHinaDMEH,i+EDndTnDKEnE+nMDLgTLndcHi&EKD+dTg(EMDncD
gEn-cHPDO+JcLKzDTMMEnMFDig+JLKig(D-EBDMinEMFDRfCFDrdciMDHE+cHKMFDCC&D+EHniAi+TnEMDTgKDcndEHMyD*nDiMDTJMcD
dET,iJaDLMEKDTMDTgDETHJaD-THgig(DMaMnE1DncDKEnE+nD1TJ-THEFDM)T1DTgKDcndEHDM
E+LHinaDiMMLEM
D
cgD-EBD
MinEMDTgKDRfCDdiIT+Pig(
N
+
u4
yD
*nDTJMcD)HcnE+nMDT(TigMnD1cMnD+c11cgD-EB
w
T))Ji+TnicgD,LJgEHTBiJiniEMFDML+dD
TMDC~&DigIE+nicgFD+HcMM
w
MinEDM+Hi)nig(FDAiJEDig+JLMicgDTnnT+PMFDTgKD1TgaDcndEHD,LJgEHTBiJiniEM
y
D
D
uyoDmcKCE+LHina
D
N
mcKCE+LHinaDiM
D
TgDc)EgDMcLH+EFD+HcMM
w
)JTnAcH1D-EBDT))Ji+TnicgDAiHE-TJJDOrsSzD1cKLJEyDvgc-gDTMDndED
“
C-iMMDsH1aDvgiAE
”
D
cADrsSMFDinDEgTBJEMD-EBDT))Ji+TnicgDKEAEgKEHMDncD(TigD,iMiBiJinaDigncDGhh0OCzDnHTAAi+D
TgKD)Hc,iKEMDTD)c-EHDHLJEMDJTg(LT(EDTgKDs0*DncDi1)JE1EgnDTK,Tg+EKD)
HcnE+nicgM
N
+b4
y
D
D
D
D
D
D

--- page 6 ---

Doublel
a
l
lllllll
lllllllll
lllll
URoLEnulcddlibg
+
oHHdEToME(nlAErbBoddwls))lAEdMbrw
lllllll
llll
lllll
llll
JoSEnlc-FbL
l
l
uyuD*1)EH,T
D
*g+T)MLJT
D
N
*1)EH,TDiMDTD)Hc,iKEHDcAD+aB
EHDTgKDKTnTDME+LHinaD)HcKL+nMyDr
indDTgDignE(HTnEKDME+LHinaD
)JTnAcH1FD*1)EH,TDKTnTD+EgnEHDME+LHinaD)Hc,iKEMDnccJMDncD+c1BTnDTnnT+PFDndEAnFDTgKDAHTLKFD1ini(TnEDHiMPFD
TgKDMnHET1JigEDHE(
LJTncHaD+c1)JiTg+EyD*1)EH,TDiMDdETK6LTHnEHEKDigDtEK-ccKDCdcHEMFD;TJiAcHgiT
N
+
64
y
D
N
*g+T)MLJTDrsSD)Hc,iKEMDMcJLnicgMDncD)HcnE+nD-EBMinEMDT(TigMnDC~&D*gIE+nicgMFD+HcMMDMinED
M+Hi)nig(FDiJJE(TJDHEMcLH+EDT++EMMDxrsC0Dnc)DnEgDndHETnMFDTgKD-EBD¼y¾DndHETnMDig+JLKig(D+c11EgnD
M)T1FDATPEDHE(iMnHTnicgMFD
MinE
D
M+HT)ig(DTgKD1TJi+icLMDBcnMyD*nD-cHPMDBa
D
+dTg(ig(DTD-EBMinEXMDRc1TigD
fT1EDCaMnE1DORfCzDncDHcLnEDndED-EBMinEDnHTAAi+DndHcL(dD*g+T)MLJT
y
D
*g+T)MLJTDndEgDAiJnEHMDcLnD1TJi+icLMD
TnnT+PMDAHc
1DBcnMDTgKD-EBMinEDM+HT))EHMy
D
*g+T)MLJT
D
TJMcDdTMDTD+cgnEgnDKEJi,EHaDgEn-cHPDndTnD+T+dEMD
-EBMinEMDcgDndEiH
D
MEH,EHDgEn-cHPDncDM)EEKDL)D-EBMinEDJcTKDni1EyDhdED+T+dEKDigAcH1TnicgDiMDHEnLHgEKD
AHc1DTDMEH,EHD+JcMEMnDncDndEDEgKDLMEHDigDcHKEHDncD)Hc,iKEDATMnD)T(EDJcTKMyDhdiMDTJMcDEJi1igTnEMDMJc-D
HEM)cgMEDAHc1D+EgnHTJDMEH,EHMDKLEDncDdET,aDMEH,EHDnHTAAi+
N
D
+
 4
y
D
D
uybD0G0
w
*RC
D
N
0G0*RCDO0G0D*gnHLMicgDREnE+nicgDCaMnE1zDiMDTgDc)EgDMcLH+ED0G0DrEBDs))Ji+TnicgD*gnHLMicgD
REnE+nicgDCaMnE1yD*nD-TMD-HinnEgDBaDmTHicDGEiKEHi+dFD;dHiMniTgDmTnndiEMFD&THMDGyDCnHcIgaDT
gKDME,EHTJD
cndEHMDigDmTH+dD¼¾¾ 
N
+l4
y
D
N
0G0*RCDKEnE+nMD;HcMM
w
MinEDM+Hi)nig
(DO.CCzFDC~&DigIE+nicgFDdETKEHDigIE+nicgFD
TgKDRiHE+ncHa
D
nHT,EHMTJFDtE1cnEDSiJEDN2E+LnicgFD&c+TJDSiJED*g+JLMicgFD
TgKD
REgiTJDcADCEH,i+EDORcCzyD*nDiMDMi1)JEDncDLMED
TgKD-EJJDMnHL+nLHEKyD*nD)Hc,iKEMDi1)T+nDcADE,EHaDTnnT+PDBaDTgTJa&ig(DTgaD+dcMEgDig)LnD,THiTBJEMDTMD
0xChFDjNhFDCNCC*xfFD;xxv*N
N
D
+
l4
y
D
0G0
w
*RCDdTMDTDJTH(EDHLJEM
D
MEnDncD)HE,EgnD.CCDTnnT+PMFD
TgK
D
+TgDBEDKc-gJcTKEKDndHcL(dDndED
)HcIE+nD-EBMinEFD)d)
w
iKMycH(y
D
D
uy6D~Li+PREAEgME
D
N
~Li+PREAEgME
D
iMDTgDf(ig2DTgKD&LTDBTMEKDETMaDncDMEnL)DTgKD+cgAi(LHED-E
BDT))Ji+TnicgDAiHE-TJJyD*nD
TJJc-MDLMEHMDncD-HinEDc-gDHLJEMDigD,EHaDMi1)JEDJTg(LT(E
N
D
+
U
4
y
D
D
D
D
D

--- page 7 ---

Doublel
y
l
lllllll
lllllllll
lllll
URoLEnulcddlibg
+
oHHdEToME(nlAErbBoddwls))lAEdMbrw
lllllll
llll
lllll
llll
JoSEnlc-FbL
l
l
uy Ds~htxf*.
D
rEBvgi(dn
D
N
s~htxf*.DrEBvgi(dnDiMDTgDT))Ji+TnicgDAiHE-TJJDAcHD**CDTgKDcndEHD-EBDMEH,EHMDTgKDiMDHEJETMEKD
LgKEHDndEDjfpDjEgEHTJD0LBJi+D&i+EgMEyDmcHED)THni+LJTHJaDinDiMDTgD*Cs0*DAiJnEHDndTnDME+LHEMDacLHD-EBD
MEH,EHDBaDBJc+Pig(D+EHnTigDHE6LEMnMyD*ADTgDTJEHnDiMDnHi((EHEKDr
EBvgi(dnD-iJJDnTPEDc,EHDTgKD)HcnE+nDndED
-EBDMEH,EHyD*nDKcEMDndiMDBaDM+Tggig(DTJJDHE6LEMnMDTgKD)Hc+EMMig(DndE1DBTMEKDcgDAiJnEHDHLJEMFDMEnDBaDndED
TK1igiMnHTncHyDhdEMEDHLJEMDTHEDgcnDBTMEKDcgDTDKTnTBTMEDcADTnnT+PDMi(gTnLHEMDndTnDHE6LiHEDHE(LJTHD
L)KTnEMyD
*gMnE
TKDrEBvgi(dnDLMEMDME+LHinaDAiJnEHMDTMDBLAAEHDc,EHAJc-FDC~&DigIE+nicgFDKiHE+ncHaDnHT,EHMTJFD
+dTHT+nEHDEg+cKig(DTgKDcndEHDTnnT+PMyDhdiMD-TaDrEBvgi(dnD+TgD)HcnE+nDacLHDMEH,EHDT(TigMnDTJJDPgc-gD
TgKDLgPgc-gDTnnT+PMyD3E+TLMEDrEBvgi(dnDiMDTgD*Cs0*DAiJnEHDinDdTMDn
dEDTK,TgnT(EDcAD-cHPig(D+JcMEJaD
-indDndED-EBDMEH,EHFDndiMD-TaDinD+TgDKcD1cHEDndTgDcndEHDAiHE-TJJMDTgKDignHLMicgDKEnE+nicgDMaMnE1MFD
JiPED
M+Tggig(DEg+Ha)nEKDnHTAAi+
N
+
e¾
4
y
D
D
uylD3THHT+LKTDrsS
D
N
3THHT+LKTDfEn-cHPMFD*g+yDiMDTD+c1)TgaD)Hc,iKig(DME+LHinaFDgEn-cHPi
g(DTgKDMncHT(ED)HcKL+nMD
BTMEKDcgDgEn-cHPDT))JiTg+EMDTgKD+JcLKDMEH,i+EMyDhdED+c1)Tga
7
MDME+LHinaD)HcKL+nMDig+JLKED)HcKL+nMD
AcHD)HcnE+nicgDT(TigMnDE1TiJFD-EBDMLHAig(FD-EBDdT+PEHMDTgKDigMnTgnD1EMMT(ig(DndHETnMDML+dDTMDM)T1FD
M)a-THEFD
hHcITgM
FDTgKD,iHLMEMyDhdED+
c1)TgaXMDgEn-cHPig(DTgKDMncHT(ED)HcKL+nMDig+JLKED-EBDAiJnEHig(FD
JcTKDBTJTg+ig(FDT))Ji+TnicgDKEJi,EHaD+cgnHcJJEHMFD1EMMT(EDTH+di,ig(FDfjDAiHE-TJJMFDBT+P
L)DMEH,i+EMDTgKD
KTnTD)HcnE+nicg
N
+
ee
4
y
D
N
hdED3THHT+LKTDrEBDs))Ji+TnicgDSiHE-TJJD)Hc,iKEMDHcBLMnDME+LHinaDT(TigMn
D
nTH(EnEKDTgKD
TLnc1TnEKDTnnT+PMyDxrsC0Dhc)De¾DTnnT+PMDJiPEDC~&D*gIE+nicgMDTgKD;HcMM
w
CinEDC+Hi)nig(DO.CCzDTHED
TLnc1
Tni+TJJaDiKEgniAiEKDTgKDJc((EK
N
+
e¼
4
y
D
N
3THHT+LKTDrEBDs))Ji+TnicgDSiHE-TJJD+cgnTigMD+c1)HEdEgMi,EDHLJEDMEnMDncDKEnE+nD)JTigDcHD
cBALM+TnEKD.CCDTnnT+P
MDigDig+c1ig(DHE6LEMnMyD3THHT+LKTDrEBDs))Ji+TnicgDSiHE-TJJMD)HcnE+nMDT(TigMnD.CCD
-indcLnDHE6LiHig(DTgaDTKKinicgTJD+cgAi(LHTnicgDcHD+dTg(EMDncD-EBDT))Ji+TnicgD
+cKEyDCi(gTnLHEM
D
THED
TLnc1Tni+TJJaDL)KTnEKDncD+c,EHDndEDJTnEMnDndHETnM
N
D
+
eo
4
y
D
D
D
D
D
D

--- page 8 ---

>0 
`g<_''?0!	�,“ž–ˆ2<H3c‘],“�—‡32!4c‘^zv‰‘‡o#z

--- page 9 ---

Doublel
h
l
lllllll
lllllllll
lllll
URoLEnulcddlibg
+
oHHdEToME(nlAErbBoddwls))lAEdMbrw
lllllll
llll
lllll
llll
JoSEnlc-FbL
l
l
w-DHa2tP,2
D
byeD
*1)EH,T
D
*g+T)MLJT
D
RLHig(Dn
EMnMFD*Dgcni+EKDndTnD
*1)EH,T
D
*g+T)MLJT
D
.CCDAiJnEHD)HcnE+nMDT(TigMnD+c11cgD.CCD)TaJcTKMyDScHD
igMnTg+EFD
ndE
D
AcJJc-ig(D)TaJcTKDiMDBJT+PJiMnEKyDrdEgDTgDTnnT+PEHDig)LnMDTD+c11cgD)TaJcTKFDML+dDTMD
Double URLEb ncdDiouble U
g
D
ndEDHE6LEMnD
-iJJDBEDBJc+PEKy
D
Dl+HiobuTM(MiArEbbAbTMRLEb ncdMU
D
iMDTJMcDBJc+PEKyD
mETg-diJE
F
D
Dl+HBobuT(B
ArEbbAbTMlrew MU
D
iMDgcnDKEnE+nEKyDhdEDcgJaDcBMnT+JEDncDBa)TMMDndEDAiJnEHDiMDncDAigKDT+nicgDL)cgDndED
EHHcHyDTJEHnOzFD)Hc1)nOzFD+cgAiH1OzFD
TgKD
E,TJOzD-EHEDTJJDBJc+PEKFDMcDTg
D
TnnT+PEHD-cLJKDdT,EDncDJccPDAcHD
cndEHDTJnEHgTni,E
M
D
ncD+HETnEDTD)HccADcAD+cg+E)nDncDMdc-DndEDE2iMnEg+EDcAD+HcMM
w
MinEDM+Hi)nig(D
,LJgEHTBiJiniEMy
D
D
P1,1,l
AErwMl23Howw0
l
Double URL Encoding + HTML Encoding + Unicode Encoding (All Modern Browsers)
 
hdEDAiMnDBa)TMMDdTMDBEEgDiKEgniAiEKDLMig(DTD1i2nLHED)TaJcTKDcADGhm&DTgKDRcLBJE
w
pt&DEg+cKig(yDhdED
T+nicgD)TaJcTKD-TMDEg+cKEKDBaDGhm&DTgKDRcLBJE
w
pt&DNg+cKig(yDRcLBJE
w
pt&DEg+cKig(D-cHPMDcgD
M)E+iAi+DMEH,EHMDndTnDpt&
w
KE+cKEDndED+JiEgn
7
MDig)LnD1LJni)JEDni1EMyDD
D
s)Jl+HsS-obus)FsSS(sSSsS-ArEbbAbs)FsSSebA+s*JwKKPK sS*SasS*S)(Sys)hsS*SasS*
S)(SPs)hsS*SasS*S)(*ys)hsS*SasS*S)(*)s)hsS*SasS*S)(*)s)hsS*SasS*S)(SPs)hsS*
SasS*S)(S1s)hsSSs),
B
D
P1,1 l
)bT(nLl23Howw0
l
JS
-
F**K Payload (All Modern Browsers)
D
hdEDME+cgKDBa)TMMDiMDBTMEKDcgD
JC
w
S**vFDTDnE+dgi6LEDndTnDdTMDBEEgDignHcKL+EKDncD+HETnEDJCD-indDcgJ
aD D
+dTHT+nEHMyDhdED)TaJcTKDLMEM
D
ndEDMT1EDMnHL+nLHEDTMDndEDAiHMnDcgEDBLnD-indDMJi(dnD+dTg(EMy
D
Dl+HiobuTM(MiArEbbAbTM230
-ttxBfR.LARvGMU
D
The 1,230~ characters to execute the alert() functio
n.
D
hdED)TaJcTKD
iMDLgJi1inEKDncDT+nicgMFDBLnD
ndE
D
cgJaDcBMnT+JEDiMDin
MDJEg(ndyDmcMnDMEH,EHMDHEMnHi+n
D
ndEDjNhD
HE6LEMnDpt&DJEg(ndyDhdEHEAcHEFDndED)TaJcTKD-cLJKD-cHPDBEnnEHDiADinD-cHPEKDcgD0xChDHE6LEMnMyDxndEHD
ndTgDndTnFDndED)TaJcTKDMEE1MDncDBEDTD)EHAE+nDMcJLn
icgDAcHD
E,TKig(D*1)EH,T
7
MD*g+T)MLJTDrsSy
D
D
D

--- page 10 ---

Doublel
l
lllllll
lllllllll
lllll
URoLEnulcddlibg
+
oHHdEToME(nlAErbBoddwls))lAEdMbrw
lllllll
llll
lllll
llll
JoSEnlc-FbL
l
l
by¼DrEBvgi(dn
D
rEBvgi(dnDnEMnig(D
-TM
D
6LinEDKiAAEHEgnFDT
MDndEDHLJEDMEn
D
cADrEBvgi(dnDTHED
L)KTnEKDAHE6LEgnJaDBaDndED
igAcH1TnicgDME+LHinaD+c11LginayD
hdEDHEMETH+dDiKEgniAiEKDn-cDKiAAEHEgnD
Ba)TMMEM
D
ndTnD
TAAE+n
M
D
rEBvgi(dnD,uye
F
D
TgKD
-EHE
D
)Tn+dEKDcgDndEDHEJETMEDcADrEBvgi(dnD,uy¼y
D
D
P1 1,l
AErwMl23Howw0
l
ontoggle JS Event (
Google 
Chrome)
 
hdEDAcJJc-ig(DBa)TMMD+LHHEgnJaD-cHPMDcgD;dHc1EDcgJayD*nDiMDE2)E+nEKDndTnDcndEHDBHc-MEH
M
D
-cLJKD
ML))cHnDndEDcgnc((JEDJCDE,EgnF
D
BLnDTnDndEDKTnEDcADndEDHEMETH+dFDndEDcgnc((JEDJCDE,EgnD+LHHEgnJaD-cHPMD
cgD;dHc1EDcgJay
D
DvE RlLoBAr AHHLETRLEb ncdU
D
D
D
P1 1 l
)bT(nLl23Howw0
l
Onshow JS event (
Mozilla 
Firefox
)
 
hdEDAcJJc-ig(D)TaJcTKD-cHPMDcg
D
SiHEAc2yD*nDiMD1TKEDLMig(DndED
N
cgMdc-
N
D
JCDE,EgnyD
rdEgDTDLMEH
D
Hi(dn
w
+Ji+P
M
FDndEDM+Hi)nD-iJJD
BE
D
E2E+LnEKFDBa)TMMig(DrEBvgi(dnD.CCD
AiJnEH
D
KEnE+nicgy
D
DvlCBuAr E( +ErwTM(ooMUmlHO 
JLluzBpEbED+ErwBlvTM(ooMBAroOA&TMRLEb ncdMU
D
D
D
D
D
D
D
D
D
D
D
D
D
D
D

--- page 11 ---

Doublel
,t
l
lllllll
lllllllll
lllll
URoLEnulcddlibg
+
oHHdEToME(nlAErbBoddwls))lAEdMbrw
lllllll
llll
lllll
llll
JoSEnlc-FbL
l
l
byoDSbD3i(D*0
D
SbD3i(D*0DPgc-gDncDBEDcgEDcADndED1cMnD
TK,Tg+EK
D
E
gnEH)HiME
w
JE,EJD-EB
w
T))Ji+Tnicg
D
AiHE-TJJMyDhdED
KiM+c,EHEKD+HcMM
w
MinEDM+Hi)nig(DE,TKig(DnE+dgi6LEMDTHEDgcnDJi1inEKDigDT+nicgMyDxgEDcADndEDKiM+c,EHEKD
Ba)TMMEMD-cHPMDcgDTJJD1cKEHgDBHc-MEHMFD-diJED
ndEDME+cgKDcgED-cHPMDcgDSiHEAc2DcgJayD
D
D
P1*1,l
AErwMl23Howw0
l
Onwhee
l JS event +
R
esizing
 
the page by specifying the height on the style attribute 
(Google Chrome & 
Mozilla Firefox & Opera Browser)
 
hdEDAcJJc-ig(D)TaJcTKD+TgDBEDLMEKDcgDTJJDBHc-MEHMyD*nDiMDAc+LMEKDcgDndED
“
cg-dEEJ
”D
JCDE,EgnyDxg+EDndED
JCDE,EgnDc++LHMFDndEDM+Hi)nD-iJJDBEDE2E+LnEKy
D
DIAv.Bo .LETMOElHO NcKKKe(MBAr&OEELTM2F;6;GMU
B
D
P1*1 l
)bT(nLl23Howw0
l
Onshow JS event (
Mozilla
 
Firefox)
 
hdEDAcJJc-ig(D)TaJcTKDiMDLMig(DndED
“
cgMdc-
”D
JCDE,EgnyD
rdEgDTDLMEHD
Hi(dn
w
+Ji+P
M
FDndEDM+Hi)nD-iJJD
BE
D
E2E+LnEKyDhdED)TaJcTKD-cHPMDcgDSiHEAc2DcgJay
D
DvlCBuAr E
( +ErwTM(ooMUmlHO 
JLluzBpEbED+ErwBlvTM(ooMBAroOA&TM2F;6;GMU
D
D
P1*1*l
x-ErLl23Howw
l
JS
-
F**K Payload 
(Google Chrome & Mozilla Firefox & Opera Browser)
 
;c11cgDALg+nicgMDndTnDigKi+TnE
D
ndEDE2iMnEg+EDcADndED.CCD,LJgEHTBiJinaD
THE
D
BJc+PEKDBaDKEATLJnDcgDSbD
3i(D
*0
yDhdEHEAcHEFD*DdTKDncDAigKDTDnE+dgi6LEDncDAigKDTDnE+dgi6LEDncDBa)TMMDndEDAiJnEHyDpMig(DJC
w
S**vD
Eg+cKig(D
TJJc-EK
D
1EDncDBa)TMMDndEDSbD3i(D*0DrsS
D
KEnE+nicg
y
D
DIAv.Bo .LETMOElHO NcKKKe(MBAr&OEELTM230
-ttzBfR.LARvGMU
D
The 1,230~ characters 
to 
execute the alert() function.
D
 
DvlCBuAr E( +ErwTM(ooMUmlHO 
JLluzBpEbED+ErwBlvTM(ooMBAroOA&TM230
-ttzB
fR.LARvGMU
D
The 1,230~ characters to execute the alert() function.
D
D
D
D

--- page 12 ---

Doublel
,,
l
lllllll
lllllllll
lllll
URoLEnulcddlibg
+
oHHdEToME(nlAErbBoddwls))lAEdMbrw
lllllll
llll
lllll
llll
JoSEnlc-FbL
l
l
P1*1Kl
A(frM-l23Howw
l
HTML Encoding + Double URL Encoding 
(Google Chrome & Mozilla Firefox & Opera Browser)
 
sgcndEHDBa)TMMDcADBJc+Pig(D+c11cgDJCDALg+nicgMD+TgDBEDKcgEDBaDTD1i2DcADEg+cKig(yD3aDLMig(DGhm&D
Eg+cKig(DTgKDKcLBJE
w
pt&DEg+cKig(FDSbD3i(D*0DrsSD.CCDAiJnEHD-cLJKDBEDBa)TMMEKy
D
DIAv.Bo .LETMOElHO NcKKKe(MBAr&OEELTMebA+sS*s)Ss))sS*s)Ss)a(PK7 ncdMU
D
D
DvlCBuAr E(
 +ErwTM(ooMUmlHO 
JLluzBpEbED+ErwBlvTM(ooMB
AroOA&TMebA+sS*s)Ss))sS*s)Ss)a(PK7 ncdMU
B
D
D
D
D
D
D
D
D
D
D
D
D
D
D
D
D
D
D
D
D
D
D
D

--- page 13 ---

Doublel
, 
l
lllllll
lllllllll
lllll
URoLEnulcddlibg
+
oHHdEToME(nlAErbBoddwls))lAEdMbrw
lllllll
llll
lllll
llll
JoSEnlc-FbL
l
l
byu
D
3THHT+LKTDrsS
D
3THHT+LKTDrsSDHEMLJnMDTHEDTMDMT1EDTMDSbD3i(D*0DHEMLJnMyDsJndcL(dDnEMnig(DndEDn-cD-EB
w
T))Ji+TnicgD
AiHE-TJJMD-EHEDME)THTnEDTgKDigDTD
KiAAEHEgnDni1ig(FDndEDHEMLJnMDEgKEKD-indDndEDMT1ED)TaJcTKMDTMD
Ba)TMMEMDndTnDTHEDgcnDKEnE+nEKDBaDSbD3i(D*0DTgKD3THHT+LKTDrsSy
D
D
P1K1,l
AErwMl23Howw0
l
Onwheel JS event +
resizing
 
the page by specifying the height on the style attribute 
(Google Chrome & 
Mozilla Firefox & Opera Browser)
 
hdEDAcJJc-ig(D)TaJcTKD+TgDBEDLMEKDcgDTJJDBHc-MEHMyD*nDiMDAc+LMEKDcgDndED
“
cg-dEEJ
”D
JCDE,EgnyDxg+EDndED
JCDE,EgnDc++LHMFDndEDM+Hi)nD-iJJDBEDE2E+LnEKy
D
DIAv.Bo .LETMOElHO NcKKKe(MBAr&OEELTMRLEb n
c
dMU
B
D
P1K1 l
)bT(nLl23Howw0
l
Onshow JS event (
Mozilla
 
Firefox)
 
hdEDAcJJ
c-ig(D)TaJcTKDiMDLMig(DndED
“
cgMdc-
”D
JCDE,EgnyD
rdEgDTDLMEHD
Hi(dn
w
+Ji+P
M
FDndEDM+Hi)nD-iJJD
BE
D
E2E+LnEKyDhdED)TaJcTKD-cHPMDcgDSiHEAc2DcgJay
D
DvlCBuAr E( +ErwTM(ooMUmlHO 
JLluzBpEbED+ErwBlvTM(ooMBAroOA&TMRLEb ncdMU
B
D
D
D
D
D
D
D
D
D
D
D
D
D

--- page 14 ---

Doublel
,*
l
lllllll
lllllllll
lllll
URoLEnulcddlibg
+
oHHdEToME(nlAErbBoddwls))lAEdMbrw
lllllll
llll
lllll
llll
JoSEnlc-FbL
l
l
byb
D
0G0
w
*RC
D
0G0
w
*RCDnEMnig(DKiAAi+LJniEMDigDndEDnEMnig(D-EHEDKiAAEHEgnDndTgD1cMnD-EB
w
T))Ji+TnicgDAiHE-TJJMyD3aD
HE,iE-ig(DndEDAiJnEHXMDHLJEDMEnMFDinDT))ETHEKDndTnDndEDHLJEDMEnMDKcEMDgcnDBJT+PJiMnDJCDE,EgnMyD*gMnETKFD0G0
w
*RCD1TigD)HcnE+nicgD-EHEDcgDndEDT+nicgMDcADndEDJC
D
E,EgnyDScHDigMnTg+EFDTJEHnOzDiMDigMnTgnJaDKEnE+nEKDBaD
0G0
w
*RCyDsJMcFDTJJD+LHHEgnJaDPgc-gDEg+cKig(DnE+dgi6LEMDTHEDBJc+PEKDnccyDhdEHEAcHEFD*DdTKDncDnTPEDncD
KiAAEHEgnD)TndDigDndEDnEMnig(yDSLHndEH1cHEFDinDdTKD+EHnTigD)HcnE+nicgDT(TigMnD)TaJcTKDMnHL+nLHEFDndTn
D
dTKD
1EDncDE2)JcinDAE-DBHc-MEH
w
BEdT,icHDiMMLEMDncDBa)TMMDinMD)HcnE+nicgD)HcnE+nicgy
D
D
P1P1,l
AErwMl23Howw0
l
Using Browser
-
Behavior Issues (All Modern Browsers)
 
hdEDBa)TMMDLMEKDAE-DBHc-MEH
w
BEdT,icHDiMMLEMDigDndED-TaDndTnDBHc-MEHMDHEgKEHMDndEDLMEHXMDig)Lny
D
D
oCH+ArLARvT+M2F;6;GM
B
hdEDTBc,ED)TaJcTKDiMDgcnDBEig(DKEnE+nEKDigD0G0
w
*RCD,¾y yD;HcMM
w
MinEDM+Hi)nig(DTnnT+PMD+TgDBEDE2E+LnEKD
LMig(DndEDMT1EDnE+dgi6LEDAcHDKiAAEHEgnD)LH)cMEMy
D
D
P1P1 l
)bT(nLl23Howw0
l
D
RcLBJEDpt&
w
Ng+cKig(DcgD;EHnTigD;dTHT+nEHMDOsJJDmcKEHgD3Hc-MEHMz
 
R
cLBJEDpt&
w
Ng+cKig(DcgD+EHnTigD+dTHT+nEHMDiMDgcnDKEnE+nEKDBaD0G0
w
*RCy
D
DoCH+ArLARvT+MRLEbsS*s)Ps)4ncdM
B
D
D
D
D
D
D
D
D
D
D
D
D

--- page 15 ---

Doublel
,K
l
lllllll
lllllllll
lllll
URoLEnulcddlibg
+
oHHdEToME(nlAErbBoddwls))lAEdMbrw
lllllll
llll
lllll
llll
JoSEnlc-FbL
l
l
g+H
e
ToM
(
ALlnibrB
D
maDHEMETH+dDMdc-EKDndTnDmcK
w
CE+LHinaDiMD,EHaDMEgMini,EDncDTgaD1TJi+icLMDHE6LEMnMyDScHDE2T1)JEFD
OELLAsSKAroA+E OlrHTvAoA+E OlrH
D
iMD1THPEKDTMDTD)cnEgniTJD+HcMM
w
MinEDM
+Hi)nig(DTnnT+PDBE+TLMED
cADndED
N
cgMc1Endig(
N
D
JccPMDMi1iJTHDncDJCDE,EgnMyDhdEHEAcHEFDndEDnEMnMDAc+LMEKDcgDAigKig(DignEHgTJDBL(MD
ndTnD+TgDBEDLMEKDncDE,TKEDmcK
w
CE+LHinaD.CCDAiJnEHy
D
D
P1a1,l
AErwMl23Howw0
l
Using (&NewLine;) and (&T
ab;) (Google Chrom
e &
 
Opera Browser 
&
 
Internet Explorer)
D
hdiMD)TaJcTKDdT,EDML++EMMALJJaDBa)TMMEKDmcK
w
CE+LHinaD.CCDAiJnEHyDhdED)TaJcTKD+cgMiMnMDcADTD+Ji+PTBJED
JigPDndTnD)cignMDncDJT,TM+
Hi)nD)
TaJcTKyD*gDgcH1TJD+TMEM
FDn
diMDnE+dgi6LEDiMDKEnE+nEKDBaDmcK
w
CE+LH
inaFDBLnD
-dEgDLMig(DTDJTH(EDgL1BEHDcADGhm&D+dTHMEnMDcADgE-DJigEMDTgKDnTBFDmcK
w
CE+LHinaDATiJMDncDKEnE+nDTgKD
BTgDndED)TaJcTKy
D
hdED)TaJcTKDiMDnHETnEKD
TMDTDgcg
w
1TJi+icLMDGhm&DnT(FD+TLMig(DndEDE,TMicgDcADmcK
w
CE+LHinaD.CCDAiJnEHy
D
DRBObEfTMj2Py*
B
I. EoBAfBn&NE&LlrE7&6RI7dGRCRouble NRLEb ncd7MUX00DiRU
B
D
P1a1 l
)bT(nLl23Howw0
l
US
-
Encoding 
Bypass (Internet Explorer 6 & Internet Explorer 7)
D
hdEDAcJJc-ig(DBa)TMMD-cHPMD
cgD*gnEHgEn
D
N2)JcHEHD6DTgKD*gnEHgEnDN2)JcHEHD yDhdED)TaJcTKD)cMMiBiJinaDncD
BED-cHPig(DML++EMMALJJaDiMDJc-FDLgJEMMDndEDLMEHDiMDLMig(DndEDTBc,EDBHc-MEHMy
D
B
¼ouble ¾RLEb n¢(oo¢d¼io
uble ¾
B
D
P1a1*l
x-ErLl23Howw0
l
Triple URL Encoding (All Modern Browsers)
D
hdiMDBa)TMMD-cHPMDT(TigMnDEg,iHcg1EgnMDndTnDEM+T)EDndEDLMEHXMDHE6LEMnD1LJni)JEDni1EM;DndHEEDni1EMDcHD
TBc,EyDsMDTDHEMLJnFDinD+TgDBEDE2)JcinEKDML++EMMALJJaD-indcLnDBEig(DKEnE+nEKDBaD
mcK
w
CE+LHinay
D
DIisS*s)Ss)*sS*s))s)asS*s)as)asS*s)Ss)*sS*s))s)asS*s)as)*+AwoEACEbTRLEb ncdU
B
D
D
D
D

--- page 16 ---

Doublel
,P
l
lllllll
lllllllll
lllll
URoLEnulcddlibg
+
oHHdEToME(nlAErbBoddwls))lAEdMbrw
lllllll
llll
lllll
llll
JoSEnlc-FbL
l
l
by 
D
~Li+PDREAEgME
D
hdED+LHHEgnDHLJEDMEnMDAcHD~Li+PREAEgMEDrsSDiMDgcnDHETKaDAcHD)HcKL+nicgDJE,EJD-EB
w
T))Ji+TnicgMyD
sJndcL(dDinDBJT+PJiMn
M
D
TDJTH(EDgL1BEHDcADJCDE,EgnM
FD~Li
+PREAEgMEDrsSD-cLJKDBEDBa)TMMEKD
LMig(DAE-D
Eg+cKig(DnE+dgi6LEM
D
D
P1y1,l
AErwMl23Howw0
l
xgCETH+dDJCDN,EgnD+
 
Unicode Encoding (
Google Chrome
)
D
*nDT))ETHMDndTnDndEDHLJEMEnD)Hc,iKEKD-indD~Li+PREAEgMEDKcEMDgcnDBJT+PJiMnDxgMETH+dDJCDE,EgnFDTJMcFD
Lgi+cKEDEg+cKig(DiMDgcnDKEnE+nEKDcg
D
~Li+PREAEgMEy
D
Dlrew B .eETMoERbuOMBAroERbuOTMRLEb
\
wKKP4ncdMU
B
B
P1y1 l
)bT(nLl23Howw0
l
OnToggle JS Event + Unicode Encoding
 
(
Google Chrome
)
 
hdEDME+cgKDBa)TMMDiMDTMDMT1EDTMDndED)HE,icLMDcgEFDBLnDigMnETKDinDLMEMDndEDxgnc((JEDJCDE,EgnyDpgi+cKED
Eg+
cKig(DiMDTJMcDLMEKy
D
DvE RlLoBAr AHHLETMRLEb
\
wKKP4ncdMU
B
D
D
D
D
D
D
D
D
D
D
D
D
D
D

--- page 17 ---

Doublel
,a
l
lllllll
lllllllll
lllll
URoLEnulcddlibg
+
oHHdEToME(nlAErbBoddwls))lAEdMbrw
lllllll
llll
lllll
llll
JoSEnlc-FbL
l
l
byl
D
CL+LHiDrsS
D
CL+LHiDrsSDiMD,EHaDMEgMini,ED
ncDTgaD1TJi+icLMDHE6LEMnMyDCL+LHiDrsSDBEdT,icHDiMDMi1iJTHDncDmcK
w
CE+LHinayD
xgDs)HiJD¼¾ebFD1TgaDHEMETH+dEHM
D
dTMD+c1)EnEKDncDE,TKEDCL+LHiDrsSyDsJJDKiM+c,EHEKDBa)TMMEMDdTMD
BEEgD)Tn+dEKyDCL+LHiDE2nEgMi,EJaD-cHPEKDncD1TPEDndED)HcKL+nDTMDMEgMini,EDTMD)cMMiBJEyDhdEDHEMETH+dD
dTMDBEEgDJTLg+dEKDTAnEHDAigiMdig(DndEDi1)Hc,E1EgnMDcgDCL+LHiDrsSyD3E+TLMEDcADinXMDMEgMini,EDBE
dT,icHD
igDKEn
E+nicgFD1cMnDcADndED
LMEKD
nE+dgi6LEMD
cgDCL+LHiDKiKDgcnD+HETnEDTgDTD)TaJcTKDndTnD+TgDBEDLMEKDncD
+HETnEDLgHEMnHi+nEKD+HcMM
w
MinEDM+Hi)nig(D)TaJcTKyDGc-E,EHFDndEDHEMETH+dDHE,ETJEKDTD1igcHDiMMLEDcgD
CL+LHiDrs
SDHL
JEDMEnMDndTnD+TgDBEDLMEKD
ncD)EHAcH1D.CCDTnnT+PMDT(TigMnDcJKEHDBHc-MEHMFDML+dDTMD*gnEHgEnD
N2)JcHEHD6DTgKD*gnEHgEnDN2)JcHEHD y
D
D
P1h1,l
23Howw0
l
pC
w
Ng+cKig(D3a)TMMDO*gnEHgEnDN2)JcHEHD6D¢D*gnEHgEnDN2)JcHEHD z
D
hdEDAcJJc-ig(D)TaJcTKDiMDE2E+LnEKDTMDTD,TJiKD.CCD)TaJcTKDT(TigMnD*gnEHgEnDN2)JcHEH
D
6DTgKD*gnEHgEnD
N2)JcHEHD DKLEDncDTDBL(DigDHEgKEHig(DpC
w
Eg+cKig(y
D
¼ouble ¾RLEb n¢(oo¢d¼iouble ¾
B
D
D
D
D
D
D
D
D
D
D
D
D
D
D
D
D

--- page 18 ---

Doublel
,y
l
lllllll
lllllllll
lllll
URoLEnulcddlibg
+
oHHdEToME(nlAErbBoddwls))lAEdMbrw
lllllll
llll
lllll
llll
JoSEnlc-FbL
l
l
F-Dua1~y3DHa2Gy12a2p
D
6yeDSb
D
hdEDAigKig(MDdTMDBEEgDHE)cHnEKDncDSbDME+LHinaDnET1FDndEaDdT,EDT+Pgc-JEK(EKDndEDAigKig(MFDTgKD
MnTnEKD
ndTnD
TgDL)KTnE
D
-iJJDBEDHEJETMEKDcgDCE)nE1BEHD¼¾eb
D
ncD)Tn+dDndEDiMMLEM
y
D
D
6y¼DrEBvgi(dn
D
s~htxf*.DrEBvgi(dnDnET1DT+Pgc-JEK(EKDndEDBa)TMMEMFDTgKDMnTnEKDndEDiMMLEMD-iJJDBED)Tn+dEKD
igD
ndED
gE2nDHEJETMEFD,uy¼y
D
D
6yoD0G0
w
*RC
D
sJJD0G0
w
*RCDKE,EJc)EHMDdTMDBEEgD+cgnT+nEKFD
BLn
D
gcDHEM)c
gME
D
-TMDdETHKDAHc1DndE1y
D
D
6yuD~Li+PREAEgMEDrsS
D
~Li+PREAEgMEDrsSDKE,EJc)EHDdTMDBEEgD+cgnT+nEKD-indDKEnTiJMDTBcLnDndEDBa)TMMEMyDhdED1TigD
KE,EJc)EHDcAD~Li+PREAEgMEDrsSDigKi+TnEKDndTnD~Li+PREAEgMEDrsSD
iMg
7
n
D
ALJJaDHETKaDAcHD)HcKL+nicgDJE,EJD
MEH,i+EMyDhdED+LHHE
gnJaDLMEKDHLJEMEnMDTHEDcgJaDE2T1)JEMyDsJMcFDndEDKE,EJc)EHDHEM)cgKEKDndTnDndEHEDgcD
+LHHEgnJaDT,TiJTBJED)HcKL+nicg
w
JE,EJDHLJEMEnMy
D
D
6ybDCL+LHi
D
CL+LHiDnET1DdTMDBEEgD+cgnT+nEKDHE(THKig(DndEDBa)TMMFDTgKDndEaDdT,ED)Tn+dEKDndEDAigKig(DigD
JEMMDndTgD
¼uDdcLHM
y
D
D
6y6D
*1)EH,TD*g+T)MLJT
D
*1)EH,T
D
*g+T)MLJTDnET1DdTMDBEEgD+cgnT+nEKFDTgKDndEaDdT,EDKiM+LMMEK
D
)cnEgniTJDiKETMDcADE2)Jcinig(
D
ndED
Ba)TMMEMDigDHETJ
w
-cHJKDM+EgTHicMyDhdEDnET1Dig,EMni(TnEKDndEDBa)TMMEMFDTgKD)Tn+dEKDndEDAigKig(My
D
D
6y D3THHT+LKTDrsS
D
3THHT+LKTDnET1DdTMDT
+Pgc-JEK(EKDndEDAigKig(MFDTgKD)Tn+dEKDndEDBa)TMMEMDigDsL(LMnD¼¾eby
D

--- page 19 ---

Doublel
,h
l
lllllll
lllllllll
lllll
URoLEnulcddlibg
+
oHHdEToME(nlAErbBoddwls))lAEdMbrw
lllllll
llll
lllll
llll
JoSEnlc-FbL
l
l
&-Ddy10Pt2xy1
D
D
3TMEKDcgDndED
HEMETH+d
D
*DdT,EDKcgEFDinDT))ETHMDndTnDE,EHaDrsSD+TgDBEDBa)TMMEKDBaD)Lnnig(DTD
ni1EDTgKDEAAcHnDigncDAigKig(DinMD-ETPgEMMEMyDN,EHaDrsSDdTMDinMDc-gD-ETPgEMMEMDndTnD+TgDBED+c1BigEKD
ncD+HETnEDTgDTnnT+PD,E+ncHDndTnD
dTM
D
gcnDBEEgDKEnE+nEKDBaDndEDrsSy
D
sJMcFDndEDBEMnD-TaDcAD
)Tn+dig(DTDME+LHinaD,LJgEHTBiJinaDiMDgcnDBaDLMig(DTDAiHE-TJJFDin
7
MDBaD
ig,EMni(Tnig(DndEDHccnD+TLMEDcADndED,LJgEHTBiJinaDTgKDAi2ig(DinyDpMig(D-EB
w
T))Ji+TnicgDAiHE-TJJMD-iJJDgcnD
)HcnE+nDAHc1DTnnT+PMDTgKDBHET+dEMFDBLnDinD1TaD
AcH+E
D
TnnT+PEHMDncDM)EgKDTKKinicgT
JDni1EDigDndED
E2)JcinTnicgD)Hc+EMMy
D
hdEDHEMETH+dDnEgKMDncDKE1cgMnHTnEDndTnDBa)TMMig(D-EB
w
T))Ji+TnicgDAiHE-TJJMDiMD)cMMiBJEyD
rdiJED
nHaig(DncD
ML11THi&EDndE
D
AigKig(MFD
gcnDTJJDKiM+c,EHEKDAigKig(M
D
THEDig+JLKEKDigDndiMD)T)EH
y
D
*nDT))ETHMDndTnDndEDKiAAi+LJniEMDigD
E,TKig(D-EB
w
T))Ji+TnicgDAiHE-TJJMDMJi(dnJaDKiAAEHMDAHc1DTD
)HcKL+nDncDTgcndEHyDScHDigMnTg+EFDMc1ED)HcKL+nMDnccPD1EDAi,ED1igLnEMDncDBa)TMMD
ndE1
FD-diJED
cndEH
D
)HcKL+nMDnccPDc,EHDAcHna
w
Ai,ED1igLnEMD
AHc1D1ED
ncDBa)TMM
yD*gDMc1EDc++TMicgMFDBa)TMMEMDKiKg
7
n
D
-cHPDcgD
E
,EHaD+JiEgn
w
MiKEDEg,iHcg1Egn
D
AcHDndEiHD)HcKL+nM
y
D
D
D

--- page 20 ---

Doublel
,~
l
lllllll
lllllllll
lllll
URoLEnulcddlibg
+
oHHdEToME(nlAErbBoddwls))lAEdMbrw
lllllll
llll
lllll
llll
JoSEnlc-FbL
l
l
I-D
b0C1ymPa~fava1,2p
D
*D-cLJKDJiPEDncDndTgPDndEDAcJJc-ig(D
igKi,iKLTJMDAcHD
ndEiH
D
ML))cHnf
D
D
D
sd1EKDsBBTM
D
D
D
sa1TgD*KHiM
D
D
D
JcdgDCnTLAAT+dEH
D
D
D
mTH+LMDtca+Ewsg(EJD0EnEHMcg
D
D
D
mTHicDGEiKEHi+d
D
D
D
D
N-D
Haha3a10a2p
D
ey
D
dnn)MfLL---yc-TM)ycH(LigKE2y)d)L;HcMM
w
MinE_C+Hi)nig(_O.CCz
D
D
¼y
D
dnn)MfLLEgy-iPi)EKiTycH(L-iPiLSb_fEn-cHPM
D
D
oy
D
dnn)MfLL
---y
Aby+c1L(JcMMTHaL-EBwT))Ji+TnicgwAiHE-TJJ
L
D
D
uy
D
dnn)MfLLEgy-iPi)EKiTycH(L-iPiLCL+LHi
D
D
by
D
dnn)MfLL---y1cKME+LHinaycH(LTBcLnydn1J
D
D
6y
D
dnn)MfLLEgy-iPi)EKiTycH(L-iPiL*1)EH,T
D
D
 y
D
dnn)MfLLEgy-iPi)EKiTycH(L-iPiL*g+T)MLJT
D
D
ly
D
dnn)MfLLEgy-iPi)EKiTycH(L-iPiL0G0*RC
D
D
Uy
D
dnn)fLLMcLH+EAcH(EygEnL)HcIE+nML6Li+PKEAEg+E-TAL
D
D
e¾y
D
dnn)MfLL---yT6nHcgi2y+
c1L?0T(E*R=UU
D
D
eey
D
dnn)MfLLEgy-iPi)EKiTycH(L-iPiL3THHT+LKT_fEn-cHPM
D
D
e¼y
D
dnn)MfLL---yBTHHT+LKTy+c1L)HcKL+nML-EBT))Ji+TnicgAiHE-TJJLAETnLHEM
D
D
eoy
D
dnn)MfLLnE+dJiByBTHHT+LKTy+c1L-TAL+HcMMMinEM+Hi)nig(TnnT+P
D
D
D
D
