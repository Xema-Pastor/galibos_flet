import flet as ft
from datos_galibos import datos_GPA, datos_GPB
from datos_variables import Variables as var
from estilos.estilos import Tamanyos

def galibos(page: ft.Page):

    #FUNCIÓN
    def cambiar(e):
        var.GPA = dd_GPA.value
        var.GPB = dd_GPB.value
        galiboPA = datos_GPA[var.GPA]
        galiboPB = datos_GPB[var.GPB]
        match var.GPA:
            case "GEA16" | "GEB16": var.hquiebroaux = 3.32
            case "GA" | "GB": var.hquiebroaux = 3.35
            case other: var.hquiebroaux = 0
        match var.GPA:
            case "GEA16": var.htopeaux = 3.7
            case "GEB16" | "GB": var.htopeaux = 4.11
            case "GA": var.htopeaux = 3.88
            case other: var.htopeaux = 0
        match var.GPA:
            case "GEA16": var.difaux = 0.38
            case "GEB16": var.difaux = 0.79
            case "GA": var.difaux = 0.63
            case "GB": var.difaux = 0.86
            case other: var.difaux = 0
        match var.GPA:
            case "GEA16": var.difaux = 4.84
            case "GEB16": var.difaux = 6.48
            case "GA": var.difaux = 5.77
            case "GB": var.difaux = 6.69
            case other: var.difaux = 0
        match var.GPA:
            case "GHE16" | "GEA16" | "GEB16" | "GEC16": var.LN = 1.668
            case "GA" | "GB" | "GC": var.LN = 1.435
            case "GEE10" | "GED10" | "PERSONALIZADO": var.LN = 1
        #CALCULAR hb_max, CELDA I9
        es_recta = cb_R.value
        es_recta_V = cb_RV.value
        var.R = 99999999999 if es_recta else tf_R.value
        var.Rv = 99999999999 if es_recta_V else tf_RV.value
        tf_R.disabled = es_recta
        tf_RV.disabled = es_recta_V
        var.DL = tf_DL.value
        var.LND = var.LN + var.DL
        var.D = float(tf_D.value)
        match var.GPA:
            case "GHE16" | "GEA16" | "GEB16" | "GEC16" | "GA" | "GB" | "GC": var.D0 = 0.05
            case "GEE10" | "GED10" | "PERSONALIZADO": var.D0 = 0.07
        var.vmax = tf_vmax.value
        var.heq = (float(var.vmax) / 3.6)**2 * var.LN / (float(var.R) * 9.81)
        var.I = var.heq - var.D
        match var.GPA:
            case "GHE16" | "GEA16" | "GEB16" | "GEC16" | "GA" | "GB" | "GC": var.I0 = 0.05
            case "GEE10" | "GED10" | "PERSONALIZADO": var.I0 = 0.07
        match var.GPA:
            case "GHE16" | "GEA16" | "GEB16" | "GEC16": var.L = 1.733
            case "GA" | "GB" | "GC": var.L = 1.5
            case "GEE10" | "GED10" | "PERSONALIZADO": var.L = 1.055
        var.hco = 0.5
        var.tipo_via = dd_TV.value
        match var.tipo_via:
            case "Vía en placa":
                var.TVIA = 0.005
                var.TD = 0.015
            case "Balasto":
                var.TVIA = 0.025
                var.TD = 0.02 if int(var.vmax) <=80 else 0.015
        var.asusp = tf_tol_sus.value
        var.acarga = tf_tol_carga.value
        var.h0 = float(var.asusp) + float(var.acarga)
        var.estado_via = dd_EV.value
        if var.GPA in ["GEE10", "GED10", "PERSONALIZADO"]:
            var.aosc_i_s0_04b = 0.20 if var.tipo_via == "Balasto" else 0.1
            var.aosc_a_s0_04b = 1.00 if var.tipo_via == "Balasto" else 0.6
            var.aosc_i_s0_03b = 0.20 if var.tipo_via == "Balasto" else 0.1
            var.aosc_a_s0_03b = 1.00 if var.tipo_via == "Balasto" else 0.6
        elif var.GPA in ["GHE16", "GEA16", "GEB16", "GEC16", "GA", "GB", "GC"]:
            if var.tipo_via == "Via en placa":
                var.aosc_i_s0_04b = 0.1
                var.aosc_a_s0_04b = 0.6
                var.aosc_i_s0_03b = 0.08
                var.aosc_a_s0_03b = 0.45
            elif var.tipo_via == "Balasto":
                if var.estado_via == "Buen estado":
                    var.aosc_i_s0_04b = 0.1
                    var.aosc_a_s0_04b = 0.6
                    var.aosc_i_s0_03b = 0.08
                    var.aosc_a_s0_03b = 0.45
                elif var.estado == "Mal estado":
                    var.aosc_i_s0_04b = 0.2
                    var.aosc_a_s0_04b = 1.0
                    var.aosc_i_s0_03b = 0.15
                    var.aosc_a_s0_03b = 0.75


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

        tabla_00_Punto.controls.clear()
        tabla_00_Punto.controls.append(ft.Text("Punto"))
        tabla_01_X.controls.clear()
        tabla_01_X.controls.append(ft.Text("X(mm)"))
        tabla_02_Y.controls.clear()
        tabla_02_Y.controls.append(ft.Text("Y(mm)"))
        tabla_03_esPT.controls.clear()
        tabla_03_esPT.controls.append(ft.Text("esPT"))
        tabla_04_k.controls.clear()
        tabla_04_k.controls.append(ft.Text("k"))
        tabla_05_s0.controls.clear()
        tabla_05_s0.controls.append(ft.Text("s0"))
        tabla_06_Sa.controls.clear()
        tabla_06_Sa.controls.append(ft.Text("Sa"))
        tabla_07_Si.controls.clear()
        tabla_07_Si.controls.append(ft.Text("Sa"))
        tabla_08_qsDai.controls.clear()
        tabla_08_qsDai.controls.append(ft.Text("qsD,ai"))
        tabla_09_qsIai.controls.clear()
        tabla_09_qsIai.controls.append(ft.Text("qsI,ai"))
        tabla_10_Tvia_ai.controls.clear()
        tabla_10_Tvia_ai.controls.append(ft.Text("Tvia,ai"))

        datos_grafico_GPA.data_points.clear()
        datos_grafico_GPB.data_points.clear()

        for nombre,punto in galiboPA.items():
            tabla_00_Punto.controls.append(ft.Text(nombre))
            var.punto.X = punto['x']
            tabla_01_X.controls.append(ft.Text(punto["x"]))
            var.punto.Y = punto['y']
            tabla_02_Y.controls.append(ft.Text(punto["y"]))
            var.punto.esPT = punto['y']
            tabla_03_esPT.controls.append(ft.Text(punto["y"]))

            datos_grafico_GPA.data_points.append(ft.LineChartDataPoint(var.punto.X, var.punto.Y))


        print(var.LND, type(var.LND))
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
            ft.dropdown.Option("GHE16"),
            ft.dropdown.Option("GEA16"),
            ft.dropdown.Option("GEB16"),
            ft.dropdown.Option("GEC16"),
            ft.dropdown.Option("GA"),
            ft.dropdown.Option("GB"),
            ft.dropdown.Option("GC"),
            ft.dropdown.Option("GEE10"),
            ft.dropdown.Option("GED10"),
            ft.dropdown.Option("PERSONALIZADO"),
        ],
        on_change=cambiar
    )

    dd_GPB = ft.Dropdown(
        label = "Gálibo de partes bajas",
        hint_text = "Introduce el gálibo de las partes bajas",
        options = [
            ft.dropdown.Option("GEI1"),
            ft.dropdown.Option("GEI2"),
            ft.dropdown.Option("GEI3"),
            ft.dropdown.Option("GI1"),
            ft.dropdown.Option("GI2"),
            ft.dropdown.Option("GI3"),
        ],
        on_change=cambiar,
    )

    dd_TV =  ft.Dropdown(
        label = "Tipo de Vía",
        hint_text = "Balasto / Vía en placa",
        options = [
            ft.dropdown.Option("Balasto"),
            ft.dropdown.Option("Vía en placa"),
        ],
        on_change=cambiar
    )

    dd_EV = ft.Dropdown(
        label = "Estado de la Vía",
        hint_text = "Buen / Mal estado",
        options = [
            ft.dropdown.Option("Buen estado"),
            ft.dropdown.Option("Mal estado"),
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
    t_h0 = ft.Text(var.h0)
    t_estado_via = ft.Text(var.estado_via)
    t_aosc_i_s0_04b = ft.Text(var.aosc_i_s0_04b)
    t_aosc_i_s0_03b = ft.Text(var.aosc_i_s0_03b)
    t_aosc_a_s0_04b = ft.Text(var.aosc_a_s0_04b)
    t_aosc_a_s0_04b = ft.Text(var.aosc_a_s0_03b)

    tf_R = ft.TextField(label="Radio de curvatura en planta (m)",value = 100, on_change=cambiar)
    cb_R = ft.Checkbox(value = False, on_change=cambiar)
    tf_RV = ft.TextField(label="Radio del acuerdo vertical (m)", on_change=cambiar)
    cb_RV = ft.Checkbox(value = False, on_change=cambiar)
    tf_DL = ft.TextField(label="Sobreancho máximo (m)",value=0.03,read_only=True, on_change=cambiar)
    tf_D = ft.TextField(label="Peralte de la vía (m)", value = 0, on_change=cambiar)
    tf_tol_sus = ft.TextField(label="Tolerancias en el reglaje de la suspensión (º)", value = 0.23, on_change=cambiar)
    tf_tol_carga = ft.TextField(label="Reparto desigual de cargas (º)", value = 0.77, on_change=cambiar)
    tf_vmax = ft.TextField(label="Velocidad máxima de la vía (km/h)", value=0, on_change=cambiar)

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
            t_h0,
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
    ],
    columns=18)

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

