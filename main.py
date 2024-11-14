import flet as ft
import configuracion as conf
from datos_galibos import datos_GPA, datos_GPB
from datos_variables import via1, via2
from estilos.estilos import Tamanyos, EGPA, EGPB, ETV, EEV
from componentes.comp_tablas import tabla_des, tabla_lim, tabla_nom, fttabla
from componentes.comp_textos import ftt
from componentes.comp_graficos import *
from componentes.mis_componentes import *
import calculos.calculos as calc
from math import sin, cos, atan, degrees, radians

def galibos(page: ft.Page):

    def cambiar_variables(galiboPA):
        
        #CÁLCULO DE LAS VARIABLES GENERALES DEL PROGRAMA
        via1.maxY = 0
        for nombre,punto in galiboPA.items():                                   #intentar hacer esto con la función max y una lambda
            if punto.Y > via1.maxY:
                via1.maxY = punto.Y
        match via1.GPA:
            case EGPA.GHE16.value | EGPA.GEA16.value | EGPA.GEB16.value | EGPA.GEC16.value | EGPA.GA.value | EGPA.GB.value | EGPA.GC.value:
                via1.hb_max = ( galiboPA["P3"].Y + galiboPA["P4"].Y ) / 2
            case EGPA.GEE10.value |EGPA.GED10.value | EGPA.PERSONALIZADO.value:
                via1.hb_max = ( galiboPA["P1"].Y + galiboPA["P2"].Y ) / 2
        match via1.GPA:
            case EGPA.GEA16.value | EGPA.GEB16.value: via1.hquiebroaux = 3.32
            case EGPA.GA.value | EGPA.GB.value: via1.hquiebroaux = 3.35
            case other: via1.hquiebroaux = 0
        match via1.GPA:
            case EGPA.GEA16.value: via1.htopeaux = 3.7
            case EGPA.GEB16.value | EGPA.GB.value: via1.htopeaux = 4.11
            case EGPA.GA.value: via1.htopeaux = 3.88
            case other: via1.htopeaux = 0
        match via1.GPA:
            case EGPA.GEA16.value: via1.difaux = 0.38
            case EGPA.GEB16.value: via1.difaux = 0.79
            case EGPA.GA.value: via1.difaux = 0.63
            case EGPA.GB.value: via1.difaux = 0.86
            case other: via1.difaux = 0
        match via1.GPA:
            case EGPA.GEA16.value: via1.otra = 4.84
            case EGPA.GEB16.value: via1.otra = 6.48
            case EGPA.GA.value: via1.otra = 5.77
            case EGPA.GB.value: via1.otra = 6.69
            case other: via1.otra = 0
        match via1.GPA:
            case EGPA.GHE16.value | EGPA.GEA16.value | EGPA.GEB16.value | EGPA.GEC16.value: via1.LN = 1.668
            case EGPA.GA.value | EGPA.GB.value | EGPA.GC.value: via1.LN = 1.435
            case EGPA.GEE10.value |EGPA.GED10.value | EGPA.PERSONALIZADO.value: via1.LN = 1

        #COMPROBACIÓN DE LOS CHECKBOXES: RADIOS EN PLANTA Y ALZADO, E INCLINACIÓN DEL GRÁFICO
        es_recta = cb_R.value
        es_recta_V = cb_RV.value
        es_girado = cb_graf_esGirado.value
        via1.R = 999999 if es_recta else int(tf_R.value)
        via1.Rv = 999999 if es_recta_V else int(tf_RV.value)
        tf_R.disabled = es_recta
        tf_RV.disabled = es_recta_V
        cb_graf_inclinacion.disabled = not es_girado
        via1.Inclinac = 0.0 if not es_girado else degrees(atan(via1.D / via1.LN))
        lado_inclinacion = cb_graf_inclinacion.value
        if lado_inclinacion == "A derechas":
            via1.Inclinac = abs(via1.Inclinac)
        elif lado_inclinacion == "A izquierdas":
            via1.Inclinac = -abs(via1.Inclinac)

        via1.DL = tf_DL.value
        via1.LND = via1.LN + via1.DL
        via1.D = float(tf_D.value)
        match via1.GPA:
            case EGPA.GHE16.value | EGPA.GEA16.value | EGPA.GEB16.value | EGPA.GEC16.value | EGPA.GA.value | EGPA.GB.value | EGPA.GC.value: via1.D0 = 0.05
            case EGPA.GEE10.value |EGPA.GED10.value | EGPA.PERSONALIZADO.value: via1.D0 = 0.07
        via1.vmax = tf_vmax.value
        via1.heq = round((float(via1.vmax) / 3.6)**2 * via1.LN / (float(via1.R) * 9.81), 4)
        #via1.I = via1.heq - via1.D
        via1.I = float(tf_I.value)
        match via1.GPA:
            case EGPA.GHE16.value | EGPA.GEA16.value | EGPA.GEB16.value | EGPA.GEC16.value | EGPA.GA.value | EGPA.GB.value | EGPA.GC.value: via1.I0 = 0.05
            case EGPA.GEE10.value |EGPA.GED10.value | EGPA.PERSONALIZADO.value: via1.I0 = 0.07
        match via1.GPA:
            case EGPA.GHE16.value | EGPA.GEA16.value | EGPA.GEB16.value | EGPA.GEC16.value: via1.L = 1.733
            case EGPA.GA.value | EGPA.GB.value | EGPA.GC.value: via1.L = 1.5
            case EGPA.GEE10.value |EGPA.GED10.value | EGPA.PERSONALIZADO.value: via1.L = 1.055
        via1.tipo_via = dd_TV.value
        match via1.tipo_via:
            case ETV.VIA_PLACA.value:
                via1.TVIA = 0.005
                via1.TD = 0.015
            case ETV.BALASTO.value:
                via1.TVIA = 0.025
                via1.TD = 0.02 if int(via1.vmax) <=80 else 0.015
        via1.asusp = tf_tol_sus.value
        via1.acarga = tf_tol_carga.value
        via1.eta0 = float(via1.asusp) + float(via1.acarga)
        via1.estado_via = dd_EV.value
        if via1.GPA in [EGPA.GEE10.value, EGPA.GED10.value, EGPA.PERSONALIZADO.value]:
            via1.aosc_i_s0_04b = 0.20 if via1.tipo_via == ETV.BALASTO.value else 0.1
            via1.aosc_a_s0_04b = 1.00 if via1.tipo_via == ETV.BALASTO.value else 0.6
            via1.aosc_i_s0_03b = 0.20 if via1.tipo_via == ETV.BALASTO.value else 0.1
            via1.aosc_a_s0_03b = 1.00 if via1.tipo_via == ETV.BALASTO.value else 0.6
        elif via1.GPA in [EGPA.GHE16.value, EGPA.GEA16.value, EGPA.GEB16.value, EGPA.GEC16.value, EGPA.GA.value, EGPA.GB.value, EGPA.GC.value]:
            if via1.tipo_via == ETV.VIA_PLACA.value:
                via1.aosc_i_s0_04b = 0.1
                via1.aosc_a_s0_04b = 0.6
                via1.aosc_i_s0_03b = 0.08
                via1.aosc_a_s0_03b = 0.45
            elif via1.tipo_via == ETV.BALASTO.value:
                if via1.estado_via == EEV.BUEN_ESTADO.value:
                    via1.aosc_i_s0_04b = 0.1
                    via1.aosc_a_s0_04b = 0.6
                    via1.aosc_i_s0_03b = 0.08
                    via1.aosc_a_s0_03b = 0.45
                elif via1.estado_via == EEV.MAL_ESTADO.value:
                    via1.aosc_i_s0_04b = 0.2
                    via1.aosc_a_s0_04b = 1.0
                    via1.aosc_i_s0_03b = 0.15
                    via1.aosc_a_s0_03b = 0.75

        via1.DhRV = round(50/float(via1.Rv), 2)
        if via1.GPA in [EGPA.GHE16.value, EGPA.GEA16.value, EGPA.GEB16.value, EGPA.GEC16.value, EGPA.GA.value, EGPA.GB.value, EGPA.GC.value]:
            if via1.tipo_via == ETV.BALASTO.value and via1.estado_via == EEV.BUEN_ESTADO.value:
                via1.aosc_i_s0_04h = 0.1
            elif via1.tipo_via == ETV.BALASTO.value and via1.estado_via == EEV.MAL_ESTADO.value:
                via1.aosc_i_s0_04h = 0.2
            elif via1.tipo_via == ETV.VIA_PLACA.value:
                via1.aosc_i_s0_04h = 0.1
        elif via1.GPA in [EGPA.GEE10.value, EGPA.GED10.value, EGPA.PERSONALIZADO.value]:
            if via1.tipo_via == ETV.BALASTO.value:
                via1.aosc_i_s0_04h = 0.2
            elif via1.tipo_via == ETV.VIA_PLACA.value:
                via1.aosc_i_s0_04h = 0.1
        
        if via1.GPA in [EGPA.GHE16.value, EGPA.GEA16.value, EGPA.GEB16.value, EGPA.GEC16.value, EGPA.GA.value, EGPA.GB.value, EGPA.GC.value]:
            if via1.tipo_via == ETV.BALASTO.value and via1.estado_via == EEV.BUEN_ESTADO.value:
                via1.aosc_i_s0_03h = 0.08
            elif via1.tipo_via == ETV.BALASTO.value and via1.estado_via == EEV.MAL_ESTADO.value:
                via1.aosc_i_s0_03h = 0.15
            elif via1.tipo_via == ETV.VIA_PLACA.value:
                via1.aosc_i_s0_03h = 0.08
        elif via1.GPA in [EGPA.GEE10.value, EGPA.GED10.value, EGPA.PERSONALIZADO.value]:
            if via1.tipo_via == ETV.BALASTO.value:
                via1.aosc_i_s0_03h = 0.2
            elif via1.tipo_via == ETV.VIA_PLACA.value:
                via1.aosc_i_s0_03h = 0.1

        if via1.GPA in [EGPA.GHE16.value, EGPA.GEA16.value, EGPA.GEB16.value, EGPA.GEC16.value, EGPA.GA.value, EGPA.GB.value, EGPA.GC.value]:
            if via1.tipo_via == ETV.BALASTO.value and via1.estado_via == EEV.BUEN_ESTADO.value:
                via1.aosc_a_s0_04h = 0.6
            elif via1.tipo_via == ETV.BALASTO.value and via1.estado_via == EEV.MAL_ESTADO.value:
                via1.aosc_a_s0_04h = 1.0
            elif via1.tipo_via == ETV.VIA_PLACA.value:
                via1.aosc_a_s0_04h = 0.6
        elif via1.GPA in [EGPA.GEE10.value, EGPA.GED10.value, EGPA.PERSONALIZADO.value]:
            if via1.tipo_via == ETV.BALASTO.value:
                via1.aosc_a_s0_04h = 1.0
            elif via1.tipo_via == ETV.VIA_PLACA.value:
                via1.aosc_a_s0_04h = 0.6
        
        if via1.GPA in [EGPA.GHE16.value, EGPA.GEA16.value, EGPA.GEB16.value, EGPA.GEC16.value, EGPA.GA.value, EGPA.GB.value, EGPA.GC.value]:
            if via1.tipo_via == ETV.BALASTO.value and via1.estado_via == EEV.BUEN_ESTADO.value:
                via1.aosc_a_s0_03h = 0.45
            elif via1.tipo_via == ETV.BALASTO.value and via1.estado_via == EEV.MAL_ESTADO.value:
                via1.aosc_a_s0_03h = 0.75
            elif via1.tipo_via == ETV.VIA_PLACA.value:
                via1.aosc_a_s0_03h = 0.45
        elif via1.GPA in [EGPA.GEE10.value, EGPA.GED10.value, EGPA.PERSONALIZADO.value]:
            if via1.tipo_via == ETV.BALASTO.value:
                via1.aosc_a_s0_03h = 1.0
            elif via1.tipo_via == ETV.VIA_PLACA.value:
                via1.aosc_a_s0_03h = 0.6

    def cambiar_elementos(galiboPA):
        def signo(num):
            return 1 if num > 0 else -1

        #ACTUALIZACIÓN DE LOS ELEMENTOS DE FLET CON LOS VALORES CALCULADOS ANTERIORMENTE
        ftt.t_R.value = via1.R
        ftt.t_RV.value = via1.Rv
        ftt.t_LN.value = via1.LN
        ftt.t_DL.value = via1.DL
        ftt.t_LND.value = via1.LND
        ftt.t_DhRV.value = via1.DhRV
        
        ftt.t_D.value = via1.D
        ftt.t_D0.value = via1.D0
        ftt.t_heq.value = via1.heq
        ftt.t_I.value = via1.I
        ftt.t_I0.value = via1.I0
        ftt.t_L.value = via1.L
        ftt.t_hco.value = via1.hco

        ftt.t_tvia.value = via1.TVIA
        ftt.t_td.value = via1.TD
        ftt.t_vmax.value = via1.vmax
        ftt.t_asusp.value = via1.asusp
        ftt.t_acarga.value = via1.acarga
        ftt.t_eta0.value = via1.eta0
        ftt.t_aosc_i_s0_04b.value = via1.aosc_i_s0_04b
        ftt.t_aosc_i_s0_03b.value = via1.aosc_i_s0_03b
        ftt.t_aosc_a_s0_04b.value = via1.aosc_a_s0_04b
        ftt.t_aosc_a_s0_03b.value = via1.aosc_a_s0_03b

        fttabla.actualizar_tabla()

        #ACTUALIZACIÓN DE LAS TABLAS DE DATOS DE FLET
        for nombre,punto in galiboPA.items():
            punto.esPT = calc.calcular_esPT(punto.Y, via1.maxY)
            punto.k = calc.calcular_k(via1.GPA, punto.Y/1000, via1.hquiebroaux, via1.htopeaux, via1.difaux)
            punto.s0 = calc.calcular_s0(via1.GPA, punto.Y/1000, via1.hquiebroaux, via1.htopeaux, via1.difaux, via1.hotra)
            punto.Sa = calc.calcular_Sa(via1.GPA, via1.GPB, via1.R, via1.LN, via1.LND, via1.hquiebroaux, punto.Y/1000, punto.k)
            punto.Si = calc.calcular_Si(via1.GPA, via1.GPB, via1.R, via1.LN, via1.LND, via1.hquiebroaux, punto.Y/1000, punto.k)
            punto.qsD_ai = calc.calcular_qsD_ai(punto.Y/1000, punto.s0, via1.D, via1.D0, via1.L, via1.hco)
            punto.qsI_ai = calc.calcular_qsI_ai(punto.Y/1000, punto.s0, via1.I, via1.I0, via1.L, via1.hco)
            punto.Tvia_ai = via1.TVIA * 1000
            punto.Dbg_ai = calc.calcular_Dbg_ai(punto.Y/1000, via1.L, via1.TD)
            punto.Dbc_ai = calc.calcular_Dbc_ai(punto.Y/1000, via1.L, via1.TD, via1.hco, punto.s0)
            punto.Dbsusp_ai = calc.calcular_Dbsusp_ai(via1.asusp, punto.Y, via1.hco * 1000)
            punto.Dbcarg_ai = calc.calcular_Dbcarg_ai(via1.acarga, punto.Y, via1.hco * 1000)
            punto.Dbeta0_ai = calc.calcular_Dbeta0_ai(via1.eta0, punto.Y, via1.hco * 1000)
            punto.aosc_a = calc.calcular_aosc(punto.s0, via1.aosc_a_s0_03b, via1.aosc_a_s0_04b)
            punto.aosc_i = calc.calcular_aosc(punto.s0, via1.aosc_i_s0_03b, via1.aosc_i_s0_04b)
            punto.Dbosc_a = calc.calcular_Dbosc(punto.aosc_a, punto.Y, via1.hco * 1000)
            punto.Dbosc_i = calc.calcular_Dbosc(punto.aosc_i, punto.Y, via1.hco * 1000)
            punto.M3b = via1.M3b * 1000
            punto.DhRv = round(via1.DhRV * 1000, 1)
            punto.DhPT_D_ai = calc.calcular_DhPT_D_ai(punto.X, punto.s0, via1.D, via1.D0, via1.L)
            punto.DhPT_I_ai = calc.calcular_DhPT_I_ai(punto.X, punto.s0, via1.I, via1.I0, via1.L)
            punto.TN = via1.TN * 1000
            punto.Dhg_a = calc.calcular_Dhg_a(punto.X/1000, via1.L, via1.TD)
            punto.Dhg_i = calc.calcular_Dhg_i(punto.X/1000, via1.L, via1.TD)
            punto.Dhc = calc.calcular_Dhc(punto.X/1000, punto.s0, via1.L, via1.TD)
            punto.Dhgca = round(punto.Dhg_a + punto.Dhc, 1)
            punto.Dhgci = round(punto.Dhg_i + punto.Dhc, 1)
            punto.Dhsusp_ai = calc.calcular_Dhsusp_ai(punto.X, via1.asusp)
            punto.Dhcarg_ai = calc.calcular_Dhcarg_ai(punto.X, via1.acarga)
            punto.Dheta0_ai = calc.calcular_Dhcarg_ai(punto.X, via1.eta0)
            punto.Dhosc_a = calc.calcular_Dhosc(punto.X, punto.aosc_i)                           #Sí, los ángulos están cambiados. Así debe ser.
            punto.Dhosc_i = calc.calcular_Dhosc(punto.X, punto.aosc_a)                           #Sí, los ángulos están cambiados. Así debe ser.
            punto.M3h = via1.M3h * 1000

            punto.lim_Sja1 = calc.calcular_lim_Sj1(punto.Y/1000, via1.hco, via1.K, via1.Kale_h_0_50, punto.Tvia_ai, punto.Dbg_ai, punto.Dbc_ai, punto.Dbsusp_ai, punto.Dbcarg_ai, punto.Dbosc_a)
            punto.lim_Sji1 = calc.calcular_lim_Sj1(punto.Y/1000, via1.hco, via1.K, via1.Kale_h_0_50, punto.Tvia_ai, punto.Dbg_ai, punto.Dbc_ai, punto.Dbsusp_ai, punto.Dbcarg_ai, punto.Dbosc_i)
            punto.lim_Sja2 = calc.calcular_lim_Sj2(punto.Y/1000, via1.hco, via1.K, via1.Kale_h_0_50, punto.Tvia_ai, punto.Dbg_ai)
            punto.lim_Sji2 = punto.lim_Sja2
            punto.lim_rad_Sja1_ast = calc.calcular_lim_rad_Sj1(punto.Tvia_ai, punto.Dbg_ai, punto.Dbc_ai, punto.Dbsusp_ai, punto.Dbcarg_ai, punto.Dbosc_a)
            punto.lim_rad_Sji1_ast = calc.calcular_lim_rad_Sj1(punto.Tvia_ai, punto.Dbg_ai, punto.Dbc_ai, punto.Dbsusp_ai, punto.Dbcarg_ai, punto.Dbosc_i)
            punto.lim_rad_Sjai2_ast = calc.calcular_lim_rad_Sj2(punto.Tvia_ai, punto.Dbg_ai)
            punto.lim_Sja1_ast = calc.calcular_lim_Sj_ast(punto.Y / 1000, via1.hco, via1.K, via1.Kale_h_0_50, punto.lim_rad_Sja1_ast)
            punto.lim_Sji1_ast = calc.calcular_lim_Sj_ast(punto.Y / 1000, via1.hco, via1.K, via1.Kale_h_0_50, punto.lim_rad_Sji1_ast)
            punto.lim_Sja2_ast = calc.calcular_lim_Sj_ast(punto.Y / 1000, via1.hco, via1.K, via1.Kale_h_0_50, punto.lim_rad_Sjai2_ast)
            punto.lim_Sji2_ast = calc.calcular_lim_Sj_ast(punto.Y / 1000, via1.hco, via1.K, via1.Kale_h_0_50, punto.lim_rad_Sjai2_ast)
            punto.lim_rad_SVi1 = calc.calcular_lim_rad_SVi1(punto.TN, punto.Dhg_i, punto.Dhc, punto.Dhsusp_ai, punto.Dhcarg_ai, punto.Dhosc_i)
            punto.lim_rad_SVa1 = calc.calcular_lim_rad_SVa1(punto.TN, punto.Dhg_a, punto.Dhc, punto.Dhsusp_ai, punto.Dhcarg_ai, punto.Dhosc_a)
            punto.lim_SVa1 = calc.calcular_lim_SV1(via1.K, punto.lim_rad_SVa1)
            punto.lim_SVi1 = calc.calcular_lim_SV1(via1.K, punto.lim_rad_SVi1)
            punto.lim_SVa2 = punto.TN
            punto.lim_SVi2 = punto.TN
            punto.lim_SVa1_ast = calc.calcular_SVa1_ast(via1.K, punto.TN, punto.Dhg_a, punto.Dhc, punto.Dhsusp_ai, punto.Dhcarg_ai, punto.Dhosc_a)
            punto.lim_SVi1_ast = calc.calcular_SVi1_ast(via1.K, punto.TN, punto.Dhg_i, punto.Dhc, punto.Dhsusp_ai, punto.Dhcarg_ai, punto.Dhosc_i)
            punto.lim_SVa2_ast = punto.TN
            punto.lim_SVi2_ast = punto.TN
            punto.lim_bobstVM_max_i = calc.calcular_lim_bobst(punto.X, punto.Y / 1000, punto.Si, -punto.qsI_ai, punto.lim_Sji1, punto.lim_Sji2)
            punto.lim_hobstVM_con_i = calc.calcular_lim_hobst(punto.Y, punto.DhRv, via1.hb_max, punto.esPT, punto.DhPT_I_ai, punto.lim_SVi1, punto.lim_SVi2)
            punto.lim_bobstVM_max_a = calc.calcular_lim_bobst(punto.X, punto.Y / 1000, punto.Sa, punto.qsI_ai, punto.lim_Sja1, punto.lim_Sja2)
            punto.lim_hobstVM_con_a = calc.calcular_lim_hobst(punto.Y, punto.DhRv, via1.hb_max, punto.esPT, -punto.DhPT_I_ai, punto.lim_SVa1, punto.lim_SVa2)
            punto.lim_bobstVM_con_i = calc.calcular_lim_bobst(punto.X, punto.Y / 1000, punto.Si, -punto.qsI_ai, punto.lim_Sji1_ast, punto.lim_Sji2_ast)
            punto.lim_hobstVM_max_i = calc.calcular_lim_hobst(punto.Y, punto.DhRv, via1.hb_max, punto.esPT, punto.DhPT_I_ai, punto.lim_SVi1_ast, punto.lim_SVi2_ast)
            punto.lim_bobstVM_con_a = calc.calcular_lim_bobst(punto.X, punto.Y / 1000, punto.Sa, punto.qsI_ai, punto.lim_Sja1_ast, punto.lim_Sja2_ast)
            punto.lim_hobstVM_max_a = calc.calcular_lim_hobst(punto.Y, punto.DhRv, via1.hb_max, punto.esPT, -punto.DhPT_I_ai, punto.lim_SVa1_ast, punto.lim_SVa2_ast)
            punto.lim_bobstV0_max_i = calc.calcular_lim_bobst(punto.X, punto.Y / 1000, punto.Si, punto.qsD_ai, punto.lim_Sji1, punto.lim_Sji2)
            punto.lim_hobstV0_con_i = calc.calcular_lim_hobst(punto.Y, punto.DhRv, via1.hb_max, punto.esPT, -punto.DhPT_D_ai, punto.lim_SVi1, punto.lim_SVi2)
            punto.lim_bobstV0_max_a = calc.calcular_lim_bobst(punto.X, punto.Y / 1000, punto.Sa, -punto.qsD_ai, punto.lim_Sja1, punto.lim_Sja2)
            punto.lim_hobstV0_con_a = calc.calcular_lim_hobst(punto.Y, punto.DhRv, via1.hb_max, punto.esPT, punto.DhPT_D_ai, punto.lim_SVa1, punto.lim_SVa2)
            punto.lim_bobstV0_con_i = calc.calcular_lim_bobst(punto.X, punto.Y / 1000, punto.Si, punto.qsD_ai, punto.lim_Sji1_ast, punto.lim_Sji2_ast)
            punto.lim_hobstV0_max_i = calc.calcular_lim_hobst(punto.Y, punto.DhRv, via1.hb_max, punto.esPT, -punto.DhPT_D_ai, punto.lim_SVi1_ast, punto.lim_SVi2_ast)
            punto.lim_bobstV0_con_a = calc.calcular_lim_bobst(punto.X, punto.Y / 1000, punto.Sa, -punto.qsD_ai, punto.lim_Sja1_ast, punto.lim_Sja2_ast)
            punto.lim_hobstV0_max_a = calc.calcular_lim_hobst(punto.Y, punto.DhRv, via1.hb_max, punto.esPT, punto.DhPT_D_ai, punto.lim_SVa1_ast, punto.lim_SVa2_ast)
            punto.lim_ba = signo(punto.X) * max(abs(punto.lim_bobstVM_max_a), abs(punto.lim_bobstVM_con_a), abs(punto.lim_bobstV0_max_a), abs(punto.lim_bobstV0_con_a))
            punto.lim_ha = calc.calcular_h(punto.Y/1000, via1.hb_max / 1000, punto.lim_hobstVM_con_a, punto.lim_hobstVM_max_a, punto.lim_hobstV0_con_a, punto.lim_hobstV0_max_a)
            punto.lim_bi = signo(punto.X) * max(abs(punto.lim_bobstVM_max_i), abs(punto.lim_bobstVM_con_i), abs(punto.lim_bobstV0_max_i), abs(punto.lim_bobstV0_con_i))
            punto.lim_hi = calc.calcular_h(punto.Y/1000, via1.hb_max / 1000, punto.lim_hobstVM_con_i, punto.lim_hobstVM_max_i, punto.lim_hobstV0_con_i, punto.lim_hobstV0_max_i)

            punto.nom_Sja3 = calc.calcular_nom_Sj3(punto.Tvia_ai, punto.Dbg_ai, punto.Dbc_ai, punto.Dbsusp_ai, punto.Dbcarg_ai, punto.Dbosc_a)
            punto.nom_Sji3 = calc.calcular_nom_Sj3(punto.Tvia_ai, punto.Dbg_ai, punto.Dbc_ai, punto.Dbsusp_ai, punto.Dbcarg_ai, punto.Dbosc_i)
            punto.nom_Sja4 = calc.calcular_nom_Sj4(punto.Tvia_ai, punto.Dbg_ai)
            punto.nom_Sji4 = calc.calcular_nom_Sj4(punto.Tvia_ai, punto.Dbg_ai)
            punto.nom_Sja3_ast = calc.calcular_nom_Sj3_ast(punto.Tvia_ai, punto.Dbg_ai, punto.Dbc_ai, punto.Dbsusp_ai, punto.Dbcarg_ai, punto.Dbosc_a)
            punto.nom_Sji3_ast = calc.calcular_nom_Sj3_ast(punto.Tvia_ai, punto.Dbg_ai, punto.Dbc_ai, punto.Dbsusp_ai, punto.Dbcarg_ai, punto.Dbosc_i)
            punto.nom_Sja4_ast = calc.calcular_nom_Sj4_ast(punto.Tvia_ai, punto.Dbg_ai)
            punto.nom_Sji4_ast = calc.calcular_nom_Sj4_ast(punto.Tvia_ai, punto.Dbg_ai)
            punto.nom_SVa3 = calc.calcular_nom_SV3a(punto.TN, punto.Dhg_a, punto.Dhc, punto.Dhsusp_ai, punto.Dhcarg_ai, punto.Dhosc_a)
            punto.nom_SVi3 = calc.calcular_nom_SV3i(punto.TN, punto.Dhg_i, punto.Dhc, punto.Dhsusp_ai, punto.Dhcarg_ai, punto.Dhosc_i)
            punto.nom_SVa4 = punto.TN
            punto.nom_SVi4 = punto.TN
            punto.nom_SVa3_ast = calc.calcular_nom_SV3a_ast(punto.TN, punto.Dhg_a, punto.Dhc, punto.Dhsusp_ai, punto.Dhcarg_ai, punto.Dhosc_a)
            punto.nom_SVi3_ast = calc.calcular_nom_SV3i_ast(punto.TN, punto.Dhg_i, punto.Dhc, punto.Dhsusp_ai, punto.Dhcarg_ai, punto.Dhosc_i)
            punto.nom_SVa4_ast = punto.TN
            punto.nom_SVi4_ast = punto.TN
            punto.nom_bobstVM_max_i = calc.calcular_nom_bobst(punto.X, punto.Y / 1000, punto.Si, -punto.qsI_ai, punto.nom_Sji3, punto.nom_Sji4, punto.M3b)
            punto.nom_hobstVM_con_i = calc.calcular_nom_hobst(punto.Y, punto.DhRv, via1.hb_max, punto.esPT, punto.DhPT_I_ai, punto.nom_SVi3, punto.nom_SVi4, punto.M3h)
            punto.nom_bobstVM_max_a = calc.calcular_nom_bobst(punto.X, punto.Y / 1000, punto.Sa, punto.qsI_ai, punto.nom_Sja3, punto.nom_Sja4, punto.M3b)
            punto.nom_hobstVM_con_a = calc.calcular_nom_hobst(punto.Y, punto.DhRv, via1.hb_max, punto.esPT, -punto.DhPT_I_ai, punto.nom_SVa3, punto.nom_SVa4, punto.M3h)
            punto.nom_bobstVM_con_i = calc.calcular_nom_bobst(punto.X, punto.Y / 1000, punto.Si, -punto.qsI_ai, punto.nom_Sji3_ast, punto.nom_Sji4_ast, punto.M3b)
            punto.nom_hobstVM_max_i = calc.calcular_nom_hobst(punto.Y, punto.DhRv, via1.hb_max, punto.esPT, punto.DhPT_I_ai, punto.nom_SVi3_ast, punto.nom_SVi4_ast,punto.M3h)
            punto.nom_bobstVM_con_a = calc.calcular_nom_bobst(punto.X, punto.Y / 1000, punto.Sa, punto.qsI_ai, punto.nom_Sja3_ast, punto.nom_Sja4_ast, punto.M3b)
            punto.nom_hobstVM_max_a = calc.calcular_nom_hobst(punto.Y, punto.DhRv, via1.hb_max, punto.esPT, -punto.DhPT_I_ai, punto.nom_SVa3_ast, punto.nom_SVa4_ast, punto.M3h)
            punto.nom_bobstV0_max_i = calc.calcular_nom_bobst(punto.X, punto.Y / 1000, punto.Si, punto.qsD_ai, punto.nom_Sji3, punto.nom_Sji4, punto.M3b)
            punto.nom_hobstV0_con_i = calc.calcular_nom_hobst(punto.Y, punto.DhRv, via1.hb_max, punto.esPT, -punto.DhPT_D_ai, punto.nom_SVi3, punto.nom_SVi4, punto.M3h)
            punto.nom_bobstV0_max_a = calc.calcular_nom_bobst(punto.X, punto.Y / 1000, punto.Sa, -punto.qsD_ai, punto.nom_Sja3, punto.nom_Sja4, punto.M3b)
            punto.nom_hobstV0_con_a = calc.calcular_nom_hobst(punto.Y, punto.DhRv, via1.hb_max, punto.esPT, punto.DhPT_D_ai, punto.nom_SVa3, punto.nom_SVa4, punto.M3h)
            punto.nom_bobstV0_con_i = calc.calcular_nom_bobst(punto.X, punto.Y / 1000, punto.Si, punto.qsD_ai, punto.nom_Sji3_ast, punto.nom_Sji4_ast, punto.M3b)
            punto.nom_hobstV0_max_i = calc.calcular_nom_hobst(punto.Y, punto.DhRv, via1.hb_max, punto.esPT, -punto.DhPT_D_ai, punto.nom_SVi3_ast, punto.nom_SVi4_ast, punto.M3h)
            punto.nom_bobstV0_con_a = calc.calcular_nom_bobst(punto.X, punto.Y / 1000, punto.Sa, -punto.qsD_ai, punto.nom_Sja3_ast, punto.nom_Sja4_ast, punto.M3b)
            punto.nom_hobstV0_max_a = calc.calcular_nom_hobst(punto.Y, punto.DhRv, via1.hb_max, punto.esPT, punto.DhPT_D_ai, punto.nom_SVa3_ast, punto.nom_SVa4_ast, punto.M3h)
            punto.nom_ba = signo(punto.X) * max(abs(punto.nom_bobstVM_max_a), abs(punto.nom_bobstVM_con_a), abs(punto.nom_bobstV0_max_a), abs(punto.nom_bobstV0_con_a))
            punto.nom_ha = calc.calcular_h(punto.Y/1000, via1.hb_max / 1000, punto.nom_hobstVM_con_a, punto.nom_hobstVM_max_a, punto.nom_hobstV0_con_a, punto.nom_hobstV0_max_a)
            punto.nom_bi = signo(punto.X) * max(abs(punto.nom_bobstVM_max_i), abs(punto.nom_bobstVM_con_i), abs(punto.nom_bobstV0_max_i), abs(punto.nom_bobstV0_con_i))
            punto.nom_hi = calc.calcular_h(punto.Y/1000, via1.hb_max / 1000, punto.nom_hobstVM_con_i, punto.nom_hobstVM_max_i, punto.nom_hobstV0_con_i, punto.nom_hobstV0_max_i)

            fttabla.tabla_00_Punto_des.controls.append(ft.Text(nombre,size=Tamanyos.TABLA_NORMAL.value))
            fttabla.tabla_00_Punto_lim.controls.append(ft.Text(nombre,size=Tamanyos.TABLA_NORMAL.value))
            fttabla.tabla_00_Punto_nom.controls.append(ft.Text(nombre,size=Tamanyos.TABLA_NORMAL.value))
            fttabla.tabla_01_X_des.controls.append(ft.Text(punto.X,size=Tamanyos.TABLA_NORMAL.value))
            fttabla.tabla_01_X_lim.controls.append(ft.Text(punto.X,size=Tamanyos.TABLA_NORMAL.value))
            fttabla.tabla_01_X_nom.controls.append(ft.Text(punto.X,size=Tamanyos.TABLA_NORMAL.value))
            fttabla.tabla_02_Y_des.controls.append(ft.Text(punto.Y,size=Tamanyos.TABLA_NORMAL.value))
            fttabla.tabla_02_Y_lim.controls.append(ft.Text(punto.Y,size=Tamanyos.TABLA_NORMAL.value))
            fttabla.tabla_02_Y_nom.controls.append(ft.Text(punto.Y,size=Tamanyos.TABLA_NORMAL.value))
            fttabla.tabla_03_esPT.controls.append(ft.Text(punto.esPT,size=Tamanyos.TABLA_NORMAL.value))
            fttabla.tabla_04_k.controls.append(ft.Text(punto.k,size=Tamanyos.TABLA_NORMAL.value))
            fttabla.tabla_05_s0.controls.append(ft.Text(punto.s0,size=Tamanyos.TABLA_NORMAL.value))
            fttabla.tabla_06_Sa.controls.append(ft.Text(punto.Sa,size=Tamanyos.TABLA_NORMAL.value))
            fttabla.tabla_07_Si.controls.append(ft.Text(punto.Si,size=Tamanyos.TABLA_NORMAL.value))
            fttabla.tabla_08_qsDai.controls.append(ft.Text(punto.qsD_ai,size=Tamanyos.TABLA_NORMAL.value))
            fttabla.tabla_09_qsIai.controls.append(ft.Text(punto.qsI_ai,size=Tamanyos.TABLA_NORMAL.value))
            fttabla.tabla_10_Tvia_ai.controls.append(ft.Text(punto.Tvia_ai,size=Tamanyos.TABLA_NORMAL.value))
            fttabla.tabla_11_Dbgai.controls.append(ft.Text(punto.Dbg_ai,size=Tamanyos.TABLA_NORMAL.value))
            fttabla.tabla_12_Dbcai.controls.append(ft.Text(punto.Dbc_ai,size=Tamanyos.TABLA_NORMAL.value))
            fttabla.tabla_13_Dbsuspai.controls.append(ft.Text(punto.Dbsusp_ai,size=Tamanyos.TABLA_NORMAL.value))
            fttabla.tabla_14_Dbcargaai.controls.append(ft.Text(punto.Dbcarg_ai,size=Tamanyos.TABLA_NORMAL.value))
            fttabla.tabla_15_Dbetaai.controls.append(ft.Text(punto.Dbeta0_ai,size=Tamanyos.TABLA_NORMAL.value))
            fttabla.tabla_16_aosca.controls.append(ft.Text(punto.aosc_a,size=Tamanyos.TABLA_NORMAL.value))
            fttabla.tabla_17_aosci.controls.append(ft.Text(punto.aosc_i,size=Tamanyos.TABLA_NORMAL.value))
            fttabla.tabla_18_Dbosca.controls.append(ft.Text(punto.Dbosc_a,size=Tamanyos.TABLA_NORMAL.value))
            fttabla.tabla_19_Dbosci.controls.append(ft.Text(punto.Dbosc_i,size=Tamanyos.TABLA_NORMAL.value))
            fttabla.tabla_20_M3h.controls.append(ft.Text(punto.M3b,size=Tamanyos.TABLA_NORMAL.value))
            fttabla.tabla_21_DhRv.controls.append(ft.Text(punto.DhRv,size=Tamanyos.TABLA_NORMAL.value))
            fttabla.tabla_22_DhPTDai.controls.append(ft.Text(punto.DhPT_D_ai,size=Tamanyos.TABLA_NORMAL.value))
            fttabla.tabla_23_DhPTIai.controls.append(ft.Text(punto.DhPT_I_ai,size=Tamanyos.TABLA_NORMAL.value))
            fttabla.tabla_24_TN.controls.append(ft.Text(punto.TN,size=Tamanyos.TABLA_NORMAL.value))
            fttabla.tabla_25_Dhga.controls.append(ft.Text(punto.Dhg_a,size=Tamanyos.TABLA_NORMAL.value))
            fttabla.tabla_26_Dhgi.controls.append(ft.Text(punto.Dhg_i,size=Tamanyos.TABLA_NORMAL.value))
            fttabla.tabla_27_Dhc.controls.append(ft.Text(punto.Dhc,size=Tamanyos.TABLA_NORMAL.value))
            fttabla.tabla_28_Dhgca.controls.append(ft.Text(punto.Dhgca,size=Tamanyos.TABLA_NORMAL.value))
            fttabla.tabla_29_Dhgci.controls.append(ft.Text(punto.Dhgci,size=Tamanyos.TABLA_NORMAL.value))
            fttabla.tabla_30_Dhsuspai.controls.append(ft.Text(punto.Dhsusp_ai,size=Tamanyos.TABLA_NORMAL.value))
            fttabla.tabla_31_Dhcargai.controls.append(ft.Text(punto.Dhcarg_ai,size=Tamanyos.TABLA_NORMAL.value))
            fttabla.tabla_32_Dhetaai.controls.append(ft.Text(punto.Dheta0_ai,size=Tamanyos.TABLA_NORMAL.value))
            fttabla.tabla_33_Dhosca.controls.append(ft.Text(punto.Dhosc_a,size=Tamanyos.TABLA_NORMAL.value))
            fttabla.tabla_34_Dhosci.controls.append(ft.Text(punto.Dhosc_i,size=Tamanyos.TABLA_NORMAL.value))
            fttabla.tabla_35_M3h.controls.append(ft.Text(punto.M3h,size=Tamanyos.TABLA_NORMAL.value))
            fttabla.tabla_36_lim_Sja1.controls.append(ft.Text(punto.lim_Sja1,size=Tamanyos.TABLA_NORMAL.value))
            fttabla.tabla_37_lim_Sji1.controls.append(ft.Text(punto.lim_Sji1,size=Tamanyos.TABLA_NORMAL.value))
            fttabla.tabla_38_lim_Sja2.controls.append(ft.Text(punto.lim_Sja2,size=Tamanyos.TABLA_NORMAL.value))
            fttabla.tabla_39_lim_Sji2.controls.append(ft.Text(punto.lim_Sji2,size=Tamanyos.TABLA_NORMAL.value))
            fttabla.tabla_40_lim_Sja1_ast.controls.append(ft.Text(punto.lim_Sja1_ast,size=Tamanyos.TABLA_NORMAL.value))
            fttabla.tabla_41_lim_Sji1_ast.controls.append(ft.Text(punto.lim_Sji1_ast,size=Tamanyos.TABLA_NORMAL.value))
            fttabla.tabla_42_lim_Sja2_ast.controls.append(ft.Text(punto.lim_Sja2_ast,size=Tamanyos.TABLA_NORMAL.value))
            fttabla.tabla_43_lim_Sji2_ast.controls.append(ft.Text(punto.lim_Sji2_ast,size=Tamanyos.TABLA_NORMAL.value))
            fttabla.tabla_44_lim_SVa1.controls.append(ft.Text(punto.lim_SVa1,size=Tamanyos.TABLA_NORMAL.value))
            fttabla.tabla_45_lim_SVi1.controls.append(ft.Text(punto.lim_SVi1,size=Tamanyos.TABLA_NORMAL.value))
            fttabla.tabla_46_lim_SVa2.controls.append(ft.Text(punto.lim_SVa2,size=Tamanyos.TABLA_NORMAL.value))
            fttabla.tabla_47_lim_SVi2.controls.append(ft.Text(punto.lim_SVi2,size=Tamanyos.TABLA_NORMAL.value))
            fttabla.tabla_48_lim_SVa1_ast.controls.append(ft.Text(punto.lim_SVa1_ast,size=Tamanyos.TABLA_NORMAL.value))
            fttabla.tabla_49_lim_SVi1_ast.controls.append(ft.Text(punto.lim_SVi1_ast,size=Tamanyos.TABLA_NORMAL.value))
            fttabla.tabla_50_lim_SVa2_ast.controls.append(ft.Text(punto.lim_SVa2_ast,size=Tamanyos.TABLA_NORMAL.value))
            fttabla.tabla_51_lim_SVi2_ast.controls.append(ft.Text(punto.lim_SVi2_ast,size=Tamanyos.TABLA_NORMAL.value))
            fttabla.tabla_52_nom_Sja3.controls.append(ft.Text(punto.nom_Sja3,size=Tamanyos.TABLA_NORMAL.value))
            fttabla.tabla_53_nom_Sji3.controls.append(ft.Text(punto.nom_Sji3,size=Tamanyos.TABLA_NORMAL.value))
            fttabla.tabla_54_nom_Sja4.controls.append(ft.Text(punto.nom_Sja4,size=Tamanyos.TABLA_NORMAL.value))
            fttabla.tabla_55_nom_Sji4.controls.append(ft.Text(punto.nom_Sji4,size=Tamanyos.TABLA_NORMAL.value))
            fttabla.tabla_56_nom_Sja3_ast.controls.append(ft.Text(punto.nom_Sja3_ast,size=Tamanyos.TABLA_NORMAL.value))
            fttabla.tabla_57_nom_Sji3_ast.controls.append(ft.Text(punto.nom_Sji3_ast,size=Tamanyos.TABLA_NORMAL.value))
            fttabla.tabla_58_nom_Sja4_ast.controls.append(ft.Text(punto.nom_Sja4_ast,size=Tamanyos.TABLA_NORMAL.value))
            fttabla.tabla_59_nom_Sji4_ast.controls.append(ft.Text(punto.nom_Sji4_ast,size=Tamanyos.TABLA_NORMAL.value))
            fttabla.tabla_60_nom_SVa3.controls.append(ft.Text(punto.nom_SVa3,size=Tamanyos.TABLA_NORMAL.value))
            fttabla.tabla_61_nom_SVi3.controls.append(ft.Text(punto.nom_SVi3,size=Tamanyos.TABLA_NORMAL.value))
            fttabla.tabla_62_nom_SVa4.controls.append(ft.Text(punto.nom_SVa4,size=Tamanyos.TABLA_NORMAL.value))
            fttabla.tabla_63_nom_SVi4.controls.append(ft.Text(punto.nom_SVi4,size=Tamanyos.TABLA_NORMAL.value))
            fttabla.tabla_64_nom_SVa3_ast.controls.append(ft.Text(punto.nom_SVa3_ast,size=Tamanyos.TABLA_NORMAL.value))
            fttabla.tabla_65_nom_SVi3_ast.controls.append(ft.Text(punto.nom_SVi3_ast,size=Tamanyos.TABLA_NORMAL.value))
            fttabla.tabla_66_nom_SVa4_ast.controls.append(ft.Text(punto.nom_SVa4_ast,size=Tamanyos.TABLA_NORMAL.value))
            fttabla.tabla_67_nom_SVi4_ast.controls.append(ft.Text(punto.nom_SVi4_ast,size=Tamanyos.TABLA_NORMAL.value))
            fttabla.tabla_68_lim_bobstVM_max_i.controls.append(ft.Text(punto.lim_bobstVM_max_i,size=Tamanyos.TABLA_NORMAL.value))
            fttabla.tabla_69_lim_hobstVM_con_i.controls.append(ft.Text(punto.lim_hobstVM_con_i,size=Tamanyos.TABLA_NORMAL.value))
            fttabla.tabla_70_lim_bobstVM_max_a.controls.append(ft.Text(punto.lim_bobstVM_max_a,size=Tamanyos.TABLA_NORMAL.value))
            fttabla.tabla_71_lim_hobstVM_con_a.controls.append(ft.Text(punto.lim_hobstVM_con_a,size=Tamanyos.TABLA_NORMAL.value))
            fttabla.tabla_72_lim_bobstVM_con_i.controls.append(ft.Text(punto.lim_bobstVM_con_i,size=Tamanyos.TABLA_NORMAL.value))
            fttabla.tabla_73_lim_hobstVM_max_i.controls.append(ft.Text(punto.lim_hobstVM_max_i,size=Tamanyos.TABLA_NORMAL.value))
            fttabla.tabla_74_lim_bobstVM_con_a.controls.append(ft.Text(punto.lim_bobstVM_con_a,size=Tamanyos.TABLA_NORMAL.value))
            fttabla.tabla_75_lim_hobstVM_max_a.controls.append(ft.Text(punto.lim_hobstVM_max_a,size=Tamanyos.TABLA_NORMAL.value))
            fttabla.tabla_76_lim_bobstV0_max_i.controls.append(ft.Text(punto.lim_bobstV0_max_i,size=Tamanyos.TABLA_NORMAL.value))
            fttabla.tabla_77_lim_hobstV0_con_i.controls.append(ft.Text(punto.lim_hobstV0_con_i,size=Tamanyos.TABLA_NORMAL.value))
            fttabla.tabla_78_lim_bobstV0_max_a.controls.append(ft.Text(punto.lim_bobstV0_max_a,size=Tamanyos.TABLA_NORMAL.value))
            fttabla.tabla_79_lim_hobstV0_con_a.controls.append(ft.Text(punto.lim_hobstV0_con_a,size=Tamanyos.TABLA_NORMAL.value))
            fttabla.tabla_80_lim_bobstV0_con_i.controls.append(ft.Text(punto.lim_bobstV0_con_i,size=Tamanyos.TABLA_NORMAL.value))
            fttabla.tabla_81_lim_hobstV0_max_i.controls.append(ft.Text(punto.lim_hobstV0_max_i,size=Tamanyos.TABLA_NORMAL.value))
            fttabla.tabla_82_lim_bobstV0_con_a.controls.append(ft.Text(punto.lim_bobstV0_con_a,size=Tamanyos.TABLA_NORMAL.value))
            fttabla.tabla_83_lim_hobstV0_max_a.controls.append(ft.Text(punto.lim_hobstV0_max_a,size=Tamanyos.TABLA_NORMAL.value))
            fttabla.tabla_84_nom_bobstVM_max_i.controls.append(ft.Text(punto.nom_bobstVM_max_i,size=Tamanyos.TABLA_NORMAL.value))
            fttabla.tabla_85_nom_hobstVM_con_i.controls.append(ft.Text(punto.nom_hobstVM_con_i,size=Tamanyos.TABLA_NORMAL.value))
            fttabla.tabla_86_nom_bobstVM_max_a.controls.append(ft.Text(punto.nom_bobstVM_max_a,size=Tamanyos.TABLA_NORMAL.value))
            fttabla.tabla_87_nom_hobstVM_con_a.controls.append(ft.Text(punto.nom_hobstVM_con_a,size=Tamanyos.TABLA_NORMAL.value))
            fttabla.tabla_88_nom_bobstVM_con_i.controls.append(ft.Text(punto.nom_bobstVM_con_i,size=Tamanyos.TABLA_NORMAL.value))
            fttabla.tabla_89_nom_hobstVM_max_i.controls.append(ft.Text(punto.nom_hobstVM_max_i,size=Tamanyos.TABLA_NORMAL.value))
            fttabla.tabla_90_nom_bobstVM_con_a.controls.append(ft.Text(punto.nom_bobstVM_con_a,size=Tamanyos.TABLA_NORMAL.value))
            fttabla.tabla_91_nom_hobstVM_max_a.controls.append(ft.Text(punto.nom_hobstVM_max_a,size=Tamanyos.TABLA_NORMAL.value))
            fttabla.tabla_92_nom_bobstV0_max_i.controls.append(ft.Text(punto.nom_bobstV0_max_i,size=Tamanyos.TABLA_NORMAL.value))
            fttabla.tabla_93_nom_hobstV0_con_i.controls.append(ft.Text(punto.nom_hobstV0_con_i,size=Tamanyos.TABLA_NORMAL.value))
            fttabla.tabla_94_nom_bobstV0_max_a.controls.append(ft.Text(punto.nom_bobstV0_max_a,size=Tamanyos.TABLA_NORMAL.value))
            fttabla.tabla_95_nom_hobstV0_con_a.controls.append(ft.Text(punto.nom_hobstV0_con_a,size=Tamanyos.TABLA_NORMAL.value))
            fttabla.tabla_96_nom_bobstV0_con_i.controls.append(ft.Text(punto.nom_bobstV0_con_i,size=Tamanyos.TABLA_NORMAL.value))
            fttabla.tabla_97_nom_hobstV0_max_i.controls.append(ft.Text(punto.nom_hobstV0_max_i,size=Tamanyos.TABLA_NORMAL.value))
            fttabla.tabla_98_nom_bobstV0_con_a.controls.append(ft.Text(punto.nom_bobstV0_con_a,size=Tamanyos.TABLA_NORMAL.value))
            fttabla.tabla_99_nom_hobstV0_max_a.controls.append(ft.Text(punto.nom_hobstV0_max_a,size=Tamanyos.TABLA_NORMAL.value))

    def cambiar_graficos(galiboPA, galiboPB):
        #ACTUALIZACIÓN DE LOS GRÁFICOS
        datos_grafico_GPA.data_points.clear()
        datos_grafico_GPA_lim.data_points.clear()
        datos_grafico_GPA_nom.data_points.clear()
        datos_grafico_GPB.data_points.clear()
        #datos_grafico_GPB_lim.data_points.clear()

        for nombre,punto in galiboPA.items():
            datos_grafico_GPA.data_points.append(ft.LineChartDataPoint(
                cos(radians(via1.Inclinac)) * punto.X/conf.ESCALA_GRAFICO + sin(radians(via1.Inclinac)) * punto.Y/conf.ESCALA_GRAFICO,
                - sin(radians(via1.Inclinac)) * punto.X/conf.ESCALA_GRAFICO + cos(radians(via1.Inclinac)) * punto.Y/conf.ESCALA_GRAFICO,
                tooltip=(nombre, punto.X, punto.Y)))
            datos_grafico_GPA_lim.data_points.append(ft.LineChartDataPoint(
                cos(radians(via1.Inclinac)) * punto.lim_bi/conf.ESCALA_GRAFICO + sin(radians(via1.Inclinac)) * punto.lim_hi/conf.ESCALA_GRAFICO,
                - sin(radians(via1.Inclinac)) * punto.lim_bi/conf.ESCALA_GRAFICO + cos(radians(via1.Inclinac)) * punto.lim_hi/conf.ESCALA_GRAFICO,
                tooltip=(nombre, punto.lim_bi, punto.lim_hi)))
            datos_grafico_GPA_nom.data_points.append(ft.LineChartDataPoint(
                cos(radians(via1.Inclinac)) * punto.nom_bi/conf.ESCALA_GRAFICO + sin(radians(via1.Inclinac)) * punto.nom_hi/conf.ESCALA_GRAFICO,
                - sin(radians(via1.Inclinac)) * punto.nom_bi/conf.ESCALA_GRAFICO + cos(radians(via1.Inclinac)) * punto.nom_hi/conf.ESCALA_GRAFICO,
                tooltip=(nombre, punto.nom_bi, punto.nom_hi)))
        datos_grafico_GPA.visible = cb_graf_GPA.value
        datos_grafico_GPA_lim.visible = cb_graf_GPA_lim.value
        datos_grafico_GPA_nom.visible = cb_graf_GPA_nom.value

        for nombre,punto in galiboPB.items():
            datos_grafico_GPB.data_points.append(ft.LineChartDataPoint(
                cos(radians(via1.Inclinac)) * punto.X/conf.ESCALA_GRAFICO + sin(radians(via1.Inclinac)) * punto.Y/conf.ESCALA_GRAFICO,
                - sin(radians(via1.Inclinac)) * punto.X/conf.ESCALA_GRAFICO + cos(radians(via1.Inclinac)) * punto.Y/conf.ESCALA_GRAFICO,
                tooltip=(nombre, punto.X, punto.Y)))
        datos_grafico_GPB.visible = cb_graf_GPB.value

    def cambiar(e):
        
        via1.GPA = dd_GPA.value
        via1.GPB = dd_GPB.value
        galiboPA = datos_GPA[via1.GPA]
        galiboPB = datos_GPB[via1.GPB]

        cambiar_variables(galiboPA)
        cambiar_elementos(galiboPA)
        cambiar_graficos(galiboPA, galiboPB)
        page.update()

    #COMPONENTES INDIVIDUALES CON EVENTOS
    dd_GPA_1 = ft.Dropdown(
        label = "Gálibo de partes altas",
        hint_text = "Introduce el gálibo de las partes altas",
        options = [
            ft.dropdown.Option(EGPA.GHE16.value),
            ft.dropdown.Option(EGPA.GEA16.value),
            ft.dropdown.Option(EGPA.GEB16.value),
            ft.dropdown.Option(EGPA.GEC16.value),
            ft.dropdown.Option(EGPA.GA.value),
            ft.dropdown.Option(EGPA.GB.value),
            ft.dropdown.Option(EGPA.GC.value),
            ft.dropdown.Option(EGPA.GEE10.value),
            ft.dropdown.Option(EGPA.GED10.value),
            ft.dropdown.Option(EGPA.PERSONALIZADO.value),
        ],
        on_change=cambiar
    )
    dd_GPB_1 = ft.Dropdown(
        label = "Gálibo de partes bajas",
        hint_text = "Introduce el gálibo de las partes bajas",
        options = [
            ft.dropdown.Option(EGPB.GEI1.value),
            ft.dropdown.Option(EGPB.GEI2.value),
            ft.dropdown.Option(EGPB.GEI3.value),
            ft.dropdown.Option(EGPB.GI1.value),
            ft.dropdown.Option(EGPB.GI2.value),
            ft.dropdown.Option(EGPB.GI3.value),
        ],
        on_change=cambiar,
    )
    dd_TV =  ft.Dropdown(
        label = "Tipo de Vía",
        hint_text = "Balasto / Vía en placa",
        options = [
            ft.dropdown.Option(ETV.BALASTO.value),
            ft.dropdown.Option(ETV.VIA_PLACA.value),
        ],
        on_change=cambiar
    )
    dd_EV = ft.Dropdown(
        label = "Estado de la Vía",
        hint_text = "Buen / Mal estado",
        options = [
            ft.dropdown.Option(EEV.BUEN_ESTADO.value),
            ft.dropdown.Option(EEV.MAL_ESTADO.value),
        ],
        on_change=cambiar,
    )

    tf_R = ft.TextField(label="Radio de curvatura en planta (m)",value = 100, on_submit=cambiar)
    cb_R = ft.Checkbox(value = False, on_change=cambiar)
    tf_RV = ft.TextField(label="Radio del acuerdo vertical (m)", value = 100, on_submit=cambiar)
    cb_RV = ft.Checkbox(value = False, on_change=cambiar)
    tf_DL = ft.TextField(label="Sobreancho máximo (m)",value=0.03,read_only=True, on_submit=cambiar)
    tf_D = ft.TextField(label="Peralte de la vía (m)", value = 0.11, on_submit=cambiar)
    tf_I = ft.TextField(label="Insuficiencia de peralte (m)", value = 0.07, on_submit=cambiar)
    tf_tol_sus = ft.TextField(label="Tolerancias en el reglaje de la suspensión (º)", value = 0.23, on_submit=cambiar)
    tf_tol_carga = ft.TextField(label="Reparto desigual de cargas (º)", value = 0.77, on_submit=cambiar)
    tf_vmax = ft.TextField(label="Velocidad máxima de la vía (km/h)", value=100, on_submit=cambiar)

    cb_graf_GPA = ft.Checkbox("Mostrar Gálibo superior", value = True, on_change = cambiar)
    cb_graf_GPB = ft.Checkbox("Mostrar Gálibo inferior", value = True, on_change = cambiar)
    cb_graf_GPA_lim = ft.Checkbox("Mostrar Gálibo límite", value = True, on_change = cambiar)
    cb_graf_GPA_nom = ft.Checkbox("Mostrar Gálibo nominal", value = True, on_change = cambiar)
    cb_graf_esGirado = ft.Checkbox("Girar gráfico", value = False, on_change = cambiar)
    cb_graf_inclinacion = ft.RadioGroup(content=ft.Row([
        ft.Radio(value="A derechas", label="A derechas"),
        ft.Radio(value="A izquierdas", label="A izquierdas")]),
        disabled = True,
        value = "A derechas",
        on_change=cambiar)

    tabla_var = ft.ResponsiveRow([
        ft.Column([
            ft.Text("Salientes", size = Tamanyos.MEDIANO.value),
            MiFilaDatos2("Radio de curvatura, planta", "R", "",  "m", ftt.t_R),
            MiFilaDatos2("Radio de curvatura, alzado", "R", "V",  "m", ftt.t_RV),
            MiFilaDatos2("Ancho de vía nominal", "l", "N", "m", ftt.t_LN),
            MiFilaDatos2("Sobreancho máximo", "D", "l", "m", ftt.t_DL),
            MiFilaDatos2("Ancho de vía", "I", "", "m", ftt.t_LND),
            MiFilaDatos2("Desplazamiento por inscripción en acuerdos vert.", "D", "hRV", "m", ftt.t_DhRV),
        ],
        col=1,
        ),
        ft.Column([
            ft.Text("Desplazamientos cuasiestáticos laterales", size = Tamanyos.MEDIANO.value),
            MiFilaDatos2("Peralte de la vía", "D", "", "m", ftt.t_D),
            MiFilaDatos2("Peralte por convenio de la vía", "D", "0", "m", ftt.t_D0),
            MiFilaDatos2("Peralte de equilibrio", "h", "eq", "m", ftt.t_heq),
            MiFilaDatos2("Insuficiencia de peralte", "I", "", "m", ftt.t_I),
            MiFilaDatos2("Insuficiencia de peralte por convenio", "I", "0", "m", ftt.t_I0),
            MiFilaDatos2("Distancia entre círculos de rodadura", "L", "", "m", ftt.t_L),
            MiFilaDatos2("Altura del centro de balanceo, por convenio", "h", "co", "m", ftt.t_hco),
        ],
        col=1
        ),
        ft.Column([
            ft.Text("Desplazamientos cuasiestáticos laterales", size = Tamanyos.MEDIANO.value),
            MiFilaDatos2("Desplazaiento lateral de la vía", "T", "via", "m", ftt.t_tvia),
            MiFilaDatos2("Diferencia entre peralte real y teórico", "T", "D", "m", ftt.t_td),
            MiFilaDatos2("Velocidad máxima de la vía", "V", "max", "km/h", ftt.t_vmax),
            MiFilaDatos2("Tolerancias en el reglaje de la suspensión", "α", "susp", "º", ftt.t_asusp),
            MiFilaDatos2("Reparto desigual de cargas", "α", "carga", "º", ftt.t_acarga),
            MiFilaDatos2("Giro total", "η", "0", "º", ftt.t_eta0),
            MiFilaDatos2("Giro por oscilaciones aleatorias por irreg. de la vía", "α", "osc,i,s0=0,4", "º", ftt.t_aosc_i_s0_04b),
            MiFilaDatos2("", "α", "osc,i,s0=0,3", "º", ftt.t_aosc_i_s0_03b),
            MiFilaDatos2("", "α", "osc,a,s0=0,4", "º", ftt.t_aosc_a_s0_04b),
            MiFilaDatos2("", "α", "osc,a,s0=0,3", "º", ftt.t_aosc_a_s0_03b),
        ],
        col=1
        ),
    ],
    columns=3
    )

    page.add(
        ft.Column([
            ft.ResponsiveRow([
                ft.Column(
                    col=4,
                    controls = [
                        ft.LineChart(
                            data_series=datos_grafico,
                            border=ft.border.all(3, ft.colors.with_opacity(0.2, ft.colors.ON_SURFACE)),
                            horizontal_grid_lines=ft.ChartGridLines(
                                interval=1000, color=ft.colors.with_opacity(0.2, ft.colors.ON_SURFACE), width=1
                            ),
                            vertical_grid_lines=ft.ChartGridLines(
                                interval=1000, color=ft.colors.with_opacity(0.2, ft.colors.ON_SURFACE), width=1
                            ),
                            left_axis=ft.ChartAxis(
                                show_labels = False,
                                labels=[],
                                labels_size=20,
                            ),
                            bottom_axis=ft.ChartAxis(
                                show_labels = False,
                                labels=[],
                                labels_size=20,
                            ),
                            tooltip_bgcolor=ft.colors.with_opacity(0.8, ft.colors.BLUE_GREY),
                            min_y=-1000,
                            max_y=2000,
                            min_x=-2000,
                            max_x=2000,
                            animate = 0,
                            #expand=True,
                            height=425,
                        ),
                        ]
                    ),
                ft.Column(
                    col=8,
                    controls = [ft.Tabs(
                        selected_index = 0,
                        animation_duration = 50,
                        tabs = [
                            ft.Tab(
                                text = "Vía única",
                                content = ft.Column(
                                    controls = [
                                        ft.Text("", size = 1),      #Espaciador, para que quede bonito
                                        ft.Row([
                                            dd_GPA,
                                            dd_GPB,
                                            dd_TV,
                                            dd_EV,
                                        ]),
                                        ft.Row([
                                            tf_R,
                                            cb_R,
                                            ft.Text("Alineación recta en planta",size=Tamanyos.PEQUENYO.value),
                                            tf_RV,
                                            cb_RV,
                                            ft.Text("Alineación recta en alzado",size=Tamanyos.PEQUENYO.value),
                                        ]),
                                        ft.Row([
                                            tf_DL,
                                            tf_D,
                                            tf_I,
                                        ]),
                                        ft.Row([
                                            tf_tol_sus,
                                            tf_tol_carga,
                                        ]),
                                        tf_vmax,
                                        ft.Row([
                                            cb_graf_GPA,
                                            cb_graf_GPB,
                                            cb_graf_GPA_lim,
                                            cb_graf_GPA_nom,
                                        ]),
                                        ft.Row([
                                            cb_graf_esGirado,
                                            cb_graf_inclinacion,
                                        ])
                                    ],
                                expand=1),
                                
                                ),
                            ft.Tab(
                                text = "Intereje",
                                content = ft.Column(
                                    controls = [
                                        ft.Text("", size = 1),      #Espaciador, para que quede bonito
                                        ft.Row([
                                            dd_GPA,
                                            dd_GPB,
                                            dd_TV,
                                            dd_EV,
                                        ]),
                                        ft.Row([
                                            tf_R,
                                            cb_R,
                                            ft.Text("Alineación recta en planta",size=Tamanyos.PEQUENYO.value),
                                            tf_RV,
                                            cb_RV,
                                            ft.Text("Alineación recta en alzado",size=Tamanyos.PEQUENYO.value),
                                        ]),
                                        ft.Row([
                                            tf_DL,
                                            tf_D,
                                            tf_I,
                                        ]),
                                        ft.Row([
                                            tf_tol_sus,
                                            tf_tol_carga,
                                        ]),
                                        tf_vmax,
                                        ft.Row([
                                            cb_graf_GPA,
                                            cb_graf_GPB,
                                            cb_graf_GPA_lim,
                                            cb_graf_GPA_nom,
                                        ]),
                                        ft.Row([
                                            cb_graf_esGirado,
                                            cb_graf_inclinacion,
                                        ])
                                    ],
                                expand=1),                            ),
                        ],
                        #expand= 0,
                    ),
                    
                ],
                height=425,),
                # ft.Column(col=8,
                #     controls = [
                #         ft.Text("DATOS", size = Tamanyos.MEDIANO.value),
                #         ft.Row([
                #             dd_GPA,
                #             dd_GPB,
                #             dd_TV,
                #             dd_EV,
                #         ]),
                #         ft.Row([
                #             tf_R,
                #             cb_R,
                #             ft.Text("Alineación recta en planta",size=Tamanyos.PEQUENYO.value),
                #             tf_RV,
                #             cb_RV,
                #             ft.Text("Alineación recta en alzado",size=Tamanyos.PEQUENYO.value),
                #         ]),
                #         ft.Row([
                #             tf_DL,
                #             tf_D,
                #             tf_I,
                #         ]),
                #         ft.Row([
                #             tf_tol_sus,
                #             tf_tol_carga,
                #         ]),
                #         tf_vmax,
                #         ft.Row([
                #             cb_graf_GPA,
                #             cb_graf_GPB,
                #             cb_graf_GPA_lim,
                #             cb_graf_GPA_nom,
                #         ]),
                #         ft.Row([
                #             cb_graf_esGirado,
                #             cb_graf_inclinacion,
                #         ])

                # ]),
        ]),
            ft.Tabs(
                selected_index=0,
                animation_duration=50,
                tabs=[
                    ft.Tab(
                        text = "Variables",
                        content = tabla_var,
                    ),
                    ft.Tab(
                        text = "Desplazamientos",
                        content = tabla_des,
                    ), 
                    ft.Tab(
                        text = "Galibo límite",
                        content = tabla_lim,
                    ), 
                    ft.Tab(
                        text = "Galibo nominal",
                        content = tabla_nom,
                    ), 
                ],
                expand = 0
                ),
        ])
    )

ft.app(galibos)