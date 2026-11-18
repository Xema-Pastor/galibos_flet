"""Controles de entrada de datos de una vía."""
import flet as ft

from datos_variables import Via
from estilos.estilos import Tamanyos, EGPA, EGPB, ETV, EEV, TIPO_PANT, TIPO_LINEA, TENSION_CAT, TIPO_CAT

LADOS_INCLINACION = ("A derechas", "A izquierdas")
ERROR_NUMERO = "Número no válido"


def leer_numero(campo: ft.TextField, minimo: float = None, estricto: bool = False):
    """Convierte el valor de un TextField en número (admite coma decimal).

    Devuelve None y marca el campo con un error si el valor no es válido.
    """
    texto = str(campo.value if campo.value is not None else "").strip().replace(",", ".")
    try:
        valor = float(texto)
        if minimo is not None and (valor <= minimo if estricto else valor < minimo):
            raise ValueError
    except ValueError:
        campo.error_text = ERROR_NUMERO
        return None
    campo.error_text = None
    return int(valor) if valor.is_integer() else valor


class EntradasVia:
    """Controles de entrada de una vía. `al_cambiar` se llama cada vez que cambia un dato."""

    def __init__(self, al_cambiar, es_via2: bool = False):
        d = Via()       # Valores por defecto
        self.al_cambiar = al_cambiar

        def desplegable(label, hint, opciones, valor, width=None):
            return ft.Dropdown(label=label, hint_text=hint, value=valor, width=width,
                               options=[ft.dropdown.Option(o.value) for o in opciones],
                               on_change=al_cambiar)

        def al_cambiar_texto(e):
            # on_submit y on_blur llegan los dos al pulsar Intro y salir del campo:
            # solo se recalcula si el texto ha cambiado desde la última vez (guardado en `data`)
            if e.control.value == e.control.data:
                return
            e.control.data = e.control.value
            al_cambiar(e)

        def campo(label, valor, width=None, **kwargs):
            # on_blur: en el navegador el usuario suele salir del campo sin pulsar Intro
            return ft.TextField(label=label, value=str(valor), width=width, data=str(valor),
                                on_submit=al_cambiar_texto, on_blur=al_cambiar_texto, **kwargs)

        def casilla(valor, label=None):
            return ft.Checkbox(label=label, value=valor, on_change=al_cambiar)

        self.dd_GPA = desplegable("Gálibo de partes altas", "Introduce el gálibo de las partes altas", EGPA, d.GPA)
        self.dd_GPB = desplegable("Gálibo de partes bajas", "Introduce el gálibo de las partes bajas", EGPB, d.GPB)
        self.dd_TV = desplegable("Tipo de Vía", "Balasto / Vía en placa", ETV, d.tipo_via)
        self.dd_EV = desplegable("Estado de la Vía", "Buen / Mal estado", EEV, d.estado_via)

        self.tf_R = campo("Radio de curvatura en planta (m)", d.R_entrada)
        self.cb_R = casilla(d.es_recta)
        self.tf_RV = campo("Radio del acuerdo vertical (m)", d.Rv_entrada)
        self.cb_RV = casilla(d.es_recta_V)
        self.tf_DL = campo("Sobreancho máximo (m)", d.DL, read_only=True)
        self.tf_D = campo("Peralte de la vía (m)", d.D)
        self.tf_I = campo("Insuficiencia de peralte (m)", d.I)
        self.tf_tol_sus = campo("Tolerancias en el reglaje de la suspensión (º)", d.asusp)
        self.tf_tol_carga = campo("Reparto desigual de cargas (º)", d.acarga)
        self.tf_vmax = campo("Velocidad máxima de la vía (km/h)", d.vmax)

        self.cb_graf_GPA = casilla(True, "Mostrar Gálibo superior")
        self.cb_graf_GPB = casilla(True, "Mostrar Gálibo inferior")
        self.cb_graf_GPA_lim = casilla(True, "Mostrar Gálibo límite")
        self.cb_graf_GPA_nom = casilla(True, "Mostrar Gálibo nominal")
        self.cb_graf_pant = casilla(True, "Mostrar Pantógrafos")
        self.cb_graf_esGirado = casilla(d.girado, "Girar gráfico")
        self.cb_graf_inclinacion = ft.RadioGroup(
            content=ft.Row([ft.Radio(value=lado, label=lado) for lado in LADOS_INCLINACION]),
            value=d.lado_inclinacion,
            on_change=al_cambiar,
        )

        self.tf_hpant = campo("Altura del hilo de contacto (m)", d.hf, width=150)
        self.dd_TIPOPAN = desplegable("Tipo de pantógrafo", "Introduce el tipo de pantógrafo", TIPO_PANT, d.tipo_pant, 300)
        self.dd_TIPOLIN = desplegable("Tipo de línea", "Introduce el tipo de línea", TIPO_LINEA, d.tipo_lin, 250)
        self.dd_TIPOCAT = desplegable("Tipo de catenaria", "Introduce el tipo de catenaria", TIPO_CAT, d.tipo_cat, 250)
        self.dd_TENCAT = desplegable("Tensión de la catenaria", "Introduce la tensión de la catenaria", TENSION_CAT, d.ten_cat, 300)

        self.es_via2 = es_via2
        if es_via2:
            self.tf_separacion_h = campo("Separación horizontal entre vias (m)", 4, border_color=ft.colors.AMBER)
            self.tf_separacion_v = campo("Separación vertical entre vias (m)", 0.2, border_color=ft.colors.AMBER)

        self.habilitar(not es_via2)

    # ------------------------------------------------------------------
    def controles(self) -> list:
        """Todos los controles editables."""
        lista = [
            self.dd_GPA, self.dd_GPB, self.dd_TV, self.dd_EV,
            self.tf_R, self.cb_R, self.tf_RV, self.cb_RV, self.tf_vmax,
            self.tf_DL, self.tf_D, self.tf_I, self.tf_tol_sus, self.tf_tol_carga,
            self.tf_hpant, self.dd_TIPOPAN, self.dd_TIPOLIN, self.dd_TIPOCAT, self.dd_TENCAT,
            self.cb_graf_GPA, self.cb_graf_GPB, self.cb_graf_GPA_lim, self.cb_graf_GPA_nom,
            self.cb_graf_pant, self.cb_graf_esGirado, self.cb_graf_inclinacion,
        ]
        if self.es_via2:
            lista += [self.tf_separacion_h, self.tf_separacion_v]
        return lista

    def habilitar(self, habilitado: bool) -> None:
        for control in self.controles():
            control.disabled = not habilitado
        # Controles que además dependen de una casilla
        self.tf_R.disabled = not habilitado or self.cb_R.value
        self.tf_RV.disabled = not habilitado or self.cb_RV.value
        self.cb_graf_inclinacion.disabled = not habilitado or not self.cb_graf_esGirado.value

    def leer(self, via) -> bool:
        """Vuelca los datos de los controles en `via`. Devuelve False si algún dato no es válido."""
        numeros = {
            "R_entrada": leer_numero(self.tf_R, 0, estricto=True),
            "Rv_entrada": leer_numero(self.tf_RV, 0, estricto=True),
            "DL": leer_numero(self.tf_DL),
            "D": leer_numero(self.tf_D),
            "I": leer_numero(self.tf_I),
            "asusp": leer_numero(self.tf_tol_sus),
            "acarga": leer_numero(self.tf_tol_carga),
            "vmax": leer_numero(self.tf_vmax, 0),
            "hf": leer_numero(self.tf_hpant, 0, estricto=True),
        }
        # Un radio que no se usa (alineación recta) no invalida el cálculo
        if self.cb_R.value:
            numeros["R_entrada"] = numeros["R_entrada"] or via.R_entrada
            self.tf_R.error_text = None
        if self.cb_RV.value:
            numeros["Rv_entrada"] = numeros["Rv_entrada"] or via.Rv_entrada
            self.tf_RV.error_text = None
        if any(valor is None for valor in numeros.values()):
            return False

        for attr, valor in numeros.items():
            setattr(via, attr, valor)
        via.GPA, via.GPB = self.dd_GPA.value, self.dd_GPB.value
        via.tipo_via, via.estado_via = self.dd_TV.value, self.dd_EV.value
        via.tipo_pant, via.tipo_lin = self.dd_TIPOPAN.value, self.dd_TIPOLIN.value
        via.tipo_cat, via.ten_cat = self.dd_TIPOCAT.value, self.dd_TENCAT.value
        via.es_recta, via.es_recta_V = bool(self.cb_R.value), bool(self.cb_RV.value)
        via.girado, via.lado_inclinacion = bool(self.cb_graf_esGirado.value), self.cb_graf_inclinacion.value
        return True

    def separacion(self) -> tuple:
        """Separación (h, v) en metros entre la vía 1 y la vía 2."""
        h = leer_numero(self.tf_separacion_h)
        v = leer_numero(self.tf_separacion_v)
        return (h or 0, v or 0)

    def visibilidad(self) -> dict:
        """Series del gráfico que se deben mostrar."""
        pant = bool(self.cb_graf_pant.value)
        return {
            "GPA": bool(self.cb_graf_GPA.value),
            "GPB": bool(self.cb_graf_GPB.value),
            "GPA_lim": bool(self.cb_graf_GPA_lim.value),
            "GPA_nom": bool(self.cb_graf_GPA_nom.value),
            "Pant_ref": pant,
            "Pant_mec": pant,
            "Pant_elec": pant,
        }

    # ------------------------------------------------------------------
    def contenido(self) -> ft.Column:
        """Disposición de los controles en la pestaña de la vía."""
        def texto(t):
            return ft.Text(t, size=Tamanyos.PEQUENYO.value)

        fila_tolerancias = [self.tf_tol_sus, self.tf_tol_carga]
        if self.es_via2:
            fila_tolerancias += [self.tf_separacion_h, self.tf_separacion_v]
        return ft.Column(
            controls=[
                ft.Text("", size=1),      #Espaciador, para que quede bonito
                ft.Row([self.dd_GPA, self.dd_GPB, self.dd_TV, self.dd_EV]),
                ft.Row([self.tf_R, self.cb_R, texto("Alineación recta en planta"),
                        self.tf_RV, self.cb_RV, texto("Alineación recta en alzado"), self.tf_vmax]),
                ft.Row([self.tf_DL, self.tf_D, self.tf_I]),
                ft.Row(fila_tolerancias),
                ft.Row([self.tf_hpant, self.dd_TIPOPAN, self.dd_TIPOLIN, self.dd_TIPOCAT, self.dd_TENCAT]),
                ft.Row([self.cb_graf_GPA, self.cb_graf_GPB, self.cb_graf_GPA_lim, self.cb_graf_GPA_nom, self.cb_graf_pant]),
                ft.Row([self.cb_graf_esGirado, self.cb_graf_inclinacion]),
            ],
            expand=1,
        )
