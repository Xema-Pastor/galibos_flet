import threading

import flet as ft

import configuracion as conf
from calculos.calculo_via import calcular_via
from componentes.comp_acerca import contenido_acerca
from componentes.comp_entradas import EntradasVia
from componentes.comp_graficos import Grafico, transformar
from componentes.comp_tablas import TablasVia
from componentes.mis_componentes import MiEtiquetaPestanya
from datos_variables import Via
from estilos.estilos import PEST_TAB

# Pestañas de resultados de cada vía: prefijo de PEST_TAB -> atributo de TablasVia
PESTANYAS_RESULTADOS = {
    "VAR_VIA": "variables",
    "DESP_VIA": "desplazamientos",
    "GAL_LIM": "limite",
    "GAL_NOM": "nominal",
    "PANT": "pantografo",
}

# Series del gráfico: clave -> (contorno del resultado, atributo X, atributo Y)
SERIES_GRAFICO = {
    "GPA": ("galiboPA", "X", "Y"),
    "GPA_lim": ("galiboPA", "lim_bi", "lim_hi"),
    "GPA_nom": ("galiboPA", "nom_bi", "nom_hi"),
    "GPB": ("galiboPB", "X", "Y"),
    "Pant_ref": ("galiboPant", "X_ref", "Y_ref"),
    "Pant_mec": ("galiboPant", "X_mec", "Y_mec"),
    "Pant_elec": ("galiboPant", "X_elec", "Y_elec"),
}


class SesionVia:
    """Datos, controles y resultados de una vía. Cada sesión (pestaña del navegador) tiene los suyos."""

    def __init__(self, numero: int, al_cambiar):
        self.numero = numero
        self.via = Via()
        self.entradas = EntradasVia(al_cambiar, es_via2=numero == 2)
        self.tablas = TablasVia()
        self.resultado = None

    def recalcular(self) -> None:
        # Si algún dato no es válido se conserva el último resultado y el campo muestra el error
        if self.entradas.leer(self.via):
            self.resultado = calcular_via(self.via)
            self.tablas.actualizar(self.via, self.resultado)


