from dataclasses import dataclass

@dataclass
class Punto:
    X: float = 0           # Valor de la coordenada X, (mm)
    Y: float = 0           # Valor de la coordenada Y, (mm)
    esPT: bool = 0         #
    k: float = 0           #
    s0: float = 0          #
    Sa: float = 0          # Salientes partes altas, exterior de la curva
    Si: float = 0          # Salientes partes altas, interior de la curva
    qsD_ai: float = 0       #
    qsI_ai: float = 0       #
    Tvia_ai: float = 0     #
    Dbg_ai: float = 0      #
    Dbc_ai: float = 0      #
    Dbsusp_ai: float = 0   #
    Dbcarg_ai: float = 0  #
    Dbeta0_ai: float = 0     #
    aosc_a: float = 0      # (º)
    aosc_i: float = 0      # (º)
    Dbosc_a: float = 0     #
    Dbosc_i: float = 0     #
    M3b: float = 0         #
    DhRv: float = 0        #
    DhPT_D_ai: float = 0   #
    DhPT_I_ai: float = 0   #
    TN: float = 0          #
    Dhg_a: float = 0       #
    Dhg_i: float = 0       #
    Dhc: float = 0         #
    Dhgca: float = 0         #
    Dhgci: float = 0         #
    Dhsusp_ai: float = 0   #
    Dhcarg_ai: float = 0   #
    Dheta0_ai: float = 0   #
    Dhosc_a: float = 0     #
    Dhosc_i: float = 0     #
    M3h: float = 0         # Márgenes horizontales

    lim_Sja1: float = 0        # Suma de desplazamientos aleatorios laterales para gálibos límite
    lim_Sji1: float = 0        # idem
    lim_Sja2: float = 0        # idem
    lim_Sji2: float = 0        # idem
    lim_rad_Sja1_ast: float = 0
    lim_rad_Sji1_ast: float = 0
    lim_rad_Sjai2_ast: float = 0
    lim_Sja1_ast: float = 0    # idem
    lim_Sji1_ast: float = 0    # idem
    lim_Sja2_ast: float = 0    # idem
    lim_Sji2_ast: float = 0    # idem
    lim_rad_SVa1: float = 0
    lim_rad_SVi1: float = 0
    lim_SVa1: float = 0        # Suma de desplazamientos aleatorios verticales para gálibos límite
    lim_SVi1: float = 0        # idem
    lim_SVa2: float = 0        # idem
    lim_SVi2: float = 0        # idem
    lim_SVa1_ast: float = 0    # idem
    lim_SVi1_ast: float = 0    # idem
    lim_SVa2_ast: float = 0    # idem
    lim_SVi2_ast: float = 0    # idem

    lim_bobstVM_max_i: float = 0 # Cálculo de glalibos límite
    lim_hobstVM_con_i: float = 0 # idem
    lim_bobstVM_max_a: float = 0 # idem
    lim_hobstVM_con_a: float = 0 # idem
    lim_bobstVM_con_i: float = 0 # idem
    lim_hobstVM_max_i: float = 0 # idem
    lim_bobstVM_con_a: float = 0 # idem
    lim_hobstVM_max_a: float = 0 # idem
    lim_bobstV0_max_i: float = 0 # idem
    lim_hobstV0_con_i: float = 0 # idem
    lim_bobstV0_max_a: float = 0 # idem
    lim_hobstV0_con_a: float = 0 # idem
    lim_bobstV0_con_i: float = 0 # idem
    lim_hobstV0_max_i: float = 0 # idem
    lim_bobstV0_con_a: float = 0 # idem
    lim_hobstV0_max_a: float = 0 # idem
    lim_ba: float = 0          # Envolvente de gálibo límite, exterior
    lim_ha: float = 0          # Envolvente de gálibo límite, exterior
    lim_bi: float = 0          # Envolvente de gálibo límite, interior
    lim_hi: float = 0          # Envolvente de gálibo límite, interior

    nom_Sja3: float = 0        # Suma de desplazamientos aleatorios laterales para gálibos límite
    nom_Sji3: float = 0        # idem
    nom_Sja4: float = 0        # idem
    nom_Sji4: float = 0        # idem
    nom_Sja3_ast: float = 0    # idem
    nom_Sji3_ast: float = 0    # idem
    nom_Sja4_ast: float = 0    # idem
    nom_Sji4_ast: float = 0    # idem
    nom_SVa3: float = 0        # Suma de desplazamientos aleatorios verticales para gálibos límite
    nom_SVi3: float = 0        # idem
    nom_SVa4: float = 0        # idem
    nom_SVi4: float = 0        # idem
    nom_SVa3_ast: float = 0    # idem
    nom_SVi3_ast: float = 0    # idem
    nom_SVa4_ast: float = 0    # idem
    nom_SVi4_ast: float = 0    # idem

    nom_bobstVM_max_i: float = 0 # Cálculo de glalibos límite
    nom_hobstVM_con_i: float = 0 # idem
    nom_bobstVM_max_a: float = 0 # idem
    nom_hobstVM_con_a: float = 0 # idem
    nom_bobstVM_con_i: float = 0 # idem
    nom_hobstVM_max_i: float = 0 # idem
    nom_bobstVM_con_a: float = 0 # idem
    nom_hobstVM_max_a: float = 0 # idem
    nom_bobstV0_max_i: float = 0 # idem
    nom_hobstV0_con_i: float = 0 # idem
    nom_bobstV0_max_a: float = 0 # idem
    nom_hobstV0_con_a: float = 0 # idem
    nom_bobstV0_con_i: float = 0 # idem
    nom_hobstV0_max_i: float = 0 # idem
    nom_bobstV0_con_a: float = 0 # idem
    nom_hobstV0_max_a: float = 0 # idem
    nom_ba: float = 0          # Envolvente de gálibo límite, exterior
    nom_ha: float = 0          # Envolvente de gálibo límite, exterior
    nom_bi: float = 0          # Envolvente de gálibo límite, interior
    nom_hi: float = 0          # Envolvente de gálibo límite, interior

    grafico_contorno_X: float = 0
    grafico_contorno_Y: float = 0
    grafico_galibo_limite_X: float = 0
    grafico_galibo_limite_Y: float = 0
    grafico_galibo_nominal_X: float = 0
    grafico_galibo_nominal_Y: float = 0

