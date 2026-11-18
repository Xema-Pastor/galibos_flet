"""Cálculo completo de una vía: parámetros generales, gálibos límite/nominal y pantógrafo.

Este módulo no depende de FLET. Recibe un objeto `Via` ya rellenado con los datos de
entrada y devuelve copias propias de los contornos de referencia con los resultados,
de modo que dos vías (o dos sesiones web) nunca comparten los mismos objetos.
"""
from copy import deepcopy
from dataclasses import dataclass
from math import atan, degrees

import calculos.calculos as calc
from datos_galibos import datos_GPA, datos_GPB, datos_Pantografo
from estilos.estilos import EGPA, ETV, EEV, TIPO_PANT, TENSION_CAT, TIPO_LINEA, TIPO_CAT

# ---------------------------------------------------------------------------
# Familias de gálibos de partes altas
# ---------------------------------------------------------------------------
GALIBOS_IBERICOS = {EGPA.GHE16.value, EGPA.GEA16.value, EGPA.GEB16.value, EGPA.GEC16.value}
GALIBOS_INTERNACIONALES = {EGPA.GA.value, EGPA.GB.value, EGPA.GC.value}
GALIBOS_METRICOS = {EGPA.GEE10.value, EGPA.GED10.value, EGPA.PERSONALIZADO.value}
GALIBOS_ANCHO_ESTANDAR = GALIBOS_IBERICOS | GALIBOS_INTERNACIONALES

# (LN, L) por familia: ancho de vía nominal y distancia entre círculos de rodadura (m)
ANCHOS = {
    "iberico": (1.668, 1.733),
    "internacional": (1.435, 1.5),
    "metrico": (1.0, 1.055),
}

# (hquiebroaux, htopeaux, difaux, hotra) para los gálibos con quiebro en partes altas
PARAMETROS_QUIEBRO = {
    EGPA.GEA16.value: (3.32, 3.70, 0.38, 4.84),
    EGPA.GEB16.value: (3.32, 4.11, 0.79, 6.48),
    EGPA.GA.value: (3.35, 3.88, 0.63, 5.77),
    EGPA.GB.value: (3.35, 4.11, 0.86, 6.69),
}

# Giros por oscilaciones aleatorias (º): (i, s0=0.4), (i, s0=0.3), (a, s0=0.4), (a, s0=0.3).
# Los valores son los mismos para los incrementos horizontales y verticales.
_AOSC_BUENO = (0.1, 0.08, 0.6, 0.45)
_AOSC_MALO = (0.2, 0.15, 1.0, 0.75)
AOSC = {
    ("estandar", ETV.VIA_PLACA.value, EEV.BUEN_ESTADO.value): _AOSC_BUENO,
    ("estandar", ETV.VIA_PLACA.value, EEV.MAL_ESTADO.value): _AOSC_BUENO,
    ("estandar", ETV.BALASTO.value, EEV.BUEN_ESTADO.value): _AOSC_BUENO,
    ("estandar", ETV.BALASTO.value, EEV.MAL_ESTADO.value): _AOSC_MALO,
    ("metrico", ETV.VIA_PLACA.value, EEV.BUEN_ESTADO.value): (0.1, 0.1, 0.6, 0.6),
    ("metrico", ETV.VIA_PLACA.value, EEV.MAL_ESTADO.value): (0.1, 0.1, 0.6, 0.6),
    ("metrico", ETV.BALASTO.value, EEV.BUEN_ESTADO.value): (0.2, 0.2, 1.0, 1.0),
    ("metrico", ETV.BALASTO.value, EEV.MAL_ESTADO.value): (0.2, 0.2, 1.0, 1.0),
}

