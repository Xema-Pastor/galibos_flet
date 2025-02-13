import flet as ft
#from estilos.estilos import Colores

class Datos_Grafico(ft.LineChartData):
    def __init__(self, color, grosor):
        super().__init__()
        self.data_points = []
        self.stroke_width = grosor
        self.color = color
        self.curved = False
        self.stroke_cap_round = True

datos_grafico_1_GPA = Datos_Grafico(ft.colors.CYAN, 3)
datos_grafico_2_GPA = Datos_Grafico(ft.colors.CYAN_300, 2)
datos_grafico_1_GPB = Datos_Grafico(ft.colors.BLUE, 3)
datos_grafico_2_GPB = Datos_Grafico(ft.colors.BLUE_300, 2)
datos_grafico_1_Pant_ref = Datos_Grafico(ft.colors.BLUE_300, 3)
datos_grafico_2_Pant_ref = Datos_Grafico(ft.colors.BLUE_300, 2)
datos_grafico_1_Pant_mec = Datos_Grafico(ft.colors.BLUE_300, 3)
datos_grafico_2_Pant_mec = Datos_Grafico(ft.colors.BLUE_300, 2)
datos_grafico_1_Pant_elec = Datos_Grafico(ft.colors.BLUE_300, 3)
datos_grafico_2_Pant_elec = Datos_Grafico(ft.colors.BLUE_300, 2)
datos_grafico_1_GPA_lim = Datos_Grafico(ft.colors.YELLOW, 3)
datos_grafico_2_GPA_lim = Datos_Grafico(ft.colors.YELLOW_300, 2)
datos_grafico_1_GPA_nom = Datos_Grafico(ft.colors.RED, 3)
datos_grafico_2_GPA_nom = Datos_Grafico(ft.colors.RED_300, 2)

datos_grafico = [
    datos_grafico_1_GPA,
    datos_grafico_2_GPA,
    datos_grafico_1_GPB,
    datos_grafico_2_GPB,
    datos_grafico_1_Pant_ref,
    datos_grafico_2_Pant_ref,
    datos_grafico_1_Pant_mec,
    datos_grafico_2_Pant_mec,
    datos_grafico_1_Pant_elec,
    datos_grafico_2_Pant_elec,
    datos_grafico_1_GPA_lim,
    datos_grafico_2_GPA_lim,
    datos_grafico_1_GPA_nom,
    datos_grafico_2_GPA_nom,
]

