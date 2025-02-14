from math import tan, radians
from estilos.estilos import EGPA, EGPB, TIPO_PANT, ETV, EEV

def calcular_esPT(Y: float, maximo: float) -> bool:
    return Y == maximo

def calcular_k(galibo: str, Y: float, hquierbroaux: float, htopeaux: float, difaux: float) -> float:
    if galibo in [EGPA.GHE16.value, EGPA.GEC16.value, EGPA.GC.value,]:
        return 0.0
    elif galibo in [EGPA.GEA16.value, EGPA.GEB16.value, EGPA.GA.value, EGPA.GB.value,]:
        if Y < hquierbroaux:
            return 0.0
        else:
            if Y >= htopeaux:
                return 1.0
            else:
                return round((Y - hquierbroaux) / difaux, 2)
    elif galibo in [EGPA.GEE10.value, EGPA.GED10.value, EGPA.PERSONALIZADO.value,]:
        return None

def calcular_s0(galibo: str, Y: float, hquierbroaux: float, htopeaux: float, difaux: float, hotra: float) -> float:
    if galibo in [EGPA.GHE16.value, EGPA.GEC16.value, EGPA.GC.value,]:
        return 0.4
    elif galibo in [EGPA.GEA16.value, EGPA.GEB16.value, EGPA.GA.value, EGPA.GB.value,]:
        if Y < hquierbroaux:
            return 0.4
        else:
            if Y >= htopeaux:
                return 0.3
            else:
                return round((hotra - Y) / (10 * difaux),2)
    elif galibo in [EGPA.GEE10.value, EGPA.GED10.value, EGPA.PERSONALIZADO.value,]:
        return 0.4

def calcular_Sa(galibo_GPA: str, galibo_GPB: str, R: float, LN: float, L: float, hquiebroaux: float, Y: float, k: float) -> float:
    if Y <= 0.4:

        if galibo_GPA in [EGPA.GHE16.value, EGPA.GEC16.value, EGPA.GC.value,EGPA.GEA16.value, EGPA.GEB16.value, EGPA.GA.value, EGPA.GB.value,]:
            if galibo_GPB in [EGPB.GEI1.value, EGPB.GEI2.value, EGPB.GI1.value, EGPB.GI2.value,]:
                if R >= 250:
                    aux = 2.5 / R
                elif R < 250:
                    aux = 60 / R - 0.225
            elif galibo_GPB in [EGPB.GEI3.value, EGPB.GI3.value,]:
                if R >= 250:
                    aux = 2.5 * (1 - k) / R
                elif R < 250:
                    aux = 60 / R - 0.225 + k * (0.065 - 20 / R)
        elif galibo_GPA in [EGPA.GEE10.value, EGPA.GED10.value, EGPA.PERSONALIZADO.value,]:
            if R >= 100:
                aux = 1.5/R
            else:
                aux = 24 / R - 0.225
        else:
            aux = 999

    else:

        if galibo_GPA in [EGPA.GHE16.value, EGPA.GEC16.value, EGPA.GC.value,]:
            if R >= 250:
                aux = 3.75 / R
            elif R < 250:
                aux = 60 / R - 0.225
        elif galibo_GPA in [EGPA.GEA16.value, EGPA.GEB16.value, EGPA.GA.value, EGPA.GB.value,]:
            if R >= 250 and Y <= hquiebroaux:
                aux = 3.75 / R
            elif R >= 250 and Y > hquiebroaux:
                aux = 3.75 / R + 16.25 * k / R
            elif R < 250  and Y <= hquiebroaux:
                aux = 60 / R - 0.225
            elif R < 250 and  Y > hquiebroaux:
                aux = 60 / R - 0.225 + k * (0.105 - 10 / R)
        elif galibo_GPA in [EGPA.GEE10.value, EGPA.GED10.value, EGPA.PERSONALIZADO.value,]:
            if R >= 100:
                aux = 1.5/R
            else:
                aux = 24 / R - 0.225
        else:
            aux = 999
    
    aux += (L - LN) / 2

    return round(aux*1000,1)         #para pasar a milímetros

