import flet as ft
import configuracion as conf
from datos_galibos import datos_GPA, datos_GPB
from datos_variables import Variables as var
from estilos.estilos import Tamanyos, EGPA, EGPB, ETV, EEV
from componentes.tablas_datos import *
from componentes.mis_componentes import *
import calculos.calculos as calc
from math import sin, cos, atan, degrees, radians

def galibos(page: ft.Page):

    #FUNCIÓN
    def cambiar(e):
        
        def signo(num):
            return 1 if num > 0 else -1
        
        #CÁLCULO DE LAS VARIABLES GENERALES DEL PROGRAMA
        #Los valores que no se definen aquí están definidos en la clase variables. No dependen de nada, son constantes
        var.GPA = dd_GPA.value
        var.GPB = dd_GPB.value
        print("-"*30)
        galiboPA = datos_GPA[var.GPA]
        galiboPB = datos_GPB[var.GPB]

        var.maxY = 0
        for nombre,punto in galiboPA.items():                                   #intentar hacer esto con la función max y una lambda
            if punto.Y > var.maxY:
                var.maxY = punto.Y
        match var.GPA:
            case EGPA.GHE16.value | EGPA.GEA16.value | EGPA.GEB16.value | EGPA.GEC16.value | EGPA.GA.value | EGPA.GB.value | EGPA.GC.value:
                var.hb_max = ( galiboPA["P3"].Y + galiboPA["P4"].Y ) / 2
            case EGPA.GEE10.value |EGPA.GED10.value | EGPA.PERSONALIZADO.value:
                var.hb_max = ( galiboPA["P1"].Y + galiboPA["P2"].Y ) / 2
        match var.GPA:
            case EGPA.GEA16.value | EGPA.GEB16.value: var.hquiebroaux = 3.32
            case EGPA.GA.value | EGPA.GB.value: var.hquiebroaux = 3.35
            case other: var.hquiebroaux = 0
        match var.GPA:
            case EGPA.GEA16.value: var.htopeaux = 3.7
            case EGPA.GEB16.value | EGPA.GB.value: var.htopeaux = 4.11
            case EGPA.GA.value: var.htopeaux = 3.88
            case other: var.htopeaux = 0
        match var.GPA:
            case EGPA.GEA16.value: var.difaux = 0.38
            case EGPA.GEB16.value: var.difaux = 0.79
            case EGPA.GA.value: var.difaux = 0.63
            case EGPA.GB.value: var.difaux = 0.86
            case other: var.difaux = 0
        match var.GPA:
            case EGPA.GEA16.value: var.otra = 4.84
            case EGPA.GEB16.value: var.otra = 6.48
            case EGPA.GA.value: var.otra = 5.77
            case EGPA.GB.value: var.otra = 6.69
            case other: var.otra = 0
        match var.GPA:
            case EGPA.GHE16.value | EGPA.GEA16.value | EGPA.GEB16.value | EGPA.GEC16.value: var.LN = 1.668
            case EGPA.GA.value | EGPA.GB.value | EGPA.GC.value: var.LN = 1.435
            case EGPA.GEE10.value |EGPA.GED10.value | EGPA.PERSONALIZADO.value: var.LN = 1

        #COMPROBACIÓN DE LOS CHECKBOXES: RADIOS EN PLANTA Y ALZADO, E INCLINACIÓN DEL GRÁFICO
        es_recta = cb_R.value
        es_recta_V = cb_RV.value
        es_girado = cb_graf_esGirado.value
        var.R = 99999999999 if es_recta else int(tf_R.value)
        var.Rv = 99999999999 if es_recta_V else int(tf_RV.value)
        tf_R.disabled = es_recta
        tf_RV.disabled = es_recta_V
        cb_graf_inclinacion.disabled = not es_girado
        var.Inclinac = 0.0 if not es_girado else degrees(atan(var.D / var.LN))
        lado_inclinacion = cb_graf_inclinacion.value
        print(lado_inclinacion)
        if lado_inclinacion == "A derechas":
            var.Inclinac = abs(var.Inclinac)
        elif lado_inclinacion == "A izquierdas":
            var.Inclinac = -abs(var.Inclinac)

        var.DL = tf_DL.value
        var.LND = var.LN + var.DL
        var.D = float(tf_D.value)
        match var.GPA:
            case EGPA.GHE16.value | EGPA.GEA16.value | EGPA.GEB16.value | EGPA.GEC16.value | EGPA.GA.value | EGPA.GB.value | EGPA.GC.value: var.D0 = 0.05
            case EGPA.GEE10.value |EGPA.GED10.value | EGPA.PERSONALIZADO.value: var.D0 = 0.07
        var.vmax = tf_vmax.value
        var.heq = (float(var.vmax) / 3.6)**2 * var.LN / (float(var.R) * 9.81)
        #var.I = var.heq - var.D
        var.I = float(tf_I.value)
        match var.GPA:
            case EGPA.GHE16.value | EGPA.GEA16.value | EGPA.GEB16.value | EGPA.GEC16.value | EGPA.GA.value | EGPA.GB.value | EGPA.GC.value: var.I0 = 0.05
            case EGPA.GEE10.value |EGPA.GED10.value | EGPA.PERSONALIZADO.value: var.I0 = 0.07
        match var.GPA:
            case EGPA.GHE16.value | EGPA.GEA16.value | EGPA.GEB16.value | EGPA.GEC16.value: var.L = 1.733
            case EGPA.GA.value | EGPA.GB.value | EGPA.GC.value: var.L = 1.5
            case EGPA.GEE10.value |EGPA.GED10.value | EGPA.PERSONALIZADO.value: var.L = 1.055
        var.tipo_via = dd_TV.value
        match var.tipo_via:
            case ETV.VIA_PLACA.value:
                var.TVIA = 0.005
                var.TD = 0.015
            case ETV.BALASTO.value:
                var.TVIA = 0.025
                var.TD = 0.02 if int(var.vmax) <=80 else 0.015
        var.asusp = tf_tol_sus.value
        var.acarga = tf_tol_carga.value
        var.eta0 = float(var.asusp) + float(var.acarga)
        var.estado_via = dd_EV.value
        if var.GPA in [EGPA.GEE10.value, EGPA.GED10.value, EGPA.PERSONALIZADO.value]:
            var.aosc_i_s0_04b = 0.20 if var.tipo_via == ETV.BALASTO.value else 0.1
            var.aosc_a_s0_04b = 1.00 if var.tipo_via == ETV.BALASTO.value else 0.6
            var.aosc_i_s0_03b = 0.20 if var.tipo_via == ETV.BALASTO.value else 0.1
            var.aosc_a_s0_03b = 1.00 if var.tipo_via == ETV.BALASTO.value else 0.6
        elif var.GPA in [EGPA.GHE16.value, EGPA.GEA16.value, EGPA.GEB16.value, EGPA.GEC16.value, EGPA.GA.value, EGPA.GB.value, EGPA.GC.value]:
            if var.tipo_via == ETV.VIA_PLACA.value:
                var.aosc_i_s0_04b = 0.1
                var.aosc_a_s0_04b = 0.6
                var.aosc_i_s0_03b = 0.08
                var.aosc_a_s0_03b = 0.45
            elif var.tipo_via == ETV.BALASTO.value:
                if var.estado_via == EEV.BUEN_ESTADO.value:
                    var.aosc_i_s0_04b = 0.1
                    var.aosc_a_s0_04b = 0.6
                    var.aosc_i_s0_03b = 0.08
                    var.aosc_a_s0_03b = 0.45
                elif var.estado_via == EEV.MAL_ESTADO.value:
                    var.aosc_i_s0_04b = 0.2
                    var.aosc_a_s0_04b = 1.0
                    var.aosc_i_s0_03b = 0.15
                    var.aosc_a_s0_03b = 0.75
        #var.Rv = tf_RV.value
        var.DhRV = 50/float(var.Rv)
        if var.GPA in [EGPA.GHE16.value, EGPA.GEA16.value, EGPA.GEB16.value, EGPA.GEC16.value, EGPA.GA.value, EGPA.GB.value, EGPA.GC.value]:
            if var.tipo_via == ETV.BALASTO.value and var.estado_via == EEV.BUEN_ESTADO.value:
                var.aosc_i_s0_04h = 0.1
            elif var.tipo_via == ETV.BALASTO.value and var.estado_via == EEV.MAL_ESTADO.value:
                var.aosc_i_s0_04h = 0.2
            elif var.tipo_via == ETV.VIA_PLACA.value:
                var.aosc_i_s0_04h = 0.1
        elif var.GPA in [EGPA.GEE10.value, EGPA.GED10.value, EGPA.PERSONALIZADO.value]:
            if var.tipo_via == ETV.BALASTO.value:
                var.aosc_i_s0_04h = 0.2
            elif var.tipo_via == ETV.VIA_PLACA.value:
                var.aosc_i_s0_04h = 0.1
        
        if var.GPA in [EGPA.GHE16.value, EGPA.GEA16.value, EGPA.GEB16.value, EGPA.GEC16.value, EGPA.GA.value, EGPA.GB.value, EGPA.GC.value]:
            if var.tipo_via == ETV.BALASTO.value and var.estado_via == EEV.BUEN_ESTADO.value:
                var.aosc_i_s0_03h = 0.08
            elif var.tipo_via == ETV.BALASTO.value and var.estado_via == EEV.MAL_ESTADO.value:
                var.aosc_i_s0_03h = 0.15
            elif var.tipo_via == ETV.VIA_PLACA.value:
                var.aosc_i_s0_03h = 0.08
        elif var.GPA in [EGPA.GEE10.value, EGPA.GED10.value, EGPA.PERSONALIZADO.value]:
            if var.tipo_via == ETV.BALASTO.value:
                var.aosc_i_s0_03h = 0.2
            elif var.tipo_via == ETV.VIA_PLACA.value:
                var.aosc_i_s0_03h = 0.1

        if var.GPA in [EGPA.GHE16.value, EGPA.GEA16.value, EGPA.GEB16.value, EGPA.GEC16.value, EGPA.GA.value, EGPA.GB.value, EGPA.GC.value]:
            if var.tipo_via == ETV.BALASTO.value and var.estado_via == EEV.BUEN_ESTADO.value:
                var.aosc_a_s0_04h = 0.6
            elif var.tipo_via == ETV.BALASTO.value and var.estado_via == EEV.MAL_ESTADO.value:
                var.aosc_a_s0_04h = 1.0
            elif var.tipo_via == ETV.VIA_PLACA.value:
                var.aosc_a_s0_04h = 0.6
        elif var.GPA in [EGPA.GEE10.value, EGPA.GED10.value, EGPA.PERSONALIZADO.value]:
            if var.tipo_via == ETV.BALASTO.value:
                var.aosc_a_s0_04h = 1.0
            elif var.tipo_via == ETV.VIA_PLACA.value:
                var.aosc_a_s0_04h = 0.6
        
        if var.GPA in [EGPA.GHE16.value, EGPA.GEA16.value, EGPA.GEB16.value, EGPA.GEC16.value, EGPA.GA.value, EGPA.GB.value, EGPA.GC.value]:
            if var.tipo_via == ETV.BALASTO.value and var.estado_via == EEV.BUEN_ESTADO.value:
                var.aosc_a_s0_03h = 0.45
            elif var.tipo_via == ETV.BALASTO.value and var.estado_via == EEV.MAL_ESTADO.value:
                var.aosc_a_s0_03h = 0.75
            elif var.tipo_via == ETV.VIA_PLACA.value:
                var.aosc_a_s0_03h = 0.45
        elif var.GPA in [EGPA.GEE10.value, EGPA.GED10.value, EGPA.PERSONALIZADO.value]:
            if var.tipo_via == ETV.BALASTO.value:
                var.aosc_a_s0_03h = 1.0
            elif var.tipo_via == ETV.VIA_PLACA.value:
                var.aosc_a_s0_03h = 0.6

        #ACTUALIZACIÓN DE LOS ELEMENTOS DE FLET CON LOS VALORES CALCULADOS ANTERIORMENTE
        t_R.value = var.R
        t_LN.value = var.LN
        t_DL.value = var.DL
        t_LND.value = var.LND
        
        t_D.value = var.D
        t_D0.value = var.D0
        t_heq.value = var.heq
        t_I.value = var.I
        t_I0.value = var.I0
        t_L.value = var.L
        t_hco.value = var.hco

        def limpiar_tabla(elemento: ft.Column, text1: str, text2: str, unidades: str):
            elemento.controls.clear()
            elemento.controls.append(MiText(text1, text2))
            elemento.controls.append(ft.Text(unidades,size=Tamanyos.TABLA_NORMAL.value))

        limpiar_tabla(tabla_00_Punto_des, "Punto", "", "()")
        limpiar_tabla(tabla_00_Punto_lim, "Punto", "", "()")
        limpiar_tabla(tabla_00_Punto_nom, "Punto", "", "()")
        limpiar_tabla(tabla_01_X_des, "X", "", "(mm)")
        limpiar_tabla(tabla_01_X_lim, "X", "", "(mm)")
        limpiar_tabla(tabla_01_X_nom, "X", "", "(mm)")
        limpiar_tabla(tabla_02_Y_des, "Y", "", "(mm)")
        limpiar_tabla(tabla_02_Y_lim, "Y", "", "(mm)")
        limpiar_tabla(tabla_02_Y_nom, "Y", "", "(mm)")
        limpiar_tabla(tabla_03_esPT, "esPT", "", "(S/N)")
        limpiar_tabla(tabla_04_k, "k", "", "()")
        limpiar_tabla(tabla_05_s0, "s", "0", "()")
        limpiar_tabla(tabla_06_Sa, "S", "a", "(mm)")
        limpiar_tabla(tabla_07_Si, "S", "i", "(mm)")
        limpiar_tabla(tabla_08_qsDai, "qs", "D,ai", "(mm)")
        limpiar_tabla(tabla_09_qsIai, "qs", "I,ai", "(mm)")
        limpiar_tabla(tabla_10_Tvia_ai, "T",  "via,ai", "(mm)")
        limpiar_tabla(tabla_11_Dbgai, "Δb", "g,ai", "(mm)")
        limpiar_tabla(tabla_12_Dbcai, "Δb", "c,ai", "(mm)")
        limpiar_tabla(tabla_13_Dbsuspai, "Δb", "susp,ai", "(mm)")
        limpiar_tabla(tabla_14_Dbcargaai, "Δb", "carg,ai", "(mm)")
        limpiar_tabla(tabla_15_Dbetaai, "Δb", "η,ai", "(mm)")
        limpiar_tabla(tabla_16_aosca, "α", "osc,a", "(º)")
        limpiar_tabla(tabla_17_aosci, "α", "osc,i", "(º)")
        limpiar_tabla(tabla_18_Dbosca, "Δb", "osc,a", "(mm)")
        limpiar_tabla(tabla_19_Dbosci, "Δb", "osc,i", "(mm)")
        limpiar_tabla(tabla_20_M3h, "M", "3b", "(mm)")
        limpiar_tabla(tabla_21_DhRv, "Δh", "Rv", "(mm)")
        limpiar_tabla(tabla_22_DhPTDai, "Δh", "PT,D,ai", "(mm)")
        limpiar_tabla(tabla_23_DhPTIai, "Δh", "PT,I,ai", "(mm)")
        limpiar_tabla(tabla_24_TN, "T", "N", "(mm)")
        limpiar_tabla(tabla_25_Dhga, "Δh", "g,a", "(mm)")
        limpiar_tabla(tabla_26_Dhgi, "Δh", "g,i", "(mm)")
        limpiar_tabla(tabla_27_Dhc, "Δh", "c", "(mm)")
        limpiar_tabla(tabla_28_Dhgca, "Δh", "g,ca", "(mm)")
        limpiar_tabla(tabla_29_Dhgci, "Δh", "g,ci", "(mm)")
        limpiar_tabla(tabla_30_Dhsuspai, "Δh", "suspai", "(mm)")
        limpiar_tabla(tabla_31_Dhcargai, "Δh", "carg,ai", "(mm)")
        limpiar_tabla(tabla_32_Dhetaai, "Δh", "η,ai", "(mm)")
        limpiar_tabla(tabla_33_Dhosca, "Δh", "osc,a", "(mm)")
        limpiar_tabla(tabla_34_Dhosci, "Δh", "osc,i", "(mm)")
        limpiar_tabla(tabla_35_M3h, "M", "3h", "(mm)")
        limpiar_tabla(tabla_36_lim_Sja1, "Σj", "a1", "(mm)")
        limpiar_tabla(tabla_37_lim_Sji1, "Σj", "i1", "(mm)")
        limpiar_tabla(tabla_38_lim_Sja2, "Σj", "a2", "(mm)")
        limpiar_tabla(tabla_39_lim_Sji2, "Σj", "i2", "mm")
        limpiar_tabla(tabla_40_lim_Sja1_ast, "Σj", "a1*", "(mm)")
        limpiar_tabla(tabla_41_lim_Sji1_ast, "Σj", "i1*", "(mm)")
        limpiar_tabla(tabla_42_lim_Sja2_ast, "Σj", "a2*", "(mm)")
        limpiar_tabla(tabla_43_lim_Sji2_ast, "Σj", "i2*", "(mm)")
        limpiar_tabla(tabla_44_lim_SVa1, "ΣV", "a1", "(mm)")
        limpiar_tabla(tabla_45_lim_SVi1, "ΣV", "i1", "(mm)")
        limpiar_tabla(tabla_46_lim_SVa2, "ΣV", "a2", "(mm)")
        limpiar_tabla(tabla_47_lim_SVi2, "ΣV", "i2", "(mm)")
        limpiar_tabla(tabla_48_lim_SVa1_ast, "ΣV", "a1*", "(mm)")
        limpiar_tabla(tabla_49_lim_SVi1_ast, "ΣV", "a2*", "(mm)")
        limpiar_tabla(tabla_50_lim_SVa2_ast, "ΣV", "i2*", "(mm)")
        limpiar_tabla(tabla_51_lim_SVi2_ast, "ΣV", "i2*", "(mm)")
        limpiar_tabla(tabla_52_nom_Sja3, "Σj", "a3", "(mm)")
        limpiar_tabla(tabla_53_nom_Sji3, "Σj", "i3", "(mm)")
        limpiar_tabla(tabla_54_nom_Sja4, "Σj", "a4", "(mm)")
        limpiar_tabla(tabla_55_nom_Sji4, "Σj", "i4", "(mm)")
        limpiar_tabla(tabla_56_nom_Sja3_ast, "Σj", "a3*", "(mm)")
        limpiar_tabla(tabla_57_nom_Sji3_ast, "Σj", "i3*", "(mm)")
        limpiar_tabla(tabla_58_nom_Sja4_ast, "Σj", "a4*", "(mm)")
        limpiar_tabla(tabla_59_nom_Sji4_ast, "Σj", "i4*", "(mm)")
        limpiar_tabla(tabla_60_nom_SVa3, "ΣV", "a3", "(mm)")
        limpiar_tabla(tabla_61_nom_SVi3, "ΣV", "i3", "(mm)")
        limpiar_tabla(tabla_62_nom_SVa4, "ΣV", "a4", "(mm)")
        limpiar_tabla(tabla_63_nom_SVi4, "ΣV", "i4", "(mm)")
        limpiar_tabla(tabla_64_nom_SVa3_ast, "ΣV", "a3*", "(mm)")
        limpiar_tabla(tabla_65_nom_SVi3_ast, "ΣV", "i3*", "(mm)")
        limpiar_tabla(tabla_66_nom_SVa4_ast, "ΣV", "a4*", "(mm)")
        limpiar_tabla(tabla_67_nom_SVi4_ast, "ΣV", "i4*", "(mm)")
        limpiar_tabla(tabla_68_lim_bobstVM_max_i, "b", "VM,max,i", "(mm)")
        limpiar_tabla(tabla_69_lim_hobstVM_con_i, "h", "VM,con,i", "(mm)")
        limpiar_tabla(tabla_70_lim_bobstVM_max_a, "b", "VM,max,a", "(mm)")
        limpiar_tabla(tabla_71_lim_hobstVM_con_a, "h", "VM,con,a", "(mm)")
        limpiar_tabla(tabla_72_lim_bobstVM_con_i, "b", "VM,con,i", "(mm)")
        limpiar_tabla(tabla_73_lim_hobstVM_max_i, "h", "VM,max,i", "(mm)")
        limpiar_tabla(tabla_74_lim_bobstVM_con_a, "b", "VM,con,a", "(mm)")
        limpiar_tabla(tabla_75_lim_hobstVM_max_a, "h", "VM,max,a", "(mm)")
        limpiar_tabla(tabla_76_lim_bobstV0_max_i, "b", "V0,max,i", "(mm)")
        limpiar_tabla(tabla_77_lim_hobstV0_con_i, "h", "V0,con,i", "(mm)")
        limpiar_tabla(tabla_78_lim_bobstV0_max_a, "b", "V0,max,a", "(mm)")
        limpiar_tabla(tabla_79_lim_hobstV0_con_a, "h", "V0,con,a", "(mm)")
        limpiar_tabla(tabla_80_lim_bobstV0_con_i, "b", "V0,con,i", "(mm)")
        limpiar_tabla(tabla_81_lim_hobstV0_max_i, "h", "V0,max,i", "(mm)")
        limpiar_tabla(tabla_82_lim_bobstV0_con_a, "b", "V0,con,a", "(mm)")
        limpiar_tabla(tabla_83_lim_hobstV0_max_a, "h", "V0,max,a", "(mm)")
        limpiar_tabla(tabla_84_nom_bobstVM_max_i, "b", "VM,max,i", "(mm)")
        limpiar_tabla(tabla_85_nom_hobstVM_con_i, "h", "VM,con,i", "(mm)")
        limpiar_tabla(tabla_86_nom_bobstVM_max_a, "b", "VM,max,a", "(mm)")
        limpiar_tabla(tabla_87_nom_hobstVM_con_a, "h", "VM,con,a", "(mm)")
        limpiar_tabla(tabla_88_nom_bobstVM_con_i, "b", "VM,con,i", "(mm)")
        limpiar_tabla(tabla_89_nom_hobstVM_max_i, "h", "VM,max,i", "(mm)")
        limpiar_tabla(tabla_90_nom_bobstVM_con_a, "b", "VM,con,a", "(mm)")
        limpiar_tabla(tabla_91_nom_hobstVM_max_a, "h", "VM,max,a", "(mm)")
        limpiar_tabla(tabla_92_nom_bobstV0_max_i, "b", "V0,max,i", "(mm)")
        limpiar_tabla(tabla_93_nom_hobstV0_con_i, "h", "V0,con,i", "(mm)")
        limpiar_tabla(tabla_94_nom_bobstV0_max_a, "b", "V0,max,a", "(mm)")
        limpiar_tabla(tabla_95_nom_hobstV0_con_a, "h", "V0,con,a", "(mm)")
        limpiar_tabla(tabla_96_nom_bobstV0_con_i, "b", "V0,con,i", "(mm)")
        limpiar_tabla(tabla_97_nom_hobstV0_max_i, "h", "V0,max,i", "(mm)")
        limpiar_tabla(tabla_98_nom_bobstV0_con_a, "b", "V0,con,a", "(mm)")
        limpiar_tabla(tabla_99_nom_hobstV0_max_a, "h", "V0,max,a", "(mm)")

        #ACTUALIZACIÓN DE LAS TABLAS DE DATOS DE FLET
        for nombre,punto in galiboPA.items():
            punto.esPT = calc.calcular_esPT(punto.Y, var.maxY)
            punto.k = calc.calcular_k(var.GPA, punto.Y/1000, var.hquiebroaux, var.htopeaux, var.difaux)
            punto.s0 = calc.calcular_s0(var.GPA, punto.Y/1000, var.hquiebroaux, var.htopeaux, var.difaux, var.hotra)
            punto.Sa = calc.calcular_Sa(var.GPA, var.GPB, var.R, var.LN, var.LND, var.hquiebroaux, punto.Y/1000, punto.k)
            punto.Si = calc.calcular_Si(var.GPA, var.GPB, var.R, var.LN, var.LND, var.hquiebroaux, punto.Y/1000, punto.k)
            punto.qsD_ai = calc.calcular_qsD_ai(punto.Y/1000, punto.s0, var.D, var.D0, var.L, var.hco)
            punto.qsI_ai = calc.calcular_qsI_ai(punto.Y/1000, punto.s0, var.I, var.I0, var.L, var.hco)
            punto.Tvia_ai = var.TVIA * 1000
            punto.Dbg_ai = calc.calcular_Dbg_ai(punto.Y/1000, var.L, var.TD)
            punto.Dbc_ai = calc.calcular_Dbc_ai(punto.Y/1000, var.L, var.TD, var.hco, punto.s0)
            punto.Dbsusp_ai = calc.calcular_Dbsusp_ai(var.asusp, punto.Y, var.hco * 1000)
            punto.Dbcarg_ai = calc.calcular_Dbcarg_ai(var.acarga, punto.Y, var.hco * 1000)
            punto.Dbeta0_ai = calc.calcular_Dbeta0_ai(var.eta0, punto.Y, var.hco * 1000)
            punto.aosc_a = calc.calcular_aosc(punto.s0, var.aosc_a_s0_03b, var.aosc_a_s0_04b)
            punto.aosc_i = calc.calcular_aosc(punto.s0, var.aosc_i_s0_03b, var.aosc_i_s0_04b)
            punto.Dbosc_a = calc.calcular_Dbosc(punto.aosc_a, punto.Y, var.hco * 1000)
            punto.Dbosc_i = calc.calcular_Dbosc(punto.aosc_i, punto.Y, var.hco * 1000)
            punto.M3b = var.M3b * 1000
            punto.DhRv = round(var.DhRV * 1000, 1)
            punto.DhPT_D_ai = calc.calcular_DhPT_D_ai(punto.X, punto.s0, var.D, var.D0, var.L)
            punto.DhPT_I_ai = calc.calcular_DhPT_I_ai(punto.X, punto.s0, var.I, var.I0, var.L)
            punto.TN = var.TN * 1000
            punto.Dhg_a = calc.calcular_Dhg_a(punto.X/1000, var.L, var.TD)
            punto.Dhg_i = calc.calcular_Dhg_i(punto.X/1000, var.L, var.TD)
            punto.Dhc = calc.calcular_Dhc(punto.X/1000, punto.s0, var.L, var.TD)
            punto.Dhgca = round(punto.Dhg_a + punto.Dhc, 1)
            punto.Dhgci = round(punto.Dhg_i + punto.Dhc, 1)
            punto.Dhsusp_ai = calc.calcular_Dhsusp_ai(punto.X, var.asusp)
            punto.Dhcarg_ai = calc.calcular_Dhcarg_ai(punto.X, var.acarga)
            punto.Dheta0_ai = calc.calcular_Dhcarg_ai(punto.X, var.eta0)
            punto.Dhosc_a = calc.calcular_Dhosc(punto.X, punto.aosc_i)                           #Sí, los ángulos están cambiados. Así debe ser.
            punto.Dhosc_i = calc.calcular_Dhosc(punto.X, punto.aosc_a)                           #Sí, los ángulos están cambiados. Así debe ser.
            punto.M3h = var.M3h * 1000

            punto.lim_Sja1 = calc.calcular_lim_Sj1(punto.Y/1000, var.hco, var.K, var.Kale_h_0_50, punto.Tvia_ai, punto.Dbg_ai, punto.Dbc_ai, punto.Dbsusp_ai, punto.Dbcarg_ai, punto.Dbosc_a)
            punto.lim_Sji1 = calc.calcular_lim_Sj1(punto.Y/1000, var.hco, var.K, var.Kale_h_0_50, punto.Tvia_ai, punto.Dbg_ai, punto.Dbc_ai, punto.Dbsusp_ai, punto.Dbcarg_ai, punto.Dbosc_i)
            punto.lim_Sja2 = calc.calcular_lim_Sj2(punto.Y/1000, var.hco, var.K, var.Kale_h_0_50, punto.Tvia_ai, punto.Dbg_ai)
            punto.lim_Sji2 = punto.lim_Sja2
            punto.lim_rad_Sja1_ast = calc.calcular_lim_rad_Sj1(punto.Tvia_ai, punto.Dbg_ai, punto.Dbc_ai, punto.Dbsusp_ai, punto.Dbcarg_ai, punto.Dbosc_a)
            punto.lim_rad_Sji1_ast = calc.calcular_lim_rad_Sj1(punto.Tvia_ai, punto.Dbg_ai, punto.Dbc_ai, punto.Dbsusp_ai, punto.Dbcarg_ai, punto.Dbosc_i)
            punto.lim_rad_Sjai2_ast = calc.calcular_lim_rad_Sj2(punto.Tvia_ai, punto.Dbg_ai)
            punto.lim_Sja1_ast = calc.calcular_lim_Sj_ast(punto.Y / 1000, var.hco, var.K, var.Kale_h_0_50, punto.lim_rad_Sja1_ast)
            punto.lim_Sji1_ast = calc.calcular_lim_Sj_ast(punto.Y / 1000, var.hco, var.K, var.Kale_h_0_50, punto.lim_rad_Sji1_ast)
            punto.lim_Sja2_ast = calc.calcular_lim_Sj_ast(punto.Y / 1000, var.hco, var.K, var.Kale_h_0_50, punto.lim_rad_Sjai2_ast)
            punto.lim_Sji2_ast = calc.calcular_lim_Sj_ast(punto.Y / 1000, var.hco, var.K, var.Kale_h_0_50, punto.lim_rad_Sjai2_ast)
            punto.lim_rad_SVi1 = calc.calcular_lim_rad_SVi1(punto.TN, punto.Dhg_i, punto.Dhc, punto.Dhsusp_ai, punto.Dhcarg_ai, punto.Dhosc_i)
            punto.lim_rad_SVa1 = calc.calcular_lim_rad_SVa1(punto.TN, punto.Dhg_a, punto.Dhc, punto.Dhsusp_ai, punto.Dhcarg_ai, punto.Dhosc_a)
            punto.lim_SVa1 = calc.calcular_lim_SV1(var.K, punto.lim_rad_SVa1)
            punto.lim_SVi1 = calc.calcular_lim_SV1(var.K, punto.lim_rad_SVi1)
            punto.lim_SVa2 = punto.TN
            punto.lim_SVi2 = punto.TN
            punto.lim_SVa1_ast = calc.calcular_SVa1_ast(var.K, punto.TN, punto.Dhg_a, punto.Dhc, punto.Dhsusp_ai, punto.Dhcarg_ai, punto.Dhosc_a)
            punto.lim_SVi1_ast = calc.calcular_SVi1_ast(var.K, punto.TN, punto.Dhg_i, punto.Dhc, punto.Dhsusp_ai, punto.Dhcarg_ai, punto.Dhosc_i)
            punto.lim_SVa2_ast = punto.TN
            punto.lim_SVi2_ast = punto.TN
            punto.lim_bobstVM_max_i = calc.calcular_lim_bobst(punto.X, punto.Y / 1000, punto.Si, -punto.qsI_ai, punto.lim_Sji1, punto.lim_Sji2)
            punto.lim_hobstVM_con_i = calc.calcular_lim_hobst(punto.Y, punto.DhRv, var.hb_max, punto.esPT, punto.DhPT_I_ai, punto.lim_SVi1, punto.lim_SVi2)
            punto.lim_bobstVM_max_a = calc.calcular_lim_bobst(punto.X, punto.Y / 1000, punto.Sa, punto.qsI_ai, punto.lim_Sja1, punto.lim_Sja2)
            punto.lim_hobstVM_con_a = calc.calcular_lim_hobst(punto.Y, punto.DhRv, var.hb_max, punto.esPT, -punto.DhPT_I_ai, punto.lim_SVa1, punto.lim_SVa2)
            punto.lim_bobstVM_con_i = calc.calcular_lim_bobst(punto.X, punto.Y / 1000, punto.Si, -punto.qsI_ai, punto.lim_Sji1_ast, punto.lim_Sji2_ast)
            punto.lim_hobstVM_max_i = calc.calcular_lim_hobst(punto.Y, punto.DhRv, var.hb_max, punto.esPT, punto.DhPT_I_ai, punto.lim_SVi1_ast, punto.lim_SVi2_ast)
            punto.lim_bobstVM_con_a = calc.calcular_lim_bobst(punto.X, punto.Y / 1000, punto.Sa, punto.qsI_ai, punto.lim_Sja1_ast, punto.lim_Sja2_ast)
            punto.lim_hobstVM_max_a = calc.calcular_lim_hobst(punto.Y, punto.DhRv, var.hb_max, punto.esPT, -punto.DhPT_I_ai, punto.lim_SVa1_ast, punto.lim_SVa2_ast)
            punto.lim_bobstV0_max_i = calc.calcular_lim_bobst(punto.X, punto.Y / 1000, punto.Si, punto.qsD_ai, punto.lim_Sji1, punto.lim_Sji2)
            punto.lim_hobstV0_con_i = calc.calcular_lim_hobst(punto.Y, punto.DhRv, var.hb_max, punto.esPT, -punto.DhPT_D_ai, punto.lim_SVi1, punto.lim_SVi2)
            punto.lim_bobstV0_max_a = calc.calcular_lim_bobst(punto.X, punto.Y / 1000, punto.Sa, -punto.qsD_ai, punto.lim_Sja1, punto.lim_Sja2)
            punto.lim_hobstV0_con_a = calc.calcular_lim_hobst(punto.Y, punto.DhRv, var.hb_max, punto.esPT, punto.DhPT_D_ai, punto.lim_SVa1, punto.lim_SVa2)
            punto.lim_bobstV0_con_i = calc.calcular_lim_bobst(punto.X, punto.Y / 1000, punto.Si, punto.qsD_ai, punto.lim_Sji1_ast, punto.lim_Sji2_ast)
            punto.lim_hobstV0_max_i = calc.calcular_lim_hobst(punto.Y, punto.DhRv, var.hb_max, punto.esPT, -punto.DhPT_D_ai, punto.lim_SVi1_ast, punto.lim_SVi2_ast)
            punto.lim_bobstV0_con_a = calc.calcular_lim_bobst(punto.X, punto.Y / 1000, punto.Sa, -punto.qsD_ai, punto.lim_Sja1_ast, punto.lim_Sja2_ast)
            punto.lim_hobstV0_max_a = calc.calcular_lim_hobst(punto.Y, punto.DhRv, var.hb_max, punto.esPT, punto.DhPT_D_ai, punto.lim_SVa1_ast, punto.lim_SVa2_ast)
            punto.lim_ba = signo(punto.X) * max(abs(punto.lim_bobstVM_max_a), abs(punto.lim_bobstVM_con_a), abs(punto.lim_bobstV0_max_a), abs(punto.lim_bobstV0_con_a))
            punto.lim_ha = calc.calcular_h(punto.Y/1000, var.hb_max / 1000, punto.lim_hobstVM_con_a, punto.lim_hobstVM_max_a, punto.lim_hobstV0_con_a, punto.lim_hobstV0_max_a)
            punto.lim_bi = signo(punto.X) * max(abs(punto.lim_bobstVM_max_i), abs(punto.lim_bobstVM_con_i), abs(punto.lim_bobstV0_max_i), abs(punto.lim_bobstV0_con_i))
            punto.lim_hi = calc.calcular_h(punto.Y/1000, var.hb_max / 1000, punto.lim_hobstVM_con_i, punto.lim_hobstVM_max_i, punto.lim_hobstV0_con_i, punto.lim_hobstV0_max_i)

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
            punto.nom_hobstVM_con_i = calc.calcular_nom_hobst(punto.Y, punto.DhRv, var.hb_max, punto.esPT, punto.DhPT_I_ai, punto.nom_SVi3, punto.nom_SVi4, punto.M3h)
            punto.nom_bobstVM_max_a = calc.calcular_nom_bobst(punto.X, punto.Y / 1000, punto.Sa, punto.qsI_ai, punto.nom_Sja3, punto.nom_Sja4, punto.M3b)
            punto.nom_hobstVM_con_a = calc.calcular_nom_hobst(punto.Y, punto.DhRv, var.hb_max, punto.esPT, -punto.DhPT_I_ai, punto.nom_SVa3, punto.nom_SVa4, punto.M3h)
            punto.nom_bobstVM_con_i = calc.calcular_nom_bobst(punto.X, punto.Y / 1000, punto.Si, -punto.qsI_ai, punto.nom_Sji3_ast, punto.nom_Sji4_ast, punto.M3b)
            punto.nom_hobstVM_max_i = calc.calcular_nom_hobst(punto.Y, punto.DhRv, var.hb_max, punto.esPT, punto.DhPT_I_ai, punto.nom_SVi3_ast, punto.nom_SVi4_ast,punto.M3h)
            punto.nom_bobstVM_con_a = calc.calcular_nom_bobst(punto.X, punto.Y / 1000, punto.Sa, punto.qsI_ai, punto.nom_Sja3_ast, punto.nom_Sja4_ast, punto.M3b)
            punto.nom_hobstVM_max_a = calc.calcular_nom_hobst(punto.Y, punto.DhRv, var.hb_max, punto.esPT, -punto.DhPT_I_ai, punto.nom_SVa3_ast, punto.nom_SVa4_ast, punto.M3h)
            punto.nom_bobstV0_max_i = calc.calcular_nom_bobst(punto.X, punto.Y / 1000, punto.Si, punto.qsD_ai, punto.nom_Sji3, punto.nom_Sji4, punto.M3b)
            punto.nom_hobstV0_con_i = calc.calcular_nom_hobst(punto.Y, punto.DhRv, var.hb_max, punto.esPT, -punto.DhPT_D_ai, punto.nom_SVi3, punto.nom_SVi4, punto.M3h)
            punto.nom_bobstV0_max_a = calc.calcular_nom_bobst(punto.X, punto.Y / 1000, punto.Sa, -punto.qsD_ai, punto.nom_Sja3, punto.nom_Sja4, punto.M3b)
            punto.nom_hobstV0_con_a = calc.calcular_nom_hobst(punto.Y, punto.DhRv, var.hb_max, punto.esPT, punto.DhPT_D_ai, punto.nom_SVa3, punto.nom_SVa4, punto.M3h)
            punto.nom_bobstV0_con_i = calc.calcular_nom_bobst(punto.X, punto.Y / 1000, punto.Si, punto.qsD_ai, punto.nom_Sji3_ast, punto.nom_Sji4_ast, punto.M3b)
            punto.nom_hobstV0_max_i = calc.calcular_nom_hobst(punto.Y, punto.DhRv, var.hb_max, punto.esPT, -punto.DhPT_D_ai, punto.nom_SVi3_ast, punto.nom_SVi4_ast, punto.M3h)
            punto.nom_bobstV0_con_a = calc.calcular_nom_bobst(punto.X, punto.Y / 1000, punto.Sa, -punto.qsD_ai, punto.nom_Sja3_ast, punto.nom_Sja4_ast, punto.M3b)
            punto.nom_hobstV0_max_a = calc.calcular_nom_hobst(punto.Y, punto.DhRv, var.hb_max, punto.esPT, punto.DhPT_D_ai, punto.nom_SVa3_ast, punto.nom_SVa4_ast, punto.M3h)
            punto.nom_ba = signo(punto.X) * max(abs(punto.nom_bobstVM_max_a), abs(punto.nom_bobstVM_con_a), abs(punto.nom_bobstV0_max_a), abs(punto.nom_bobstV0_con_a))
            punto.nom_ha = calc.calcular_h(punto.Y/1000, var.hb_max / 1000, punto.nom_hobstVM_con_a, punto.nom_hobstVM_max_a, punto.nom_hobstV0_con_a, punto.nom_hobstV0_max_a)
            punto.nom_bi = signo(punto.X) * max(abs(punto.nom_bobstVM_max_i), abs(punto.nom_bobstVM_con_i), abs(punto.nom_bobstV0_max_i), abs(punto.nom_bobstV0_con_i))
            punto.nom_hi = calc.calcular_h(punto.Y/1000, var.hb_max / 1000, punto.nom_hobstVM_con_i, punto.nom_hobstVM_max_i, punto.nom_hobstV0_con_i, punto.nom_hobstV0_max_i)

            tabla_00_Punto_des.controls.append(ft.Text(nombre,size=Tamanyos.TABLA_NORMAL.value))
            tabla_00_Punto_lim.controls.append(ft.Text(nombre,size=Tamanyos.TABLA_NORMAL.value))
            tabla_00_Punto_nom.controls.append(ft.Text(nombre,size=Tamanyos.TABLA_NORMAL.value))
            tabla_01_X_des.controls.append(ft.Text(punto.X,size=Tamanyos.TABLA_NORMAL.value))
            tabla_01_X_lim.controls.append(ft.Text(punto.X,size=Tamanyos.TABLA_NORMAL.value))
            tabla_01_X_nom.controls.append(ft.Text(punto.X,size=Tamanyos.TABLA_NORMAL.value))
            tabla_02_Y_des.controls.append(ft.Text(punto.Y,size=Tamanyos.TABLA_NORMAL.value))
            tabla_02_Y_lim.controls.append(ft.Text(punto.Y,size=Tamanyos.TABLA_NORMAL.value))
            tabla_02_Y_nom.controls.append(ft.Text(punto.Y,size=Tamanyos.TABLA_NORMAL.value))
            tabla_03_esPT.controls.append(ft.Text(punto.esPT,size=Tamanyos.TABLA_NORMAL.value))
            tabla_04_k.controls.append(ft.Text(punto.k,size=Tamanyos.TABLA_NORMAL.value))
            tabla_05_s0.controls.append(ft.Text(punto.s0,size=Tamanyos.TABLA_NORMAL.value))
            tabla_06_Sa.controls.append(ft.Text(punto.Sa,size=Tamanyos.TABLA_NORMAL.value))
            tabla_07_Si.controls.append(ft.Text(punto.Si,size=Tamanyos.TABLA_NORMAL.value))
            tabla_08_qsDai.controls.append(ft.Text(punto.qsD_ai,size=Tamanyos.TABLA_NORMAL.value))
            tabla_09_qsIai.controls.append(ft.Text(punto.qsI_ai,size=Tamanyos.TABLA_NORMAL.value))
            tabla_10_Tvia_ai.controls.append(ft.Text(punto.Tvia_ai,size=Tamanyos.TABLA_NORMAL.value))
            tabla_11_Dbgai.controls.append(ft.Text(punto.Dbg_ai,size=Tamanyos.TABLA_NORMAL.value))
            tabla_12_Dbcai.controls.append(ft.Text(punto.Dbc_ai,size=Tamanyos.TABLA_NORMAL.value))
            tabla_13_Dbsuspai.controls.append(ft.Text(punto.Dbsusp_ai,size=Tamanyos.TABLA_NORMAL.value))
            tabla_14_Dbcargaai.controls.append(ft.Text(punto.Dbcarg_ai,size=Tamanyos.TABLA_NORMAL.value))
            tabla_15_Dbetaai.controls.append(ft.Text(punto.Dbeta0_ai,size=Tamanyos.TABLA_NORMAL.value))
            tabla_16_aosca.controls.append(ft.Text(punto.aosc_a,size=Tamanyos.TABLA_NORMAL.value))
            tabla_17_aosci.controls.append(ft.Text(punto.aosc_i,size=Tamanyos.TABLA_NORMAL.value))
            tabla_18_Dbosca.controls.append(ft.Text(punto.Dbosc_a,size=Tamanyos.TABLA_NORMAL.value))
            tabla_19_Dbosci.controls.append(ft.Text(punto.Dbosc_i,size=Tamanyos.TABLA_NORMAL.value))
            tabla_20_M3h.controls.append(ft.Text(punto.M3b,size=Tamanyos.TABLA_NORMAL.value))
            tabla_21_DhRv.controls.append(ft.Text(punto.DhRv,size=Tamanyos.TABLA_NORMAL.value))
            tabla_22_DhPTDai.controls.append(ft.Text(punto.DhPT_D_ai,size=Tamanyos.TABLA_NORMAL.value))
            tabla_23_DhPTIai.controls.append(ft.Text(punto.DhPT_I_ai,size=Tamanyos.TABLA_NORMAL.value))
            tabla_24_TN.controls.append(ft.Text(punto.TN,size=Tamanyos.TABLA_NORMAL.value))
            tabla_25_Dhga.controls.append(ft.Text(punto.Dhg_a,size=Tamanyos.TABLA_NORMAL.value))
            tabla_26_Dhgi.controls.append(ft.Text(punto.Dhg_i,size=Tamanyos.TABLA_NORMAL.value))
            tabla_27_Dhc.controls.append(ft.Text(punto.Dhc,size=Tamanyos.TABLA_NORMAL.value))
            tabla_28_Dhgca.controls.append(ft.Text(punto.Dhgca,size=Tamanyos.TABLA_NORMAL.value))
            tabla_29_Dhgci.controls.append(ft.Text(punto.Dhgci,size=Tamanyos.TABLA_NORMAL.value))
            tabla_30_Dhsuspai.controls.append(ft.Text(punto.Dhsusp_ai,size=Tamanyos.TABLA_NORMAL.value))
            tabla_31_Dhcargai.controls.append(ft.Text(punto.Dhcarg_ai,size=Tamanyos.TABLA_NORMAL.value))
            tabla_32_Dhetaai.controls.append(ft.Text(punto.Dheta0_ai,size=Tamanyos.TABLA_NORMAL.value))
            tabla_33_Dhosca.controls.append(ft.Text(punto.Dhosc_a,size=Tamanyos.TABLA_NORMAL.value))
            tabla_34_Dhosci.controls.append(ft.Text(punto.Dhosc_i,size=Tamanyos.TABLA_NORMAL.value))
            tabla_35_M3h.controls.append(ft.Text(punto.M3h,size=Tamanyos.TABLA_NORMAL.value))
            tabla_36_lim_Sja1.controls.append(ft.Text(punto.lim_Sja1,size=Tamanyos.TABLA_NORMAL.value))
            tabla_37_lim_Sji1.controls.append(ft.Text(punto.lim_Sji1,size=Tamanyos.TABLA_NORMAL.value))
            tabla_38_lim_Sja2.controls.append(ft.Text(punto.lim_Sja2,size=Tamanyos.TABLA_NORMAL.value))
            tabla_39_lim_Sji2.controls.append(ft.Text(punto.lim_Sji2,size=Tamanyos.TABLA_NORMAL.value))
            tabla_40_lim_Sja1_ast.controls.append(ft.Text(punto.lim_Sja1_ast,size=Tamanyos.TABLA_NORMAL.value))
            tabla_41_lim_Sji1_ast.controls.append(ft.Text(punto.lim_Sji1_ast,size=Tamanyos.TABLA_NORMAL.value))
            tabla_42_lim_Sja2_ast.controls.append(ft.Text(punto.lim_Sja2_ast,size=Tamanyos.TABLA_NORMAL.value))
            tabla_43_lim_Sji2_ast.controls.append(ft.Text(punto.lim_Sji2_ast,size=Tamanyos.TABLA_NORMAL.value))
            tabla_44_lim_SVa1.controls.append(ft.Text(punto.lim_SVa1,size=Tamanyos.TABLA_NORMAL.value))
            tabla_45_lim_SVi1.controls.append(ft.Text(punto.lim_SVi1,size=Tamanyos.TABLA_NORMAL.value))
            tabla_46_lim_SVa2.controls.append(ft.Text(punto.lim_SVa2,size=Tamanyos.TABLA_NORMAL.value))
            tabla_47_lim_SVi2.controls.append(ft.Text(punto.lim_SVi2,size=Tamanyos.TABLA_NORMAL.value))
            tabla_48_lim_SVa1_ast.controls.append(ft.Text(punto.lim_SVa1_ast,size=Tamanyos.TABLA_NORMAL.value))
            tabla_49_lim_SVi1_ast.controls.append(ft.Text(punto.lim_SVi1_ast,size=Tamanyos.TABLA_NORMAL.value))
            tabla_50_lim_SVa2_ast.controls.append(ft.Text(punto.lim_SVa2_ast,size=Tamanyos.TABLA_NORMAL.value))
            tabla_51_lim_SVi2_ast.controls.append(ft.Text(punto.lim_SVi2_ast,size=Tamanyos.TABLA_NORMAL.value))
            tabla_52_nom_Sja3.controls.append(ft.Text(punto.nom_Sja3,size=Tamanyos.TABLA_NORMAL.value))
            tabla_53_nom_Sji3.controls.append(ft.Text(punto.nom_Sji3,size=Tamanyos.TABLA_NORMAL.value))
            tabla_54_nom_Sja4.controls.append(ft.Text(punto.nom_Sja4,size=Tamanyos.TABLA_NORMAL.value))
            tabla_55_nom_Sji4.controls.append(ft.Text(punto.nom_Sji4,size=Tamanyos.TABLA_NORMAL.value))
            tabla_56_nom_Sja3_ast.controls.append(ft.Text(punto.nom_Sja3_ast,size=Tamanyos.TABLA_NORMAL.value))
            tabla_57_nom_Sji3_ast.controls.append(ft.Text(punto.nom_Sji3_ast,size=Tamanyos.TABLA_NORMAL.value))
            tabla_58_nom_Sja4_ast.controls.append(ft.Text(punto.nom_Sja4_ast,size=Tamanyos.TABLA_NORMAL.value))
            tabla_59_nom_Sji4_ast.controls.append(ft.Text(punto.nom_Sji4_ast,size=Tamanyos.TABLA_NORMAL.value))
            tabla_60_nom_SVa3.controls.append(ft.Text(punto.nom_SVa3,size=Tamanyos.TABLA_NORMAL.value))
            tabla_61_nom_SVi3.controls.append(ft.Text(punto.nom_SVi3,size=Tamanyos.TABLA_NORMAL.value))
            tabla_62_nom_SVa4.controls.append(ft.Text(punto.nom_SVa4,size=Tamanyos.TABLA_NORMAL.value))
            tabla_63_nom_SVi4.controls.append(ft.Text(punto.nom_SVi4,size=Tamanyos.TABLA_NORMAL.value))
            tabla_64_nom_SVa3_ast.controls.append(ft.Text(punto.nom_SVa3_ast,size=Tamanyos.TABLA_NORMAL.value))
            tabla_65_nom_SVi3_ast.controls.append(ft.Text(punto.nom_SVi3_ast,size=Tamanyos.TABLA_NORMAL.value))
            tabla_66_nom_SVa4_ast.controls.append(ft.Text(punto.nom_SVa4_ast,size=Tamanyos.TABLA_NORMAL.value))
            tabla_67_nom_SVi4_ast.controls.append(ft.Text(punto.nom_SVi4_ast,size=Tamanyos.TABLA_NORMAL.value))
            tabla_68_lim_bobstVM_max_i.controls.append(ft.Text(punto.lim_bobstVM_max_i,size=Tamanyos.TABLA_NORMAL.value))
            tabla_69_lim_hobstVM_con_i.controls.append(ft.Text(punto.lim_hobstVM_con_i,size=Tamanyos.TABLA_NORMAL.value))
            tabla_70_lim_bobstVM_max_a.controls.append(ft.Text(punto.lim_bobstVM_max_a,size=Tamanyos.TABLA_NORMAL.value))
            tabla_71_lim_hobstVM_con_a.controls.append(ft.Text(punto.lim_hobstVM_con_a,size=Tamanyos.TABLA_NORMAL.value))
            tabla_72_lim_bobstVM_con_i.controls.append(ft.Text(punto.lim_bobstVM_con_i,size=Tamanyos.TABLA_NORMAL.value))
            tabla_73_lim_hobstVM_max_i.controls.append(ft.Text(punto.lim_hobstVM_max_i,size=Tamanyos.TABLA_NORMAL.value))
            tabla_74_lim_bobstVM_con_a.controls.append(ft.Text(punto.lim_bobstVM_con_a,size=Tamanyos.TABLA_NORMAL.value))
            tabla_75_lim_hobstVM_max_a.controls.append(ft.Text(punto.lim_hobstVM_max_a,size=Tamanyos.TABLA_NORMAL.value))
            tabla_76_lim_bobstV0_max_i.controls.append(ft.Text(punto.lim_bobstV0_max_i,size=Tamanyos.TABLA_NORMAL.value))
            tabla_77_lim_hobstV0_con_i.controls.append(ft.Text(punto.lim_hobstV0_con_i,size=Tamanyos.TABLA_NORMAL.value))
            tabla_78_lim_bobstV0_max_a.controls.append(ft.Text(punto.lim_bobstV0_max_a,size=Tamanyos.TABLA_NORMAL.value))
            tabla_79_lim_hobstV0_con_a.controls.append(ft.Text(punto.lim_hobstV0_con_a,size=Tamanyos.TABLA_NORMAL.value))
            tabla_80_lim_bobstV0_con_i.controls.append(ft.Text(punto.lim_bobstV0_con_i,size=Tamanyos.TABLA_NORMAL.value))
            tabla_81_lim_hobstV0_max_i.controls.append(ft.Text(punto.lim_hobstV0_max_i,size=Tamanyos.TABLA_NORMAL.value))
            tabla_82_lim_bobstV0_con_a.controls.append(ft.Text(punto.lim_bobstV0_con_a,size=Tamanyos.TABLA_NORMAL.value))
            tabla_83_lim_hobstV0_max_a.controls.append(ft.Text(punto.lim_hobstV0_max_a,size=Tamanyos.TABLA_NORMAL.value))
            tabla_84_nom_bobstVM_max_i.controls.append(ft.Text(punto.nom_bobstVM_max_i,size=Tamanyos.TABLA_NORMAL.value))
            tabla_85_nom_hobstVM_con_i.controls.append(ft.Text(punto.nom_hobstVM_con_i,size=Tamanyos.TABLA_NORMAL.value))
            tabla_86_nom_bobstVM_max_a.controls.append(ft.Text(punto.nom_bobstVM_max_a,size=Tamanyos.TABLA_NORMAL.value))
            tabla_87_nom_hobstVM_con_a.controls.append(ft.Text(punto.nom_hobstVM_con_a,size=Tamanyos.TABLA_NORMAL.value))
            tabla_88_nom_bobstVM_con_i.controls.append(ft.Text(punto.nom_bobstVM_con_i,size=Tamanyos.TABLA_NORMAL.value))
            tabla_89_nom_hobstVM_max_i.controls.append(ft.Text(punto.nom_hobstVM_max_i,size=Tamanyos.TABLA_NORMAL.value))
            tabla_90_nom_bobstVM_con_a.controls.append(ft.Text(punto.nom_bobstVM_con_a,size=Tamanyos.TABLA_NORMAL.value))
            tabla_91_nom_hobstVM_max_a.controls.append(ft.Text(punto.nom_hobstVM_max_a,size=Tamanyos.TABLA_NORMAL.value))
            tabla_92_nom_bobstV0_max_i.controls.append(ft.Text(punto.nom_bobstV0_max_i,size=Tamanyos.TABLA_NORMAL.value))
            tabla_93_nom_hobstV0_con_i.controls.append(ft.Text(punto.nom_hobstV0_con_i,size=Tamanyos.TABLA_NORMAL.value))
            tabla_94_nom_bobstV0_max_a.controls.append(ft.Text(punto.nom_bobstV0_max_a,size=Tamanyos.TABLA_NORMAL.value))
            tabla_95_nom_hobstV0_con_a.controls.append(ft.Text(punto.nom_hobstV0_con_a,size=Tamanyos.TABLA_NORMAL.value))
            tabla_96_nom_bobstV0_con_i.controls.append(ft.Text(punto.nom_bobstV0_con_i,size=Tamanyos.TABLA_NORMAL.value))
            tabla_97_nom_hobstV0_max_i.controls.append(ft.Text(punto.nom_hobstV0_max_i,size=Tamanyos.TABLA_NORMAL.value))
            tabla_98_nom_bobstV0_con_a.controls.append(ft.Text(punto.nom_bobstV0_con_a,size=Tamanyos.TABLA_NORMAL.value))
            tabla_99_nom_hobstV0_max_a.controls.append(ft.Text(punto.nom_hobstV0_max_a,size=Tamanyos.TABLA_NORMAL.value))

        #ACTUALIZACIÓN DE LOS GRÁFICOS
        datos_grafico_GPA.data_points.clear()
        datos_grafico_GPA_lim.data_points.clear()
        datos_grafico_GPA_nom.data_points.clear()
        datos_grafico_GPB.data_points.clear()
        #datos_grafico_GPB_lim.data_points.clear()

        for nombre,punto in galiboPA.items():
            datos_grafico_GPA.data_points.append(ft.LineChartDataPoint(
                cos(radians(var.Inclinac)) * punto.X/conf.ESCALA_GRAFICO + sin(radians(var.Inclinac)) * punto.Y/conf.ESCALA_GRAFICO,
                - sin(radians(var.Inclinac)) * punto.X/conf.ESCALA_GRAFICO + cos(radians(var.Inclinac)) * punto.Y/conf.ESCALA_GRAFICO,
                tooltip=(nombre, punto.X, punto.Y)))
            datos_grafico_GPA_lim.data_points.append(ft.LineChartDataPoint(
                cos(radians(var.Inclinac)) * punto.lim_bi/conf.ESCALA_GRAFICO + sin(radians(var.Inclinac)) * punto.lim_hi/conf.ESCALA_GRAFICO,
                - sin(radians(var.Inclinac)) * punto.lim_bi/conf.ESCALA_GRAFICO + cos(radians(var.Inclinac)) * punto.lim_hi/conf.ESCALA_GRAFICO,
                tooltip=(nombre, punto.lim_bi, punto.lim_hi)))
            datos_grafico_GPA_nom.data_points.append(ft.LineChartDataPoint(
                cos(radians(var.Inclinac)) * punto.nom_bi/conf.ESCALA_GRAFICO + sin(radians(var.Inclinac)) * punto.nom_hi/conf.ESCALA_GRAFICO,
                - sin(radians(var.Inclinac)) * punto.nom_bi/conf.ESCALA_GRAFICO + cos(radians(var.Inclinac)) * punto.nom_hi/conf.ESCALA_GRAFICO,
                tooltip=(nombre, punto.nom_bi, punto.nom_hi)))
        datos_grafico_GPA.visible = cb_graf_GPA.value
        datos_grafico_GPA_lim.visible = cb_graf_GPA_lim.value
        datos_grafico_GPA_nom.visible = cb_graf_GPA_nom.value

        for nombre,punto in galiboPB.items():
            datos_grafico_GPB.data_points.append(ft.LineChartDataPoint(
                cos(radians(var.Inclinac)) * punto.X/conf.ESCALA_GRAFICO + sin(radians(var.Inclinac)) * punto.Y/conf.ESCALA_GRAFICO,
                - sin(radians(var.Inclinac)) * punto.X/conf.ESCALA_GRAFICO + cos(radians(var.Inclinac)) * punto.Y/conf.ESCALA_GRAFICO,
                tooltip=(nombre, punto.X, punto.Y)))
        datos_grafico_GPB.visible = cb_graf_GPB.value
        
        page.update()

    datos_grafico_GPA = ft.LineChartData(
        data_points=[],
        stroke_width=3,
        color=ft.colors.CYAN,
        curved=False,
        stroke_cap_round=True,
    )
    datos_grafico_GPB = ft.LineChartData(
        data_points=[],
        stroke_width=3,
        color=ft.colors.CYAN_100,
        curved=False,
        stroke_cap_round=True,
    )
    datos_grafico_GPA_lim = ft.LineChartData(
        data_points=[],
        stroke_width=3,
        color=ft.colors.YELLOW,
        curved=False,
        stroke_cap_round=True,
    )
    datos_grafico_GPA_nom = ft.LineChartData(
        data_points=[],
        stroke_width=3,
        color=ft.colors.RED,
        curved=False,
        stroke_cap_round=True,
    )
    datos_grafico = [
        datos_grafico_GPA,
        datos_grafico_GPB,
        datos_grafico_GPA_lim,
        datos_grafico_GPA_nom,
    ]

    #COMPONENTES INDIVIDUALES
    dd_GPA = ft.Dropdown(
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

    dd_GPB = ft.Dropdown(
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

    t_R = ft.Text(var.R)
    t_LN = ft.Text(var.LN)
    t_DL = ft.Text(var.DL)
    t_LND = ft.Text(var.LND)

    t_D = ft.Text(var.D)    
    t_D0 = ft.Text(var.D0)
    t_heq = ft.Text(var.heq)
    t_I = ft.Text(var.I)
    t_I0 = ft.Text(var.I0)
    t_L = ft.Text(var.L)
    t_hco = ft.Text(var.hco)

    t_tipo_via = ft.Text(var.D)
    t_tvia = ft.Text(var.TVIA)
    t_td = ft.Text(var.TD)
    t_vmax = ft.Text(var.vmax)
    t_asusp = ft.Text(var.asusp)
    t_acarga = ft.Text(var.acarga)
    t_eta0 = ft.Text(var.eta0)
    t_estado_via = ft.Text(var.estado_via)
    t_aosc_i_s0_04b = ft.Text(var.aosc_i_s0_04b)
    t_aosc_i_s0_03b = ft.Text(var.aosc_i_s0_03b)
    t_aosc_a_s0_04b = ft.Text(var.aosc_a_s0_04b)
    t_aosc_a_s0_04b = ft.Text(var.aosc_a_s0_03b)

    tf_R = ft.TextField(label="Radio de curvatura en planta (m)",value = 100, on_submit=cambiar)
    cb_R = ft.Checkbox(value = False, on_change=cambiar)
    tf_RV = ft.TextField(label="Radio del acuerdo vertical (m)", value = 100, on_submit=cambiar)
    cb_RV = ft.Checkbox(value = False, on_change=cambiar)
    tf_DL = ft.TextField(label="Sobreancho máximo (m)",value=0.03,read_only=True, on_submit=cambiar)
    tf_D = ft.TextField(label="Peralte de la vía (m)", value = 0, on_submit=cambiar)
    tf_I = ft.TextField(label="Insuficiencia de peralte (m)", value = 0, on_submit=cambiar)
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

    t_3221 = ft.ResponsiveRow([
        ft.Column([
            ft.Text("Radio de curvatura"),
            ft.Text("Ancho de vía nominal"),
            ft.Text("Sobreancho máximo"),
            ft.Text("Ancho de vía"),
        ],
        col=6,),
        ft.Column([
            ft.Text("R="),
            ft.Text("lN="),
            ft.Text("Dl="),
            ft.Text("I=Dl+lN="),
        ],
        col=2,),
        ft.Column([
            t_R,
            t_LN,
            t_DL,
            t_LND,
        ],
        col=2,),
        ft.Column([
            ft.Text("m"),
            ft.Text("m"),
            ft.Text("m"),
            ft.Text("m"),
        ],
        col=2,),
        ],
        columns=12)
    t_3222 = ft.ResponsiveRow([
        ft.Column([
            ft.Text("Peralte de la vía"),
            ft.Text("Peralte por convenio de la vía"),
            ft.Text("Peralte de equilibrio"),
            ft.Text("Insuficiencia de peralte"),
            ft.Text("Insuficiencia de peralte por convenio"),
            ft.Text("Distancia entre círculos de rodadura"),
            ft.Text("Altura  del  centro  de  balanceo  del  vehículo, por convenio"),
            ],
            col=6,),
        ft.Column([
            ft.Text("D="),
            ft.Text("D0="),
            ft.Text("heq="),
            ft.Text("I="),
            ft.Text("I0="),
            ft.Text("L="),
            ft.Text("hco="),
            ],
            col=2,),
        ft.Column([
            t_D,
            t_D0 ,
            t_heq,
            t_I,
            t_I0,
            t_L,
            t_hco,
            ],
            col=2,),
        ft.Column([
            ft.Text("m"),
            ft.Text("m"),
            ft.Text("m"),
            ft.Text("m"),
            ft.Text("m"),
            ft.Text("m"),
            ft.Text("m"),
            ],
            col=2,),
            ],
            columns=12)
    t_3223 = ft.ResponsiveRow([
        ft.Column([
            ft.Text("Tipo de vía"),
            ft.Text("Desplazaiento lateral de la vía"),
            ft.Text("Diferencia entre peralte real y teórico"),
            ft.Text("Velocidad máxima de la vía"),
            ft.Text("Tolerancias en el reglaje de la suspensión"),
            ft.Text("Reparto desigual de cargas"),
            ft.Text("Giro total"),
            ft.Text("Estado de la vía"),
            ft.Text("Giro por oscilaciones aleatorias por irregularidades de la vía"),
            ft.Text(""),
            ft.Text(""),
            ft.Text(""),
            ],
            col=6,),
        ft.Column([
            ft.Text(""),
            ft.Text("Tvia="),
            ft.Text("TD="),
            ft.Text("Vmax="),
            ft.Text("asusp="),
            ft.Text("acarga="),
            ft.Text("n0="),
            ft.Text(""),
            ft.Text("aosc,i,s0=0,4="),
            ft.Text("aosc,i,s0=0,3="),
            ft.Text("aosc,a,s0=0,4="),
            ft.Text("aosc,a,s0=0,3="),
            ],
            col=2,),
        ft.Column([
            t_tipo_via,
            t_tvia,
            t_td,
            t_vmax,
            t_asusp,
            t_acarga,
            t_eta0,
            t_estado_via,
            t_aosc_i_s0_04b,
            t_aosc_i_s0_03b,
            t_aosc_a_s0_04b,
            t_aosc_a_s0_04b,
            ],
            col=2,),
        ft.Column([
            ft.Text(""),
            ft.Text("m"),
            ft.Text("m"),
            ft.Text("km/h"),
            ft.Text("º"),
            ft.Text("º"),
            ft.Text("º"),
            ft.Text(""),
            ft.Text("º"),
            ft.Text("º"),
            ft.Text("º"),
            ft.Text("º"),
            ],
            col=2,),
            ],
            columns=12)

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
                ft.Column(col=8,
                    controls = [
                        ft.Text("DATOS", size = Tamanyos.MEDIANO.value),
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

                ]),
        ]),
            ft.Tabs(
                selected_index=3,
                animation_duration=50,
                tabs=[
                    ft.Tab(
                        text = "3.2.2.1.- Salientes",
                        content = t_3221,
                    ),
                    ft.Tab(
                        text = "3.2.2.2.- Desplazamientos cuasiestáticos laterales",
                        content = t_3222,
                    ),
                    ft.Tab(
                        text = "3.2.2.3.- Desplazamientos aleatorios laterales",
                        content = t_3223,
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
                expand = 1
                ),
        ])
    )

ft.app(galibos)