# Pantógrafo: (bp, bw, epo, epu, D0p, I0p)
PANTOGRAFOS = {
    TIPO_PANT.ANCHO_1600.value: (1.6, 0.8, 0.17, 0.11, 0.067, 0.067),
    TIPO_PANT.ANCHO_1700.value: (1.7, 0.85, 0.15, 0.082, 0.07, 0.07),
    TIPO_PANT.ANCHO_1950.value: (1.9, 0.975, 0.17, 0.11, 0.067, 0.067),
}
# Tensión de la catenaria: (belec_estat, belec_dinam)
AISLAMIENTOS = {
    TENSION_CAT.CC_1500.value: (0.1, 0.05),
    TENSION_CAT.CC_3000.value: (0.15, 0.05),
    TENSION_CAT.CA_25000.value: (0.27, 0.15),
}
# Tipo de línea: cw
TROCADORES = {
    TIPO_LINEA.EXISTENTES.value: 0.2,
    TIPO_LINEA.NUEVAS.value: 0.0,
}
# Tipo de catenaria: (fsvmax, fsvmin)
ELEVACIONES = {
    TIPO_CAT.CA160.value: (0.195, 0.078),
    TIPO_CAT.CA220.value: (0.148, 0.045),
    TIPO_CAT.CAU220.value: (0.152, 0.046),
    TIPO_CAT.SICAT.value: (0.154, 0.04),
    TIPO_CAT.EAC350.value: (0.162, 0.041),
    TIPO_CAT.RIGIDA.value: (0.015, 0.015),
}

RECTA = 999999      # Radio equivalente a una alineación recta (m)


@dataclass
class ResultadoVia:
    galiboPA: dict      # Contorno de partes altas con todos los resultados por punto
    galiboPB: dict      # Contorno de partes bajas (solo geometría)
    galiboPant: dict    # Pantógrafo con todos los resultados por punto


def familia(gpa: str) -> str:
    if gpa in GALIBOS_IBERICOS:
        return "iberico"
    if gpa in GALIBOS_INTERNACIONALES:
        return "internacional"
    return "metrico"


def signo(num: float) -> int:
    return 1 if num >= 0 else -1


def calcular_via(via) -> ResultadoVia:
    """Calcula todos los resultados de la vía a partir de sus datos de entrada."""
    galiboPA = deepcopy(datos_GPA[via.GPA])
    galiboPB = datos_GPB[via.GPB]                   # No se modifica: no hace falta copiarlo
    galiboPant = deepcopy(datos_Pantografo[via.tipo_pant])

    calcular_parametros(via, galiboPA)
    for punto in galiboPA.values():
        calcular_punto(via, punto)
    calcular_pantografo(via, galiboPant)

    return ResultadoVia(galiboPA, galiboPB, galiboPant)


# ---------------------------------------------------------------------------
# Variables generales de la vía
# ---------------------------------------------------------------------------
def calcular_parametros(via, galibo: dict) -> None:
    fam = familia(via.GPA)
    metrico = fam == "metrico"

    via.maxY = max(0, max(punto.Y for punto in galibo.values()))
    if metrico:
        via.hb_max = (galibo["P1"].Y + galibo["P2"].Y) / 2
    else:
        via.hb_max = (galibo["P3"].Y + galibo["P4"].Y) / 2
    via.hquiebroaux, via.htopeaux, via.difaux, via.hotra = PARAMETROS_QUIEBRO.get(via.GPA, (0, 0, 0, 0))
    via.LN, via.L = ANCHOS[fam]

    via.R = RECTA if via.es_recta else via.R_entrada
    via.Rv = RECTA if via.es_recta_V else via.Rv_entrada

    via.LND = via.LN + via.DL
    via.D0 = via.I0 = 0.07 if metrico else 0.05

    # La inclinación se calcula con el peralte ya actualizado
    if via.girado:
        inclinacion = abs(degrees(atan(via.D / via.LN)))
        via.Inclinac = inclinacion if via.lado_inclinacion == "A derechas" else -inclinacion
    else:
        via.Inclinac = 0.0

    via.heq = round((via.vmax / 3.6) ** 2 * via.LN / (via.R * 9.81), 4)

    if via.tipo_via == ETV.VIA_PLACA.value:
        via.TVIA, via.TD = 0.005, 0.015
    elif via.tipo_via == ETV.BALASTO.value:
        via.TVIA = 0.025
        via.TD = 0.02 if via.vmax <= 80 else 0.015

    via.eta0 = via.asusp + via.acarga

    aosc = AOSC.get(("metrico" if metrico else "estandar", via.tipo_via, via.estado_via))
    if aosc:
        via.aosc_i_s0_04b, via.aosc_i_s0_03b, via.aosc_a_s0_04b, via.aosc_a_s0_03b = aosc
        via.aosc_i_s0_04h, via.aosc_i_s0_03h, via.aosc_a_s0_04h, via.aosc_a_s0_03h = aosc

    via.DhRV = round(50 / via.Rv, 2)

    # Pantógrafo y catenaria
    if via.tipo_pant in PANTOGRAFOS:
        via.bp, via.bw, via.epo, via.epu, via.D0p, via.I0p = PANTOGRAFOS[via.tipo_pant]
    if via.ten_cat in AISLAMIENTOS:
        via.belec_estat, via.belec_dinam = AISLAMIENTOS[via.ten_cat]
    if via.tipo_lin in TROCADORES:
        via.cw = TROCADORES[via.tipo_lin]
    if via.tipo_cat in ELEVACIONES:
        via.fsvmax, via.fsvmin = ELEVACIONES[via.tipo_cat]

    via.heffvmax = via.hf + via.fsvmax + via.fwswa
    via.heffvmin = via.hf + via.fsvmin + via.fwswa
    via.heffelecvmax = via.heffvmax + via.belec_dinam
    via.heffelecvmin = via.heffvmin + via.belec_estat
    via.heff = max(via.heffvmax, via.heffvmin)
    via.heffelec = max(via.heffelecvmax, via.heffelecvmin)