def calcular_Si(galibo_GPA: str, galibo_GPB: str, R: float, LN: float, L: float, hquiebroaux: float, Y: float, k: float) -> float:
    if Y <= 0.4:

        if galibo_GPA in [EGPA.GHE16.value, EGPA.GEC16.value, EGPA.GC.value,EGPA.GEA16.value, EGPA.GEB16.value, EGPA.GA.value, EGPA.GB.value,]:
            if galibo_GPB in [EGPB.GEI1.value, EGPB.GEI2.value, EGPB.GI1.value, EGPB.GI2.value,]:
                if R >= 250:
                    aux = 2.5 / R
                elif R < 250:
                    aux = 50 / R - 0.185
            elif galibo_GPB in [EGPB.GEI3.value, EGPB.GI3.value,]:
                if R >= 250:
                    aux = 2.5 / R
                elif R < 250:
                    aux = 50 / R - 0.185 + k * (0.05 - 12.5 / R)
        elif galibo_GPA in [EGPA.GEE10.value, EGPA.GED10.value, EGPA.PERSONALIZADO.value,]:
            if R >= 100:
                aux = 1.5/R
            else:
                aux = 20 / R - 0.185
        else:
            aux = 999

    else:

        if galibo_GPA in [EGPA.GHE16.value, EGPA.GEC16.value, EGPA.GC.value,]:
            if R >= 250:
                aux = 3.75 / R
            elif R < 250:
                aux = 50 / R - 0.185
        elif galibo_GPA in [EGPA.GEA16.value, EGPA.GEB16.value, EGPA.GA.value, EGPA.GB.value,]:
            if R >= 250 and Y <= hquiebroaux:
                aux = 3.75 / R
            elif R >= 250 and Y > hquiebroaux:
                aux = 3.75 / R + 16.25 * k / R
            elif R < 250  and Y <= hquiebroaux:
                aux = 50 / R - 0.185
            elif R < 250 and  Y > hquiebroaux:
                aux = 50 / R - 0.185 + k * 0.065
        elif galibo_GPA in [EGPA.GEE10.value, EGPA.GED10.value, EGPA.PERSONALIZADO.value,]:
            if R >= 100:
                aux = 1.5/R
            else:
                aux = 20 / R - 0.185
        else:
            aux = 999
    
    aux += (L - LN) / 2

    return round(aux*1000,1)         #para pasar a milímetros

def calcular_qsD_ai(Y: float, s0: float, D: float, D0: float, L: float, hco: float) -> float:
    return round(1000 * s0 / L * max(0, D - D0 ) * max(0, Y - hco), 1)

def calcular_qsI_ai(Y: float, s0: float, I: float, I0: float, L: float, hco: float) -> float:
    return round(1000 * s0 / L * max(0, I - I0 ) * max(0, Y - hco), 1)

def calcular_Dbg_ai(Y: float, L: float, TD: float) -> float:
    return round(Y * 1000 * TD / L, 1)

def calcular_Dbc_ai(Y: float, L: float, TD: float, hco: float, s0: float) -> float:
    return round(s0 * TD * max(0, Y - hco) / L * 1000, 1)

def calcular_Dbsusp_ai(ang_susp: float, Y: float, hco: float) -> float:
    return round(tan(radians(ang_susp)) * max(0, Y - hco), 1)

def calcular_Dbcarg_ai(ang_carga: float, Y: float, hco: float) -> float:
    return round(tan(radians(ang_carga)) * max(0, Y - hco), 1)

def calcular_Dbeta0_ai(ang_eta0: float, Y: float, hco: float) -> float:
    return round(tan(radians(ang_eta0)) * max(0, Y - hco), 1)

def calcular_aosc(s0: float, ang03: float, ang04: float) -> float:
    return round(10 * (s0 - 0.3) * ang04 - 10 * (s0 - 0.4) * ang03, 2)