ft_grafico = ft.LineChart(
    data_series=datos_grafico,
    border=ft.border.all(3, ft.colors.with_opacity(0.2, ft.colors.ON_SURFACE)),
    horizontal_grid_lines=ft.ChartGridLines(
        interval=100, color=ft.colors.with_opacity(0.2, ft.colors.ON_SURFACE), width=1, dash_pattern=[1, 2]
    ),
    vertical_grid_lines=ft.ChartGridLines(
        interval=100, color=ft.colors.with_opacity(0.2, ft.colors.ON_SURFACE), width=1, dash_pattern=[1, 2]
    ),
    top_axis=ft.ChartAxis(
        show_labels = False,
        labels=[],
        labels_size=40,
        title = ft.Container(
                    ft.Text(
                        "               DETERMINACION DE GÁLIBOS SEGÚN LA INSTRUCCIÓN FERROVIARIA (Orden FOM/1630/2015)",
                        size=12,
                        weight=ft.FontWeight.BOLD,
                        color=ft.colors.WHITE,
                    ),
                    #margin=ft.margin.only(top=10),
                ),
        title_size = 20
    ),
    left_axis=ft.ChartAxis(
        show_labels = True,
        labels=[
                ft.ChartAxisLabel(value=-2000, label=ft.Text("-2.0m", size=10,),),
                ft.ChartAxisLabel(value=-1500, label=ft.Text("-1.5m", size=10,),),
                ft.ChartAxisLabel(value=-1000, label=ft.Text("-1.0m", size=10,),),
                ft.ChartAxisLabel(value=-500, label=ft.Text("-0.5m", size=10,),),
                ft.ChartAxisLabel(value=0, label=ft.Text("0.0m", size=10,),),
                ft.ChartAxisLabel(value=500, label=ft.Text("0.5m", size=10,),),
                ft.ChartAxisLabel(value=1000, label=ft.Text("1.0m", size=10,),),
                ft.ChartAxisLabel(value=1500, label=ft.Text("1.5m", size=10,),),
                ft.ChartAxisLabel(value=2000, label=ft.Text("2.0m", size=10,),),
                ft.ChartAxisLabel(value=2500, label=ft.Text("2.5m", size=10,),),
                ft.ChartAxisLabel(value=3000, label=ft.Text("3.0m", size=10,),),
                ft.ChartAxisLabel(value=3500, label=ft.Text("3.5m", size=10,),),
                ft.ChartAxisLabel(value=4000, label=ft.Text("4.0m", size=10,),),
                ft.ChartAxisLabel(value=4500, label=ft.Text("4.5m", size=10,),),
                ft.ChartAxisLabel(value=5000, label=ft.Text("5.0m", size=10,),),
                ft.ChartAxisLabel(value=5500, label=ft.Text("5.5m", size=10,),),
        ],
        labels_size=40,
        title = ft.Container(
                    ft.Text(
                        "Y",
                        size=15,
                        weight=ft.FontWeight.BOLD,
                        color=ft.colors.with_opacity(0.5, ft.colors.ON_SURFACE),
                    ),
                    #margin=ft.margin.only(top=10),
                ),
        title_size = 20
    ),
    bottom_axis=ft.ChartAxis(
        show_labels = True,
        labels=[
                ft.ChartAxisLabel(value=-2000, label=ft.Text("-2.0m", size=10,),),
                ft.ChartAxisLabel(value=-1500, label=ft.Text("-1.5m", size=10,),),
                ft.ChartAxisLabel(value=-1000, label=ft.Text("-1.0m", size=10,),),
                ft.ChartAxisLabel(value=-500, label=ft.Text("-0.5m", size=10,),),
                ft.ChartAxisLabel(value=0, label=ft.Text("0.0m", size=10,),),
                ft.ChartAxisLabel(value=500, label=ft.Text("0.5m", size=10,),),
                ft.ChartAxisLabel(value=1000, label=ft.Text("1.0m", size=10,),),
                ft.ChartAxisLabel(value=1500, label=ft.Text("1.5m", size=10,),),
                ft.ChartAxisLabel(value=2000, label=ft.Text("2.0m", size=10,),),
                ft.ChartAxisLabel(value=2500, label=ft.Text("2.5m", size=10,),),
                ft.ChartAxisLabel(value=3000, label=ft.Text("3.0m", size=10,),),
                ft.ChartAxisLabel(value=3500, label=ft.Text("3.5m", size=10,),),
                ft.ChartAxisLabel(value=4000, label=ft.Text("4.0m", size=10,),),
                ft.ChartAxisLabel(value=4500, label=ft.Text("4.5m", size=10,),),
                ft.ChartAxisLabel(value=5000, label=ft.Text("5.0m", size=10,),),
                ft.ChartAxisLabel(value=5500, label=ft.Text("5.5m", size=10,),),
                ],
        labels_size=20,
        title = ft.Container(
                    ft.Text(
                        "X",
                        size=15,
                        weight=ft.FontWeight.BOLD,
                        color=ft.colors.with_opacity(0.5, ft.colors.ON_SURFACE),
                    ),
                    #margin=ft.margin.only(top=10),
                ),
        title_size = 20,
    ),
    tooltip_bgcolor=ft.colors.with_opacity(0.8, ft.colors.BLUE_GREY),
    min_y=-500,
    max_y=2000,
    min_x=-2000,
    max_x=2000,
    animate = 0,
    #expand=True,
    height=425,
    width=650,
)
