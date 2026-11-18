"""Tablas de resultados.

Cada tabla se define mediante una lista de columnas (`Columna`). A partir de esa lista se
construyen los controles de FLET, se refrescan los valores y se genera el texto que se copia
al portapapeles, de modo que añadir una variable solo requiere añadir una línea aquí.

Para que la interfaz web se refresque con rapidez, las celdas se crean una sola vez y en
cada recálculo únicamente se cambia su valor: FLET envía al navegador solo los cambios.
"""
from dataclasses import dataclass

import flet as ft

from componentes.mis_componentes import MiColumnaTabla, MiText, MiFilaDatos2
from datos_galibos import dic_datos_via
from estilos.estilos import Tamanyos


@dataclass(frozen=True)
class Columna:
    attr: str           # Atributo del punto ("nombre" para el identificador del punto)
    simbolo: str        # Símbolo principal de la cabecera
    subindice: str      # Subíndice de la cabecera
    unidades: str


def formatear(valor) -> str:
    if valor is None:
        return "-"
    if isinstance(valor, bool):
        return "S" if valor else "N"
    return str(valor)


def _cols(unidades: str, *definiciones) -> list:
    return [Columna(attr, simbolo, sub, unidades) for attr, simbolo, sub in definiciones]


# ---------------------------------------------------------------------------
# Definición de columnas
# ---------------------------------------------------------------------------
COLS_PUNTO = [Columna("nombre", "Punto", "", "()")] + _cols("(mm)", ("X", "X", ""), ("Y", "Y", ""))

COLS_DESPLAZAMIENTOS = COLS_PUNTO + [
    Columna("esPT", "esPT", "", "(S/N)"),
    Columna("k", "k", "", "()"),
    Columna("s0", "s", "0", "()"),
] + _cols("(mm)",
    ("Sa", "S", "a"), ("Si", "S", "i"),
    ("qsD_ai", "qs", "D,ai"), ("qsI_ai", "qs", "I,ai"),
    ("Tvia_ai", "T", "via,ai"),
    ("Dbg_ai", "Δb", "g,ai"), ("Dbc_ai", "Δb", "c,ai"), ("Dbsusp_ai", "Δb", "susp,ai"),
    ("Dbcarg_ai", "Δb", "carg,ai"), ("Dbeta0_ai", "Δb", "η,ai"),
) + _cols("(º)", ("aosc_a", "α", "osc,a"), ("aosc_i", "α", "osc,i")) + _cols("(mm)",
    ("Dbosc_a", "Δb", "osc,a"), ("Dbosc_i", "Δb", "osc,i"),
    ("M3b", "M", "3b"), ("DhRv", "Δh", "Rv"),
    ("DhPT_D_ai", "Δh", "PT,D,ai"), ("DhPT_I_ai", "Δh", "PT,I,ai"),
    ("TN", "T", "N"),
    ("Dhg_a", "Δh", "g,a"), ("Dhg_i", "Δh", "g,i"), ("Dhc", "Δh", "c"),
    ("Dhgca", "Δh", "g,ca"), ("Dhgci", "Δh", "g,ci"),
    ("Dhsusp_ai", "Δh", "susp,ai"), ("Dhcarg_ai", "Δh", "carg,ai"), ("Dheta0_ai", "Δh", "η,ai"),
    ("Dhosc_a", "Δh", "osc,a"), ("Dhosc_i", "Δh", "osc,i"),
    ("M3h", "M", "3h"),
)


def _cols_galibo(prefijo: str, n1: int, n2: int) -> list:
    """Columnas comunes a los gálibos límite (Σ1, Σ2) y nominal (Σ3, Σ4)."""
    aleatorios = []
    for simbolo, letra in (("Σj", "Sj"), ("ΣV", "SV")):
        for ast in ("", "_ast"):
            for n in (n1, n2):
                for lado in ("a", "i"):
                    marca = "*" if ast else ""
                    aleatorios.append((f"{prefijo}_{letra}{lado}{n}{ast}", simbolo, f"{lado}{n}{marca}"))
    obstaculos = []
    for vel in ("VM", "V0"):
        for b_tipo, h_tipo in (("max", "con"), ("con", "max")):
            for lado in ("i", "a"):
                obstaculos.append((f"{prefijo}_bobst{vel}_{b_tipo}_{lado}", "b", f"{vel},{b_tipo},{lado}"))
                obstaculos.append((f"{prefijo}_hobst{vel}_{h_tipo}_{lado}", "h", f"{vel},{h_tipo},{lado}"))
    envolventes = [(f"{prefijo}_{c}{lado}", c, f"{prefijo},{lado}") for lado in ("a", "i") for c in ("b", "h")]
    return COLS_PUNTO + _cols("(mm)", *aleatorios, *obstaculos, *envolventes)