def calcular_Dbosc(ang: float, Y: float, hco: float) -> float:
    return round(tan(radians(ang)) * max(0, Y - hco), 1)

def calcular_DhPT_D_ai(X: float, s0: float,D: float, D0: float, L: float) -> float:
    return round(abs(X) * s0 * max(0, D - D0) / L, 1)

def calcular_DhPT_I_ai(X: float, s0: float,I: float, I0: float, L: float) -> float:
    return round(abs(X) * s0 * max(0, I - I0) / L, 1)

def calcular_Dhg_a(X: float, L: float, TD: float) -> float:
    return round(1000 * (abs(X) / L + 0.5) * TD, 1)

def calcular_Dhg_i(X: float, L: float, TD: float) -> float:
    return round(1000 * (abs(X) / L - 0.5) * TD, 1)

def calcular_Dhc(X: float, s0: float, L: float, TD: float) -> float:
    return round(1000 * s0 * abs(X) * TD / L, 1)

def calcular_Dhsusp_ai(X: float, ang: float) -> float:
    return round(abs(X) * tan(radians(ang)), 1)

def calcular_Dhcarg_ai(X: float, ang: float) -> float:
    return round(abs(X) * tan(radians(ang)), 1)

def calcular_Dheta0_ai(X: float, ang: float) -> float:
    return round(abs(X) * tan(radians(ang)), 1)

def calcular_Dhosc(X: float, ang: float) -> float:
    return round(abs(X) * tan(radians(ang)), 1)

def calcular_lim_Sj1(Y: float, hco: float, k: float, kale: float, Tvia: float, Dbgai: float, Dbcai: float, Dbsusp: float, dbcarg: float, dbosc: float) -> float:
    keff = kale if Y < hco else k
    res = keff * (Tvia**2 + (Dbgai + Dbcai)**2 + (Dbsusp**2 + dbcarg**2 + dbosc**2))**0.5
    return round(res,1)

def calcular_lim_Sj2(Y: float, hco: float, k: float, kale: float, Tvia: float, Dbgai: float) -> float:
    keff = kale if Y < hco else k
    res = keff * (Tvia**2 + Dbgai**2)**0.5
    return round(res,1)

def calcular_lim_rad_Sj1(Tvia_ai:float, Dbg_ai: float, Dbc_ai:float, Dbsusp_ai: float, Dbcarg_ai: float, Dbosc):
    return round(Tvia_ai**2 - (Dbg_ai + Dbc_ai)**2 - (Dbsusp_ai**2 + Dbcarg_ai**2 + Dbosc**2),1)

def calcular_lim_rad_Sj2(Tvia_ai:float, Dbg_ai:float):
    return round(Tvia_ai**2 - Dbg_ai**2, 1)

def calcular_lim_Sj_ast(Y: float, hco: float, k: float, kale: float, radic: float) -> float:
    keff = kale if Y < hco else k
    signo = 1 if radic > 0 else -1
    res = keff * signo * (abs(radic))**0.5
    return round(res, 1)

def calcular_lim_rad_SVi1(TN: float, Dhgi: float, Dhc: float, Dhsusp: float, Dhcarg: float, Dhosci: float) -> float:
    res = TN**2 + (max(0, -Dhgi - Dhc))**2 - (Dhsusp**2 + Dhcarg**2 + Dhosci**2)
    return round(res, 1)

def calcular_lim_rad_SVa1(TN: float, Dhga: float, Dhc: float, Dhsusp: float, Dhcarg: float, Dhosci: float) -> float:
    res = TN**2 - (Dhga + Dhc)**2 - (Dhsusp**2 + Dhcarg**2 + Dhosci**2)
    return round(res, 1)

def calcular_lim_SV1(k: float, radic: float) -> float:
    signo = 1 if radic > 0 else -1
    res = k * signo * (abs(radic))**0.5
    return round(res, 1)

