import flet as ft

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
