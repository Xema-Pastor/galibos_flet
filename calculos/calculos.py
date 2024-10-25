from math import tan, radians
from estilos.estilos import EGPA

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

def calcular_Sa(galibo: str, R: float, LN: float, L: float, hquiebroaux: float, Y: float, k: float) -> float:
    if galibo in [EGPA.GHE16.value, EGPA.GEC16.value, EGPA.GC.value,]:
        if R >= 250:
            aux = 3.75 / R
        elif R < 250:
            aux = 60 / R - 0.225
    elif galibo in [EGPA.GEA16.value, EGPA.GEB16.value, EGPA.GA.value, EGPA.GB.value,]:
        if R >= 250 and Y <= hquiebroaux:
            aux = 3.75 / R
        elif R >= 250 and Y > hquiebroaux:
            aux = 3.75 / R + 16.25 * k / R
        elif R < 250  and Y <= hquiebroaux:
            aux = 60 / R - 0.225
        elif R < 250 and  Y > hquiebroaux:
            aux = 60 / R - 0.225 + k * (0.105 - 10 / R)
    elif galibo in [EGPA.GEE10.value, EGPA.GED10.value, EGPA.PERSONALIZADO.value,]:
        if R >= 100:
            aux = 1.5/R
        else:
            aux = 24 / R - 0.225
    
    aux += (L - LN) / 2

    return round(aux*1000,1)         #para pasar a milímetros

def calcular_Si(galibo: str, R: float, LN: float, L: float, hquiebroaux: float, Y: float, k: float) -> float:
    if galibo in [EGPA.GHE16.value, EGPA.GEC16.value, EGPA.GC.value,]:
        if R >= 250:
            aux = 3.75 / R
        elif R < 250:
            aux = 50 / R - 0.185
    elif galibo in [EGPA.GEA16.value, EGPA.GEB16.value, EGPA.GA.value, EGPA.GB.value,]:
        if R >= 250 and Y <= hquiebroaux:
            aux = 3.75 / R
        elif R >= 250 and Y > hquiebroaux:
            aux = 3.75 / R + 16.25 * k / R
        elif R < 250  and Y <= hquiebroaux:
            aux = 50 / R - 0.185
        elif R < 250 and  Y > hquiebroaux:
            aux = 50 / R - 0.185 + k * 0.065
    elif galibo in [EGPA.GEE10.value, EGPA.GED10.value, EGPA.PERSONALIZADO.value,]:
        if R >= 100:
            aux = 1.5/R
        else:
            aux = 20 / R - 0.185
    
    aux += (L - LN) / 2

    return round(aux*1000,2)         #para pasar a milímetros

def calcular_qsD_ai(Y: float, s0: float, D: float, D0: float, L: float, hco: float) -> float:
    return round(s0 / L * max(0, D - D0 ) * max(0, Y - hco), 2)

def calcular_qsI_ai(Y: float, s0: float, I: float, I0: float, L: float, hco: float) -> float:
    return round(s0 / L * max(0, I - I0 ) * max(0, Y - hco), 2)

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
    return round(10 * (s0 - 0.3) * ang04 - 10*(s0 - 0.4) * ang03, 2)

def calcular_Dbosc(ang: float, Y: float, hco: float) -> float:
    return round(tan(ang) * max(0, Y - hco), 2)

def calcular_DhPT_D_ai(X: float, s0: float,D: float, D0: float, L: float) -> float:
    return round(abs(X) * s0 * max(0, D - D0) / L, 1)

def calcular_DhPT_I_ai(X: float, s0: float,I: float, I0: float, L: float) -> float:
    return round(abs(X) * s0 * max(0, I - I0) / L, 1)

def calcular_Dhg_a(X: float, L: float, TD: float) -> float:
    return round((abs(X) / L + 0.5) * TD, 1)

def calcular_Dhg_i(X: float, L: float, TD: float) -> float:
    return round((abs(X) / L - 0.5) * TD, 1)

def calcular_Dhc(X: float, s0: float, L: float, TD: float) -> float:
    return round(s0 * abs(X) * TD / L, 1)

def calcular_Dhsusp_ai(X: float, ang: float) -> float:
    return round(abs(X * 1000) * tan(radians(ang)), 1)

def calcular_Dhcarg_ai(X: float, ang: float) -> float:
    return round(abs(X * 1000) * tan(radians(ang)), 1)

def calcular_Dheta0_ai(X: float, ang: float) -> float:
    return round(abs(X * 1000) * tan(radians(ang)), 1)

def calcular_Dhosc(X: float, ang: float) -> float:
    return round(abs(X * 1000) * tan(radians(ang)), 1)

def calcular_lim_Sj1(Y: float, hco: float, k: float, kale: float, Tvia: float, Dbgai: float, Dbcai: float, Dbsusp: float, dbcarg: float, dbosc: float) -> float:
    keff = kale if Y < hco else k
    res = keff * (Tvia**2 + (Dbgai + dbcarg)**2 + (Dbsusp**2 + dbcarg**2 + dbosc**2))**0.5
    return round(res,1)

def calcular_lim_Sj2(Y: float, hco: float, k: float, kale: float, Tvia: float, Dbgai: float) -> float:
    keff = kale if Y < hco else k
    res = keff * (Tvia**2 + Dbgai**2)**0.5
    return round(res,1)

def calcular_lim_Sj_ast(Y: float, hco: float, k: float, kale: float, radic: float) -> float:
    keff = kale if Y < hco else k
    signo = 1 if radic > 0 else -1
    res = keff * signo * abs(radic)
    return round(res, 1)

def calcular_lim_rad_SVi1(TN: float, Dhgi: float, Dhc: float, Dhsusp: float, Dhcarg: float, Dhosci: float) -> float:
    res = TN**2 + (max(0, -Dhgi - Dhc))**2 - (Dhsusp**2 + Dhcarg**2 + Dhosci**2)
    return round(res, 1)

def calcular_lim_rad_SVa1(TN: float, Dhga: float, Dhc: float, Dhsusp: float, Dhcarg: float, Dhosci: float) -> float:
    res = TN**2 - (-Dhga + Dhc)**2 - (Dhsusp**2 + Dhcarg**2 + Dhosci**2)
    return round(res, 1)

def calcular_lim_SV1(k: float, radic: float) -> float:
    signo = 1 if radic > 0 else -1
    res = k * signo * abs(radic)
    return round(res, 1)

def calcular_SVa1_ast(k: float, TN: float, Dhga: float, Dhc: float, Dhsusp: float, Dhcarg: float, Dhosci: float) -> float:
    res = k * (TN**2 + (Dhga + Dhc)**2 + (Dhsusp**2 + Dhcarg**2 + Dhosci**2))**0.5
    return round(res, 1)

def calcular_SVi1_ast(k: float, TN: float, Dhgi: float, Dhc: float, Dhsusp: float, Dhcarg: float, Dhosci: float) -> float:
    res = k * (TN**2 + (max(0, Dhgi + Dhc))**2 + (Dhsusp**2 + Dhcarg**2 + Dhosci**2))**0.5
    return round(res, 1)