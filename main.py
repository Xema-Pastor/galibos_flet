import flet as ft
from datos_galibos import datos_GPA, datos_GPB
from datos_variables import Variables as var
from estilos.estilos import Tamanyos, EGPA, EGPB, ETV, EEV
from componentes.tablas_datos import *
import calculos.calculos as calc

def galibos(page: ft.Page):

    #FUNCIÓN
    def cambiar(e):

        #CÁLCULO DE LAS VARIABLES GENERALES DEL PROGRAMA
        #Los valores que no se definen aquí están definidos en la clase variables. No dependen de nada, son constantes
        var.GPA = dd_GPA.value
        var.GPB = dd_GPB.value
        galiboPA = datos_GPA[var.GPA]
        galiboPB = datos_GPB[var.GPB]
        var.maxY = 0
        for nombre,punto in galiboPA.items():                                   #intentar hacer esto con la función max y una lambda
            if punto.Y > var.maxY:
                var.maxY = punto.Y
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
        #CALCULAR hb_max, CELDA I9
        es_recta = cb_R.value
        es_recta_V = cb_RV.value
        var.R = 99999999999 if es_recta else int(tf_R.value)
        var.Rv = 99999999999 if es_recta_V else int(tf_RV.value)
        print(type(var.R))
        tf_R.disabled = es_recta
        tf_RV.disabled = es_recta_V
        #PROGRAMAR LO DE QUE GIRE A DERECHA O A IZQUIERDA CON var.Inclinac
        var.DL = tf_DL.value
        var.LND = var.LN + var.DL
        var.D = float(tf_D.value)
        match var.GPA:
            case EGPA.GHE16.value | EGPA.GEA16.value | EGPA.GEB16.value | EGPA.GEC16.value | EGPA.GA.value | EGPA.GB.value | EGPA.GC.value: var.D0 = 0.05
            case EGPA.GEE10.value |EGPA.GED10.value | EGPA.PERSONALIZADO.value: var.D0 = 0.07
        var.vmax = tf_vmax.value
        var.heq = (float(var.vmax) / 3.6)**2 * var.LN / (float(var.R) * 9.81)
        var.I = var.heq - var.D
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
        var.Rv = tf_RV.value
        var.DhRV = 50/float(var.Rv)
        var.aosc_i_s0_04h = var.aosc_a_s0_04b
        var.aosc_a_s0_04h = var.aosc_i_s0_04b
        var.aosc_i_s0_03h = var.aosc_a_s0_03b
        var.aosc_a_s0_03h = var.aosc_i_s0_03b


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

        #LIMPIEZA DE LAS TABLAS DE DATOS Y GRÁFICOS DE FLET
        def limpiar_tabla(elemento: ft.Column, texto: str, unidades: str):
            elemento.controls.clear()
            elemento.controls.append(ft.Text(texto,size=10))
            elemento.controls.append(ft.Text(unidades,size=10))
        limpiar_tabla(tabla_00_Punto, "Punto", "()")
        limpiar_tabla(tabla_01_X, "X", "(mm)")
        limpiar_tabla(tabla_02_Y, "Y", "(mm)")
        limpiar_tabla(tabla_03_esPT, "esPT", "(S/N)")
        limpiar_tabla(tabla_04_k, "k", "()")
        limpiar_tabla(tabla_05_s0, "s0", "()")
        limpiar_tabla(tabla_06_Sa, "Sa", "(mm)")
        limpiar_tabla(tabla_07_Si, "Si", "(mm)")
        limpiar_tabla(tabla_08_qsDai, "qsD,ai", "(mm)")
        limpiar_tabla(tabla_09_qsIai, "qsI,ai", "(mm)")
        limpiar_tabla(tabla_10_Tvia_ai, "Tvia,ai", "(mm)")
        limpiar_tabla(tabla_11_Dbgai, "Dbgai", "(mm)")
        limpiar_tabla(tabla_12_Dbcai, "Dbcai", "(mm)")
        limpiar_tabla(tabla_13_Dbsuspai, "Dbsuspai", "(mm)")
        limpiar_tabla(tabla_14_Dbcargaai, "Dbcargai", "(mm)")
        limpiar_tabla(tabla_15_Dbetaai, "Dbetaai", "(mm)")
        limpiar_tabla(tabla_16_aosca, "aosca", "(º)")
        limpiar_tabla(tabla_17_aosci, "aosci", "(º)")
        limpiar_tabla(tabla_18_Dbosca, "Dbosca", "(mm)")
        limpiar_tabla(tabla_19_Dbosci, "Dbosci", "(mm)")
        limpiar_tabla(tabla_20_M3h, "M3h", "(mm)")
        limpiar_tabla(tabla_21_DhRv, "DhRv", "(mm)")
        limpiar_tabla(tabla_22_DhPTDai, "DhPTDai", "(mm)")
        limpiar_tabla(tabla_23_DhPTIai, "DhPTIai", "(mm)")
        limpiar_tabla(tabla_24_TN, "TN", "(mm)")
        limpiar_tabla(tabla_25_Dhga, "Dhga", "(mm)")
        limpiar_tabla(tabla_26_Dhgi, "Dhgi", "(mm)")
        limpiar_tabla(tabla_27_Dhc, "Dhc", "(mm)")
        limpiar_tabla(tabla_28_Dhgca, "Dhgca", "(mm)")
        limpiar_tabla(tabla_29_Dhgci, "Dhgci", "(mm)")
        limpiar_tabla(tabla_30_Dhsuspai, "Dhsuspai", "(mm)")
        limpiar_tabla(tabla_31_Dhcargai, "Dhcargai", "(mm)")
        limpiar_tabla(tabla_32_Dhetaai, "Dhetaai", "(mm)")
        limpiar_tabla(tabla_33_Dhosca, "Dhosca", "(mm)")
        limpiar_tabla(tabla_34_Dhosci, "Dhosci", "(mm)")
        limpiar_tabla(tabla_35_M3h, "M3h", "(mm)")
        limpiar_tabla(tabla_36_lim_Sja1, "Sja1", "(mm)")
        limpiar_tabla(tabla_37_lim_Sji1, "Sji1", "(mm)")
        limpiar_tabla(tabla_38_lim_Sja2, "Sja2", "(mm)")
        limpiar_tabla(tabla_39_lim_Sji2, "Sji2", "mm")
        limpiar_tabla(tabla_40_lim_Sja1_ast, "Sja1*", "(mm)")
        limpiar_tabla(tabla_41_lim_Sji1_ast, "Sji1*", "(mm)")
        limpiar_tabla(tabla_42_lim_Sja2_ast, "Sja2*", "(mm)")
        limpiar_tabla(tabla_43_lim_Sji2_ast, "Sji2*", "(mm)")
        limpiar_tabla(tabla_44_lim_SVa1, "SVa1", "(mm)")
        limpiar_tabla(tabla_45_lim_SVi1, "SVi1", "(mm)")
        limpiar_tabla(tabla_46_lim_SVa2, "SVa2", "(mm)")
        limpiar_tabla(tabla_47_lim_SVi2, "SVi2", "(mm)")
        limpiar_tabla(tabla_48_lim_SVa1_ast, "SVa1*", "(mm)")
        limpiar_tabla(tabla_49_lim_SVa2_ast, "SVa2*", "(mm)")
        limpiar_tabla(tabla_50_lim_SVi2_ast, "SVi2*", "(mm)")
        limpiar_tabla(tabla_51_lim_SVi2_ast, "SVi2*", "(mm)")
        #limpiar_tabla(tabla_44, "", "()")

        datos_grafico_GPA.data_points.clear()
        datos_grafico_GPB.data_points.clear()

        #ACTUALIZACIÓN DE LAS TABLAS DE DATOS Y GRÁFICOS DE FLET
        for nombre,punto in galiboPA.items():
            punto.esPT = calc.calcular_esPT(punto.Y, var.maxY)
            punto.k = calc.calcular_k(var.GPA, punto.Y/1000, var.hquiebroaux, var.htopeaux, var.difaux)
            punto.s0 = calc.calcular_s0(var.GPA, punto.Y/1000, var.hquiebroaux, var.htopeaux, var.difaux, var.hotra)
            punto.Sa = calc.calcular_Sa(var.GPA, var.R, var.LN, var.LND, var.hquiebroaux, punto.Y/1000, punto.k)
            punto.Si = calc.calcular_Si(var.GPA, var.R, var.LN, var.LND, var.hquiebroaux, punto.Y/1000, punto.k)
            punto.qsD_ai = calc.calcular_qsD_ai(punto.Y/1000, punto.s0, var.D, var.D0, var.L, var.hco)
            punto.qsI_ai = calc.calcular_qsI_ai(punto.Y/1000, punto.s0, var.I, var.I0, var.L, var.hco)
            punto.Tvia_ai = var.TVIA * 1000
            punto.Dbg_ai = calc.calcular_Dbg_ai(punto.Y/1000, var.L, var.TD)
            punto.Dbc_ai = calc.calcular_Dbc_ai(punto.Y/1000, var.L, var.TD, var.hco, punto.s0)
            punto.Dbsusp_ai = calc.calcular_Dbsusp_ai(var.asusp, punto.Y, var.hco)
            punto.Dbcarg_ai = calc.calcular_Dbcarg_ai(var.acarga, punto.Y, var.hco)
            punto.Dbeta0_ai = calc.calcular_Dbeta0_ai(var.eta0, punto.Y, var.hco)
            punto.aosc_a = calc.calcular_aosc(punto.s0, var.aosc_a_s0_03b, var.aosc_a_s0_04b)
            punto.aosc_i = calc.calcular_aosc(punto.s0, var.aosc_i_s0_03b, var.aosc_i_s0_04b)
            punto.Dbosc_a = calc.calcular_Dbosc(punto.aosc_a, punto.Y/1000, var.hco)
            punto.Dbosc_i = calc.calcular_Dbosc(punto.aosc_i, punto.Y/1000, var.hco)
            punto.M3b = var.M3h * 1000
            punto.DhRv = var.DhRV * 1000
            punto.DhPT_D_ai = calc.calcular_DhPT_D_ai(punto.X/1000, punto.s0, var.D, var.D0, var.L)
            punto.DhPT_I_ai = calc.calcular_DhPT_I_ai(punto.X/1000, punto.s0, var.I, var.I0, var.L)
            punto.TN = var.TN * 1000
            punto.Dhg_a = calc.calcular_Dhg_a(punto.X/1000, var.L, var.TD)
            punto.Dhg_i = calc.calcular_Dhg_i(punto.X/1000, var.L, var.TD)
            punto.Dhc = calc.calcular_Dhc(punto.X/1000, punto.s0, var.L, var.TD)
            punto.Dhgca = punto.Dhg_a + punto.Dhc
            punto.Dhgci = punto.Dhg_i + punto.Dhc
            punto.Dhsusp_ai = calc.calcular_Dhsusp_ai(punto.X / 1000, var.asusp)
            punto.Dhcarg_ai = calc.calcular_Dhcarg_ai(punto.X / 1000, var.acarga)
            punto.Dheta0_ai = calc.calcular_Dhcarg_ai(punto.X / 1000, var.eta0)
            punto.Dhosc_a = calc.calcular_Dhosc(punto.X, punto.aosc_i)                           #Sí, los ángulos están cambiados
            punto.Dhosc_i = calc.calcular_Dhosc(punto.X, punto.aosc_a)                           #Sí, los ángulos están cambiados
            punto.M3h = var.M3h
            punto.lim_Sja1 = calc.calcular_lim_Sj1(punto.Y/1000, var.hco, var.K, var.Kale_h_0_50, punto.Tvia_ai, punto.Dbg_ai, punto.Dbc_ai, punto.Dbsusp_ai, punto.Dbcarg_ai, punto.Dbosc_a)
            punto.lim_Sji1 = calc.calcular_lim_Sj1(punto.Y/1000, var.hco, var.K, var.Kale_h_0_50, punto.Tvia_ai, punto.Dbg_ai, punto.Dbc_ai, punto.Dbsusp_ai, punto.Dbcarg_ai, punto.Dbosc_i)
            punto.lim_Sja2 = calc.calcular_lim_Sj2(punto.Y/1000, var.hco, var.K, var.Kale_h_0_50, punto.Tvia_ai, punto.Dbg_ai)
            punto.lim_Sji2 = punto.lim_Sja2
            punto.lim_rad_Sja1_ast = punto.Tvia_ai**2 - (punto.Dbg_ai + punto.Dbc_ai)**2 - (punto.Dbsusp_ai**2 + punto.Dbcarg_ai**2 + punto.Dbosc_a**2)
            punto.lim_rad_Sji1_ast = punto.Tvia_ai**2 - (punto.Dbg_ai + punto.Dbc_ai)**2 - (punto.Dbsusp_ai**2 + punto.Dbcarg_ai**2 + punto.Dbosc_i**2)
            punto.lim_rad_Sjai2_ast = punto.Tvia_ai**2 - punto.Dbg_ai**2
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
            #punto.lim_bobst_max_i
            #punto.lim_hobst_conc_i
            #punto.lim_bobst_max_a
            #punto.lim_hobst_conc_a
            #punto.lim_bconc_max_i
            #punto.lim_hmax_conc_i
            #punto.lim_bconc_max_a
            #punto.lim_hmax_conc_a
            #punto.lim_bobst_max_i
            #punto.lim_hobst_conc_
            #punto.lim_bobst_max_a
            #punto.lim_hobst_conc_
            #punto.lim_bconc_max_i
            #punto.lim_hmax_conc_i
            #punto.lim_bconc_max_a
            #punto.lim_hmax_conc_a
            #punto.lim_ba
            #punto.lim_ha
            #punto.lim_bi
            #punto.lim_hi
            #punto.nom_Sja1
            #punto.nom_Sji1
            #punto.nom_Sja2
            #punto.nom_Sji2
            #punto.nom_Sja1_ast
            #punto.nom_Sji1_ast
            #punto.nom_Sja2_ast
            #punto.nom_Sji2_ast
            #punto.nom_SVa1
            #punto.nom_SVi1
            #punto.nom_SVa2
            #punto.nom_SVi2
            #punto.nom_SVa1_ast
            #punto.nom_SVi1_ast
            #punto.nom_SVa2_ast
            #punto.nom_SVi2_ast
            #punto.nom_bobst_max_i
            #punto.nom_hobst_conc_i
            #punto.nom_bobst_max_a
            #punto.nom_hobst_conc_a
            #punto.nom_bconc_max_i
            #punto.nom_hmax_conc_i
            #punto.nom_bconc_max_a
            #punto.nom_hmax_conc_a
            #punto.nom_bobst_max_i
            #punto.nom_hobst_conc_
            #punto.nom_bobst_max_a
            #punto.nom_hobst_conc_
            #punto.nom_bconc_max_i
            #punto.nom_hmax_conc_i
            #punto.nom_bconc_max_a
            #punto.nom_hmax_conc_a
            #punto.nom_ba
            #punto.nom_ha
            #punto.nom_bi
            #punto.nom_hi
            #punto.

            tabla_00_Punto.controls.append(ft.Text(nombre,size=10))
            tabla_01_X.controls.append(ft.Text(punto.X,size=10))
            tabla_02_Y.controls.append(ft.Text(punto.Y,size=10))
            tabla_03_esPT.controls.append(ft.Text(punto.esPT,size=10))
            tabla_04_k.controls.append(ft.Text(punto.k,size=10))
            tabla_05_s0.controls.append(ft.Text(punto.s0,size=10))
            tabla_06_Sa.controls.append(ft.Text(punto.Sa,size=10))
            tabla_07_Si.controls.append(ft.Text(punto.Si,size=10))
            tabla_08_qsDai.controls.append(ft.Text(punto.qsD_ai,size=10))
            tabla_09_qsIai.controls.append(ft.Text(punto.qsI_ai,size=10))
            tabla_10_Tvia_ai.controls.append(ft.Text(punto.Tvia_ai,size=10))
            tabla_11_Dbgai.controls.append(ft.Text(punto.Dbg_ai,size=10))
            tabla_12_Dbcai.controls.append(ft.Text(punto.Dbc_ai,size=10))
            tabla_13_Dbsuspai.controls.append(ft.Text(punto.Dbsusp_ai,size=10))
            tabla_14_Dbcargaai.controls.append(ft.Text(punto.Dbcarg_ai,size=10))
            tabla_15_Dbetaai.controls.append(ft.Text(punto.Dbeta0_ai,size=10))
            tabla_16_aosca.controls.append(ft.Text(punto.aosc_a,size=10))
            tabla_17_aosci.controls.append(ft.Text(punto.aosc_i,size=10))
            tabla_18_Dbosca.controls.append(ft.Text(punto.Dbosc_a,size=10))
            tabla_19_Dbosci.controls.append(ft.Text(punto.Dbosc_i,size=10))
            tabla_20_M3h.controls.append(ft.Text(punto.M3b,size=10))
            tabla_21_DhRv.controls.append(ft.Text(punto.DhRv,size=10))
            tabla_22_DhPTDai.controls.append(ft.Text(punto.DhPT_D_ai,size=10))
            tabla_23_DhPTIai.controls.append(ft.Text(punto.DhPT_I_ai,size=10))
            tabla_24_TN.controls.append(ft.Text(punto.TN,size=10))
            tabla_25_Dhga.controls.append(ft.Text(punto.Dhg_a,size=10))
            tabla_26_Dhgi.controls.append(ft.Text(punto.Dhg_i,size=10))
            tabla_27_Dhc.controls.append(ft.Text(punto.Dhc,size=10))
            tabla_28_Dhgca.controls.append(ft.Text(punto.Dhg_a,size=10))
            tabla_29_Dhgci.controls.append(ft.Text(punto.Dhg_i,size=10))
            tabla_30_Dhsuspai.controls.append(ft.Text(punto.Dhc,size=10))
            tabla_31_Dhcargai.controls.append(ft.Text(punto.Dhsusp_ai,size=10))
            tabla_32_Dhetaai.controls.append(ft.Text(punto.Dhcarg_ai,size=10))
            tabla_33_Dhosca.controls.append(ft.Text(punto.Dhosc_a,size=10))
            tabla_34_Dhosci.controls.append(ft.Text(punto.Dhosc_i,size=10))
            tabla_35_M3h.controls.append(ft.Text(punto.M3h,size=10))
            tabla_36_lim_Sja1.controls.append(ft.Text(punto.lim_Sja1,size=10))
            tabla_37_lim_Sji1.controls.append(ft.Text(punto.lim_Sji1,size=10))
            tabla_38_lim_Sja2.controls.append(ft.Text(punto.lim_Sja2,size=10))
            tabla_39_lim_Sji2.controls.append(ft.Text(punto.lim_Sji2,size=10))
            tabla_40_lim_Sja1_ast.controls.append(ft.Text(punto.lim_Sja1_ast,size=10))
            tabla_41_lim_Sji1_ast.controls.append(ft.Text(punto.lim_Sji1_ast,size=10))
            tabla_42_lim_Sja2_ast.controls.append(ft.Text(punto.lim_Sja2_ast,size=10))
            tabla_43_lim_Sji2_ast.controls.append(ft.Text(punto.lim_Sji2_ast,size=10))
            tabla_44_lim_SVa1.controls.append(ft.Text(punto.lim_SVa1,size=10))
            tabla_45_lim_SVi1.controls.append(ft.Text(punto.lim_SVi1,size=10))
            tabla_46_lim_SVa2.controls.append(ft.Text(punto.lim_SVa2,size=10))
            tabla_47_lim_SVi2.controls.append(ft.Text(punto.lim_SVi2,size=10))
            tabla_48_lim_SVa1_ast.controls.append(ft.Text(punto.lim_SVa1_ast,size=10))
            tabla_49_lim_SVa2_ast.controls.append(ft.Text(punto.lim_SVa2_ast,size=10))
            tabla_50_lim_SVi2_ast.controls.append(ft.Text(punto.lim_SVi2_ast,size=10))
            tabla_51_lim_SVi2_ast.controls.append(ft.Text(punto.lim_SVi2_ast,size=10))


            datos_grafico_GPA.data_points.append(ft.LineChartDataPoint(punto.X, punto.Y))

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
        color=ft.colors.RED,
        curved=False,
        stroke_cap_round=True,
    )
    datos_grafico = [
        datos_grafico_GPA,
        datos_grafico_GPB,
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

    tf_R = ft.TextField(label="Radio de curvatura en planta (m)",value = 100, on_change=cambiar)
    cb_R = ft.Checkbox(value = False, on_change=cambiar)
    tf_RV = ft.TextField(label="Radio del acuerdo vertical (m)", value = 100, on_change=cambiar)
    cb_RV = ft.Checkbox(value = False, on_change=cambiar)
    tf_DL = ft.TextField(label="Sobreancho máximo (m)",value=0.03,read_only=True, on_change=cambiar)
    tf_D = ft.TextField(label="Peralte de la vía (m)", value = 0, on_change=cambiar)
    tf_tol_sus = ft.TextField(label="Tolerancias en el reglaje de la suspensión (º)", value = 0.23, on_change=cambiar)
    tf_tol_carga = ft.TextField(label="Reparto desigual de cargas (º)", value = 0.77, on_change=cambiar)
    tf_vmax = ft.TextField(label="Velocidad máxima de la vía (km/h)", value=100, on_change=cambiar)

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
                        ),
                        bottom_axis=ft.ChartAxis(
                            labels=[],
                            labels_size=20,
                        ),
                        tooltip_bgcolor=ft.colors.with_opacity(0.8, ft.colors.BLUE_GREY),
                        min_y=-2000,
                        max_y=6000,
                        min_x=-2000,
                        max_x=2000,
                        animate = 0,
                        expand=True,
                        height=1000,
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
                    ]),
                    ft.Row([
                        tf_tol_sus,
                        tf_tol_carga,
                    ]),
                    tf_vmax,
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
                                text = "Tabla de resultados",
                                content = tabla,
                            ), 
                        ],
                        expand = 1
                        ),
            ]),
        ])
    )

ft.app(galibos)