# ---------------------------------------------------------------------------
# Desplazamientos y gálibos de cada punto del contorno de referencia
# ---------------------------------------------------------------------------
def calcular_punto(via, punto) -> None:
    Y_m = punto.Y / 1000
    X_m = punto.X / 1000
    hco_mm = via.hco * 1000

    punto.esPT = calc.calcular_esPT(punto.Y, via.maxY)
    punto.k = calc.calcular_k(via.GPA, Y_m, via.hquiebroaux, via.htopeaux, via.difaux)
    punto.s0 = calc.calcular_s0(via.GPA, Y_m, via.hquiebroaux, via.htopeaux, via.difaux, via.hotra)
    punto.Sa = calc.calcular_Sa(via.GPA, via.GPB, via.R, via.LN, via.LND, via.hquiebroaux, Y_m, punto.k)
    punto.Si = calc.calcular_Si(via.GPA, via.GPB, via.R, via.LN, via.LND, via.hquiebroaux, Y_m, punto.k)
    punto.qsD_ai = calc.calcular_qsD_ai(Y_m, punto.s0, via.D, via.D0, via.L, via.hco)
    punto.qsI_ai = calc.calcular_qsI_ai(Y_m, punto.s0, via.I, via.I0, via.L, via.hco)
    punto.Tvia_ai = via.TVIA * 1000
    punto.Dbg_ai = calc.calcular_Dbg_ai(Y_m, via.L, via.TD)
    punto.Dbc_ai = calc.calcular_Dbc_ai(Y_m, via.L, via.TD, via.hco, punto.s0)
    punto.Dbsusp_ai = calc.calcular_Dbsusp_ai(via.asusp, punto.Y, hco_mm)
    punto.Dbcarg_ai = calc.calcular_Dbcarg_ai(via.acarga, punto.Y, hco_mm)
    punto.Dbeta0_ai = calc.calcular_Dbeta0_ai(via.eta0, punto.Y, hco_mm)
    punto.aosc_a = calc.calcular_aosc(punto.s0, via.aosc_a_s0_03b, via.aosc_a_s0_04b)
    punto.aosc_i = calc.calcular_aosc(punto.s0, via.aosc_i_s0_03b, via.aosc_i_s0_04b)
    punto.Dbosc_a = calc.calcular_Dbosc(punto.aosc_a, punto.Y, hco_mm)
    punto.Dbosc_i = calc.calcular_Dbosc(punto.aosc_i, punto.Y, hco_mm)
    punto.M3b = via.M3b * 1000
    punto.DhRv = round(via.DhRV * 1000, 1)
    punto.DhPT_D_ai = calc.calcular_DhPT_D_ai(punto.X, punto.s0, via.D, via.D0, via.L)
    punto.DhPT_I_ai = calc.calcular_DhPT_I_ai(punto.X, punto.s0, via.I, via.I0, via.L)
    punto.TN = via.TN * 1000
    punto.Dhg_a = calc.calcular_Dhg_a(X_m, via.L, via.TD)
    punto.Dhg_i = calc.calcular_Dhg_i(X_m, via.L, via.TD)
    punto.Dhc = calc.calcular_Dhc(X_m, punto.s0, via.L, via.TD)
    punto.Dhgca = round(punto.Dhg_a + punto.Dhc, 1)
    punto.Dhgci = round(punto.Dhg_i + punto.Dhc, 1)
    punto.Dhsusp_ai = calc.calcular_Dhsusp_ai(punto.X, via.asusp)
    punto.Dhcarg_ai = calc.calcular_Dhcarg_ai(punto.X, via.acarga)
    punto.Dheta0_ai = calc.calcular_Dheta0_ai(punto.X, via.eta0)
    punto.Dhosc_a = calc.calcular_Dhosc(punto.X, punto.aosc_i)      # Sí, los ángulos están cambiados. Así debe ser.
    punto.Dhosc_i = calc.calcular_Dhosc(punto.X, punto.aosc_a)      # Sí, los ángulos están cambiados. Así debe ser.
    punto.M3h = via.M3h * 1000

    # Desplazamientos aleatorios para el gálibo límite
    kale = via.Kale_h_0_50
    punto.lim_Sja1 = calc.calcular_lim_Sj1(Y_m, via.hco, via.K, kale, punto.Tvia_ai, punto.Dbg_ai, punto.Dbc_ai, punto.Dbsusp_ai, punto.Dbcarg_ai, punto.Dbosc_a)
    punto.lim_Sji1 = calc.calcular_lim_Sj1(Y_m, via.hco, via.K, kale, punto.Tvia_ai, punto.Dbg_ai, punto.Dbc_ai, punto.Dbsusp_ai, punto.Dbcarg_ai, punto.Dbosc_i)
    punto.lim_Sja2 = calc.calcular_lim_Sj2(Y_m, via.hco, via.K, kale, punto.Tvia_ai, punto.Dbg_ai)
    punto.lim_Sji2 = punto.lim_Sja2
    punto.lim_rad_Sja1_ast = calc.calcular_lim_rad_Sj1(punto.Tvia_ai, punto.Dbg_ai, punto.Dbc_ai, punto.Dbsusp_ai, punto.Dbcarg_ai, punto.Dbosc_a)
    punto.lim_rad_Sji1_ast = calc.calcular_lim_rad_Sj1(punto.Tvia_ai, punto.Dbg_ai, punto.Dbc_ai, punto.Dbsusp_ai, punto.Dbcarg_ai, punto.Dbosc_i)
    punto.lim_rad_Sjai2_ast = calc.calcular_lim_rad_Sj2(punto.Tvia_ai, punto.Dbg_ai)
    punto.lim_Sja1_ast = calc.calcular_lim_Sj_ast(Y_m, via.hco, via.K, kale, punto.lim_rad_Sja1_ast)
    punto.lim_Sji1_ast = calc.calcular_lim_Sj_ast(Y_m, via.hco, via.K, kale, punto.lim_rad_Sji1_ast)
    punto.lim_Sja2_ast = calc.calcular_lim_Sj_ast(Y_m, via.hco, via.K, kale, punto.lim_rad_Sjai2_ast)
    punto.lim_Sji2_ast = punto.lim_Sja2_ast
    punto.lim_rad_SVi1 = calc.calcular_lim_rad_SVi1(punto.TN, punto.Dhg_i, punto.Dhc, punto.Dhsusp_ai, punto.Dhcarg_ai, punto.Dhosc_i)
    punto.lim_rad_SVa1 = calc.calcular_lim_rad_SVa1(punto.TN, punto.Dhg_a, punto.Dhc, punto.Dhsusp_ai, punto.Dhcarg_ai, punto.Dhosc_a)
    punto.lim_SVa1 = calc.calcular_lim_SV1(via.K, punto.lim_rad_SVa1)
    punto.lim_SVi1 = calc.calcular_lim_SV1(via.K, punto.lim_rad_SVi1)
    punto.lim_SVa1_ast = calc.calcular_SVa1_ast(via.K, punto.TN, punto.Dhg_a, punto.Dhc, punto.Dhsusp_ai, punto.Dhcarg_ai, punto.Dhosc_a)
    punto.lim_SVi1_ast = calc.calcular_SVi1_ast(via.K, punto.TN, punto.Dhg_i, punto.Dhc, punto.Dhsusp_ai, punto.Dhcarg_ai, punto.Dhosc_i)
    punto.lim_SVa2 = punto.lim_SVi2 = punto.lim_SVa2_ast = punto.lim_SVi2_ast = punto.TN

    # Desplazamientos aleatorios para el gálibo nominal
    punto.nom_Sja3 = calc.calcular_nom_Sj3(punto.Tvia_ai, punto.Dbg_ai, punto.Dbc_ai, punto.Dbsusp_ai, punto.Dbcarg_ai, punto.Dbosc_a)
    punto.nom_Sji3 = calc.calcular_nom_Sj3(punto.Tvia_ai, punto.Dbg_ai, punto.Dbc_ai, punto.Dbsusp_ai, punto.Dbcarg_ai, punto.Dbosc_i)
    punto.nom_Sja4 = punto.nom_Sji4 = calc.calcular_nom_Sj4(punto.Tvia_ai, punto.Dbg_ai)
    punto.nom_Sja3_ast = calc.calcular_nom_Sj3_ast(punto.Tvia_ai, punto.Dbg_ai, punto.Dbc_ai, punto.Dbsusp_ai, punto.Dbcarg_ai, punto.Dbosc_a)
    punto.nom_Sji3_ast = calc.calcular_nom_Sj3_ast(punto.Tvia_ai, punto.Dbg_ai, punto.Dbc_ai, punto.Dbsusp_ai, punto.Dbcarg_ai, punto.Dbosc_i)
    punto.nom_Sja4_ast = punto.nom_Sji4_ast = calc.calcular_nom_Sj4_ast(punto.Tvia_ai, punto.Dbg_ai)
    punto.nom_SVa3 = calc.calcular_nom_SV3a(punto.TN, punto.Dhg_a, punto.Dhc, punto.Dhsusp_ai, punto.Dhcarg_ai, punto.Dhosc_a)
    punto.nom_SVi3 = calc.calcular_nom_SV3i(punto.TN, punto.Dhg_i, punto.Dhc, punto.Dhsusp_ai, punto.Dhcarg_ai, punto.Dhosc_i)
    punto.nom_SVa3_ast = calc.calcular_nom_SV3a_ast(punto.TN, punto.Dhg_a, punto.Dhc, punto.Dhsusp_ai, punto.Dhcarg_ai, punto.Dhosc_a)
    punto.nom_SVi3_ast = calc.calcular_nom_SV3i_ast(punto.TN, punto.Dhg_i, punto.Dhc, punto.Dhsusp_ai, punto.Dhcarg_ai, punto.Dhosc_i)
    punto.nom_SVa4 = punto.nom_SVi4 = punto.nom_SVa4_ast = punto.nom_SVi4_ast = punto.TN

    calcular_obstaculos(via, punto, "lim", (1, 2))
    calcular_obstaculos(via, punto, "nom", (3, 4))