def calcular_SVa1_ast(k: float, TN: float, Dhga: float, Dhc: float, Dhsusp: float, Dhcarg: float, Dhosci: float) -> float:
    res = k * (TN**2 + (Dhga + Dhc)**2 + (Dhsusp**2 + Dhcarg**2 + Dhosci**2))**0.5
    return round(res, 1)

def calcular_SVi1_ast(k: float, TN: float, Dhgi: float, Dhc: float, Dhsusp: float, Dhcarg: float, Dhosci: float) -> float:
    res = k * (TN**2 + (max(0, Dhgi + Dhc))**2 + (Dhsusp**2 + Dhcarg**2 + Dhosci**2))**0.5
    return round(res, 1)

def calcular_nom_Sj3(Tvia: float, Dbgai: float, Dbcai: float, Dbsusp: float, Dbcarg: float, Dbosc: float) -> float:
    res = Tvia + Dbgai + Dbcai + Dbsusp + Dbcarg + Dbosc
    return round(res,1)

def calcular_nom_Sj4(Tvia: float, Dbgai: float) -> float:
    return round(Tvia + Dbgai, 1)

def calcular_nom_Sj3_ast(Tvia: float, Dbgai: float, Dbcai: float, Dbsusp: float, Dbcarg: float, Dbosc: float) -> float:
    res = Tvia - Dbgai - Dbcai - Dbsusp - Dbcarg - Dbosc
    return round(res, 1)

def calcular_nom_Sj4_ast(Tvia: float, Dbgai: float) -> float:
    res = Tvia - Dbgai
    return round(res,1)

def calcular_nom_SV3a(TN: float, Dhga: float, Dhc: float, Dhsusp: float, Dhcarg: float, Dhosc: float) -> float:
    res = TN - Dhga - Dhc - Dhsusp - Dhcarg - Dhosc
    return round(res, 1)

def calcular_nom_SV3i(TN: float, Dhga: float, Dhc: float, Dhsusp: float, Dhcarg: float, Dhosc: float) -> float:
    res = TN + max(0, -(Dhga + Dhc)) - Dhsusp - Dhcarg - Dhosc
    return round(res,1)

def calcular_nom_SV3a_ast(TN: float, Dhga: float, Dhc: float, Dhsusp: float, Dhcarg: float, Dhosc: float) -> float:
    res = TN + Dhga + Dhc + Dhsusp + Dhcarg + Dhosc
    return round(res, 1)

def calcular_nom_SV3i_ast(TN: float, Dhga: float, Dhc: float, Dhsusp: float, Dhcarg: float, Dhosc: float) -> float:
    res = TN + max(0, Dhga + Dhc) + Dhsusp + Dhcarg + Dhosc
    return round(res, 1)

def calcular_h(Y: float, hbmax: float, lim_hobstVM_con: float, lim_hobstVM_max: float, lim_hobstV0_con: float, lim_hobstV0_max: float) -> float:
    if Y > hbmax:
        return max(abs(lim_hobstVM_con), abs(lim_hobstVM_max), abs(lim_hobstV0_con), abs(lim_hobstV0_max))
    else:
        return min(abs(lim_hobstVM_con), abs(lim_hobstVM_max), abs(lim_hobstV0_con), abs(lim_hobstV0_max))

def calcular_lim_bobst(X: float, Y: float, S: float, qS: float, j1: float, j2: float) -> float:
    signo_X = 1 if X > 0 else -1
    j = j1 if Y > 0.4 else j2
    saliente = qS if Y > 0.4 else 0

    res = X + signo_X * (S + saliente + j)
    return round(res, 1)

def calcular_nom_bobst(X: float, Y: float, S: float, qS: float, j1: float, j2: float, M3b: float) -> float:
    signo_X = 1 if X > 0 else -1
    j = j1 if Y > 0.4 else j2
    saliente = qS if Y > 0.4 else 0

    res = X + signo_X * (S + saliente + j + M3b)
    return round(res, 1)