@dataclass
class PuntoI:
    X: float = 0           # Valor de la coordenada X, (mm)
    Y: float = 0           # Valor de la coordenada Y, (mm)

class Variables():

    #3.1
    GPA = "GA"          # galibo_partes_altas (GHE16|GEA16|GEB16|GEC16|GA|GB|GC|GEE10|GED10|PERSONALIZADO)
    GPB = "GEI2"        # galibo_partes_bajas (GEI1|GEI2|GEI3|GI1|GI2|GI3)
    maxY = 0            # Valor de la máxima coordenada Y (mm)
    maxX = 0            # valor de la máxima coordenada X (mm)
    hquiebroaux = 0
    htopeaux = 0
    difaux = 0
    hotra = 0
    hb_max = 0

    #3.2.2.1
    R = 100               #Radio de curvatura en planta
    Inclinac = "A derechas"#Inclinación de la curva
    LN = 0              #Ancho de vía nominal
    DL = 0              #Sobreancho máximo
    LND = 0             #Ancho de vía

    #3.2.2.2
    D = 0               #Peralte de la vía
    D0 = 0              #Peralte por convenio de la vía
    heq = 0             #Peralte de equilibrio
    I = 0               #Insuficiencia de peralte
    I0 = 0              #Insuficiencia de peralte por convenio
    L = 0               #Distancia entre circulos de rodadura
    hco = 0.50          #Altura  del  centro  de  balanceo  del  vehículo, por convenio

    #3.2.2.3
    tipo_via = ""       #Tipo de vía (BALASTO|PLACA)
    TVIA = 0            #Desplazaiento lateral de la vía
    TD = 0              #Diferencia entre peralte real y teórico
    vmax = 0            #Velocidad máxima de la vía
    asusp = 0           #Tolerancias en el reglaje de la suspensión
    acarga = 0          #Reparto desigual de cargas
    eta0 = 0              #Giro total
    estado_via = ""     #Estado de la vía (BUEN ESTADO|MAL ESTADO)
    aosc_i_s0_04b = 0    #Giro debido a oscilaciones aleatorias causadas por irregularidades de la vía. Cálculo incrementos HORIZONTALES
    aosc_i_s0_03b = 0
    aosc_a_s0_04b = 0
    aosc_a_s0_03b = 0

    #3.2.2.4
    M3b = 0.2           #Márgenes horizontales

    #3.2.3.1
    Rv = 0              #Radio del acuerdo vertical
    DhRV = 0            #Desplazamiento por inscripción
    
    #3.2.3.3
    TN = 0.02           #Desplazamiento vertical de la vía
    aosc_i_s0_04h = 0   #Giro debido a oscilaciones aleatorias causadas por irregularidades de la vía. Cálculo incrementos VERTICALES
    aosc_i_s0_03h = 0
    aosc_a_s0_04h = 0
    aosc_a_s0_03h = 0

    #3.2.3.4
    M3h = 0.15          #Márgenes verticales   

    #3.3
    K = 1.2             #Factor de seguridad, general
    Kale_h_0_50 = 1.0   #Factor de seguridad, para desplazamientos aleatorios laterales (h<0,50)

via1 = Variables()
via2 = Variables()