def calcular_obstaculos(via, punto, prefijo: str, indices: tuple) -> None:
    """Coordenadas de obstáculo (b, h) y envolventes del gálibo límite ("lim") o nominal ("nom").

    Para cada lado (i: interior, a: exterior) y cada situación de velocidad
    (VM: velocidad máxima, se usa la insuficiencia I; V0: parado, se usa el peralte D)
    se obtienen cuatro combinaciones:
        b..._max / h..._con -> desplazamientos aleatorios Σj, ΣV
        b..._con / h..._max -> desplazamientos aleatorios Σj*, ΣV*
    """
    n1, n2 = indices
    nominal = prefijo == "nom"
    Y_m = punto.Y / 1000

    def valor(nombre):
        return getattr(punto, f"{prefijo}_{nombre}")

    def bobst(S, qs, j1, j2):
        if nominal:
            return calc.calcular_nom_bobst(punto.X, Y_m, S, qs, j1, j2, punto.M3b)
        return calc.calcular_lim_bobst(punto.X, Y_m, S, qs, j1, j2)

    def hobst(DhPT, SV1, SV2):
        if nominal:
            return calc.calcular_nom_hobst(punto.Y, punto.DhRv, via.hb_max, punto.esPT, DhPT, SV1, SV2, punto.M3h)
        return calc.calcular_lim_hobst(punto.Y, punto.DhRv, via.hb_max, punto.esPT, DhPT, SV1, SV2)

    for lado, S in (("i", punto.Si), ("a", punto.Sa)):
        sgn = -1 if lado == "i" else 1
        situaciones = {
            "VM": (sgn * punto.qsI_ai, -sgn * punto.DhPT_I_ai),
            "V0": (-sgn * punto.qsD_ai, sgn * punto.DhPT_D_ai),
        }
        j1, j2 = valor(f"Sj{lado}{n1}"), valor(f"Sj{lado}{n2}")
        j1_ast, j2_ast = valor(f"Sj{lado}{n1}_ast"), valor(f"Sj{lado}{n2}_ast")
        SV1, SV2 = valor(f"SV{lado}{n1}"), valor(f"SV{lado}{n2}")
        SV1_ast, SV2_ast = valor(f"SV{lado}{n1}_ast"), valor(f"SV{lado}{n2}_ast")

        for vel, (qs, DhPT) in situaciones.items():
            setattr(punto, f"{prefijo}_bobst{vel}_max_{lado}", bobst(S, qs, j1, j2))
            setattr(punto, f"{prefijo}_hobst{vel}_con_{lado}", hobst(DhPT, SV1, SV2))
            setattr(punto, f"{prefijo}_bobst{vel}_con_{lado}", bobst(S, qs, j1_ast, j2_ast))
            setattr(punto, f"{prefijo}_hobst{vel}_max_{lado}", hobst(DhPT, SV1_ast, SV2_ast))

        b = [valor(f"bobst{vel}_{tipo}_{lado}") for vel in ("VM", "V0") for tipo in ("max", "con")]
        setattr(punto, f"{prefijo}_b{lado}", signo(punto.X) * max(abs(x) for x in b))
        setattr(punto, f"{prefijo}_h{lado}", calc.calcular_h(
            Y_m, via.hb_max / 1000,
            valor(f"hobstVM_con_{lado}"), valor(f"hobstVM_max_{lado}"),
            valor(f"hobstV0_con_{lado}"), valor(f"hobstV0_max_{lado}"),
        ))