def calcular_lim_hobst(Y: float, DhRV: float, hb_max: float, esPT: bool, DhPT: float, SV1: float, SV2: float) -> float:
    signo_Y = 1 if Y - hb_max > 0 else -1
    cond1 = 1 if esPT else 0
    cond2 = 1 if not esPT else 0

    res = Y + DhRV * signo_Y + cond1 * (DhPT + SV1) + cond2 * signo_Y * SV2
    return round(res, 1)

def calcular_nom_hobst(Y: float, DhRV: float, hb_max: float, esPT: bool, DhPT: float, SV1: float, SV2: float, M3h: float) -> float:
    signo_Y = 1 if Y - hb_max > 0 else -1
    cond1 = 1 if esPT else 0
    cond2 = 1 if not esPT else 0

    res = Y + (DhRV + M3h) * signo_Y + cond1 * (DhPT + SV1) + cond2 * signo_Y * SV2
    return round(res , 1)



def calcular_pant_Sai(galibo_GPA: str, R: float, LN: float, L: float) -> float:
    if galibo_GPA in [EGPA.GHE16.value, EGPA.GEC16.value, EGPA.GC.value,EGPA.GEA16.value, EGPA.GEB16.value, EGPA.GA.value, EGPA.GB.value,]:
        aux = 2.5 / R
    elif galibo_GPA in [EGPA.GEE10.value, EGPA.GED10.value, EGPA.PERSONALIZADO.value,]:
        aux = 1.5/R
    else:
        aux = 999
    
    aux += (L - LN) / 2

    return round(aux*1000,1)         #para pasar a milímetros

def calcular_pant_qsa(galibo_GPA: str, Y: float, I: float, hco: float) -> float:
    if galibo_GPA in [EGPA.GHE16.value, EGPA.GEC16.value, EGPA.GEA16.value, EGPA.GEB16.value,]:
        return round(1000 * 0.225 / 1.733 * max(0, I - 1/15 ) * max(0, Y - hco), 1)
    elif galibo_GPA in [EGPA.GA.value, EGPA.GB.value,EGPA.GC.value,]:
        return round(1000 * 0.225 / 1.5 * max(0, I - 1/15 ) * max(0, Y - hco), 1)
    elif galibo_GPA in [EGPA.GEE10.value, EGPA.GED10.value, EGPA.PERSONALIZADO.value,]:
        return round(1000 * 0.225 / 1.055 * max(0, I - 1/15 ) * max(0, Y - hco), 1)
    else:
        return 999

def calcular_pant_qsi(galibo_GPA: str, Y: float, D: float, hco: float) -> float:
    if galibo_GPA in [EGPA.GHE16.value, EGPA.GEC16.value, EGPA.GEA16.value, EGPA.GEB16.value,]:
        return round(1000 * 0.225 / 1.733 * max(0, D - 1/15 ) * max(0, Y - hco), 1)
    elif galibo_GPA in [EGPA.GA.value, EGPA.GB.value,EGPA.GC.value,]:
        return round(1000 * 0.225 / 1.5 * max(0, D - 1/15 ) * max(0, Y - hco), 1)
    elif galibo_GPA in [EGPA.GEE10.value, EGPA.GED10.value, EGPA.PERSONALIZADO.value,]:
        return round(1000 * 0.225 / 1.055 * max(0, D - 1/15 ) * max(0, Y - hco), 1)
    else:
        return 999

def calcular_pant_Dbg_ai(Y: float, L: float, TD: float) -> float:
    return round(Y * 1000 * TD / L, 1)

def calcular_pant_Dbc_ai(Y: float, L: float, TD: float, hco: float) -> float:
    return round(0.225 * TD * max(0, Y - hco) / L * 1000, 1)

