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
datos_grafico_1_GPA_lim = Datos_Grafico(ft.colors.YELLOW, 3)
datos_grafico_2_GPA_lim = Datos_Grafico(ft.colors.YELLOW_300, 2)
datos_grafico_1_GPA_nom = Datos_Grafico(ft.colors.RED, 3)
datos_grafico_2_GPA_nom = Datos_Grafico(ft.colors.RED_300, 2)

datos_grafico = [
    datos_grafico_1_GPA,
    datos_grafico_2_GPA,
    datos_grafico_1_GPB,
    datos_grafico_2_GPB,
    datos_grafico_1_GPA_lim,
    datos_grafico_2_GPA_lim,
    datos_grafico_1_GPA_nom,
    datos_grafico_2_GPA_nom,
]

ft_grafico = ft.LineChart(
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
)
