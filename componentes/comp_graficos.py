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
datos_grafico_2_GPA = Datos_Grafico(ft.colors.BLUE_GREY, 3)

'''datos_grafico_GPA = ft.LineChartData(
    data_points=[],
    stroke_width=3,
    color=ft.colors.CYAN,
    curved=False,
    stroke_cap_round=True,
)
'''
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
    datos_grafico_1_GPA,
    datos_grafico_2_GPA,
    datos_grafico_GPB,
    datos_grafico_GPA_lim,
    datos_grafico_GPA_nom,
]