def calcular_pant_aosc(tipo_via: str, estado_via: str, LN: float, tipo: str) -> float:
    if LN in [1.668, 1.435]:
        if tipo_via == ETV.BALASTO.value:
            if tipo == "i":
                if estado_via == EEV.BUEN_ESTADO.value:
                    return 0.06
                elif estado_via == EEV.MAL_ESTADO.value:
                    return 0.11
                else: return 999
            elif tipo == "a":
                if estado_via == EEV.BUEN_ESTADO.value:
                    return 0.34
                elif estado_via == EEV.MAL_ESTADO.value:
                    return 0.6
                else: return 999
            else: return 999
        elif tipo_via == ETV.VIA_PLACA.value:
            if tipo == "i":
                return 0.06
            elif tipo == "a":
                return 0.34
            else: return 999
        else: return 999
    elif LN == 1:
        if tipo_via == ETV.BALASTO.value:
            if tipo == "i":
                return 0.11
            elif tipo == "a":
                return 0.6
            else: return 999
        elif tipo_via == ETV.VIA_PLACA.value:
            if tipo == "i":
                return 0.06
            elif tipo == "a":
                return 0.34
            else: return 999
        else: return 999
    else: return 999
        
def calcular_pant_Sj(Tvia: float, Dbgai: float, Dbcai: float, Dbsusp: float, Dbcarg: float, Dbosc: float) -> float:
    res = (Tvia**2 + (Dbgai + Dbcai)**2 + (Dbsusp**2 + Dbcarg**2 + Dbosc**2))**0.5
    return round(res,1)

def calcular_pant_bobst(nombre: str, bw: float, epo: float, epu: float, S_ai: float, qs_a: float, Sj: float) -> float:
    if nombre in ["P1", "P4",]:
        ep = epu
    elif nombre in ["P2", "P3",]:
        ep = epo
    else:
        ep = 999
    return round(bw + ep + S_ai + qs_a + Sj, 1)

def calcular_pant_bobst_hmax_a(nombre: str, bobst: float, Dbobst_a_12: float, Dbobst_a_34: float, dy: float, heff: float, tipo_pant: dict) -> float:
    if nombre in ["P1", "P4",]:
        return bobst
    elif nombre in ["P2", "P3",]:
        if nombre == "P2":
            dx = Dbobst_a_12
            aux1 = (heff - tipo_pant["P1"].Y_ref)
            aux2 = tipo_pant["P1"].bobst_a
        elif nombre == "P3":
            dx = Dbobst_a_34
            aux1 = (heff - tipo_pant["P4"].Y_ref)
            aux2 = tipo_pant["P4"].bobst_a
        else:
            return None
        return round(dx * aux1 / dy + aux2, 1)
    else:
        return None
    
def calcular_pant_bobst_hmax_i(nombre: str, bobst: float, Dbobst_i_12: float, Dbobst_i_34: float, dy: float, heff: float, tipo_pant: dict) -> float:
    if nombre in ["P1", "P4",]:
        return bobst
    elif nombre in ["P2", "P3",]:
        if nombre == "P2":
            dx = Dbobst_i_12
            aux1 = (heff - tipo_pant["P1"].Y_ref)
            aux2 = tipo_pant["P1"].bobst_i
        elif nombre == "P3":
            dx = Dbobst_i_34
            aux1 = (heff - tipo_pant["P4"].Y_ref)
            aux2 = tipo_pant["P4"].bobst_i
        else:
            return None
        return round(dx * aux1 / dy + aux2, 1)
    else:
        return None

def calcular_pant_elec(bheff: float, belec: float, cw: float) -> float:
    return round(bheff + belec - cw, 1)

def calcular_pant_pant_mec_X(x_ref: float, bobst_i: float, bobst_a: float, lado: int) -> float:
    signo = 1 if x_ref > 0 else -1
    if (lado == 1 and signo ==1) or (lado == 2 and signo ==-1):
        res = bobst_i
    elif (lado == 1 and signo ==-1) or (lado == 2 and signo ==1):
        res = bobst_a
    else:
        res = 999
    return round(signo * res, 1)

def calcular_pant_pant_mec_Y(nombre: str, Y: float, h: float) -> float:
    if nombre in ["P1", "P4",]:
        return round(Y, 1)
    elif nombre in ["P2", "P3",]:
        return round(h, 1)
    else:
        return 999