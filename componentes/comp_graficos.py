from math import sin, cos, radians

import flet as ft

from configuracion import ESCALA_GRAFICO

# Series del gráfico: clave -> (color vía 1, color vía 2, grosor vía 1, grosor vía 2, discontinua)
SERIES = {
    "GPA": (ft.colors.CYAN, ft.colors.CYAN_300, 3, 2, True),
    "GPB": (ft.colors.BLUE, ft.colors.BLUE_300, 3, 2, True),
    "Pant_ref": (ft.colors.BLUE, ft.colors.BLUE_300, 2, 1, True),
    "Pant_mec": (ft.colors.GREEN, ft.colors.GREEN_300, 2, 1, False),
    "Pant_elec": (ft.colors.YELLOW, ft.colors.YELLOW_300, 2, 1, False),
    "GPA_lim": (ft.colors.ORANGE, ft.colors.ORANGE_300, 3, 2, False),
    "GPA_nom": (ft.colors.RED, ft.colors.RED_300, 3, 2, False),
}

TITULO = "DETERMINACION DE GÁLIBOS SEGÚN LA INSTRUCCIÓN FERROVIARIA (Orden FOM/1630/2015)"
MAX_X, MIN_X, MAX_Y, MIN_Y = 2000, -2000, 2500, -250


class Datos_Grafico(ft.LineChartData):
    def __init__(self, color, grosor, dash_pattern = [1, 0]):
        super().__init__()
        self.data_points = []
        self.stroke_width = grosor
        self.color = color
        self.curved = False
        self.stroke_cap_round = True
        self.dash_pattern = dash_pattern


def transformar(x: float, y: float, inclinacion: float, dx: float = 0, dy: float = 0) -> tuple:
    """Pasa de coordenadas de la vía (mm) a coordenadas del gráfico, girando según el peralte."""
    c, s = cos(radians(inclinacion)), sin(radians(inclinacion))
    x, y = x / ESCALA_GRAFICO, y / ESCALA_GRAFICO
    return c * x + s * y + dx, -s * x + c * y + dy


def _etiquetas() -> list:
    return [ft.ChartAxisLabel(value=v, label=ft.Text(f"{v / 1000 * ESCALA_GRAFICO:.1f}m", size=10))
            for v in range(-2000, 5501, 500)]


def _titulo_eje(texto: str, **kwargs) -> ft.Container:
    return ft.Container(ft.Text(texto, weight=ft.FontWeight.BOLD, **kwargs))


class Grafico(ft.LineChart):
    def __init__(self):
        super().__init__()
        self.series = {}
        for via in (1, 2):
            for clave, (color1, color2, grosor1, grosor2, discontinua) in SERIES.items():
                color, grosor = (color1, grosor1) if via == 1 else (color2, grosor2)
                self.series[(via, clave)] = Datos_Grafico(color, grosor, [10, 5] if discontinua else [1, 0])
        self.data_series = list(self.series.values())

        cuadricula = dict(interval=100, color=ft.colors.with_opacity(0.2, ft.colors.ON_SURFACE), width=1, dash_pattern=[1, 2])
        color_eje = ft.colors.with_opacity(0.5, ft.colors.ON_SURFACE)
        self.border = ft.border.all(3, ft.colors.with_opacity(0.2, ft.colors.ON_SURFACE))
        self.horizontal_grid_lines = ft.ChartGridLines(**cuadricula)
        self.vertical_grid_lines = ft.ChartGridLines(**cuadricula)
        self.top_axis = ft.ChartAxis(show_labels=False, labels=[], labels_size=40, title_size=20,
                                     title=_titulo_eje(TITULO, size=12, color=ft.colors.WHITE))
        self.left_axis = ft.ChartAxis(labels=_etiquetas(), labels_size=40, title_size=20,
                                      title=_titulo_eje("Y", size=15, color=color_eje))
        self.bottom_axis = ft.ChartAxis(labels=_etiquetas(), labels_size=20, title_size=20,
                                        title=_titulo_eje("X", size=15, color=color_eje))
        self.tooltip_bgcolor = ft.colors.with_opacity(0.8, ft.colors.BLUE_GREY)
        self.tooltip_fit_inside_horizontally = True
        self.min_x, self.max_x, self.min_y, self.max_y = MIN_X, MAX_X, MIN_Y, MAX_Y
        self.animate = 0
        self.height = 425
        self.width = 650

    def fijar_serie(self, via: int, clave: str, puntos: list, visible: bool = True) -> None:
        """Actualiza una serie con [(x, y, tooltip)]. Reutiliza los puntos existentes si es posible."""
        serie = self.series[(via, clave)]
        serie.visible = visible
        if len(serie.data_points) != len(puntos):
            serie.data_points = [ft.LineChartDataPoint(x, y, tooltip=t) for x, y, t in puntos]
            return
        for punto, (x, y, t) in zip(serie.data_points, puntos):
            punto.x, punto.y, punto.tooltip = x, y, t

    def ocultar_via(self, via: int) -> None:
        for clave in SERIES:
            self.series[(via, clave)].visible = False

    def ajustar_limites(self, separacion_h: float = 0, separacion_v: float = 0) -> None:
        self.max_x = MAX_X + max(0, separacion_h)
        self.max_y = MAX_Y + max(0, separacion_v)
