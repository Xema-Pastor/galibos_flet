import flet as ft
import configuracion as conf
from datos_galibos import datos_GPA, datos_GPB, datos_Pantografo
from datos_variables import via1, via2
from estilos.estilos import Tamanyos, EGPA, EGPB, ETV, EEV, TIPO_PANT, TIPO_LINEA, TENSION_CAT, TIPO_CAT
from componentes.comp_tablas import ftt_1, ftt_2, tabla_var_1, tabla_des_1, tabla_lim_1, tabla_nom_1, tabla_pant_1, fttabla_1, tabla_var_2, tabla_des_2, tabla_lim_2, tabla_nom_2, tabla_pant_2, fttabla_2, fttablaPant_1, fttablaPant_2
from componentes.comp_graficos import *
from componentes.mis_componentes import *
import calculos.calculos as calc
from math import sin, cos, atan, degrees, radians

def galibos(page: ft.Page):

    page.title = "Determinación de gálibos de material rodante de acuerdo a la Orden FOM/1630/2015 "
    page.window.height = 600
    page.window.width = 1800

    def cambiar_via(galibo, via, ft_elem):
        
        #CÁLCULO DE LAS VARIABLES GENERALES DEL PROGRAMA
        via.maxY = 0
        for nombre,punto in galibo.items():                                   #intentar hacer esto con la función max y una lambda
            if punto.Y > via.maxY:
                via.maxY = punto.Y
        match via.GPA:
            case EGPA.GHE16.value | EGPA.GEA16.value | EGPA.GEB16.value | EGPA.GEC16.value | EGPA.GA.value | EGPA.GB.value | EGPA.GC.value:
                via.hb_max = ( galibo["P3"].Y + galibo["P4"].Y ) / 2
            case EGPA.GEE10.value |EGPA.GED10.value | EGPA.PERSONALIZADO.value:
                via.hb_max = ( galibo["P1"].Y + galibo["P2"].Y ) / 2
        match via.GPA:
            case EGPA.GEA16.value | EGPA.GEB16.value: via.hquiebroaux = 3.32
            case EGPA.GA.value | EGPA.GB.value: via.hquiebroaux = 3.35
            case other: via.hquiebroaux = 0
        match via.GPA:
            case EGPA.GEA16.value: via.htopeaux = 3.7
            case EGPA.GEB16.value | EGPA.GB.value: via.htopeaux = 4.11
            case EGPA.GA.value: via.htopeaux = 3.88
            case other: via.htopeaux = 0
        match via.GPA:
            case EGPA.GEA16.value: via.difaux = 0.38
            case EGPA.GEB16.value: via.difaux = 0.79
            case EGPA.GA.value: via.difaux = 0.63
            case EGPA.GB.value: via.difaux = 0.86
            case other: via.difaux = 0
        match via.GPA:
            case EGPA.GEA16.value: via.otra = 4.84
            case EGPA.GEB16.value: via.otra = 6.48
            case EGPA.GA.value: via.otra = 5.77
            case EGPA.GB.value: via.otra = 6.69
            case other: via.otra = 0
        match via.GPA:
            case EGPA.GHE16.value | EGPA.GEA16.value | EGPA.GEB16.value | EGPA.GEC16.value: via.LN = 1.668
            case EGPA.GA.value | EGPA.GB.value | EGPA.GC.value: via.LN = 1.435
            case EGPA.GEE10.value |EGPA.GED10.value | EGPA.PERSONALIZADO.value: via.LN = 1

        #COMPROBACIÓN DE LOS CHECKBOXES: RADIOS EN PLANTA Y ALZADO, E INCLINACIÓN DEL GRÁFICO
        es_recta = ft_elem.cb_R.value
        es_recta_V = ft_elem.cb_RV.value
        es_girado = ft_elem.cb_graf_esGirado.value
        via.R = 999999 if es_recta else int(ft_elem.tf_R.value)
        via.Rv = 999999 if es_recta_V else int(ft_elem.tf_RV.value)
        ft_elem.tf_R.disabled = es_recta
        ft_elem.tf_RV.disabled = es_recta_V
        ft_elem.cb_graf_inclinacion.disabled = not es_girado
        via.Inclinac = 0.0 if not es_girado else degrees(atan(via.D / via.LN))
        lado_inclinacion = ft_elem.cb_graf_inclinacion.value
        if lado_inclinacion == "A derechas":
            via.Inclinac = abs(via.Inclinac)
        elif lado_inclinacion == "A izquierdas":
            via.Inclinac = -abs(via.Inclinac)

        via.DL = ft_elem.tf_DL.value
        via.LND = via.LN + via.DL
        via.D = float(ft_elem.tf_D.value)
        match via.GPA:
            case EGPA.GHE16.value | EGPA.GEA16.value | EGPA.GEB16.value | EGPA.GEC16.value | EGPA.GA.value | EGPA.GB.value | EGPA.GC.value: via.D0 = 0.05
            case EGPA.GEE10.value |EGPA.GED10.value | EGPA.PERSONALIZADO.value: via.D0 = 0.07
        via.vmax = ft_elem.tf_vmax.value
        via.heq = round((float(via.vmax) / 3.6)**2 * via.LN / (float(via.R) * 9.81), 4)
        #via1.I = via1.heq - via1.D
        via.I = float(ft_elem.tf_I.value)
        match via.GPA:
            case EGPA.GHE16.value | EGPA.GEA16.value | EGPA.GEB16.value | EGPA.GEC16.value | EGPA.GA.value | EGPA.GB.value | EGPA.GC.value: via.I0 = 0.05
            case EGPA.GEE10.value |EGPA.GED10.value | EGPA.PERSONALIZADO.value: via.I0 = 0.07
        match via.GPA:
            case EGPA.GHE16.value | EGPA.GEA16.value | EGPA.GEB16.value | EGPA.GEC16.value: via.L = 1.733
            case EGPA.GA.value | EGPA.GB.value | EGPA.GC.value: via.L = 1.5
            case EGPA.GEE10.value |EGPA.GED10.value | EGPA.PERSONALIZADO.value: via.L = 1.055
        via.tipo_via = ft_elem.dd_TV.value
        match via.tipo_via:
            case ETV.VIA_PLACA.value:
                via.TVIA = 0.005
                via.TD = 0.015
            case ETV.BALASTO.value:
                via.TVIA = 0.025
                via.TD = 0.02 if int(via.vmax) <=80 else 0.015
        via.asusp = ft_elem.tf_tol_sus.value
        via.acarga = ft_elem.tf_tol_carga.value
        via.eta0 = float(via.asusp) + float(via.acarga)
        via.estado_via = ft_elem.dd_EV.value
        if via.GPA in [EGPA.GEE10.value, EGPA.GED10.value, EGPA.PERSONALIZADO.value]:
            via.aosc_i_s0_04b = 0.20 if via.tipo_via == ETV.BALASTO.value else 0.1
            via.aosc_a_s0_04b = 1.00 if via.tipo_via == ETV.BALASTO.value else 0.6
            via.aosc_i_s0_03b = 0.20 if via.tipo_via == ETV.BALASTO.value else 0.1
            via.aosc_a_s0_03b = 1.00 if via.tipo_via == ETV.BALASTO.value else 0.6
        elif via.GPA in [EGPA.GHE16.value, EGPA.GEA16.value, EGPA.GEB16.value, EGPA.GEC16.value, EGPA.GA.value, EGPA.GB.value, EGPA.GC.value]:
            if via.tipo_via == ETV.VIA_PLACA.value:
                via.aosc_i_s0_04b = 0.1
                via.aosc_a_s0_04b = 0.6
                via.aosc_i_s0_03b = 0.08
                via.aosc_a_s0_03b = 0.45
            elif via.tipo_via == ETV.BALASTO.value:
                if via.estado_via == EEV.BUEN_ESTADO.value:
                    via.aosc_i_s0_04b = 0.1
                    via.aosc_a_s0_04b = 0.6
                    via.aosc_i_s0_03b = 0.08
                    via.aosc_a_s0_03b = 0.45
                elif via.estado_via == EEV.MAL_ESTADO.value:
                    via.aosc_i_s0_04b = 0.2
                    via.aosc_a_s0_04b = 1.0
                    via.aosc_i_s0_03b = 0.15
                    via.aosc_a_s0_03b = 0.75

        via.DhRV = round(50/float(via.Rv), 2)
        if via.GPA in [EGPA.GHE16.value, EGPA.GEA16.value, EGPA.GEB16.value, EGPA.GEC16.value, EGPA.GA.value, EGPA.GB.value, EGPA.GC.value]:
            if via.tipo_via == ETV.BALASTO.value and via.estado_via == EEV.BUEN_ESTADO.value:
                via.aosc_i_s0_04h = 0.1
            elif via.tipo_via == ETV.BALASTO.value and via.estado_via == EEV.MAL_ESTADO.value:
                via.aosc_i_s0_04h = 0.2
            elif via.tipo_via == ETV.VIA_PLACA.value:
                via.aosc_i_s0_04h = 0.1
        elif via.GPA in [EGPA.GEE10.value, EGPA.GED10.value, EGPA.PERSONALIZADO.value]:
            if via.tipo_via == ETV.BALASTO.value:
                via.aosc_i_s0_04h = 0.2
            elif via.tipo_via == ETV.VIA_PLACA.value:
                via.aosc_i_s0_04h = 0.1
        
        if via.GPA in [EGPA.GHE16.value, EGPA.GEA16.value, EGPA.GEB16.value, EGPA.GEC16.value, EGPA.GA.value, EGPA.GB.value, EGPA.GC.value]:
            if via.tipo_via == ETV.BALASTO.value and via.estado_via == EEV.BUEN_ESTADO.value:
                via.aosc_i_s0_03h = 0.08
            elif via.tipo_via == ETV.BALASTO.value and via.estado_via == EEV.MAL_ESTADO.value:
                via.aosc_i_s0_03h = 0.15
            elif via.tipo_via == ETV.VIA_PLACA.value:
                via.aosc_i_s0_03h = 0.08
        elif via.GPA in [EGPA.GEE10.value, EGPA.GED10.value, EGPA.PERSONALIZADO.value]:
            if via.tipo_via == ETV.BALASTO.value:
                via.aosc_i_s0_03h = 0.2
            elif via.tipo_via == ETV.VIA_PLACA.value:
                via.aosc_i_s0_03h = 0.1

        if via.GPA in [EGPA.GHE16.value, EGPA.GEA16.value, EGPA.GEB16.value, EGPA.GEC16.value, EGPA.GA.value, EGPA.GB.value, EGPA.GC.value]:
            if via.tipo_via == ETV.BALASTO.value and via.estado_via == EEV.BUEN_ESTADO.value:
                via.aosc_a_s0_04h = 0.6
            elif via.tipo_via == ETV.BALASTO.value and via.estado_via == EEV.MAL_ESTADO.value:
                via.aosc_a_s0_04h = 1.0
            elif via.tipo_via == ETV.VIA_PLACA.value:
                via.aosc_a_s0_04h = 0.6
        elif via.GPA in [EGPA.GEE10.value, EGPA.GED10.value, EGPA.PERSONALIZADO.value]:
            if via.tipo_via == ETV.BALASTO.value:
                via.aosc_a_s0_04h = 1.0
            elif via.tipo_via == ETV.VIA_PLACA.value:
                via.aosc_a_s0_04h = 0.6
        
        if via.GPA in [EGPA.GHE16.value, EGPA.GEA16.value, EGPA.GEB16.value, EGPA.GEC16.value, EGPA.GA.value, EGPA.GB.value, EGPA.GC.value]:
            if via.tipo_via == ETV.BALASTO.value and via.estado_via == EEV.BUEN_ESTADO.value:
                via.aosc_a_s0_03h = 0.45
            elif via.tipo_via == ETV.BALASTO.value and via.estado_via == EEV.MAL_ESTADO.value:
                via.aosc_a_s0_03h = 0.75
            elif via.tipo_via == ETV.VIA_PLACA.value:
                via.aosc_a_s0_03h = 0.45
        elif via.GPA in [EGPA.GEE10.value, EGPA.GED10.value, EGPA.PERSONALIZADO.value]:
            if via.tipo_via == ETV.BALASTO.value:
                via.aosc_a_s0_03h = 1.0
            elif via.tipo_via == ETV.VIA_PLACA.value:
                via.aosc_a_s0_03h = 0.6

        #CÁLCULOS RELATIVOS AL PANTÓGRAFO
        # via.tipo_pant = ft_elem.dd_TIPOPAN
        # via.tipo_cat =  ft_elem.dd_TIPOCAT
        # via.tipo_lin =  ft_elem.dd_TIPOLIN
        # via.ten_cat =  ft_elem.dd_TENCAT
        via.hf = float(ft_elem.tf_hpant.value)

        match via.tipo_pant:
            case TIPO_PANT.ANCHO_1600.value:
                via.bp = 1.6
                via.bw = 0.8
                via.epo = 0.17
                via.epu = 0.11
                via.D0p = 0.067
                via.I0p = 0.067
            case TIPO_PANT.ANCHO_1700.value:
                via.bp = 1.7
                via.bw = 0.85
                via.epo = 0.15
                via.epu = 0.082
                via.D0p = 0.07
                via.I0p = 0.07
            case TIPO_PANT.ANCHO_1950.value:
                via.bp = 1.9
                via.bw = 0.975
                via.epo = 0.17
                via.epu = 0.11
                via.D0p = 0.067
                via.I0p = 0.067

        match via.ten_cat:
            case TENSION_CAT.CC_1500.value:
                via.belec_estat = 0.1
                via.belec_dinam = 0.05
            case TENSION_CAT.CC_3000.value:
                via.belec_estat = 0.15
                via.belec_dinam = 0.05
            case TENSION_CAT.CA_25000.value:
                via.belec_estat = 0.27
                via.belec_dinam = 0.15

        match via.tipo_lin:
            case TIPO_LINEA.EXISTENTES.value:
                via.cw = 0.2
            case TIPO_LINEA.NUEVAS.value:
                via.cw = 0.0
        
        match via.tipo_cat:
            case TIPO_CAT.CA160.value:
                via.fsvmax = 0.195
                via.fsvmin = 0.078
            case TIPO_CAT.CA220.value:
                via.fsvmax = 0.148
                via.fsvmin = 0.045
            case TIPO_CAT.CAU220.value:
                via.fsvmax = 0.152
                via.fsvmin = 0.046
            case TIPO_CAT.SICAT.value:
                via.fsvmax = 0.154
                via.fsvmin = 0.04
            case TIPO_CAT.EAC350.value:
                via.fsvmax = 0.162
                via.fsvmin = 0.041
            case TIPO_CAT.RIGIDA.value:
                via.fsvmax = 0.015
                via.fsvmin = 0.015

        via.heffvmax = via.hf + via.fsvmax + via.fwswa
        via.heffvmin = via.hf + via.fsvmin + via.fwswa
        via.heffelecvmax = via.heffvmax + via.belec_dinam
        via.heffelecvmin = via.heffvmin + via.belec_estat
        via.heff = max(via.heffvmax, via.heffvmin)
        via.heffelec = max(via.heffelecvmax, via.heffelecvmin)

    def cambiar_elementos(galiboPA, galiboPant, ftt, fttabla, fttablaPant, via):
        def signo(num):
            return 1 if num >= 0 else -1

        #ACTUALIZACIÓN DE LOS ELEMENTOS DE FLET CON LOS VALORES CALCULADOS ANTERIORMENTE
        ftt.t_R.value = via.R
        ftt.t_RV.value = via.Rv
        ftt.t_LN.value = via.LN
        ftt.t_DL.value = via.DL
        ftt.t_LND.value = via.LND
        ftt.t_DhRV.value = via.DhRV
        
        ftt.t_D.value = via.D
        ftt.t_D0.value = via.D0
        ftt.t_heq.value = via.heq
        ftt.t_I.value = via.I
        ftt.t_I0.value = via.I0
        ftt.t_L.value = via.L
        ftt.t_hco.value = via.hco

        ftt.t_tvia.value = via.TVIA
        ftt.t_td.value = via.TD
        ftt.t_vmax.value = via.vmax
        ftt.t_asusp.value = via.asusp
        ftt.t_acarga.value = via.acarga
        ftt.t_eta0.value = via.eta0
        ftt.t_aosc_i_s0_04b.value = via.aosc_i_s0_04b
        ftt.t_aosc_i_s0_03b.value = via.aosc_i_s0_03b
        ftt.t_aosc_a_s0_04b.value = via.aosc_a_s0_04b
        ftt.t_aosc_a_s0_03b.value = via.aosc_a_s0_03b

        fttabla.actualizar_tabla()

        #ACTUALIZACIÓN DE LAS TABLAS DE DATOS DE FLET
        for nombre,punto in galiboPA.items():
            punto.esPT = calc.calcular_esPT(punto.Y, via.maxY)
            punto.k = calc.calcular_k(via.GPA, punto.Y/1000, via.hquiebroaux, via.htopeaux, via.difaux)
            punto.s0 = calc.calcular_s0(via.GPA, punto.Y/1000, via.hquiebroaux, via.htopeaux, via.difaux, via.hotra)
            punto.Sa = calc.calcular_Sa(via.GPA, via.GPB, via.R, via.LN, via.LND, via.hquiebroaux, punto.Y/1000, punto.k)
            punto.Si = calc.calcular_Si(via.GPA, via.GPB, via.R, via.LN, via.LND, via.hquiebroaux, punto.Y/1000, punto.k)
            punto.qsD_ai = calc.calcular_qsD_ai(punto.Y/1000, punto.s0, via.D, via.D0, via.L, via.hco)
            punto.qsI_ai = calc.calcular_qsI_ai(punto.Y/1000, punto.s0, via.I, via.I0, via.L, via.hco)
            punto.Tvia_ai = via.TVIA * 1000
            punto.Dbg_ai = calc.calcular_Dbg_ai(punto.Y/1000, via.L, via.TD)
            punto.Dbc_ai = calc.calcular_Dbc_ai(punto.Y/1000, via.L, via.TD, via.hco, punto.s0)
            punto.Dbsusp_ai = calc.calcular_Dbsusp_ai(via.asusp, punto.Y, via.hco * 1000)
            punto.Dbcarg_ai = calc.calcular_Dbcarg_ai(via.acarga, punto.Y, via.hco * 1000)
            punto.Dbeta0_ai = calc.calcular_Dbeta0_ai(via.eta0, punto.Y, via.hco * 1000)
            punto.aosc_a = calc.calcular_aosc(punto.s0, via.aosc_a_s0_03b, via.aosc_a_s0_04b)
            punto.aosc_i = calc.calcular_aosc(punto.s0, via.aosc_i_s0_03b, via.aosc_i_s0_04b)
            punto.Dbosc_a = calc.calcular_Dbosc(punto.aosc_a, punto.Y, via.hco * 1000)
            punto.Dbosc_i = calc.calcular_Dbosc(punto.aosc_i, punto.Y, via.hco * 1000)
            punto.M3b = via.M3b * 1000
            punto.DhRv = round(via.DhRV * 1000, 1)
            punto.DhPT_D_ai = calc.calcular_DhPT_D_ai(punto.X, punto.s0, via.D, via.D0, via.L)
            punto.DhPT_I_ai = calc.calcular_DhPT_I_ai(punto.X, punto.s0, via.I, via.I0, via.L)
            punto.TN = via.TN * 1000
            punto.Dhg_a = calc.calcular_Dhg_a(punto.X/1000, via.L, via.TD)
            punto.Dhg_i = calc.calcular_Dhg_i(punto.X/1000, via.L, via.TD)
            punto.Dhc = calc.calcular_Dhc(punto.X/1000, punto.s0, via.L, via.TD)
            punto.Dhgca = round(punto.Dhg_a + punto.Dhc, 1)
            punto.Dhgci = round(punto.Dhg_i + punto.Dhc, 1)
            punto.Dhsusp_ai = calc.calcular_Dhsusp_ai(punto.X, via.asusp)
            punto.Dhcarg_ai = calc.calcular_Dhcarg_ai(punto.X, via.acarga)
            punto.Dheta0_ai = calc.calcular_Dhcarg_ai(punto.X, via.eta0)
            punto.Dhosc_a = calc.calcular_Dhosc(punto.X, punto.aosc_i)                           #Sí, los ángulos están cambiados. Así debe ser.
            punto.Dhosc_i = calc.calcular_Dhosc(punto.X, punto.aosc_a)                           #Sí, los ángulos están cambiados. Así debe ser.
            punto.M3h = via.M3h * 1000

            punto.lim_Sja1 = calc.calcular_lim_Sj1(punto.Y/1000, via.hco, via.K, via.Kale_h_0_50, punto.Tvia_ai, punto.Dbg_ai, punto.Dbc_ai, punto.Dbsusp_ai, punto.Dbcarg_ai, punto.Dbosc_a)
            punto.lim_Sji1 = calc.calcular_lim_Sj1(punto.Y/1000, via.hco, via.K, via.Kale_h_0_50, punto.Tvia_ai, punto.Dbg_ai, punto.Dbc_ai, punto.Dbsusp_ai, punto.Dbcarg_ai, punto.Dbosc_i)
            punto.lim_Sja2 = calc.calcular_lim_Sj2(punto.Y/1000, via.hco, via.K, via.Kale_h_0_50, punto.Tvia_ai, punto.Dbg_ai)
            punto.lim_Sji2 = punto.lim_Sja2
            punto.lim_rad_Sja1_ast = calc.calcular_lim_rad_Sj1(punto.Tvia_ai, punto.Dbg_ai, punto.Dbc_ai, punto.Dbsusp_ai, punto.Dbcarg_ai, punto.Dbosc_a)
            punto.lim_rad_Sji1_ast = calc.calcular_lim_rad_Sj1(punto.Tvia_ai, punto.Dbg_ai, punto.Dbc_ai, punto.Dbsusp_ai, punto.Dbcarg_ai, punto.Dbosc_i)
            punto.lim_rad_Sjai2_ast = calc.calcular_lim_rad_Sj2(punto.Tvia_ai, punto.Dbg_ai)
            punto.lim_Sja1_ast = calc.calcular_lim_Sj_ast(punto.Y / 1000, via.hco, via.K, via.Kale_h_0_50, punto.lim_rad_Sja1_ast)
            punto.lim_Sji1_ast = calc.calcular_lim_Sj_ast(punto.Y / 1000, via.hco, via.K, via.Kale_h_0_50, punto.lim_rad_Sji1_ast)
            punto.lim_Sja2_ast = calc.calcular_lim_Sj_ast(punto.Y / 1000, via.hco, via.K, via.Kale_h_0_50, punto.lim_rad_Sjai2_ast)
            punto.lim_Sji2_ast = calc.calcular_lim_Sj_ast(punto.Y / 1000, via.hco, via.K, via.Kale_h_0_50, punto.lim_rad_Sjai2_ast)
            punto.lim_rad_SVi1 = calc.calcular_lim_rad_SVi1(punto.TN, punto.Dhg_i, punto.Dhc, punto.Dhsusp_ai, punto.Dhcarg_ai, punto.Dhosc_i)
            punto.lim_rad_SVa1 = calc.calcular_lim_rad_SVa1(punto.TN, punto.Dhg_a, punto.Dhc, punto.Dhsusp_ai, punto.Dhcarg_ai, punto.Dhosc_a)
            punto.lim_SVa1 = calc.calcular_lim_SV1(via.K, punto.lim_rad_SVa1)
            punto.lim_SVi1 = calc.calcular_lim_SV1(via.K, punto.lim_rad_SVi1)
            punto.lim_SVa2 = punto.TN
            punto.lim_SVi2 = punto.TN
            punto.lim_SVa1_ast = calc.calcular_SVa1_ast(via.K, punto.TN, punto.Dhg_a, punto.Dhc, punto.Dhsusp_ai, punto.Dhcarg_ai, punto.Dhosc_a)
            punto.lim_SVi1_ast = calc.calcular_SVi1_ast(via.K, punto.TN, punto.Dhg_i, punto.Dhc, punto.Dhsusp_ai, punto.Dhcarg_ai, punto.Dhosc_i)
            punto.lim_SVa2_ast = punto.TN
            punto.lim_SVi2_ast = punto.TN
            punto.lim_bobstVM_max_i = calc.calcular_lim_bobst(punto.X, punto.Y / 1000, punto.Si, -punto.qsI_ai, punto.lim_Sji1, punto.lim_Sji2)
            punto.lim_hobstVM_con_i = calc.calcular_lim_hobst(punto.Y, punto.DhRv, via.hb_max, punto.esPT, punto.DhPT_I_ai, punto.lim_SVi1, punto.lim_SVi2)
            punto.lim_bobstVM_max_a = calc.calcular_lim_bobst(punto.X, punto.Y / 1000, punto.Sa, punto.qsI_ai, punto.lim_Sja1, punto.lim_Sja2)
            punto.lim_hobstVM_con_a = calc.calcular_lim_hobst(punto.Y, punto.DhRv, via.hb_max, punto.esPT, -punto.DhPT_I_ai, punto.lim_SVa1, punto.lim_SVa2)
            punto.lim_bobstVM_con_i = calc.calcular_lim_bobst(punto.X, punto.Y / 1000, punto.Si, -punto.qsI_ai, punto.lim_Sji1_ast, punto.lim_Sji2_ast)
            punto.lim_hobstVM_max_i = calc.calcular_lim_hobst(punto.Y, punto.DhRv, via.hb_max, punto.esPT, punto.DhPT_I_ai, punto.lim_SVi1_ast, punto.lim_SVi2_ast)
            punto.lim_bobstVM_con_a = calc.calcular_lim_bobst(punto.X, punto.Y / 1000, punto.Sa, punto.qsI_ai, punto.lim_Sja1_ast, punto.lim_Sja2_ast)
            punto.lim_hobstVM_max_a = calc.calcular_lim_hobst(punto.Y, punto.DhRv, via.hb_max, punto.esPT, -punto.DhPT_I_ai, punto.lim_SVa1_ast, punto.lim_SVa2_ast)
            punto.lim_bobstV0_max_i = calc.calcular_lim_bobst(punto.X, punto.Y / 1000, punto.Si, punto.qsD_ai, punto.lim_Sji1, punto.lim_Sji2)
            punto.lim_hobstV0_con_i = calc.calcular_lim_hobst(punto.Y, punto.DhRv, via.hb_max, punto.esPT, -punto.DhPT_D_ai, punto.lim_SVi1, punto.lim_SVi2)
            punto.lim_bobstV0_max_a = calc.calcular_lim_bobst(punto.X, punto.Y / 1000, punto.Sa, -punto.qsD_ai, punto.lim_Sja1, punto.lim_Sja2)
            punto.lim_hobstV0_con_a = calc.calcular_lim_hobst(punto.Y, punto.DhRv, via.hb_max, punto.esPT, punto.DhPT_D_ai, punto.lim_SVa1, punto.lim_SVa2)
            punto.lim_bobstV0_con_i = calc.calcular_lim_bobst(punto.X, punto.Y / 1000, punto.Si, punto.qsD_ai, punto.lim_Sji1_ast, punto.lim_Sji2_ast)
            punto.lim_hobstV0_max_i = calc.calcular_lim_hobst(punto.Y, punto.DhRv, via.hb_max, punto.esPT, -punto.DhPT_D_ai, punto.lim_SVi1_ast, punto.lim_SVi2_ast)
            punto.lim_bobstV0_con_a = calc.calcular_lim_bobst(punto.X, punto.Y / 1000, punto.Sa, -punto.qsD_ai, punto.lim_Sja1_ast, punto.lim_Sja2_ast)
            punto.lim_hobstV0_max_a = calc.calcular_lim_hobst(punto.Y, punto.DhRv, via.hb_max, punto.esPT, punto.DhPT_D_ai, punto.lim_SVa1_ast, punto.lim_SVa2_ast)
            punto.lim_ba = signo(punto.X) * max(abs(punto.lim_bobstVM_max_a), abs(punto.lim_bobstVM_con_a), abs(punto.lim_bobstV0_max_a), abs(punto.lim_bobstV0_con_a))
            punto.lim_ha = calc.calcular_h(punto.Y/1000, via.hb_max / 1000, punto.lim_hobstVM_con_a, punto.lim_hobstVM_max_a, punto.lim_hobstV0_con_a, punto.lim_hobstV0_max_a)
            punto.lim_bi = signo(punto.X) * max(abs(punto.lim_bobstVM_max_i), abs(punto.lim_bobstVM_con_i), abs(punto.lim_bobstV0_max_i), abs(punto.lim_bobstV0_con_i))
            punto.lim_hi = calc.calcular_h(punto.Y/1000, via.hb_max / 1000, punto.lim_hobstVM_con_i, punto.lim_hobstVM_max_i, punto.lim_hobstV0_con_i, punto.lim_hobstV0_max_i)

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
            punto.nom_hobstVM_con_i = calc.calcular_nom_hobst(punto.Y, punto.DhRv, via.hb_max, punto.esPT, punto.DhPT_I_ai, punto.nom_SVi3, punto.nom_SVi4, punto.M3h)
            punto.nom_bobstVM_max_a = calc.calcular_nom_bobst(punto.X, punto.Y / 1000, punto.Sa, punto.qsI_ai, punto.nom_Sja3, punto.nom_Sja4, punto.M3b)
            punto.nom_hobstVM_con_a = calc.calcular_nom_hobst(punto.Y, punto.DhRv, via.hb_max, punto.esPT, -punto.DhPT_I_ai, punto.nom_SVa3, punto.nom_SVa4, punto.M3h)
            punto.nom_bobstVM_con_i = calc.calcular_nom_bobst(punto.X, punto.Y / 1000, punto.Si, -punto.qsI_ai, punto.nom_Sji3_ast, punto.nom_Sji4_ast, punto.M3b)
            punto.nom_hobstVM_max_i = calc.calcular_nom_hobst(punto.Y, punto.DhRv, via.hb_max, punto.esPT, punto.DhPT_I_ai, punto.nom_SVi3_ast, punto.nom_SVi4_ast,punto.M3h)
            punto.nom_bobstVM_con_a = calc.calcular_nom_bobst(punto.X, punto.Y / 1000, punto.Sa, punto.qsI_ai, punto.nom_Sja3_ast, punto.nom_Sja4_ast, punto.M3b)
            punto.nom_hobstVM_max_a = calc.calcular_nom_hobst(punto.Y, punto.DhRv, via.hb_max, punto.esPT, -punto.DhPT_I_ai, punto.nom_SVa3_ast, punto.nom_SVa4_ast, punto.M3h)
            punto.nom_bobstV0_max_i = calc.calcular_nom_bobst(punto.X, punto.Y / 1000, punto.Si, punto.qsD_ai, punto.nom_Sji3, punto.nom_Sji4, punto.M3b)
            punto.nom_hobstV0_con_i = calc.calcular_nom_hobst(punto.Y, punto.DhRv, via.hb_max, punto.esPT, -punto.DhPT_D_ai, punto.nom_SVi3, punto.nom_SVi4, punto.M3h)
            punto.nom_bobstV0_max_a = calc.calcular_nom_bobst(punto.X, punto.Y / 1000, punto.Sa, -punto.qsD_ai, punto.nom_Sja3, punto.nom_Sja4, punto.M3b)
            punto.nom_hobstV0_con_a = calc.calcular_nom_hobst(punto.Y, punto.DhRv, via.hb_max, punto.esPT, punto.DhPT_D_ai, punto.nom_SVa3, punto.nom_SVa4, punto.M3h)
            punto.nom_bobstV0_con_i = calc.calcular_nom_bobst(punto.X, punto.Y / 1000, punto.Si, punto.qsD_ai, punto.nom_Sji3_ast, punto.nom_Sji4_ast, punto.M3b)
            punto.nom_hobstV0_max_i = calc.calcular_nom_hobst(punto.Y, punto.DhRv, via.hb_max, punto.esPT, -punto.DhPT_D_ai, punto.nom_SVi3_ast, punto.nom_SVi4_ast, punto.M3h)
            punto.nom_bobstV0_con_a = calc.calcular_nom_bobst(punto.X, punto.Y / 1000, punto.Sa, -punto.qsD_ai, punto.nom_Sja3_ast, punto.nom_Sja4_ast, punto.M3b)
            punto.nom_hobstV0_max_a = calc.calcular_nom_hobst(punto.Y, punto.DhRv, via.hb_max, punto.esPT, punto.DhPT_D_ai, punto.nom_SVa3_ast, punto.nom_SVa4_ast, punto.M3h)
            punto.nom_ba = signo(punto.X) * max(abs(punto.nom_bobstVM_max_a), abs(punto.nom_bobstVM_con_a), abs(punto.nom_bobstV0_max_a), abs(punto.nom_bobstV0_con_a))
            punto.nom_ha = calc.calcular_h(punto.Y/1000, via.hb_max / 1000, punto.nom_hobstVM_con_a, punto.nom_hobstVM_max_a, punto.nom_hobstV0_con_a, punto.nom_hobstV0_max_a)
            punto.nom_bi = signo(punto.X) * max(abs(punto.nom_bobstVM_max_i), abs(punto.nom_bobstVM_con_i), abs(punto.nom_bobstV0_max_i), abs(punto.nom_bobstV0_con_i))
            punto.nom_hi = calc.calcular_h(punto.Y/1000, via.hb_max / 1000, punto.nom_hobstVM_con_i, punto.nom_hobstVM_max_i, punto.nom_hobstV0_con_i, punto.nom_hobstV0_max_i)

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
            fttabla.tabla_100_lim_ba.controls.append(ft.Text(punto.lim_ba, size=Tamanyos.TABLA_NORMAL.value))
            fttabla.tabla_101_lim_ha.controls.append(ft.Text(punto.lim_ha, size=Tamanyos.TABLA_NORMAL.value))
            fttabla.tabla_102_lim_bi.controls.append(ft.Text(punto.lim_bi, size=Tamanyos.TABLA_NORMAL.value))
            fttabla.tabla_103_lim_hi.controls.append(ft.Text(punto.lim_hi, size=Tamanyos.TABLA_NORMAL.value))
            fttabla.tabla_104_nom_ba.controls.append(ft.Text(punto.nom_ba, size=Tamanyos.TABLA_NORMAL.value))
            fttabla.tabla_105_nom_ha.controls.append(ft.Text(punto.nom_ha, size=Tamanyos.TABLA_NORMAL.value))
            fttabla.tabla_106_nom_bi.controls.append(ft.Text(punto.nom_bi, size=Tamanyos.TABLA_NORMAL.value))
            fttabla.tabla_107_nom_hi.controls.append(ft.Text(punto.nom_hi, size=Tamanyos.TABLA_NORMAL.value))

        #Cálculos relativos al pantógrafo

        fttablaPant.actualizar_tabla()

        for nombre,punto in galiboPant.items():
            punto.S_ai = calc.calcular_pant_Sai(via.GPA, via.R, via.LN, via.LND)
            punto.qs_a = calc.calcular_pant_qsa(via.GPA, punto.Y_ref/1000, via.I, via.hco)
            punto.qs_i = calc.calcular_pant_qsi(via.GPA, punto.Y_ref/1000, via.D, via.hco)
            punto.Dbg_ai = calc.calcular_pant_Dbg_ai(punto.Y_ref/1000, via.L, via.TD)            #Se usa la fórmula general porque es igual en los pantografos que en los galibos normales
            punto.Dbc_ai = calc.calcular_pant_Dbc_ai(punto.Y_ref/1000, via.L, via.TD, via.hco)
            punto.Dbsusp_ai = calc.calcular_Dbsusp_ai(via.asusp, punto.Y_ref, via.hco * 1000)    #Se usa la ....
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
        #Alternativamente a esto, podría hacer que los gálibos iniciales de 
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
        for nombre,punto in galiboPant.items():
            punto.bobst_a_hmax = calc.calcular_pant_bobst_hmax_a(nombre, punto.bobst_a, Dbobst_a_12, Dbobst_a_34, Dy, via.heff * 1000,  datos_Pantografo[via.tipo_pant])
            punto.bobst_i_hmax = calc.calcular_pant_bobst_hmax_i(nombre, punto.bobst_i, Dbobst_i_12, Dbobst_i_34, Dy, via.heff * 1000, datos_Pantografo[via.tipo_pant])
            punto.bobst_a_hmax_heff_elec = calc.calcular_pant_bobst_hmax_a(nombre, punto.bobst_a, Dbobst_a_12, Dbobst_a_34, Dy, via.heffelec * 1000, datos_Pantografo[via.tipo_pant])
            punto.bobst_i_hmax_heff_elec = calc.calcular_pant_bobst_hmax_i(nombre, punto.bobst_i, Dbobst_i_12, Dbobst_i_34, Dy, via.heffelec * 1000, datos_Pantografo[via.tipo_pant])
            punto.bobst_a_hmax_elec = calc.calcular_pant_elec(punto.bobst_a_hmax_heff_elec, via.belec_dinam * 1000, via.cw * 1000)
            punto.bobst_i_hmax_elec = calc.calcular_pant_elec(punto.bobst_i_hmax_heff_elec, via.belec_estat * 1000, via.cw * 1000)

            punto.X_mec = calc.calcular_pant_pant_mec_X(punto.X_ref, punto.bobst_a, punto.bobst_i, lado)
            punto.Y_mec = calc.calcular_pant_pant_mec_Y(nombre, punto.Y_ref, 1000 * via.heff)
            punto.X_elec = calc.calcular_pant_pant_mec_X(punto.X_ref, punto.bobst_a_hmax_elec, punto.bobst_i_hmax_elec, lado)
            punto.Y_elec = calc.calcular_pant_pant_mec_Y(nombre, punto.Y_ref, 1000 * via.heffelec)

            fttablaPant.tablaPant_00_Punto.controls.append(ft.Text(nombre,size=Tamanyos.TABLA_NORMAL.value))
            fttablaPant.tablaPant_01_X_ref.controls.append(ft.Text(punto.X_ref,size=Tamanyos.TABLA_NORMAL.value))
            fttablaPant.tablaPant_02_Y_ref.controls.append(ft.Text(punto.Y_ref,size=Tamanyos.TABLA_NORMAL.value))
            fttablaPant.tablaPant_03_Sai.controls.append(ft.Text(punto.S_ai,size=Tamanyos.TABLA_NORMAL.value))
            fttablaPant.tablaPant_04_qsa.controls.append(ft.Text(punto.qs_a,size=Tamanyos.TABLA_NORMAL.value))
            fttablaPant.tablaPant_05_qsi.controls.append(ft.Text(punto.qs_i,size=Tamanyos.TABLA_NORMAL.value))
            fttablaPant.tablaPant_06_Dbgai.controls.append(ft.Text(punto.Dbg_ai,size=Tamanyos.TABLA_NORMAL.value))
            fttablaPant.tablaPant_07_Dbcai.controls.append(ft.Text(punto.Dbc_ai,size=Tamanyos.TABLA_NORMAL.value))
            fttablaPant.tablaPant_08_Dbsuspai.controls.append(ft.Text(punto.Dbsusp_ai,size=Tamanyos.TABLA_NORMAL.value))
            fttablaPant.tablaPant_09_Dbcargai.controls.append(ft.Text(punto.Dbcarg_ai,size=Tamanyos.TABLA_NORMAL.value))
            fttablaPant.tablaPant_10_Dbetaai.controls.append(ft.Text(punto.Dbeta0_ai,size=Tamanyos.TABLA_NORMAL.value))
            fttablaPant.tablaPant_11_aosca.controls.append(ft.Text(punto.aosc_a,size=Tamanyos.TABLA_NORMAL.value))
            fttablaPant.tablaPant_12_aosci.controls.append(ft.Text(punto.aosc_i,size=Tamanyos.TABLA_NORMAL.value))
            fttablaPant.tablaPant_13_Dbosca.controls.append(ft.Text(punto.Dbosc_a,size=Tamanyos.TABLA_NORMAL.value))
            fttablaPant.tablaPant_14_Dbosci.controls.append(ft.Text(punto.Dbosc_i,size=Tamanyos.TABLA_NORMAL.value))
            fttablaPant.tablaPant_15_TVia.controls.append(ft.Text(punto.Tvia_ai,size=Tamanyos.TABLA_NORMAL.value))
            fttablaPant.tablaPant_16_Sja.controls.append(ft.Text(punto.Sja,size=Tamanyos.TABLA_NORMAL.value))
            fttablaPant.tablaPant_17_Sji.controls.append(ft.Text(punto.Sji,size=Tamanyos.TABLA_NORMAL.value))
            fttablaPant.tablaPant_18_bobst_a.controls.append(ft.Text(punto.bobst_a,size=Tamanyos.TABLA_NORMAL.value))
            fttablaPant.tablaPant_19_bobst_i.controls.append(ft.Text(punto.bobst_i,size=Tamanyos.TABLA_NORMAL.value))
            fttablaPant.tablaPant_20_bobst_a_hmax.controls.append(ft.Text(punto.bobst_a_hmax,size=Tamanyos.TABLA_NORMAL.value))
            fttablaPant.tablaPant_21_bobst_i_hmax.controls.append(ft.Text(punto.bobst_i_hmax,size=Tamanyos.TABLA_NORMAL.value))
            fttablaPant.tablaPant_22_bobst_a_hmax_heff_elec.controls.append(ft.Text(punto.bobst_a_hmax_heff_elec,size=Tamanyos.TABLA_NORMAL.value))
            fttablaPant.tablaPant_23_bobst_i_hmax_heff_elec.controls.append(ft.Text(punto.bobst_i_hmax_heff_elec,size=Tamanyos.TABLA_NORMAL.value))
            fttablaPant.tablaPant_24_bobst_a_hmax_elec.controls.append(ft.Text(punto.bobst_a_hmax_elec,size=Tamanyos.TABLA_NORMAL.value))
            fttablaPant.tablaPant_25_bobst_i_hmax_elec.controls.append(ft.Text(punto.bobst_i_hmax_elec,size=Tamanyos.TABLA_NORMAL.value))
            fttablaPant.tablaPant_26_X_mec.controls.append(ft.Text(punto.X_mec,size=Tamanyos.TABLA_NORMAL.value))
            fttablaPant.tablaPant_27_Y_mec.controls.append(ft.Text(punto.Y_mec,size=Tamanyos.TABLA_NORMAL.value))
            fttablaPant.tablaPant_28_X_elec.controls.append(ft.Text(punto.X_elec,size=Tamanyos.TABLA_NORMAL.value))
            fttablaPant.tablaPant_29_Y_elec.controls.append(ft.Text(punto.Y_elec,size=Tamanyos.TABLA_NORMAL.value))

    def cambiar_graficos(galiboPA1, galiboPB1, galiboPA2, galiboPB2, galiboPant1, galiboPant2):
        #ACTUALIZACIÓN DE LOS GRÁFICOS
        datos_grafico_1_GPA.data_points.clear()
        datos_grafico_1_GPA_lim.data_points.clear()
        datos_grafico_1_GPA_nom.data_points.clear()
        datos_grafico_1_GPB.data_points.clear()
        datos_grafico_1_Pant_ref.data_points.clear()
        datos_grafico_1_Pant_mec.data_points.clear()
        datos_grafico_1_Pant_elec.data_points.clear()

        datos_grafico_2_GPA.data_points.clear()
        datos_grafico_2_GPA_lim.data_points.clear()
        datos_grafico_2_GPA_nom.data_points.clear()
        datos_grafico_2_GPB.data_points.clear()
        datos_grafico_2_Pant_ref.data_points.clear()
        datos_grafico_2_Pant_mec.data_points.clear()
        datos_grafico_2_Pant_elec.data_points.clear()

        for nombre,punto in galiboPA1.items():
            datos_grafico_1_GPA.data_points.append(ft.LineChartDataPoint(
                cos(radians(via1.Inclinac)) * punto.X/conf.ESCALA_GRAFICO + sin(radians(via1.Inclinac)) * punto.Y/conf.ESCALA_GRAFICO,
                - sin(radians(via1.Inclinac)) * punto.X/conf.ESCALA_GRAFICO + cos(radians(via1.Inclinac)) * punto.Y/conf.ESCALA_GRAFICO,
                tooltip=(nombre, f'x={punto.X}', f'y={punto.Y}')))
            datos_grafico_1_GPA_lim.data_points.append(ft.LineChartDataPoint(
                cos(radians(via1.Inclinac)) * punto.lim_bi/conf.ESCALA_GRAFICO + sin(radians(via1.Inclinac)) * punto.lim_hi/conf.ESCALA_GRAFICO,
                - sin(radians(via1.Inclinac)) * punto.lim_bi/conf.ESCALA_GRAFICO + cos(radians(via1.Inclinac)) * punto.lim_hi/conf.ESCALA_GRAFICO,
                tooltip=(nombre, f'x={punto.lim_bi}', f'y={punto.lim_hi}')))
            datos_grafico_1_GPA_nom.data_points.append(ft.LineChartDataPoint(
                cos(radians(via1.Inclinac)) * punto.nom_bi/conf.ESCALA_GRAFICO + sin(radians(via1.Inclinac)) * punto.nom_hi/conf.ESCALA_GRAFICO,
                - sin(radians(via1.Inclinac)) * punto.nom_bi/conf.ESCALA_GRAFICO + cos(radians(via1.Inclinac)) * punto.nom_hi/conf.ESCALA_GRAFICO,
                tooltip=(nombre, f'x={punto.nom_bi}', f'y={punto.nom_hi}')))
        
        for nombre, punto in galiboPant1.items():
            datos_grafico_1_Pant_ref.data_points.append(ft.LineChartDataPoint(
                cos(radians(via1.Inclinac)) * punto.X_ref/conf.ESCALA_GRAFICO + sin(radians(via1.Inclinac)) * punto.Y_ref/conf.ESCALA_GRAFICO,
                - sin(radians(via1.Inclinac)) * punto.X_ref/conf.ESCALA_GRAFICO + cos(radians(via1.Inclinac)) * punto.Y_ref/conf.ESCALA_GRAFICO,
                tooltip=(nombre, f'x={punto.X_ref}', f'y={punto.Y_ref}')))
            datos_grafico_1_Pant_mec.data_points.append(ft.LineChartDataPoint(
                cos(radians(via1.Inclinac)) * punto.X_mec/conf.ESCALA_GRAFICO + sin(radians(via1.Inclinac)) * punto.Y_mec/conf.ESCALA_GRAFICO,
                - sin(radians(via1.Inclinac)) * punto.X_mec/conf.ESCALA_GRAFICO + cos(radians(via1.Inclinac)) * punto.Y_mec/conf.ESCALA_GRAFICO,
                tooltip=(nombre, f'x={punto.X_mec}', f'y={punto.Y_mec}')))
            datos_grafico_1_Pant_elec.data_points.append(ft.LineChartDataPoint(
                cos(radians(via1.Inclinac)) * punto.X_elec/conf.ESCALA_GRAFICO + sin(radians(via1.Inclinac)) * punto.Y_elec/conf.ESCALA_GRAFICO,
                - sin(radians(via1.Inclinac)) * punto.X_elec/conf.ESCALA_GRAFICO + cos(radians(via1.Inclinac)) * punto.Y_elec/conf.ESCALA_GRAFICO,
                tooltip=(nombre, f'x={punto.X_elec}', f'y={punto.Y_elec}')))
            
        datos_grafico_1_GPA.visible = ftElem_1.cb_graf_GPA.value
        datos_grafico_1_GPA_lim.visible = ftElem_1.cb_graf_GPA_lim.value
        datos_grafico_1_GPA_nom.visible = ftElem_1.cb_graf_GPA_nom.value
        datos_grafico_1_Pant_ref.visible = ftElem_1.cb_graf_pant.value
        datos_grafico_1_Pant_mec.visible = ftElem_1.cb_graf_pant.value               #Tengo que cambiar esto, y ponerle un check propio
        datos_grafico_1_Pant_elec.visible = ftElem_1.cb_graf_pant.value               #Tengo que cambiar esto, y ponerle un check propio

        for nombre,punto in galiboPB1.items():
            datos_grafico_1_GPB.data_points.append(ft.LineChartDataPoint(
                cos(radians(via1.Inclinac)) * punto.X/conf.ESCALA_GRAFICO + sin(radians(via1.Inclinac)) * punto.Y/conf.ESCALA_GRAFICO,
                - sin(radians(via1.Inclinac)) * punto.X/conf.ESCALA_GRAFICO + cos(radians(via1.Inclinac)) * punto.Y/conf.ESCALA_GRAFICO,
                tooltip=(nombre, f'x={punto.X}', f'x={punto.Y}')))
        datos_grafico_1_GPB.visible = ftElem_1.cb_graf_GPB.value

        separacion_h = float(ftElem_2.tf_separacion_h.value) * 1000 / conf.ESCALA_GRAFICO
        separacion_v = float(ftElem_2.tf_separacion_v.value) * 1000 / conf.ESCALA_GRAFICO
        if cb_via2.value:
            for nombre,punto in galiboPA2.items():
                datos_grafico_2_GPA.data_points.append(ft.LineChartDataPoint(
                    cos(radians(via2.Inclinac)) * punto.X/conf.ESCALA_GRAFICO + sin(radians(via2.Inclinac)) * punto.Y/conf.ESCALA_GRAFICO + separacion_h,
                    - sin(radians(via2.Inclinac)) * punto.X/conf.ESCALA_GRAFICO + cos(radians(via2.Inclinac)) * punto.Y/conf.ESCALA_GRAFICO + separacion_v,
                    tooltip=(nombre, f'x={punto.X}', f'y={punto.Y}')))
                datos_grafico_2_GPA_lim.data_points.append(ft.LineChartDataPoint(
                    cos(radians(via2.Inclinac)) * punto.lim_bi/conf.ESCALA_GRAFICO + sin(radians(via2.Inclinac)) * punto.lim_hi/conf.ESCALA_GRAFICO + separacion_h,
                    - sin(radians(via2.Inclinac)) * punto.lim_bi/conf.ESCALA_GRAFICO + cos(radians(via2.Inclinac)) * punto.lim_hi/conf.ESCALA_GRAFICO + separacion_v,
                    tooltip=(nombre, f'x={punto.lim_bi}', f'y={punto.lim_hi}')))
                datos_grafico_2_GPA_nom.data_points.append(ft.LineChartDataPoint(
                    cos(radians(via2.Inclinac)) * punto.nom_bi/conf.ESCALA_GRAFICO + sin(radians(via2.Inclinac)) * punto.nom_hi/conf.ESCALA_GRAFICO + separacion_h,
                    - sin(radians(via2.Inclinac)) * punto.nom_bi/conf.ESCALA_GRAFICO + cos(radians(via2.Inclinac)) * punto.nom_hi/conf.ESCALA_GRAFICO + separacion_v,
                    tooltip=(nombre, f'x={punto.nom_bi}', f'y={punto.nom_hi}')))
            
            for nombre, punto in galiboPant2.items():
                datos_grafico_2_Pant_ref.data_points.append(ft.LineChartDataPoint(
                    cos(radians(via2.Inclinac)) * punto.X_ref/conf.ESCALA_GRAFICO + sin(radians(via2.Inclinac)) * punto.Y_ref/conf.ESCALA_GRAFICO + separacion_h,
                    - sin(radians(via2.Inclinac)) * punto.X_ref/conf.ESCALA_GRAFICO + cos(radians(via2.Inclinac)) * punto.Y_ref/conf.ESCALA_GRAFICO + separacion_v,
                    tooltip=(nombre, f'x={punto.X_ref}', f'y={punto.Y_ref}')))
                datos_grafico_2_Pant_mec.data_points.append(ft.LineChartDataPoint(
                    cos(radians(via2.Inclinac)) * punto.X_mec/conf.ESCALA_GRAFICO + sin(radians(via2.Inclinac)) * punto.Y_mec/conf.ESCALA_GRAFICO + separacion_h,
                    - sin(radians(via2.Inclinac)) * punto.X_mec/conf.ESCALA_GRAFICO + cos(radians(via2.Inclinac)) * punto.Y_mec/conf.ESCALA_GRAFICO + separacion_v,
                    tooltip=(nombre, f'x={punto.X_mec}', f'y={punto.Y_mec}')))
                datos_grafico_2_Pant_elec.data_points.append(ft.LineChartDataPoint(
                    cos(radians(via2.Inclinac)) * punto.X_elec/conf.ESCALA_GRAFICO + sin(radians(via2.Inclinac)) * punto.Y_elec/conf.ESCALA_GRAFICO + separacion_h,
                    - sin(radians(via2.Inclinac)) * punto.X_elec/conf.ESCALA_GRAFICO + cos(radians(via2.Inclinac)) * punto.Y_elec/conf.ESCALA_GRAFICO + separacion_v,
                    tooltip=(nombre, f'x={punto.X_elec}', f'y={punto.Y_elec}')))
            
            datos_grafico_2_GPA.visible = ftElem_2.cb_graf_GPA.value
            datos_grafico_2_GPA_lim.visible = ftElem_2.cb_graf_GPA_lim.value
            datos_grafico_2_GPA_nom.visible = ftElem_2.cb_graf_GPA_nom.value
            datos_grafico_2_Pant_ref.visible = ftElem_2.cb_graf_pant.value
            datos_grafico_2_Pant_mec.visible = ftElem_2.cb_graf_pant.value               #Tengo que cambiar esto, y ponerle un check propio
            datos_grafico_2_Pant_elec.visible = ftElem_2.cb_graf_pant.value               #Tengo que cambiar esto, y ponerle un check propio

        if cb_via2.value:
            for nombre,punto in galiboPB2.items():
                datos_grafico_2_GPB.data_points.append(ft.LineChartDataPoint(
                    cos(radians(via2.Inclinac)) * punto.X/conf.ESCALA_GRAFICO + sin(radians(via2.Inclinac)) * punto.Y/conf.ESCALA_GRAFICO + separacion_h,
                    - sin(radians(via2.Inclinac)) * punto.X/conf.ESCALA_GRAFICO + cos(radians(via2.Inclinac)) * punto.Y/conf.ESCALA_GRAFICO + separacion_v,
                    tooltip=(nombre, f'x={punto.X}', f'y={punto.Y}')))
            datos_grafico_2_GPB.visible = ftElem_2.cb_graf_GPB.value
        
        ft_grafico.max_x = 2000 + separacion_h if galiboPA2 else 2000
        ft_grafico.max_y = 4000 if galiboPA2 else 2000

    def cambiar(e):
        habilitar_via2()

        via1.GPA = ftElem_1.dd_GPA.value
        via1.GPB = ftElem_1.dd_GPB.value
        via1.tipo_pant = ftElem_1.dd_TIPOPAN.value
        via1.tipo_cat =  ftElem_1.dd_TIPOCAT.value
        via1.tipo_lin =  ftElem_1.dd_TIPOLIN.value
        via1.ten_cat =  ftElem_1.dd_TENCAT.value

        via2.GPA = ftElem_2.dd_GPA.value
        via2.GPB = ftElem_2.dd_GPB.value
        via2.tipo_pant = ftElem_2.dd_TIPOPAN.value
        via2.tipo_cat =  ftElem_2.dd_TIPOCAT.value
        via2.tipo_lin =  ftElem_2.dd_TIPOLIN.value
        via2.ten_cat =  ftElem_2.dd_TENCAT.value

        galiboPA1 = datos_GPA[via1.GPA]
        galiboPB1 = datos_GPB[via1.GPB]
        galiboPant1 = datos_Pantografo[via1.tipo_pant]

        cambiar_via(galiboPA1, via1, ftElem_1)
        cambiar_elementos(galiboPA1, galiboPant1, ftt_1, fttabla_1, fttablaPant_1, via1)

        galiboPA2 = None
        galiboPB2 = None
        galiboPant2 = None
        if cb_via2.value:
            galiboPA2 = datos_GPA[via2.GPA]
            galiboPB2 = datos_GPB[via2.GPB]
            galiboPant2 = datos_Pantografo[via2.tipo_pant]
            cambiar_via(galiboPA2, via2, ftElem_2)
            cambiar_elementos(galiboPA2, galiboPant2, ftt_2, fttabla_2, fttablaPant_2, via2)
        cambiar_graficos(galiboPA1, galiboPB1, galiboPA2, galiboPB2, galiboPant1, galiboPant2)

        page.update()

    def habilitar_via2():
        ftElem_2.dd_GPA.disabled = not cb_via2.value
        ftElem_2.dd_GPB.disabled = not cb_via2.value
        ftElem_2.dd_EV.disabled = not cb_via2.value
        ftElem_2.dd_TV.disabled = not cb_via2.value
        ftElem_2.tf_R.disabled = not cb_via2.value
        ftElem_2.cb_R.disabled = not cb_via2.value
        ftElem_2.tf_RV.disabled = not cb_via2.value
        ftElem_2.cb_RV.disabled = not cb_via2.value
        ftElem_2.tf_DL.disabled = not cb_via2.value
        ftElem_2.tf_D.disabled = not cb_via2.value
        ftElem_2.tf_I.disabled = not cb_via2.value
        ftElem_2.tf_tol_sus.disabled = not cb_via2.value
        ftElem_2.tf_tol_carga.disabled = not cb_via2.value
        ftElem_2.tf_vmax.disabled = not cb_via2.value
        ftElem_2.cb_graf_GPA.disabled = not cb_via2.value
        ftElem_2.cb_graf_GPB.disabled = not cb_via2.value
        ftElem_2.cb_graf_GPA_lim.disabled = not cb_via2.value
        ftElem_2.cb_graf_GPA_nom.disabled = not cb_via2.value
        ftElem_2.cb_graf_pant.disabled = not cb_via2.value
        ftElem_2.cb_graf_esGirado.disabled = not cb_via2.value
        ftElem_2.tf_separacion_h.disabled = not cb_via2.value
        ftElem_2.tf_separacion_v.disabled = not cb_via2.value
        ftElem_2.tf_hpant.disabled = not cb_via2.value
        ftElem_2.dd_TIPOPAN.disabled = not cb_via2.value
        ftElem_2.dd_TIPOLIN.disabled = not cb_via2.value
        ftElem_2.dd_TIPOCAT.disabled = not cb_via2.value
        ftElem_2.dd_TENCAT.disabled = not cb_via2.value
        page.update()

    #COMPONENTES INDIVIDUALES CON EVENTOS
    class ftElementos:
        def __init__(self, inhabilitado = False, es2via = False):

            self.dd_GPA = ft.Dropdown(
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
                on_change=cambiar,
                disabled = inhabilitado,
            )
            self.dd_GPB = ft.Dropdown(
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
                disabled = inhabilitado
            )
            self.dd_TV =  ft.Dropdown(
                label = "Tipo de Vía",
                hint_text = "Balasto / Vía en placa",
                options = [
                    ft.dropdown.Option(ETV.BALASTO.value),
                    ft.dropdown.Option(ETV.VIA_PLACA.value),
                ],
                on_change=cambiar,
                disabled = inhabilitado
            )
            self.dd_EV = ft.Dropdown(
                label = "Estado de la Vía",
                hint_text = "Buen / Mal estado",
                options = [
                    ft.dropdown.Option(EEV.BUEN_ESTADO.value),
                    ft.dropdown.Option(EEV.MAL_ESTADO.value),
                ],
                on_change=cambiar,
                disabled = inhabilitado
            )

            self.tf_R = ft.TextField(label="Radio de curvatura en planta (m)",value = 100, on_submit=cambiar, disabled = inhabilitado)
            self.cb_R = ft.Checkbox(value = False, on_change=cambiar, disabled = inhabilitado)
            self.tf_RV = ft.TextField(label="Radio del acuerdo vertical (m)", value = 100, on_submit=cambiar, disabled = inhabilitado)
            self.cb_RV = ft.Checkbox(value = False, on_change=cambiar, disabled = inhabilitado)
            self.tf_DL = ft.TextField(label="Sobreancho máximo (m)",value=0.03,read_only=True, on_submit=cambiar, disabled = inhabilitado)
            self.tf_D = ft.TextField(label="Peralte de la vía (m)", value = 0.11, on_submit=cambiar, disabled = inhabilitado)
            self.tf_I = ft.TextField(label="Insuficiencia de peralte (m)", value = 0.07, on_submit=cambiar, disabled = inhabilitado)
            self.tf_tol_sus = ft.TextField(label="Tolerancias en el reglaje de la suspensión (º)", value = 0.23, on_submit=cambiar, disabled = inhabilitado)
            self.tf_tol_carga = ft.TextField(label="Reparto desigual de cargas (º)", value = 0.77, on_submit=cambiar, disabled = inhabilitado)
            self.tf_vmax = ft.TextField(label="Velocidad máxima de la vía (km/h)", value=100, on_submit=cambiar, disabled = inhabilitado)

            self.cb_graf_GPA = ft.Checkbox("Mostrar Gálibo superior", value = True, on_change = cambiar, disabled = inhabilitado)
            self.cb_graf_GPB = ft.Checkbox("Mostrar Gálibo inferior", value = True, on_change = cambiar, disabled = inhabilitado)
            self.cb_graf_GPA_lim = ft.Checkbox("Mostrar Gálibo límite", value = True, on_change = cambiar, disabled = inhabilitado)
            self.cb_graf_GPA_nom = ft.Checkbox("Mostrar Gálibo nominal", value = True, on_change = cambiar, disabled = inhabilitado)
            self.cb_graf_pant = ft.Checkbox("Mostrar Pantógrafos", value = True, on_change = cambiar, disabled = inhabilitado)
            self.cb_graf_esGirado = ft.Checkbox("Girar gráfico", value = False, on_change = cambiar, disabled = inhabilitado)
            self.cb_graf_inclinacion = ft.RadioGroup(content=ft.Row([
                ft.Radio(value="A derechas", label="A derechas"),
                ft.Radio(value="A izquierdas", label="A izquierdas")]),
                disabled = True,
                value = "A derechas",
                on_change=cambiar,
            )
            self.tf_hpant = ft.TextField(label="Altura del hilo de contacto (m)",value = 5, on_submit=cambiar, disabled = inhabilitado, width = 150)
            self.dd_TIPOPAN = ft.Dropdown(
                label = "Tipo de pantógrafo",
                hint_text = "Introduce el tipo de pantógrafo",
                options = [
                    ft.dropdown.Option(TIPO_PANT.ANCHO_1600.value),
                    ft.dropdown.Option(TIPO_PANT.ANCHO_1700.value),
                    ft.dropdown.Option(TIPO_PANT.ANCHO_1950.value),
                    ],
                on_change=cambiar,
                disabled = inhabilitado,
                width = 300,
                #max_menu_height=40
            )
            self.dd_TIPOLIN = ft.Dropdown(
                label = "Tipo de línea",
                hint_text = "Introduce el tipo de línea",
                options = [
                    ft.dropdown.Option(TIPO_LINEA.EXISTENTES.value),
                    ft.dropdown.Option(TIPO_LINEA.NUEVAS.value),
                    ],
                on_change=cambiar,
                disabled = inhabilitado,
                width = 250 
            )
            self.dd_TIPOCAT = ft.Dropdown(
                label = "Tipo de catenaria",
                hint_text = "Introduce el tipo de catenaria",
                options = [
                    ft.dropdown.Option(TIPO_CAT.CA160.value),
                    ft.dropdown.Option(TIPO_CAT.CA220.value),
                    ft.dropdown.Option(TIPO_CAT.CAU220.value),
                    ft.dropdown.Option(TIPO_CAT.EAC350.value),
                    ft.dropdown.Option(TIPO_CAT.SICAT.value),
                    ft.dropdown.Option(TIPO_CAT.RIGIDA.value),
                    ],
                on_change=cambiar,
                disabled = inhabilitado,
                width = 250
            )
            self.dd_TENCAT = ft.Dropdown(
                label = "Tensión de la catenaria",
                hint_text = "Introduce la tensión de la catenaria",
                options = [
                    ft.dropdown.Option(TENSION_CAT.CC_1500.value),
                    ft.dropdown.Option(TENSION_CAT.CC_3000.value),
                    ft.dropdown.Option(TENSION_CAT.CA_25000.value),
                    ],
                on_change=cambiar,
                disabled = inhabilitado,
                width = 300
            )
            if es2via:
                self.tf_separacion_h = ft.TextField(label="Separación horizontal entre vias (m)", value=4, on_submit=cambiar, disabled = inhabilitado, border_color= ft.colors.AMBER)
                self.tf_separacion_v = ft.TextField(label="Separación vertical entre vias (m)", value=0.2, on_submit=cambiar, disabled = inhabilitado, border_color= ft.colors.AMBER)

    ftElem_1 = ftElementos()
    ftElem_2 = ftElementos(inhabilitado=True, es2via = True)

    cb_via2 = ft.Checkbox(value = False, on_change=cambiar)

    page.add(
        ft.Column([
            ft.ResponsiveRow([
                ft.Column(
                    col=4,
                    controls = [ft_grafico,]
                    ),
                ft.Column(
                    col=8,
                    controls = [ft.Tabs(
                        selected_index = 0,
                        animation_duration = 50,
                        tabs = [
                            ft.Tab(
                                text = "Vía 1",
                                content = ft.Column(
                                    controls = [
                                        ft.Text("", size = 1),      #Espaciador, para que quede bonito
                                        ft.Row([
                                            ftElem_1.dd_GPA,
                                            ftElem_1.dd_GPB,
                                            ftElem_1.dd_TV,
                                            ftElem_1.dd_EV,
                                        ]),
                                        ft.Row([
                                            ftElem_1.tf_R,
                                            ftElem_1.cb_R,
                                            ft.Text("Alineación recta en planta",size=Tamanyos.PEQUENYO.value),
                                            ftElem_1.tf_RV,
                                            ftElem_1.cb_RV,
                                            ft.Text("Alineación recta en alzado",size=Tamanyos.PEQUENYO.value),
                                            ftElem_1.tf_vmax,
                                        ]),
                                        ft.Row([
                                            ftElem_1.tf_DL,
                                            ftElem_1.tf_D,
                                            ftElem_1.tf_I,
                                        ]),
                                        ft.Row([
                                            ftElem_1.tf_tol_sus,
                                            ftElem_1.tf_tol_carga,
                                        ]),
                                        ft.Row([
                                            ftElem_1.tf_hpant,
                                            ftElem_1.dd_TIPOPAN,
                                            ftElem_1.dd_TIPOLIN,
                                            ftElem_1.dd_TIPOCAT,
                                            ftElem_1.dd_TENCAT,
                                        ]),                                        
                                        ft.Row([
                                            ftElem_1.cb_graf_GPA,
                                            ftElem_1.cb_graf_GPB,
                                            ftElem_1.cb_graf_GPA_lim,
                                            ftElem_1.cb_graf_GPA_nom,
                                            ftElem_1.cb_graf_pant,
                                        ]),
                                        ft.Row([
                                            ftElem_1.cb_graf_esGirado,
                                            ftElem_1.cb_graf_inclinacion,
                                        ])
                                    ],
                                expand=1),
                                
                                ),
                            ft.Tab(
                                tab_content=ft.Row([cb_via2,ft.Text("Vía 2")]),
                                content = ft.Column(
                                    controls = [
                                        ft.Text("", size = 1),      #Espaciador, para que quede bonito
                                        ft.Row([
                                            ftElem_2.dd_GPA,
                                            ftElem_2.dd_GPB,
                                            ftElem_2.dd_TV,
                                            ftElem_2.dd_EV,
                                        ]),
                                        ft.Row([
                                            ftElem_2.tf_R,
                                            ftElem_2.cb_R,
                                            ft.Text("Alineación recta en planta",size=Tamanyos.PEQUENYO.value),
                                            ftElem_2.tf_RV,
                                            ftElem_2.cb_RV,
                                            ft.Text("Alineación recta en alzado",size=Tamanyos.PEQUENYO.value),
                                            ftElem_2.tf_vmax,
                                        ]),
                                        ft.Row([
                                            ftElem_2.tf_DL,
                                            ftElem_2.tf_D,
                                            ftElem_2.tf_I,
                                        ]),
                                        ft.Row([
                                            ftElem_2.tf_tol_sus,
                                            ftElem_2.tf_tol_carga,
                                            ftElem_2.tf_separacion_h,
                                            ftElem_2.tf_separacion_v,
                                        ]),
                                        ft.Row([
                                            ftElem_2.tf_hpant,
                                            ftElem_2.dd_TIPOPAN,
                                            ftElem_2.dd_TIPOLIN,
                                            ftElem_2.dd_TIPOCAT,
                                            ftElem_2.dd_TENCAT,
                                        ]),
                                        ft.Row([
                                            ftElem_2.cb_graf_GPA,
                                            ftElem_2.cb_graf_GPB,
                                            ftElem_2.cb_graf_GPA_lim,
                                            ftElem_2.cb_graf_GPA_nom,
                                            ftElem_2.cb_graf_pant,
                                        ]),
                                        ft.Row([
                                            ftElem_2.cb_graf_esGirado,
                                            ftElem_2.cb_graf_inclinacion,
                                        ])
                                    ],
                                expand=1),
                                ),
                        ],
                        #expand= 0,
                    ),
                    
                ],
                height=425,),
        ]),
            ft.Tabs(
                selected_index=0,
                animation_duration=50,
                tabs=[
                    ft.Tab(
                        text = "Variables Via 1",
                        content = tabla_var_1,
                    ),
                    ft.Tab(
                        text = "Desplazamientos Via 1",
                        content = tabla_des_1,
                    ), 
                    ft.Tab(
                        text = "Galibo límite Via 1",
                        content = tabla_lim_1,
                    ), 
                    ft.Tab(
                        text = "Galibo nominal Via 1",
                        content = tabla_nom_1,
                    ),
                    ft.Tab(
                        text = "Pantógrafo Via 1",
                        content = tabla_pant_1,
                    ),
                    ft.Tab(
                        text = "Variables Via 2",
                        content = tabla_var_2,
                    ), 
                    ft.Tab(
                        text = "Desplazamientos Via 2",
                        content = tabla_des_2,
                    ), 
                    ft.Tab(
                        text = "Galibo límite Via 2",
                        content = tabla_lim_2,
                    ), 
                    ft.Tab(
                        text = "Galibo nominal Via 2",
                        content = tabla_nom_2,
                    ), 
                    ft.Tab(
                        text = "Pantógrafo Via 2",
                        content = tabla_pant_2,
                    ),
                ],
                expand = 0
                ),
        ])
    )

ft.app(galibos)