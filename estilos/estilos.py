from enum import Enum
import flet as ft

class Tamanyos(Enum):
    GRANDE = 50
    MEDIANO = 25
    PEQUENYO = 10
    NORMAL = 15
    TABLA_NORMAL = 11
    TABLA_SUBTITULO = 9

'''class Colores(Enum):
    CYAN = ft.colors.CYAN'''
# AMBER 100-900
# AMBER_ACCENT 100, 200, 400, 700
# BLACK 12, 26, 38, 45, 54, 87
# BLUE 100-900 
# BLUE_ACCENT 100, 200, 400, 700
# BLUE_GREY 100-900
# BROWN 100-900
# CYAN 100-900
# CYAN_ACCENT 100, 200, 400, 700
# DEEP_ORANGE 100-900
# DEEP_ORANGE_ACCENT 100, 200, 400, 700
# DEEP_PURPLE 100-900
# DEEP_PURPLE_ACCENT 100, 200, 400, 700
# GREEN
# GREEN_ACCENT
# GREY
# INDIGO
# INDIGO_ACCENT
# LIGHT_BLUE
# LIGHT_BLUE_ACCENT
# LIGHT_GREEN
# LIGHT_GREEN_ACCENT
# LIME
# LIME_ACCENT
# ORANGE
# ORANGE_ACCENT
# PINK
# PINK_ACCENT
# PURPLE
# PURPLE_ACCENT
# RED
# RED_ACCENT
# TEAL
# TEAL_ACCENT
# WHITE 10, 12, 24, 30, 38, 54, 60, 70
# YELLOW
# YELLOW_ACCENT

class EGPA(Enum):
    GHE16 = "GHE16"
    GEA16 = "GEA16"
    GEB16 = "GEB16"
    GEC16 = "GEC16"
    GA = "GA"
    GB = "GB"
    GC = "GC"
    GEE10 = "GEE10"
    GED10 = "GED10"
    PERSONALIZADO = "PERSONALIZADO"

class EGPB(Enum):
    GEI1 = "GEI1"
    GEI2 = "GEI2"
    GEI3 = "GEI3"
    GI1 = "GI1"
    GI2 = "GI2"
    GI3 = "GI3"

class ETV(Enum):
    BALASTO = "Balasto"
    VIA_PLACA = "Vía en placa"

class EEV(Enum):
    BUEN_ESTADO = "Buen estado"
    MAL_ESTADO = "Mal estado"

class TIPO_PANT(Enum):
    ANCHO_1950 = "Ancho 1950 (ibérico e internacional)"
    ANCHO_1600 = "Ancho 1600 (ibérico e internacional)"
    ANCHO_1700 = "Ancho 1700 (métrico)"

class TENSION_CAT(Enum):
    
    CC_1500 = "1.5 kV, c.c."
    CC_3000 = "3.0 kV, c.c."
    CA_25000 = "25 kV, c.a."

class TIPO_LINEA(Enum):
    EXISTENTES = "Existentes"
    NUEVAS = "Nuevas o acondicionadas"

class TIPO_CAT(Enum):
    CA160 = "CA-160"
    CAU220 = "CAU-220"
    CA220 = "CA-220"
    SICAT = "SICAT H 1.0"
    EAC350 = "EAC-350"
    RIGIDA = "RIGIDA"
