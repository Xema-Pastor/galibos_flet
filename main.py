import flet as ft
from datos_galibos import datos_GPA, datos_GPB
from datos_variables import Variables as var
from estilos.estilos import Tamanyos, EGPA, EGPB, ETV, EEV
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
            if punto["y"] > var.maxY:
                var.maxY = punto["y"]
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
        tabla_00_Punto.controls.clear()
        tabla_00_Punto.controls.append(ft.Text("Punto",size=10))
        tabla_00_Punto.controls.append(ft.Text("()",size=10))
        tabla_01_X.controls.clear()
        tabla_01_X.controls.append(ft.Text("X",size=10))
        tabla_01_X.controls.append(ft.Text("(mm)",size=10))
        tabla_02_Y.controls.clear()
        tabla_02_Y.controls.append(ft.Text("Y",size=10))
        tabla_02_Y.controls.append(ft.Text("(mm)",size=10))
        tabla_03_esPT.controls.clear()
        tabla_03_esPT.controls.append(ft.Text("esPT",size=10))
        tabla_03_esPT.controls.append(ft.Text("S/N",size=10))
        tabla_04_k.controls.clear()
        tabla_04_k.controls.append(ft.Text("k",size=10))
        tabla_04_k.controls.append(ft.Text("()",size=10))
        tabla_05_s0.controls.clear()
        tabla_05_s0.controls.append(ft.Text("s0",size=10))
        tabla_05_s0.controls.append(ft.Text("()",size=10))
        tabla_06_Sa.controls.clear()
        tabla_06_Sa.controls.append(ft.Text("Sa",size=10))
        tabla_06_Sa.controls.append(ft.Text("(mm)",size=10))
        tabla_07_Si.controls.clear()
        tabla_07_Si.controls.append(ft.Text("Si",size=10))
        tabla_07_Si.controls.append(ft.Text("(mm)",size=10))
        tabla_08_qsDai.controls.clear()
        tabla_08_qsDai.controls.append(ft.Text("qsD,ai",size=10))
        tabla_08_qsDai.controls.append(ft.Text("(mm)",size=10))
        tabla_09_qsIai.controls.clear()
        tabla_09_qsIai.controls.append(ft.Text("qsI,ai",size=10))
        tabla_09_qsIai.controls.append(ft.Text("(mm)",size=10))
        tabla_10_Tvia_ai.controls.clear()
        tabla_10_Tvia_ai.controls.append(ft.Text("Tvia,ai",size=10))
        tabla_10_Tvia_ai.controls.append(ft.Text("(mm)",size=10))

        datos_grafico_GPA.data_points.clear()
        datos_grafico_GPB.data_points.clear()

        #ACTUALIZACIÓN DE LAS TABLAS DE DATOS Y GRÁFICOS DE FLET
        for nombre,punto in galiboPA.items():
            tabla_00_Punto.controls.append(ft.Text(nombre,size=10))
            punto["punto"].X = punto["x"]
            punto["punto"].Y = punto["y"]
            punto["punto"].esPT = calc.calcular_esPT(punto["punto"].Y, var.maxY)
            punto["punto"].k = calc.calcular_k(var.GPA, punto["punto"].Y/1000, var.hquiebroaux, var.htopeaux, var.difaux)
            punto["punto"].s0 = calc.calcular_s0(var.GPA, punto["punto"].Y/1000, var.hquiebroaux, var.htopeaux, var.difaux, var.hotra)
            punto["punto"].Sa = calc.calcular_Sa(var.GPA, var.R, var.LN, var.LND, var.hquiebroaux, punto["punto"].Y/1000, punto["punto"].k)
            punto["punto"].Si = calc.calcular_Si(var.GPA, var.R, var.LN, var.LND, var.hquiebroaux, punto["punto"].Y/1000, punto["punto"].k)
            punto["punto"].qsDai = calc.calcular_qsD_ai(punto["punto"].Y/1000, punto["punto"].s0, var.D, var.D0, var.L, var.hco)
            punto["punto"].qsIai = calc.calcular_qsI_ai(punto["punto"].Y/1000, punto["punto"].s0, var.I, var.I0, var.L, var.hco)
            #punto["punto"].Tvia_ai
            #punto["punto"].Dbg_ai
            #punto["punto"].Dbc_ai
            #punto["punto"].Dbsusp_ai
            #punto["punto"].Dbcarga_ai
            #punto["punto"].Dbh0_ai
            #punto["punto"].aosc_a
            #punto["punto"].aosc_i
            #punto["punto"].Dbosc_a
            #punto["punto"].Dbosc_i
            #punto["punto"].M3b
            #punto["punto"].DhRv
            #punto["punto"].DhPT_D_ai
            #punto["punto"].DhPT_I_ai
            #punto["punto"].TN
            #punto["punto"].Dhg_a
            #punto["punto"].Dhg_i
            #punto["punto"].Dhc
            #punto["punto"].Dhsusp_ai
            #punto["punto"].Dhcarga_ai
            #punto["punto"].Dhh0_ai
            #punto["punto"].Dhosc_a
            #punto["punto"].Dhosc_i
            #punto["punto"].M3h
            #punto["punto"].Kale
            #punto["punto"].Kgeneral
            #punto["punto"].lim_Sja1
            #punto["punto"].lim_Sji1
            #punto["punto"].lim_Sja2
            #punto["punto"].lim_Sji2
            #punto["punto"].lim_Sja1_ast
            #punto["punto"].lim_Sji1_ast
            #punto["punto"].lim_Sja2_ast
            #punto["punto"].lim_Sji2_ast
            #punto["punto"].lim_SVa1
            #punto["punto"].lim_SVi1
            #punto["punto"].lim_SVa2
            #punto["punto"].lim_SVi2
            #punto["punto"].lim_SVa1_ast
            #punto["punto"].lim_SVi1_ast
            #punto["punto"].lim_SVa2_ast
            #punto["punto"].lim_SVi2_ast
            #punto["punto"].lim_bobst_max_i
            #punto["punto"].lim_hobst_conc_i
            #punto["punto"].lim_bobst_max_a
            #punto["punto"].lim_hobst_conc_a
            #punto["punto"].lim_bconc_max_i
            #punto["punto"].lim_hmax_conc_i
            #punto["punto"].lim_bconc_max_a
            #punto["punto"].lim_hmax_conc_a
            #punto["punto"].lim_bobst_max_i
            #punto["punto"].lim_hobst_conc_
            #punto["punto"].lim_bobst_max_a
            #punto["punto"].lim_hobst_conc_
            #punto["punto"].lim_bconc_max_i
            #punto["punto"].lim_hmax_conc_i
            #punto["punto"].lim_bconc_max_a
            #punto["punto"].lim_hmax_conc_a
            #punto["punto"].lim_ba
            #punto["punto"].lim_ha
            #punto["punto"].lim_bi
            #punto["punto"].lim_hi
            #punto["punto"].nom_Sja1
            #punto["punto"].nom_Sji1
            #punto["punto"].nom_Sja2
            #punto["punto"].nom_Sji2
            #punto["punto"].nom_Sja1_ast
            #punto["punto"].nom_Sji1_ast
            #punto["punto"].nom_Sja2_ast
            #punto["punto"].nom_Sji2_ast
            #punto["punto"].nom_SVa1
            #punto["punto"].nom_SVi1
            #punto["punto"].nom_SVa2
            #punto["punto"].nom_SVi2
            #punto["punto"].nom_SVa1_ast
            #punto["punto"].nom_SVi1_ast
            #punto["punto"].nom_SVa2_ast
            #punto["punto"].nom_SVi2_ast
            #punto["punto"].nom_bobst_max_i
            #punto["punto"].nom_hobst_conc_i
            #punto["punto"].nom_bobst_max_a
            #punto["punto"].nom_hobst_conc_a
            #punto["punto"].nom_bconc_max_i
            #punto["punto"].nom_hmax_conc_i
            #punto["punto"].nom_bconc_max_a
            #punto["punto"].nom_hmax_conc_a
            #punto["punto"].nom_bobst_max_i
            #punto["punto"].nom_hobst_conc_
            #punto["punto"].nom_bobst_max_a
            #punto["punto"].nom_hobst_conc_
            #punto["punto"].nom_bconc_max_i
            #punto["punto"].nom_hmax_conc_i
            #punto["punto"].nom_bconc_max_a
            #punto["punto"].nom_hmax_conc_a
            #punto["punto"].nom_ba
            #punto["punto"].nom_ha
            #punto["punto"].nom_bi
            #punto["punto"].nom_hi
            #punto["punto"].


            punto["punto"].M3h = var.M3h


            var.punto.X = punto['x']
            tabla_01_X.controls.append(ft.Text(punto["x"],size=10))
            var.punto.Y = punto['y']
            tabla_02_Y.controls.append(ft.Text(punto["y"],size=10))
            tabla_03_esPT.controls.append(ft.Text(punto["punto"].esPT,size=10))
            tabla_04_k.controls.append(ft.Text(punto["punto"].k,size=10))
            tabla_05_s0.controls.append(ft.Text(punto["punto"].s0,size=10))
            tabla_06_Sa.controls.append(ft.Text(punto["punto"].Sa,size=10))
            tabla_07_Si.controls.append(ft.Text(punto["punto"].Si,size=10))
            tabla_08_qsDai.controls.append(ft.Text(punto["punto"].qsDai,size=10))
            tabla_09_qsIai.controls.append(ft.Text(punto["punto"].qsIai,size=10))

            datos_grafico_GPA.data_points.append(ft.LineChartDataPoint(var.punto.X, var.punto.Y))

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

    #COMPONENTES DE TABLAS
    tabla_00_Punto = ft.Column([],col=1)
    tabla_01_X = ft.Column([],col=1)
    tabla_02_Y = ft.Column([],col=1)
    tabla_03_esPT = ft.Column([],col=1)
    tabla_04_k = ft.Column([],col=1)
    tabla_05_s0 = ft.Column([],col=1)
    tabla_06_Sa = ft.Column([],col=1)
    tabla_07_Si = ft.Column([],col=1)
    tabla_08_qsDai = ft.Column([],col=1)
    tabla_09_qsIai = ft.Column([],col=1)
    tabla_10_Tvia_ai = ft.Column([],col=1)
    tabla_11_Dbgai = ft.Column([],col=1)
    tabla_12_Dbcai = ft.Column([],col=1)
    tabla_13_Dbsuspai = ft.Column([],col=1)
    tabla_14_Dbcargaai = ft.Column([],col=1)
    tabla_15_Dbetaai = ft.Column([],col=1)
    tabla_16_aosca = ft.Column([],col=1)
    tabla_17_aosci = ft.Column([],col=1)
    tabla_18_Dbosca = ft.Column([],col=1)
    tabla_19_Dbosci = ft.Column([],col=1)
    tabla_20_M3h = ft.Column([],col=1)


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
    tabla = ft.ResponsiveRow([
        tabla_00_Punto,
        tabla_01_X,
        tabla_02_Y,
        tabla_03_esPT,
        tabla_04_k,
        tabla_05_s0,
        tabla_06_Sa,
        tabla_07_Si,
        tabla_08_qsDai,
        tabla_09_qsIai,
        tabla_10_Tvia_ai,
        tabla_11_Dbgai,
        tabla_12_Dbcai,
        tabla_13_Dbsuspai,
        tabla_14_Dbcargaai,
        tabla_15_Dbetaai,
        tabla_16_aosca,
        tabla_17_aosci,
        tabla_18_Dbosca,
        tabla_19_Dbosci,
        tabla_20_M3h,

    ],
    columns=30)

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
                        selected_index=0,
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