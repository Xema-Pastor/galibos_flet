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

@dataclass
class PuntoP:
    X_ref: float = 0           # Valor de la coordenada X del pantógrafo de referencia, (mm)
    Y_ref: float = 0           # Valor de la coordenada Y del pantógrafo de referencia, (mm)
    X_mec: float = 0           # Valor de la coordenada X del controrno mecánico, (mm)
    Y_mec: float = 0           # Valor de la coordenada Y del controrno mecánico, (mm)
    X_elec: float = 0          # Valor de la coordenada X del controrno eléctrico, (mm)
    Y_elec: float = 0          # Valor de la coordenada Y del controrno eléctrico, (mm)

    S_ai: float = 0            # Salientes (mm)
    qs_a: float = 0            # Desplazamientos cuasiestáticos horizontales, lado exterior (mm)
    qs_i: float = 0            # Desplazamientos cuasiestáticos horizontales, lado interior (mm)
    Dbg_ai: float = 0      #
    Dbc_ai: float = 0      #
    Dbsusp_ai: float = 0   #
    Dbcarg_ai: float = 0  #
    Dbeta0_ai: float = 0     #
    aosc_a: float = 0      # (º)
    aosc_i: float = 0      # (º)
    Dbosc_a: float = 0     #
    Dbosc_i: float = 0     #
    Tvia_ai: float = 0     #
    Sja: float = 0        # Suma de desplazamientos aleatorios laterales
    Sji: float = 0        # idem

    bobst_a: float = 0
    bobst_i: float = 0
    bobst_a_hmax: float = 0
    bobst_i_hmax: float = 0
    bobst_a_hmax_heff_elec: float = 0
    bobst_i_hmax_heff_elec: float = 0
    bobst_a_hmax_elec: float = 0
    bobst_i_hmax_elec: float = 0

class Via():
    def __init__(self):
        #3.1
        self.GPA = "GA"          # galibo_partes_altas (GHE16|GEA16|GEB16|GEC16|GA|GB|GC|GEE10|GED10|PERSONALIZADO)
        self.GPB = "GEI2"        # galibo_partes_bajas (GEI1|GEI2|GEI3|GI1|GI2|GI3)
        self.maxY = 0            # Valor de la máxima coordenada Y (mm)
        self.maxX = 0            # valor de la máxima coordenada X (mm)
        self.hquiebroaux = 0
        self.htopeaux = 0
        self.difaux = 0
        self.hotra = 0
        self.hb_max = 0

        #3.2.2.1
        self.R = 100               #Radio de curvatura en planta
        self.Inclinac = "A derechas"#Inclinación de la curva
        self.LN = 0              #Ancho de vía nominal
        self.DL = 0              #Sobreancho máximo
        self.LND = 0             #Ancho de vía

        #3.2.2.2
        self.D = 0               #Peralte de la vía
        self.D0 = 0              #Peralte por convenio de la vía
        self.heq = 0             #Peralte de equilibrio
        self.I = 0               #Insuficiencia de peralte
        self.I0 = 0              #Insuficiencia de peralte por convenio
        self.L = 0               #Distancia entre circulos de rodadura
        self.hco = 0.50          #Altura  del  centro  de  balanceo  del  vehículo, por convenio

        #3.2.2.3
        self.tipo_via = ""       #Tipo de vía (BALASTO|PLACA)
        self.TVIA = 0            #Desplazaiento lateral de la vía
        self.TD = 0              #Diferencia entre peralte real y teórico
        self.vmax = 0            #Velocidad máxima de la vía
        self.asusp = 0           #Tolerancias en el reglaje de la suspensión
        self.acarga = 0          #Reparto desigual de cargas
        self.eta0 = 0              #Giro total
        self.estado_via = ""     #Estado de la vía (BUEN ESTADO|MAL ESTADO)
        self.aosc_i_s0_04b = 0    #Giro debido a oscilaciones aleatorias causadas por irregularidades de la vía. Cálculo incrementos HORIZONTALES
        self.aosc_i_s0_03b = 0
        self.aosc_a_s0_04b = 0
        self.aosc_a_s0_03b = 0

        #3.2.2.4
        self.M3b = 0.2           #Márgenes horizontales

        #3.2.3.1
        self.Rv = 0              #Radio del acuerdo vertical
        self.DhRV = 0            #Desplazamiento por inscripción
        
        #3.2.3.3
        self.TN = 0.02           #Desplazamiento vertical de la vía
        self.aosc_i_s0_04h = 0   #Giro debido a oscilaciones aleatorias causadas por irregularidades de la vía. Cálculo incrementos VERTICALES
        self.aosc_i_s0_03h = 0
        self.aosc_a_s0_04h = 0
        self.aosc_a_s0_03h = 0

        #3.2.3.4
        self.M3h = 0.15          #Márgenes verticales   

        #3.3
        self.K = 1.2             #Factor de seguridad, general
        self.Kale_h_0_50 = 1.0   #Factor de seguridad, para desplazamientos aleatorios laterales (h<0,50)

        #Pantógrafo
        self.tipo_pant = "Ancho 1600 (ibérico e internacional)"          #Tipo de pantógrafo
        self.tipo_cat = ""           #Tipo de catenaria
        self.tipo_lin = ""          #Tipo de línea
        self.ten_cat = ""           #Tensión en la catenaria
        self.hf = 5.00              #Altura del hilo de contacto (m)
        self.bp = 1.7               #Anchura del pantógrafo (m)
        self.bw = 0.85              #Semiancho de la mesilla del pantógrafo (m)
        self.epo = 0.15             #Desplazamieno lateral máximo del pantógrafo (1) (m)
        self.epu = 0.82             #Desplazamieno lateral máximo del pantógrafo (2) (m)
        self.D0p = 0.07             #Peralte por convenio de la vía, para el pantógrafo (m)
        self.I0p = 0.07             #Insuficiencia de peralte por convenio de la vía, para el pantógrafo (m)
        self.s0p = 0.225            #Coeficiente de flexibilidad del vehículo, para el pantógrafo
        self.cw = 0.0               #Proyección del ancho del trocador (m)
        self.belec_estat = 0.27     #Aislamiento elétrctrico estático (m)
        self.belec_dinam = 0.27     #Aislamiento elétrctrico dinámico (m)
        self.fsvmax = 0.162         #Elevación del hilo de contacto debido a la fuerza del pantógrafo, vmax (m)
        self.fsvmin = 0.041         #Elevación del hilo de contacto debido a la fuerza del pantógrafo, vmin (m)
        self.fwswa = 0.07           #Elevación del pantógrafo debido al desgaste de la pletina y a flexibilidad del pantógrado (m)
        self.heffvmax = 0           #Altura máxima del gálibo mecánico, vmax (m)
        self.heffelecvmax = 0       #Altura del gálibo eléctrico, vmax (m)
        self.heffvmin = 0           #Altura máxima del gálibo mecánico, vmin (m)
        self.heffelecvmin = 0       #Altura del gálibo eléctrico, vmin (m)
        self.heff = 0               #Altura máxima del gálibo mecánico (m)
        self.heffelec = 0           #Altura máxima del gálibo eléctrico (m)

via1 = Via()
via2 = Via()