COLS_LIMITE = _cols_galibo("lim", 1, 2)
COLS_NOMINAL = _cols_galibo("nom", 3, 4)

COLS_PANTOGRAFO = [Columna("nombre", "Punto", "", "()")] + _cols("(mm)",
    ("X_ref", "X", "ref"), ("Y_ref", "Y", "ref"),
    ("S_ai", "S", "ai"), ("qs_a", "qs", "a"), ("qs_i", "qs", "i"),
    ("Dbg_ai", "Δb", "g,ai"), ("Dbc_ai", "Δb", "c,ai"), ("Dbsusp_ai", "Δb", "susp,ai"),
    ("Dbcarg_ai", "Δb", "carg,ai"), ("Dbeta0_ai", "Δb", "η,ai"),
) + _cols("(º)", ("aosc_a", "α", "osc,a"), ("aosc_i", "α", "osc,i")) + _cols("(mm)",
    ("Dbosc_a", "Δb", "osc,a"), ("Dbosc_i", "Δb", "osc,i"),
    ("Tvia_ai", "T", "via"), ("Sja", "Σj", "a"), ("Sji", "Σj", "i"),
    ("bobst_a", "b", "obst,a,ref"), ("bobst_i", "b", "obst,i,ref"),
    ("bobst_a_hmax", "b", "obst,a"), ("bobst_i_hmax", "b", "obst,i"),
    ("bobst_a_hmax_heff_elec", "b", "obst,a,heff"), ("bobst_i_hmax_heff_elec", "b", "obst,i,heff"),
    ("bobst_a_hmax_elec", "b", "obst,a,elec"), ("bobst_i_hmax_elec", "b", "obst,i,elec"),
    ("X_mec", "X", "mec"), ("Y_mec", "Y", "mec"), ("X_elec", "X", "elec"), ("Y_elec", "Y", "elec"),
)

# Variables generales de la vía: (título del bloque, [(descripción, símbolo, subíndice, unidades, atributo)])
SECCIONES_VARIABLES = [
    ("Salientes", [
        ("Radio de curvatura, planta", "R", "", "m", "R"),
        ("Radio de curvatura, alzado", "R", "V", "m", "Rv"),
        ("Ancho de vía nominal", "l", "N", "m", "LN"),
        ("Sobreancho máximo", "D", "l", "m", "DL"),
        ("Ancho de vía", "I", "", "m", "LND"),
        ("Desplazamiento por inscripción en acuerdos vert.", "D", "hRV", "m", "DhRV"),
    ]),
    ("Desplazamientos cuasiestáticos laterales", [
        ("Peralte de la vía", "D", "", "m", "D"),
        ("Peralte por convenio de la vía", "D", "0", "m", "D0"),
        ("Peralte de equilibrio", "h", "eq", "m", "heq"),
        ("Insuficiencia de peralte", "I", "", "m", "I"),
        ("Insuficiencia de peralte por convenio", "I", "0", "m", "I0"),
        ("Distancia entre círculos de rodadura", "L", "", "m", "L"),
        ("Altura del centro de balanceo, por convenio", "h", "co", "m", "hco"),
    ]),
    ("Desplazamientos aleatorios laterales", [
        ("Desplazamiento lateral de la vía", "T", "via", "m", "TVIA"),
        ("Diferencia entre peralte real y teórico", "T", "D", "m", "TD"),
        ("Velocidad máxima de la vía", "V", "max", "km/h", "vmax"),
        ("Tolerancias en el reglaje de la suspensión", "α", "susp", "º", "asusp"),
        ("Reparto desigual de cargas", "α", "carga", "º", "acarga"),
        ("Giro total", "η", "0", "º", "eta0"),
        ("Giro por oscilaciones aleatorias por irreg. de la vía", "α", "osc,i,s0=0,4", "º", "aosc_i_s0_04b"),
        ("", "α", "osc,i,s0=0,3", "º", "aosc_i_s0_03b"),
        ("", "α", "osc,a,s0=0,4", "º", "aosc_a_s0_04b"),
        ("", "α", "osc,a,s0=0,3", "º", "aosc_a_s0_03b"),
    ]),
    ("Pantógrafo", [
        ("Semiancho de la mesilla", "b", "w", "m", "bw"),
        ("Desplazamiento lateral máximo", "e", "po", "m", "epo"),
        ("", "e", "pu", "m", "epu"),
        ("Peralte por convenio de la vía", "D'", "0", "m", "D0p"),
        ("Insuficiencia de peralte por convenio", "I", "0", "m", "I0p"),
        ("Coeficiente de flexibilidad del vehículo", "s'", "0", "m", "s0p"),
        ("Proyección del ancho del trocador", "c", "w", "m", "cw"),
        ("Aislamiento eléctrico estático", "b", "elec,estat,i", "m", "belec_estat"),
        ("Aislamiento eléctrico dinámico", "b", "elec,dinam,a", "m", "belec_dinam"),
        ("Elevación del hilo de contacto, vmax", "f", "s,vmax", "m", "fsvmax"),
        ("Elevación del hilo de contacto, vmin", "f", "s,vmin", "m", "fsvmin"),
        ("Elevación por desgaste de pletina y flexibilidad", "f", "wswa", "m", "fwswa"),
        ("Altura máxima del gálibo mecánico", "h", "eff", "m", "heff"),
        ("Altura máxima del gálibo eléctrico", "h", "eff,elec", "m", "heffelec"),
    ]),
]