# def galibos(page: ft.Page):
#     def funcion(e):
#         print(crp.value)
#         rp.disabled = crp.value
#         rp.update()
#     page.add(ft.Container(

#     ))
#     page.add(ft.Text("DATOS DE ENTRADA"),
#              )
#     page.add(selectores.selector_galibo_partes_altas())
#     page.add(selectores.selector_galibo_partes_bajas())
#     # page.add(ft.TextField(label="Radio de curvatura en planta (m)", on_change=funcion_de_cambios_por_definir))
#     rp = ft.TextField(label="Radio de curvatura en planta (m)", on_change=funcion_de_cambios_por_definir)
#     crp = ft.Checkbox(label="Alineación recta en planta", value = False, on_change=funcion)
#     page.add(rp, crp)
#     # page.add(ft.Checkbox(label="Alineación recta en planta", value = False, on_change=funcion_de_cambios_por_definir))
#     page.add(ft.TextField(label="Radio del acuerdo vertical (m)",on_change=funcion_de_cambios_por_definir))
#     page.add(ft.Checkbox(label="Alineación recta en alzado", on_change=funcion_de_cambios_por_definir))
#     page.add(ft.TextField(label="Sobreancho máximo (m)",read_only=True, on_change=funcion_de_cambios_por_definir))
#     page.add(ft.TextField(label="Peralte de la vía (m)", on_change=funcion_de_cambios_por_definir))
#     page.add(ft.TextField(label="Velocidad máxima de la vía (km/h)", on_change=funcion_de_cambios_por_definir))
#     page.add(ft.TextField(label="Tolerancias en el reglaje de la suspensión (º)", on_change=funcion_de_cambios_por_definir))
#     page.add(ft.TextField(label="Reparto desigual de cargas (º)", on_change=funcion_de_cambios_por_definir))    

#     page.add(ft.DataTable(
#         columns=[
#             ft.DataColumn(ft.Text("Punto")),
#             ft.DataColumn(ft.Text("X (mm)"),numeric=True),
#             ft.DataColumn(ft.Text("Y (mm)"),numeric=True),   
#             ],
#         rows=rellenar_tabla(datos)
#     ))
#     page.add(ft.SafeArea(ft.Text("Hello, Fletttttthhhtt!")))

ft.app(galibos)