def galibos(page: ft.Page):

    page.title = "Determinación de gálibos de material rodante de acuerdo a la Orden FOM/1630/2015 "
    page.window.height = 600
    page.window.width = 1800

    bloqueo = threading.Lock()      # Protege `estado`; ver cambiar()
    estado = {"calculando": False, "pendiente": False}
    aviso = ft.SnackBar(ft.Text(""))   # Se reutiliza para no acumular controles en la página

    def avisar(texto: str):
        aviso.content.value = texto
        page.open(aviso)

    def generar_DXF(e):

        lista_puntos = []

        if ft_dxf.value[-1] == "1":
            galibo = vias[1].resultado.galiboPA
        if ft_dxf.value[-1] == "2":
            galibo = vias[2].resultado.galiboPA

        if "Referencia" in ft_dxf.value:
            for nombre,punto in galibo.items():
                lista_puntos.append((punto.X/1000, punto.Y/1000))

        if "Limite" in ft_dxf.value:
            for nombre,punto in galibo.items():
                lista_puntos.append((punto.lim_ba/1000, punto.lim_ha/1000))

        if "Nominal" in ft_dxf.value:
            for nombre,punto in galibo.items():
                lista_puntos.append((punto.nom_ba/1000, punto.nom_ha/1000))

        def write_dxf(filename, point_list):

            with open(filename, "w") as f:
                f.write("0\nSECTION\n2\nHEADER\n0\nENDSEC\n")
                f.write("0\nSECTION\n2\nTABLES\n0\nENDSEC\n")
                f.write("0\nSECTION\n2\nBLOCKS\n0\nENDSEC\n")
                f.write("0\nSECTION\n2\nENTITIES\n")

                # Start polyline
                f.write("0\nPOLYLINE\n8\nPolylineLayer\n66\n1\n")

                # Write points as VERTEX entries
                for x, y in point_list:
                    f.write(f"0\nVERTEX\n8\nPolylineLayer\n10\n{x}\n20\n{y}\n30\n0.0\n")

                # End polyline
                f.write("0\nSEQEND\n")

                # DXF Footer
                f.write("0\nENDSEC\n0\nEOF\n")

        file_path = "c:/Autodesk/nomsalida.dxf"
        write_dxf(file_path, lista_puntos)

    def copiar_portapapeles(e):
        titulo = e.control.data
        page.set_clipboard(tablas_pestanya[titulo].texto(titulo))
        avisar(f"Copiado al portapapeles: {titulo}")

    def via2_activa() -> bool:
        return bool(cb_via2.value)

    def dibujar():
        sep_h, sep_v = vias[2].entradas.separacion()
        dx = sep_h * 1000 / conf.ESCALA_GRAFICO
        dy = sep_v * 1000 / conf.ESCALA_GRAFICO

        for n, sesion in vias.items():
            if sesion.resultado is None or (n == 2 and not via2_activa()):
                grafico.ocultar_via(n)
                continue
            desplazamiento = (0, 0) if n == 1 else (dx, dy)
            visible = sesion.entradas.visibilidad()
            for clave, (contorno, ax, ay) in SERIES_GRAFICO.items():
                puntos = []
                for nombre, punto in getattr(sesion.resultado, contorno).items():
                    x, y = getattr(punto, ax), getattr(punto, ay)
                    puntos.append((*transformar(x, y, sesion.via.Inclinac, *desplazamiento), f"{nombre}\nx={x}\ny={y}"))
                grafico.fijar_serie(n, clave, puntos, visible[clave])

        if via2_activa():
            grafico.ajustar_limites(dx, dy)
        else:
            grafico.ajustar_limites()

    def recalcular_todo():
        vias[1].entradas.habilitar(True)
        vias[2].entradas.habilitar(via2_activa())
        try:
            vias[1].recalcular()
            if via2_activa():
                vias[2].recalcular()
            dibujar()
        except Exception as ex:      # Sin esto FLET descarta el error y la interfaz deja de refrescarse
            avisar(f"Error en el cálculo: {ex}")
        page.update()

    def cambiar(e=None):
        # Los eventos se atienden en hilos. Solo un hilo calcula a la vez; los eventos que llegan
        # mientras tanto no esperan en cola: marcan "pendiente" y el hilo que calcula repite
        # una única vez al terminar. Así se agrupan las ráfagas de eventos y no se agotan los hilos.
        with bloqueo:
            if estado["calculando"]:
                estado["pendiente"] = True
                return
            estado["calculando"] = True
        try:
            while True:
                with bloqueo:
                    estado["pendiente"] = False
                recalcular_todo()
                with bloqueo:
                    if not estado["pendiente"]:
                        estado["calculando"] = False
                        return
        except BaseException:
            with bloqueo:
                estado["calculando"] = False
            raise

    vias = {1: SesionVia(1, cambiar), 2: SesionVia(2, cambiar)}
    grafico = Grafico()
    cb_via2 = ft.Checkbox(value = False, on_change=cambiar)

    ft_dxf = ft.RadioGroup(
        content = ft.Column([
            ft.Radio(value = "Referencia_1", label = "Contorno de referencia via 1"),
            ft.Radio(value = "Limite_1", label = "Gálibo límite vía 1"),
            ft.Radio(value = "Nominal_1", label = "Gálibo nominal vía 1"),
            ft.Radio(value = "Referencia_2", label = "Contorno de referencia via 2"),
            ft.Radio(value = "Limite_2", label = "Gálibo límite vía 2"),
            ft.Radio(value = "Nominal_2", label = "Gálibo nominal vía 2"),
        ])
    )

    # Pestañas de resultados (tablas) de las dos vías
    tablas_pestanya = {}
    pestanyas_resultados = []
    for n, sesion in vias.items():
        for prefijo, attr in PESTANYAS_RESULTADOS.items():
            titulo = PEST_TAB[f"{prefijo}_{n}"].value
            tabla = getattr(sesion.tablas, attr)
            tablas_pestanya[titulo] = tabla
            pestanyas_resultados.append(ft.Tab(tab_content=MiEtiquetaPestanya(titulo, copiar_portapapeles), content=tabla))

    page.add(
        ft.Column([
            ft.ResponsiveRow([
                ft.Column(
                    col=4,
                    controls = [grafico],
                    ),
                ft.Column(
                    col=8,
                    controls = [ft.Tabs(
                        selected_index = 0,
                        animation_duration = 50,
                        tabs = [
                            ft.Tab(text = "Vía 1", content = vias[1].entradas.contenido()),
                            ft.Tab(tab_content=ft.Row([cb_via2, ft.Text("Vía 2")]), content = vias[2].entradas.contenido()),
                            ft.Tab(
                                text = "DXF",
                                content = ft.Column(
                                    controls = [
                                        ft.Column([
                                            ft.OutlinedButton("Exportar a DXF", icon=ft.icons.DOWNLOAD, on_click=generar_DXF,
                                                style=ft.ButtonStyle(bgcolor=ft.colors.with_opacity(0.15, ft.colors.GREY), side=ft.BorderSide(1, ft.colors.GREY_500))),
                                            ft_dxf,
                                        ]),
                                    ],
                                expand=1),
                            ),
                            ft.Tab(text = "?", content = contenido_acerca()),
                        ],
                    ),
                ],
                height=425,),
            ]),
            ft.Tabs(
                selected_index=0,
                animation_duration=50,
                tabs=pestanyas_resultados,
                expand = 0
            ),
        ])
    )

    cambiar()       # Primer cálculo con los valores por defecto


ft.app(galibos, assets_dir="assets")