# ---------------------------------------------------------------------------
# Pantógrafo (misma formulación que la versión original)
# ---------------------------------------------------------------------------
def calcular_pantografo(via, galiboPant: dict) -> None:
    for nombre, punto in galiboPant.items():
        punto.S_ai = calc.calcular_pant_Sai(via.GPA, via.R, via.LN, via.LND)
        punto.qs_a = calc.calcular_pant_qsa(via.GPA, punto.Y_ref/1000, via.I, via.hco)
        punto.qs_i = calc.calcular_pant_qsi(via.GPA, punto.Y_ref/1000, via.D, via.hco)
        punto.Dbg_ai = calc.calcular_pant_Dbg_ai(punto.Y_ref/1000, via.L, via.TD)            #Se usa la fórmula general porque es igual en los pantografos que en los galibos normales
        punto.Dbc_ai = calc.calcular_pant_Dbc_ai(punto.Y_ref/1000, via.L, via.TD, via.hco)
        punto.Dbsusp_ai = calc.calcular_Dbsusp_ai(via.asusp, punto.Y_ref, via.hco * 1000)
        punto.Dbcarg_ai = calc.calcular_Dbcarg_ai(via.acarga, punto.Y_ref, via.hco * 1000)
        punto.Dbeta0_ai = calc.calcular_Dbeta0_ai(via.eta0, punto.Y_ref, via.hco * 1000)
        punto.aosc_a = calc.calcular_pant_aosc(via.tipo_via, via.estado_via, via.LN, "a")
        punto.aosc_i = calc.calcular_pant_aosc(via.tipo_via, via.estado_via, via.LN, "i")
        punto.Dbosc_a = calc.calcular_Dbosc(punto.aosc_a, punto.Y_ref, via.hco * 1000)
        punto.Dbosc_i = calc.calcular_Dbosc(punto.aosc_i, punto.Y_ref, via.hco * 1000)
        punto.Tvia_ai = via.TVIA * 1000
        punto.Sja = calc.calcular_pant_Sj(punto.Tvia_ai, punto.Dbg_ai, punto.Dbc_ai, punto.Dbsusp_ai, punto.Dbcarg_ai, punto.Dbosc_a)
        punto.Sji = calc.calcular_pant_Sj(punto.Tvia_ai, punto.Dbg_ai, punto.Dbc_ai, punto.Dbsusp_ai, punto.Dbcarg_ai, punto.Dbosc_i)
        punto.bobst_a = calc.calcular_pant_bobst(nombre, via.bw * 1000, via.epo * 1000, via.epu * 1000, punto.S_ai, punto.qs_a, punto.Sja)
        punto.bobst_i = calc.calcular_pant_bobst(nombre, via.bw * 1000, via.epo * 1000, via.epu * 1000, punto.S_ai, punto.qs_i, punto.Sji)

    #Debo parar el bucle porque tengo que calcular las diferencias de bobst entre distintos puntos del bucle
    Dbobst_a_12 = galiboPant["P2"].bobst_a - galiboPant["P1"].bobst_a
    Dbobst_a_34 = galiboPant["P3"].bobst_a - galiboPant["P4"].bobst_a
    Dbobst_i_12 = galiboPant["P2"].bobst_i - galiboPant["P1"].bobst_i
    Dbobst_i_34 = galiboPant["P3"].bobst_i - galiboPant["P4"].bobst_i
    Dy = galiboPant["P3"].Y_ref - galiboPant["P4"].Y_ref             #Da igual coger el 2 que el 3, porque son iguales. Idem con 1 y 4
    BLA_BLA_BLA = "A derechas"
    if BLA_BLA_BLA == "A derechas":
        lado = 1
    elif BLA_BLA_BLA == "A izquierdas":
        lado = 2

    '''
    IMPORTANTE
    Tengo que hacer esto del lado dinámico. lo tiene que leer de ftElem_1.cb_graf_inclinacion o ftElem_2.cb_graf_inclinacion
    '''
    for nombre, punto in galiboPant.items():
        punto.bobst_a_hmax = calc.calcular_pant_bobst_hmax_a(nombre, punto.bobst_a, Dbobst_a_12, Dbobst_a_34, Dy, via.heff * 1000, galiboPant)
        punto.bobst_i_hmax = calc.calcular_pant_bobst_hmax_i(nombre, punto.bobst_i, Dbobst_i_12, Dbobst_i_34, Dy, via.heff * 1000, galiboPant)
        punto.bobst_a_hmax_heff_elec = calc.calcular_pant_bobst_hmax_a(nombre, punto.bobst_a, Dbobst_a_12, Dbobst_a_34, Dy, via.heffelec * 1000, galiboPant)
        punto.bobst_i_hmax_heff_elec = calc.calcular_pant_bobst_hmax_i(nombre, punto.bobst_i, Dbobst_i_12, Dbobst_i_34, Dy, via.heffelec * 1000, galiboPant)
        punto.bobst_a_hmax_elec = calc.calcular_pant_elec(punto.bobst_a_hmax_heff_elec, via.belec_dinam * 1000, via.cw * 1000)
        punto.bobst_i_hmax_elec = calc.calcular_pant_elec(punto.bobst_i_hmax_heff_elec, via.belec_estat * 1000, via.cw * 1000)

        punto.X_mec = calc.calcular_pant_pant_mec_X(punto.X_ref, punto.bobst_a, punto.bobst_i, lado)
        punto.Y_mec = calc.calcular_pant_pant_mec_Y(nombre, punto.Y_ref, 1000 * via.heff)
        punto.X_elec = calc.calcular_pant_pant_mec_X(punto.X_ref, punto.bobst_a_hmax_elec, punto.bobst_i_hmax_elec, lado)
        punto.Y_elec = calc.calcular_pant_pant_mec_Y(nombre, punto.Y_ref, 1000 * via.heffelec)
