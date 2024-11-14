from enum import Enum

class Tamanyos(Enum):
    GRANDE = 50
    MEDIANO = 25
    PEQUENYO = 10
    NORMAL = 15
    TABLA_NORMAL = 11
    TABLA_SUBTITULO = 9

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