# ---------------------------------------------------------------------------
# Controles
# ---------------------------------------------------------------------------
class TablaPuntos(ft.ResponsiveRow):
    """Tabla de resultados por punto. Una columna de FLET por cada variable."""

    def __init__(self, columnas: list):
        super().__init__()
        self.especificacion = columnas
        self.columnas_ft = []
        for col in columnas:
            columna = MiColumnaTabla()
            columna.controls = [MiText(col.simbolo, col.subindice),
                                ft.Text(col.unidades, size=Tamanyos.TABLA_NORMAL.value)]
            self.columnas_ft.append(columna)
        self.controls = self.columnas_ft
        self.columns = len(columnas)
        self.filas = []     # [(nombre, punto)] mostrados actualmente

    def actualizar(self, puntos: dict) -> None:
        self.filas = list(puntos.items())
        n = len(self.filas)
        for col, columna in zip(self.especificacion, self.columnas_ft):
            celdas = columna.controls[2:]
            if len(celdas) != n:        # Solo se crean controles si cambia el número de puntos
                celdas = [ft.Text(size=Tamanyos.TABLA_NORMAL.value) for _ in range(n)]
                columna.controls[2:] = celdas
            for celda, (nombre, punto) in zip(celdas, self.filas):
                celda.value = nombre if col.attr == "nombre" else formatear(getattr(punto, col.attr))

    def texto(self, titulo: str) -> str:
        """Contenido de la tabla separado por tabuladores, listo para pegar en una hoja de cálculo."""
        lineas = [titulo,
                  "\t".join("Punto" if c.attr == "nombre" else c.attr for c in self.especificacion),
                  "\t".join(c.unidades for c in self.especificacion)]
        for nombre, punto in self.filas:
            lineas.append("\t".join(nombre if c.attr == "nombre" else formatear(getattr(punto, c.attr))
                                    for c in self.especificacion))
        return "\n".join(lineas) + "\n"


class TablaVariables(ft.ResponsiveRow):
    """Variables generales de la vía, agrupadas en bloques."""

    # Variables auxiliares que no se copian al portapapeles
    _EXCLUIDAS_PORTAPAPELES = {"hquiebroaux", "htopeaux", "difaux", "hotra"}

    def __init__(self):
        super().__init__()
        self.textos = {}        # atributo -> ft.Text
        bloques = []
        for titulo, filas in SECCIONES_VARIABLES:
            controles = [ft.Text(titulo, size=Tamanyos.MEDIANO.value)]
            for descripcion, simbolo, sub, unidades, attr in filas:
                self.textos[attr] = ft.Text(width=50)
                controles.append(MiFilaDatos2(descripcion, simbolo, sub, unidades, self.textos[attr]))
            bloques.append(ft.Column(controles, col=1))
        self.controls = bloques
        self.columns = len(bloques)
        self.via = None

    def actualizar(self, via) -> None:
        self.via = via
        for attr, texto in self.textos.items():
            texto.value = formatear(getattr(via, attr))

    def texto(self, titulo: str) -> str:
        lineas = [titulo]
        if self.via is not None:
            for attr, descripcion in dic_datos_via.items():
                if attr not in self._EXCLUIDAS_PORTAPAPELES:
                    lineas.append(f"{descripcion}\t{formatear(getattr(self.via, attr))}")
        return "\n".join(lineas) + "\n"


class TablasVia:
    """Todas las tablas de resultados de una vía."""

    def __init__(self):
        self.variables = TablaVariables()
        self.desplazamientos = TablaPuntos(COLS_DESPLAZAMIENTOS)
        self.limite = TablaPuntos(COLS_LIMITE)
        self.nominal = TablaPuntos(COLS_NOMINAL)
        self.pantografo = TablaPuntos(COLS_PANTOGRAFO)

    def actualizar(self, via, resultado) -> None:
        self.variables.actualizar(via)
        for tabla in (self.desplazamientos, self.limite, self.nominal):
            tabla.actualizar(resultado.galiboPA)
        self.pantografo.actualizar(resultado.galiboPant)
