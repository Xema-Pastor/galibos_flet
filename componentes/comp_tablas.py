import flet as ft
from dataclasses import dataclass
from componentes.mis_componentes import MiColumnaTabla, MiText, MiFilaDatos2
from datos_variables import via1, via2
from estilos.estilos import Tamanyos

#COMPONENETES DE TEXTOS
@dataclass
class ftText:
    def __init__(self, via):
        self.t_R = ft.Text(via.R,width=50)
        self.t_RV = ft.Text(via.R,width=50)
        self.t_LN = ft.Text(via.LN,width=50)
        self.t_DL = ft.Text(via.DL,width=50)
        self.t_LND = ft.Text(via.LND,width=50)
        self.t_DhRV = ft.Text(via.LND,width=50)

        self.t_D = ft.Text(via.D,width=50)
        self.t_D0 = ft.Text(via.D0,width=50)
        self.t_heq = ft.Text(via.heq,width=50)
        self.t_I = ft.Text(via.I,width=50)
        self.t_I0 = ft.Text(via.I0,width=50)
        self.t_L = ft.Text(via.L,width=50)
        self.t_hco = ft.Text(via.hco,width=50)

        self.t_tvia = ft.Text(via.TVIA,width=50)
        self.t_td = ft.Text(via.TD,width=50)
        self.t_vmax = ft.Text(via.vmax,width=50)
        self.t_asusp = ft.Text(via.asusp,width=50)
        self.t_acarga = ft.Text(via.acarga,width=50)
        self.t_eta0 = ft.Text(via.eta0,width=50)
        self.t_aosc_i_s0_04b = ft.Text(via.aosc_i_s0_04b,width=50)
        self.t_aosc_i_s0_03b = ft.Text(via.aosc_i_s0_03b,width=50)
        self.t_aosc_a_s0_04b = ft.Text(via.aosc_a_s0_04b,width=50)
        self.t_aosc_a_s0_03b = ft.Text(via.aosc_a_s0_03b,width=50)

        self.t_bp = ft.Text(via.bp,width=50)
        self.t_bw = ft.Text(via.bw,width=50)
        self.t_epo = ft.Text(via.epo,width=50)
        self.t_epu = ft.Text(via.epu,width=50)
        self.t_D0p = ft.Text(via.D0p,width=50)
        self.t_I0p = ft.Text(via.I0p,width=50)
        self.t_s0p = ft.Text(via.s0p,width=50)
        self.t_cw = ft.Text(via.cw,width=50)
        self.t_belec_estat = ft.Text(via.belec_estat,width=50)
        self.t_belec_dinam = ft.Text(via.belec_dinam,width=50)
        self.t_fsvmax = ft.Text(via.fsvmax,width=50)
        self.t_fsvmin = ft.Text(via.fsvmin,width=50)
        self.t_fwswa = ft.Text(via.fwswa,width=50)
        self.t_heffvmax = ft.Text(via.heffvmax,width=50)
        self.t_heffelecvmax = ft.Text(via.heffelecvmax,width=50)
        self.t_heffvmin = ft.Text(via.heffvmin,width=50)
        self.t_heffelecvmin = ft.Text(via.heffelecvmin,width=50)
        self.t_heff = ft.Text(via.heff,width=50)
        self.t_heffelec = ft.Text(via.heffelec,width=50)

ftt_1 = ftText(via1)
ftt_2 = ftText(via2)

#COMPONENTES DE TABLAS
@dataclass
class ftTabla:
    def __init__(self):
        self.tabla_00_Punto_des = MiColumnaTabla()
        self.tabla_00_Punto_lim = MiColumnaTabla()
        self.tabla_00_Punto_nom = MiColumnaTabla()
        self.tabla_01_X_des = MiColumnaTabla()
        self.tabla_01_X_lim = MiColumnaTabla()
        self.tabla_01_X_nom = MiColumnaTabla()
        self.tabla_02_Y_des = MiColumnaTabla()
        self.tabla_02_Y_lim = MiColumnaTabla()
        self.tabla_02_Y_nom = MiColumnaTabla()
        self.tabla_03_esPT = MiColumnaTabla()
        self.tabla_04_k = MiColumnaTabla()
        self.tabla_05_s0 = MiColumnaTabla()
        self.tabla_06_Sa = MiColumnaTabla()
        self.tabla_07_Si = MiColumnaTabla()
        self.tabla_08_qsDai = MiColumnaTabla()
        self.tabla_09_qsIai = MiColumnaTabla()
        self.tabla_10_Tvia_ai = MiColumnaTabla()
        self.tabla_11_Dbgai = MiColumnaTabla()
        self.tabla_12_Dbcai = MiColumnaTabla()
        self.tabla_13_Dbsuspai = MiColumnaTabla()
        self.tabla_14_Dbcargaai = MiColumnaTabla()
        self.tabla_15_Dbetaai = MiColumnaTabla()
        self.tabla_16_aosca = MiColumnaTabla()
        self.tabla_17_aosci = MiColumnaTabla()
        self.tabla_18_Dbosca = MiColumnaTabla()
        self.tabla_19_Dbosci = MiColumnaTabla()
        self.tabla_20_M3h = MiColumnaTabla()
        self.tabla_21_DhRv = MiColumnaTabla()
        self.tabla_22_DhPTDai = MiColumnaTabla()
        self.tabla_23_DhPTIai = MiColumnaTabla()
        self.tabla_24_TN = MiColumnaTabla()
        self.tabla_25_Dhga = MiColumnaTabla()
        self.tabla_26_Dhgi = MiColumnaTabla()
        self.tabla_27_Dhc = MiColumnaTabla()
        self.tabla_28_Dhgca = MiColumnaTabla()
        self.tabla_29_Dhgci = MiColumnaTabla()
        self.tabla_30_Dhsuspai = MiColumnaTabla()
        self.tabla_31_Dhcargai = MiColumnaTabla()
        self.tabla_32_Dhetaai = MiColumnaTabla()
        self.tabla_33_Dhosca = MiColumnaTabla()
        self.tabla_34_Dhosci = MiColumnaTabla()
        self.tabla_35_M3h = MiColumnaTabla()
        self.tabla_36_lim_Sja1 = MiColumnaTabla()
        self.tabla_37_lim_Sji1 = MiColumnaTabla()
        self.tabla_38_lim_Sja2 = MiColumnaTabla()
        self.tabla_39_lim_Sji2 = MiColumnaTabla()
        self.tabla_40_lim_Sja1_ast = MiColumnaTabla()
        self.tabla_41_lim_Sji1_ast = MiColumnaTabla()
        self.tabla_42_lim_Sja2_ast = MiColumnaTabla()
        self.tabla_43_lim_Sji2_ast = MiColumnaTabla()
        self.tabla_44_lim_SVa1 = MiColumnaTabla()
        self.tabla_45_lim_SVi1 = MiColumnaTabla()
        self.tabla_46_lim_SVa2 = MiColumnaTabla()
        self.tabla_47_lim_SVi2 = MiColumnaTabla()
        self.tabla_48_lim_SVa1_ast = MiColumnaTabla()
        self.tabla_49_lim_SVi1_ast = MiColumnaTabla()
        self.tabla_50_lim_SVa2_ast = MiColumnaTabla()
        self.tabla_51_lim_SVi2_ast = MiColumnaTabla()
        self.tabla_52_nom_Sja3 = MiColumnaTabla()
        self.tabla_53_nom_Sji3 = MiColumnaTabla()
        self.tabla_54_nom_Sja4 = MiColumnaTabla()
        self.tabla_55_nom_Sji4 = MiColumnaTabla()
        self.tabla_56_nom_Sja3_ast = MiColumnaTabla()
        self.tabla_57_nom_Sji3_ast = MiColumnaTabla()
        self.tabla_58_nom_Sja4_ast = MiColumnaTabla()
        self.tabla_59_nom_Sji4_ast = MiColumnaTabla()
        self.tabla_60_nom_SVa3 = MiColumnaTabla()
        self.tabla_61_nom_SVi3 = MiColumnaTabla()
        self.tabla_62_nom_SVa4 = MiColumnaTabla()
        self.tabla_63_nom_SVi4 = MiColumnaTabla()
        self.tabla_64_nom_SVa3_ast = MiColumnaTabla()
        self.tabla_65_nom_SVi3_ast = MiColumnaTabla()
        self.tabla_66_nom_SVa4_ast = MiColumnaTabla()
        self.tabla_67_nom_SVi4_ast = MiColumnaTabla()
        self.tabla_68_lim_bobstVM_max_i = MiColumnaTabla()
        self.tabla_69_lim_hobstVM_con_i = MiColumnaTabla()
        self.tabla_70_lim_bobstVM_max_a = MiColumnaTabla()
        self.tabla_71_lim_hobstVM_con_a = MiColumnaTabla()
        self.tabla_72_lim_bobstVM_con_i = MiColumnaTabla()
        self.tabla_73_lim_hobstVM_max_i = MiColumnaTabla()
        self.tabla_74_lim_bobstVM_con_a = MiColumnaTabla()
        self.tabla_75_lim_hobstVM_max_a = MiColumnaTabla()
        self.tabla_76_lim_bobstV0_max_i = MiColumnaTabla()
        self.tabla_77_lim_hobstV0_con_i = MiColumnaTabla()
        self.tabla_78_lim_bobstV0_max_a = MiColumnaTabla()
        self.tabla_79_lim_hobstV0_con_a = MiColumnaTabla()
        self.tabla_80_lim_bobstV0_con_i = MiColumnaTabla()
        self.tabla_81_lim_hobstV0_max_i = MiColumnaTabla()
        self.tabla_82_lim_bobstV0_con_a = MiColumnaTabla()
        self.tabla_83_lim_hobstV0_max_a = MiColumnaTabla()
        self.tabla_84_nom_bobstVM_max_i = MiColumnaTabla()
        self.tabla_85_nom_hobstVM_con_i = MiColumnaTabla()
        self.tabla_86_nom_bobstVM_max_a = MiColumnaTabla()
        self.tabla_87_nom_hobstVM_con_a = MiColumnaTabla()
        self.tabla_88_nom_bobstVM_con_i = MiColumnaTabla()
        self.tabla_89_nom_hobstVM_max_i = MiColumnaTabla()
        self.tabla_90_nom_bobstVM_con_a = MiColumnaTabla()
        self.tabla_91_nom_hobstVM_max_a = MiColumnaTabla()
        self.tabla_92_nom_bobstV0_max_i = MiColumnaTabla()
        self.tabla_93_nom_hobstV0_con_i = MiColumnaTabla()
        self.tabla_94_nom_bobstV0_max_a = MiColumnaTabla()
        self.tabla_95_nom_hobstV0_con_a = MiColumnaTabla()
        self.tabla_96_nom_bobstV0_con_i = MiColumnaTabla()
        self.tabla_97_nom_hobstV0_max_i = MiColumnaTabla()
        self.tabla_98_nom_bobstV0_con_a = MiColumnaTabla()
        self.tabla_99_nom_hobstV0_max_a = MiColumnaTabla()
        self.tabla_100_lim_ba = MiColumnaTabla()
        self.tabla_101_lim_ha = MiColumnaTabla()
        self.tabla_102_lim_bi = MiColumnaTabla()
        self.tabla_103_lim_hi = MiColumnaTabla()
        self.tabla_104_nom_ba = MiColumnaTabla()
        self.tabla_105_nom_ha = MiColumnaTabla()
        self.tabla_106_nom_bi = MiColumnaTabla()
        self.tabla_107_nom_hi = MiColumnaTabla()


    def limpiar_tabla(self, elemento: ft.Column, text1: str, text2: str, unidades: str):
            elemento.controls.clear()
            elemento.controls.append(MiText(text1, text2))
            elemento.controls.append(ft.Text(unidades,size=Tamanyos.TABLA_NORMAL.value))
    
    def actualizar_tabla(self):
        self.limpiar_tabla(self.tabla_00_Punto_des, "Punto", "", "()")
        self.limpiar_tabla(self.tabla_00_Punto_lim, "Punto", "", "()")
        self.limpiar_tabla(self.tabla_00_Punto_nom, "Punto", "", "()")
        self.limpiar_tabla(self.tabla_01_X_des, "X", "", "(mm)")
        self.limpiar_tabla(self.tabla_01_X_lim, "X", "", "(mm)")
        self.limpiar_tabla(self.tabla_01_X_nom, "X", "", "(mm)")
        self.limpiar_tabla(self.tabla_02_Y_des, "Y", "", "(mm)")
        self.limpiar_tabla(self.tabla_02_Y_lim, "Y", "", "(mm)")
        self.limpiar_tabla(self.tabla_02_Y_nom, "Y", "", "(mm)")
        self.limpiar_tabla(self.tabla_03_esPT, "esPT", "", "(S/N)")
        self.limpiar_tabla(self.tabla_04_k, "k", "", "()")
        self.limpiar_tabla(self.tabla_05_s0, "s", "0", "()")
        self.limpiar_tabla(self.tabla_06_Sa, "S", "a", "(mm)")
        self.limpiar_tabla(self.tabla_07_Si, "S", "i", "(mm)")
        self.limpiar_tabla(self.tabla_08_qsDai, "qs", "D,ai", "(mm)")
        self.limpiar_tabla(self.tabla_09_qsIai, "qs", "I,ai", "(mm)")
        self.limpiar_tabla(self.tabla_10_Tvia_ai, "T",  "via,ai", "(mm)")
        self.limpiar_tabla(self.tabla_11_Dbgai, "Δb", "g,ai", "(mm)")
        self.limpiar_tabla(self.tabla_12_Dbcai, "Δb", "c,ai", "(mm)")
        self.limpiar_tabla(self.tabla_13_Dbsuspai, "Δb", "susp,ai", "(mm)")
        self.limpiar_tabla(self.tabla_14_Dbcargaai, "Δb", "carg,ai", "(mm)")
        self.limpiar_tabla(self.tabla_15_Dbetaai, "Δb", "η,ai", "(mm)")
        self.limpiar_tabla(self.tabla_16_aosca, "α", "osc,a", "(º)")
        self.limpiar_tabla(self.tabla_17_aosci, "α", "osc,i", "(º)")
        self.limpiar_tabla(self.tabla_18_Dbosca, "Δb", "osc,a", "(mm)")
        self.limpiar_tabla(self.tabla_19_Dbosci, "Δb", "osc,i", "(mm)")
        self.limpiar_tabla(self.tabla_20_M3h, "M", "3b", "(mm)")
        self.limpiar_tabla(self.tabla_21_DhRv, "Δh", "Rv", "(mm)")
        self.limpiar_tabla(self.tabla_22_DhPTDai, "Δh", "PT,D,ai", "(mm)")
        self.limpiar_tabla(self.tabla_23_DhPTIai, "Δh", "PT,I,ai", "(mm)")
        self.limpiar_tabla(self.tabla_24_TN, "T", "N", "(mm)")
        self.limpiar_tabla(self.tabla_25_Dhga, "Δh", "g,a", "(mm)")
        self.limpiar_tabla(self.tabla_26_Dhgi, "Δh", "g,i", "(mm)")
        self.limpiar_tabla(self.tabla_27_Dhc, "Δh", "c", "(mm)")
        self.limpiar_tabla(self.tabla_28_Dhgca, "Δh", "g,ca", "(mm)")
        self.limpiar_tabla(self.tabla_29_Dhgci, "Δh", "g,ci", "(mm)")
        self.limpiar_tabla(self.tabla_30_Dhsuspai, "Δh", "suspai", "(mm)")
        self.limpiar_tabla(self.tabla_31_Dhcargai, "Δh", "carg,ai", "(mm)")
        self.limpiar_tabla(self.tabla_32_Dhetaai, "Δh", "η,ai", "(mm)")
        self.limpiar_tabla(self.tabla_33_Dhosca, "Δh", "osc,a", "(mm)")
        self.limpiar_tabla(self.tabla_34_Dhosci, "Δh", "osc,i", "(mm)")
        self.limpiar_tabla(self.tabla_35_M3h, "M", "3h", "(mm)")
        self.limpiar_tabla(self.tabla_36_lim_Sja1, "Σj", "a1", "(mm)")
        self.limpiar_tabla(self.tabla_37_lim_Sji1, "Σj", "i1", "(mm)")
        self.limpiar_tabla(self.tabla_38_lim_Sja2, "Σj", "a2", "(mm)")
        self.limpiar_tabla(self.tabla_39_lim_Sji2, "Σj", "i2", "mm")
        self.limpiar_tabla(self.tabla_40_lim_Sja1_ast, "Σj", "a1*", "(mm)")
        self.limpiar_tabla(self.tabla_41_lim_Sji1_ast, "Σj", "i1*", "(mm)")
        self.limpiar_tabla(self.tabla_42_lim_Sja2_ast, "Σj", "a2*", "(mm)")
        self.limpiar_tabla(self.tabla_43_lim_Sji2_ast, "Σj", "i2*", "(mm)")
        self.limpiar_tabla(self.tabla_44_lim_SVa1, "ΣV", "a1", "(mm)")
        self.limpiar_tabla(self.tabla_45_lim_SVi1, "ΣV", "i1", "(mm)")
        self.limpiar_tabla(self.tabla_46_lim_SVa2, "ΣV", "a2", "(mm)")
        self.limpiar_tabla(self.tabla_47_lim_SVi2, "ΣV", "i2", "(mm)")
        self.limpiar_tabla(self.tabla_48_lim_SVa1_ast, "ΣV", "a1*", "(mm)")
        self.limpiar_tabla(self.tabla_49_lim_SVi1_ast, "ΣV", "a2*", "(mm)")
        self.limpiar_tabla(self.tabla_50_lim_SVa2_ast, "ΣV", "i2*", "(mm)")
        self.limpiar_tabla(self.tabla_51_lim_SVi2_ast, "ΣV", "i2*", "(mm)")
        self.limpiar_tabla(self.tabla_52_nom_Sja3, "Σj", "a3", "(mm)")
        self.limpiar_tabla(self.tabla_53_nom_Sji3, "Σj", "i3", "(mm)")
        self.limpiar_tabla(self.tabla_54_nom_Sja4, "Σj", "a4", "(mm)")
        self.limpiar_tabla(self.tabla_55_nom_Sji4, "Σj", "i4", "(mm)")
        self.limpiar_tabla(self.tabla_56_nom_Sja3_ast, "Σj", "a3*", "(mm)")
        self.limpiar_tabla(self.tabla_57_nom_Sji3_ast, "Σj", "i3*", "(mm)")
        self.limpiar_tabla(self.tabla_58_nom_Sja4_ast, "Σj", "a4*", "(mm)")
        self.limpiar_tabla(self.tabla_59_nom_Sji4_ast, "Σj", "i4*", "(mm)")
        self.limpiar_tabla(self.tabla_60_nom_SVa3, "ΣV", "a3", "(mm)")
        self.limpiar_tabla(self.tabla_61_nom_SVi3, "ΣV", "i3", "(mm)")
        self.limpiar_tabla(self.tabla_62_nom_SVa4, "ΣV", "a4", "(mm)")
        self.limpiar_tabla(self.tabla_63_nom_SVi4, "ΣV", "i4", "(mm)")
        self.limpiar_tabla(self.tabla_64_nom_SVa3_ast, "ΣV", "a3*", "(mm)")
        self.limpiar_tabla(self.tabla_65_nom_SVi3_ast, "ΣV", "i3*", "(mm)")
        self.limpiar_tabla(self.tabla_66_nom_SVa4_ast, "ΣV", "a4*", "(mm)")
        self.limpiar_tabla(self.tabla_67_nom_SVi4_ast, "ΣV", "i4*", "(mm)")
        self.limpiar_tabla(self.tabla_68_lim_bobstVM_max_i, "b", "VM,max,i", "(mm)")
        self.limpiar_tabla(self.tabla_69_lim_hobstVM_con_i, "h", "VM,con,i", "(mm)")
        self.limpiar_tabla(self.tabla_70_lim_bobstVM_max_a, "b", "VM,max,a", "(mm)")
        self.limpiar_tabla(self.tabla_71_lim_hobstVM_con_a, "h", "VM,con,a", "(mm)")
        self.limpiar_tabla(self.tabla_72_lim_bobstVM_con_i, "b", "VM,con,i", "(mm)")
        self.limpiar_tabla(self.tabla_73_lim_hobstVM_max_i, "h", "VM,max,i", "(mm)")
        self.limpiar_tabla(self.tabla_74_lim_bobstVM_con_a, "b", "VM,con,a", "(mm)")
        self.limpiar_tabla(self.tabla_75_lim_hobstVM_max_a, "h", "VM,max,a", "(mm)")
        self.limpiar_tabla(self.tabla_76_lim_bobstV0_max_i, "b", "V0,max,i", "(mm)")
        self.limpiar_tabla(self.tabla_77_lim_hobstV0_con_i, "h", "V0,con,i", "(mm)")
        self.limpiar_tabla(self.tabla_78_lim_bobstV0_max_a, "b", "V0,max,a", "(mm)")
        self.limpiar_tabla(self.tabla_79_lim_hobstV0_con_a, "h", "V0,con,a", "(mm)")
        self.limpiar_tabla(self.tabla_80_lim_bobstV0_con_i, "b", "V0,con,i", "(mm)")
        self.limpiar_tabla(self.tabla_81_lim_hobstV0_max_i, "h", "V0,max,i", "(mm)")
        self.limpiar_tabla(self.tabla_82_lim_bobstV0_con_a, "b", "V0,con,a", "(mm)")
        self.limpiar_tabla(self.tabla_83_lim_hobstV0_max_a, "h", "V0,max,a", "(mm)")
        self.limpiar_tabla(self.tabla_84_nom_bobstVM_max_i, "b", "VM,max,i", "(mm)")
        self.limpiar_tabla(self.tabla_85_nom_hobstVM_con_i, "h", "VM,con,i", "(mm)")
        self.limpiar_tabla(self.tabla_86_nom_bobstVM_max_a, "b", "VM,max,a", "(mm)")
        self.limpiar_tabla(self.tabla_87_nom_hobstVM_con_a, "h", "VM,con,a", "(mm)")
        self.limpiar_tabla(self.tabla_88_nom_bobstVM_con_i, "b", "VM,con,i", "(mm)")
        self.limpiar_tabla(self.tabla_89_nom_hobstVM_max_i, "h", "VM,max,i", "(mm)")
        self.limpiar_tabla(self.tabla_90_nom_bobstVM_con_a, "b", "VM,con,a", "(mm)")
        self.limpiar_tabla(self.tabla_91_nom_hobstVM_max_a, "h", "VM,max,a", "(mm)")
        self.limpiar_tabla(self.tabla_92_nom_bobstV0_max_i, "b", "V0,max,i", "(mm)")
        self.limpiar_tabla(self.tabla_93_nom_hobstV0_con_i, "h", "V0,con,i", "(mm)")
        self.limpiar_tabla(self.tabla_94_nom_bobstV0_max_a, "b", "V0,max,a", "(mm)")
        self.limpiar_tabla(self.tabla_95_nom_hobstV0_con_a, "h", "V0,con,a", "(mm)")
        self.limpiar_tabla(self.tabla_96_nom_bobstV0_con_i, "b", "V0,con,i", "(mm)")
        self.limpiar_tabla(self.tabla_97_nom_hobstV0_max_i, "h", "V0,max,i", "(mm)")
        self.limpiar_tabla(self.tabla_98_nom_bobstV0_con_a, "b", "V0,con,a", "(mm)")
        self.limpiar_tabla(self.tabla_99_nom_hobstV0_max_a, "h", "V0,max,a", "(mm)")
        self.limpiar_tabla(self.tabla_100_lim_ba, "b", "lim,a", "(mm)")
        self.limpiar_tabla(self.tabla_101_lim_ha, "h", "lim,a", "(mm)")
        self.limpiar_tabla(self.tabla_102_lim_bi, "b", "lim,i", "(mm)")
        self.limpiar_tabla(self.tabla_103_lim_hi, "h", "lim,i", "(mm)")
        self.limpiar_tabla(self.tabla_104_nom_ba, "b", "nom,a", "(mm)")
        self.limpiar_tabla(self.tabla_105_nom_ha, "h", "nom,a", "(mm)")
        self.limpiar_tabla(self.tabla_106_nom_bi, "b", "nom,i", "(mm)")
        self.limpiar_tabla(self.tabla_107_nom_hi, "h", "nom,i", "(mm)")

@dataclass
class ftTablaPant:
    def __init__(self):
        self.tablaPant_00_Punto = MiColumnaTabla()
        self.tablaPant_01_X_ref = MiColumnaTabla()
        self.tablaPant_02_Y_ref = MiColumnaTabla()
        self.tablaPant_03_Sai = MiColumnaTabla()
        self.tablaPant_04_qsa = MiColumnaTabla()
        self.tablaPant_05_qsi = MiColumnaTabla()
        self.tablaPant_06_Dbgai = MiColumnaTabla()
        self.tablaPant_07_Dbcai = MiColumnaTabla()
        self.tablaPant_08_Dbsuspai = MiColumnaTabla()
        self.tablaPant_09_Dbcargai = MiColumnaTabla()
        self.tablaPant_10_Dbetaai = MiColumnaTabla()
        self.tablaPant_11_aosca = MiColumnaTabla()
        self.tablaPant_12_aosci = MiColumnaTabla()
        self.tablaPant_13_Dbosca = MiColumnaTabla()
        self.tablaPant_14_Dbosci = MiColumnaTabla()
        self.tablaPant_15_TVia = MiColumnaTabla()
        self.tablaPant_16_Sja = MiColumnaTabla()
        self.tablaPant_17_Sji = MiColumnaTabla()
        self.tablaPant_18_bobst_a = MiColumnaTabla()
        self.tablaPant_19_bobst_i = MiColumnaTabla()
        self.tablaPant_20_bobst_a_hmax = MiColumnaTabla()
        self.tablaPant_21_bobst_i_hmax = MiColumnaTabla()
        self.tablaPant_22_bobst_a_hmax_heff_elec = MiColumnaTabla()
        self.tablaPant_23_bobst_i_hmax_heff_elec = MiColumnaTabla()
        self.tablaPant_24_bobst_a_hmax_elec = MiColumnaTabla()
        self.tablaPant_25_bobst_i_hmax_elec = MiColumnaTabla()
        self.tablaPant_26_X_mec = MiColumnaTabla()
        self.tablaPant_27_Y_mec = MiColumnaTabla()
        self.tablaPant_28_X_elec = MiColumnaTabla()
        self.tablaPant_29_Y_elec = MiColumnaTabla()

    def limpiar_tabla(self, elemento: ft.Column, text1: str, text2: str, unidades: str):
            elemento.controls.clear()
            elemento.controls.append(MiText(text1, text2))
            elemento.controls.append(ft.Text(unidades,size=Tamanyos.TABLA_NORMAL.value))
    
    def actualizar_tabla(self):
        self.limpiar_tabla(self.tablaPant_00_Punto, "Punto", "", "()")
        self.limpiar_tabla(self.tablaPant_01_X_ref, "X", "ref", "(mm)")
        self.limpiar_tabla(self.tablaPant_02_Y_ref, "Y", "ref", "(mm)")
        self.limpiar_tabla(self.tablaPant_03_Sai, "S", "ai", "(mm)")
        self.limpiar_tabla(self.tablaPant_04_qsa, "qs", "a", "(mm)")
        self.limpiar_tabla(self.tablaPant_05_qsi, "qs", "i", "(mm)")
        self.limpiar_tabla(self.tablaPant_06_Dbgai, "Δb", "g,ai", "(mm)")
        self.limpiar_tabla(self.tablaPant_07_Dbcai, "Δb", "c,ai", "(mm)")
        self.limpiar_tabla(self.tablaPant_08_Dbsuspai, "Δb", "susp,ai", "(mm)")
        self.limpiar_tabla(self.tablaPant_09_Dbcargai, "Δb", "carg,ai", "(mm)")
        self.limpiar_tabla(self.tablaPant_10_Dbetaai, "Δb", "η,ai", "(mm)")
        self.limpiar_tabla(self.tablaPant_11_aosca, "α", "osc,a", "(º)")
        self.limpiar_tabla(self.tablaPant_12_aosci, "α", "osc,i", "(º)")
        self.limpiar_tabla(self.tablaPant_13_Dbosca, "Δb", "osc,a", "(mm)")
        self.limpiar_tabla(self.tablaPant_14_Dbosci, "Δb", "osc,i", "(mm)")
        self.limpiar_tabla(self.tablaPant_15_TVia, "T", "via", "(mm)")
        self.limpiar_tabla(self.tablaPant_16_Sja, "Σj", "a", "(mm)")
        self.limpiar_tabla(self.tablaPant_17_Sji, "Σj", "i", "(mm)")
        self.limpiar_tabla(self.tablaPant_18_bobst_a, "b", "obst,a,ref", "(mm)")
        self.limpiar_tabla(self.tablaPant_19_bobst_i, "b", "obst,i,ref", "mm")
        self.limpiar_tabla(self.tablaPant_20_bobst_a_hmax, "b", "obst,a", "(mm)")
        self.limpiar_tabla(self.tablaPant_21_bobst_i_hmax, "b", "obst,i", "(mm)")
        self.limpiar_tabla(self.tablaPant_22_bobst_a_hmax_heff_elec, "b", "obst,a,heff", "(mm)")
        self.limpiar_tabla(self.tablaPant_23_bobst_i_hmax_heff_elec, "b", "obst,i,heff", "(mm)")
        self.limpiar_tabla(self.tablaPant_24_bobst_a_hmax_elec, "b", "obst,a,elec", "(mm)")
        self.limpiar_tabla(self.tablaPant_25_bobst_i_hmax_elec, "b", "obst,i,elec", "(mm)")
        self.limpiar_tabla(self.tablaPant_26_X_mec, "X", "mec", "(mm)")
        self.limpiar_tabla(self.tablaPant_27_Y_mec, "Y", "mec", "(mm)")
        self.limpiar_tabla(self.tablaPant_28_X_elec, "X", "elec", "(mm)")
        self.limpiar_tabla(self.tablaPant_29_Y_elec, "Y", "elec", "(mm)")

fttabla_1 = ftTabla()
fttabla_2 = ftTabla()
fttablaPant_1 = ftTablaPant()
fttablaPant_2 = ftTablaPant()

class Tabla_Var(ft.ResponsiveRow):
    def __init__(self, ftt):
        super().__init__()
        self.controls = [
            ft.Column([
                ft.Text("Salientes", size = Tamanyos.MEDIANO.value),
                MiFilaDatos2("Radio de curvatura, planta", "R", "",  "m", ftt.t_R),
                MiFilaDatos2("Radio de curvatura, alzado", "R", "V",  "m", ftt.t_RV),
                MiFilaDatos2("Ancho de vía nominal", "l", "N", "m", ftt.t_LN),
                MiFilaDatos2("Sobreancho máximo", "D", "l", "m", ftt.t_DL),
                MiFilaDatos2("Ancho de vía", "I", "", "m", ftt.t_LND),
                MiFilaDatos2("Desplazamiento por inscripción en acuerdos vert.", "D", "hRV", "m", ftt.t_DhRV),
            ],
            col=1,
            ),
            ft.Column([
                ft.Text("Desplazamientos cuasiestáticos laterales", size = Tamanyos.MEDIANO.value),
                MiFilaDatos2("Peralte de la vía", "D", "", "m", ftt.t_D),
                MiFilaDatos2("Peralte por convenio de la vía", "D", "0", "m", ftt.t_D0),
                MiFilaDatos2("Peralte de equilibrio", "h", "eq", "m", ftt.t_heq),
                MiFilaDatos2("Insuficiencia de peralte", "I", "", "m", ftt.t_I),
                MiFilaDatos2("Insuficiencia de peralte por convenio", "I", "0", "m", ftt.t_I0),
                MiFilaDatos2("Distancia entre círculos de rodadura", "L", "", "m", ftt.t_L),
                MiFilaDatos2("Altura del centro de balanceo, por convenio", "h", "co", "m", ftt.t_hco),
            ],
            col=1
            ),
            ft.Column([
                ft.Text("Desplazamientos cuasiestáticos laterales", size = Tamanyos.MEDIANO.value),
                MiFilaDatos2("Desplazaiento lateral de la vía", "T", "via", "m", ftt.t_tvia),
                MiFilaDatos2("Diferencia entre peralte real y teórico", "T", "D", "m", ftt.t_td),
                MiFilaDatos2("Velocidad máxima de la vía", "V", "max", "km/h", ftt.t_vmax),
                MiFilaDatos2("Tolerancias en el reglaje de la suspensión", "α", "susp", "º", ftt.t_asusp),
                MiFilaDatos2("Reparto desigual de cargas", "α", "carga", "º", ftt.t_acarga),
                MiFilaDatos2("Giro total", "η", "0", "º", ftt.t_eta0),
                MiFilaDatos2("Giro por oscilaciones aleatorias por irreg. de la vía", "α", "osc,i,s0=0,4", "º", ftt.t_aosc_i_s0_04b),
                MiFilaDatos2("", "α", "osc,i,s0=0,3", "º", ftt.t_aosc_i_s0_03b),
                MiFilaDatos2("", "α", "osc,a,s0=0,4", "º", ftt.t_aosc_a_s0_04b),
                MiFilaDatos2("", "α", "osc,a,s0=0,3", "º", ftt.t_aosc_a_s0_03b),
            ],
            col=1
            ),
            ft.Column([
                ft.Text("Pantógrafo", size = Tamanyos.MEDIANO.value),
                MiFilaDatos2("Semiancho de la mesilla", "b", "w", "m", ftt.t_bw),
                MiFilaDatos2("Desplazamiento lateral máximo", "e", "po", "m", ftt.t_epo),
                MiFilaDatos2("", "e", "pu", "m", ftt.t_epu),
                MiFilaDatos2("Peralte por convenio de la vía", "D'", "0", "m", ftt.t_D0p),
                MiFilaDatos2("Insuficiencia de peralte por convenio", "I", "0", "m", ftt.t_I0p),
                MiFilaDatos2("Coeficiente de flexibilidad del vehículo", "s'", "0", "m", ftt.t_s0p),
                MiFilaDatos2("Proyección del ancho del trocador", "c", "w", "m", ftt.t_cw),
                MiFilaDatos2("Aislamiento eléctrico estático", "b", "elec,estat,i", "m", ftt.t_belec_estat),
                MiFilaDatos2("Aislamiento eléctrico dinámico", "α", "elec,dinam,a", "m", ftt.t_belec_dinam),
                MiFilaDatos2("Elevación del hilo de contacto, vmax", "f", "s,vmax", "m", ftt.t_fsvmax),
                MiFilaDatos2("Elevación del hilo de contacto, vmin", "f", "s,vmin", "m", ftt.t_fsvmin),
                MiFilaDatos2("Elevación por desgaste de pletina y flexibilidad", "f", "wswa", "m", ftt.t_fwswa),
                # MiFilaDatos2("Altura máxima del gálibo mecánico, vmax", "h", "eff,vmax", "m", ftt.t_heffvmax),
                # MiFilaDatos2("Altura del gálibo eléctrico, vmax", "h", "eff,elec,vmax", "m", ftt.t_heffelecvmax),
                # MiFilaDatos2("Altura máxima del gálibo mecánico, vmin", "h", "eff,vmin", "m", ftt.t_heffvmin),
                # MiFilaDatos2("Altura del gálibo eléctrico, vmin", "h", "eff,elec,vmin", "m", ftt.t_heffelecvmin),
                MiFilaDatos2("Altura máxima del gálibo mecánico", "h", "eff", "m", ftt.t_heff),
                MiFilaDatos2("Altura máxima del gálibo eléctrico", "h", "eff,elec", "m", ftt.t_heffelec),
            ],
            col=1
            ),
        ]
        self.columns=4
        
class Tabla_Des(ft.ResponsiveRow):
        def __init__(self, fttabla):
            super().__init__()
            self.controls = [
                fttabla.tabla_00_Punto_des,
                fttabla.tabla_01_X_des,
                fttabla.tabla_02_Y_des,
                fttabla.tabla_03_esPT,
                fttabla.tabla_04_k,
                fttabla.tabla_05_s0,
                fttabla.tabla_06_Sa,
                fttabla.tabla_07_Si,
                fttabla.tabla_08_qsDai,
                fttabla.tabla_09_qsIai,
                fttabla.tabla_10_Tvia_ai,
                fttabla.tabla_11_Dbgai,
                fttabla.tabla_12_Dbcai,
                fttabla.tabla_13_Dbsuspai,
                fttabla.tabla_14_Dbcargaai,
                fttabla.tabla_15_Dbetaai,
                fttabla.tabla_16_aosca,
                fttabla.tabla_17_aosci,
                fttabla.tabla_18_Dbosca,
                fttabla.tabla_19_Dbosci,
                fttabla.tabla_20_M3h,
                fttabla.tabla_21_DhRv,
                fttabla.tabla_22_DhPTDai,
                fttabla.tabla_23_DhPTIai,
                fttabla.tabla_24_TN,
                fttabla.tabla_25_Dhga,
                fttabla.tabla_26_Dhgi,
                fttabla.tabla_27_Dhc,
                fttabla.tabla_28_Dhgca,
                fttabla.tabla_29_Dhgci,
                fttabla.tabla_30_Dhsuspai,
                fttabla.tabla_31_Dhcargai,
                fttabla.tabla_32_Dhetaai,
                fttabla.tabla_33_Dhosca,
                fttabla.tabla_34_Dhosci,
                fttabla.tabla_35_M3h,
            ]
            self.columns=36

class Tabla_Lim(ft.ResponsiveRow):
        def __init__(self, fttabla):
            super().__init__()
            self.controls = [
                fttabla.tabla_00_Punto_lim,
                fttabla.tabla_01_X_lim,
                fttabla.tabla_02_Y_lim,
                fttabla.tabla_36_lim_Sja1,
                fttabla.tabla_37_lim_Sji1,
                fttabla.tabla_38_lim_Sja2,
                fttabla.tabla_39_lim_Sji2,
                fttabla.tabla_40_lim_Sja1_ast,
                fttabla.tabla_41_lim_Sji1_ast,
                fttabla.tabla_42_lim_Sja2_ast,
                fttabla.tabla_43_lim_Sji2_ast,
                fttabla.tabla_44_lim_SVa1,
                fttabla.tabla_45_lim_SVi1,
                fttabla.tabla_46_lim_SVa2,
                fttabla.tabla_47_lim_SVi2,
                fttabla.tabla_48_lim_SVa1_ast,
                fttabla.tabla_49_lim_SVi1_ast,
                fttabla.tabla_50_lim_SVa2_ast,
                fttabla.tabla_51_lim_SVi2_ast,
                fttabla.tabla_68_lim_bobstVM_max_i,
                fttabla.tabla_69_lim_hobstVM_con_i,
                fttabla.tabla_70_lim_bobstVM_max_a,
                fttabla.tabla_71_lim_hobstVM_con_a,
                fttabla.tabla_72_lim_bobstVM_con_i,
                fttabla.tabla_73_lim_hobstVM_max_i,
                fttabla.tabla_74_lim_bobstVM_con_a,
                fttabla.tabla_75_lim_hobstVM_max_a,
                fttabla.tabla_76_lim_bobstV0_max_i,
                fttabla.tabla_77_lim_hobstV0_con_i,
                fttabla.tabla_78_lim_bobstV0_max_a,
                fttabla.tabla_79_lim_hobstV0_con_a,
                fttabla.tabla_80_lim_bobstV0_con_i,
                fttabla.tabla_81_lim_hobstV0_max_i,
                fttabla.tabla_82_lim_bobstV0_con_a,
                fttabla.tabla_83_lim_hobstV0_max_a,
                fttabla.tabla_100_lim_ba,
                fttabla.tabla_101_lim_ha,
                fttabla.tabla_102_lim_bi,
                fttabla.tabla_103_lim_hi,
            ]
            self.columns = 39

class Tabla_Nom(ft.ResponsiveRow):
        def __init__(self, fttabla):
            super().__init__()
            self.controls = [
                fttabla.tabla_00_Punto_nom,
                fttabla.tabla_01_X_nom,
                fttabla.tabla_02_Y_nom,
                fttabla.tabla_52_nom_Sja3,
                fttabla.tabla_53_nom_Sji3,
                fttabla.tabla_54_nom_Sja4,
                fttabla.tabla_55_nom_Sji4,
                fttabla.tabla_56_nom_Sja3_ast,
                fttabla.tabla_57_nom_Sji3_ast,
                fttabla.tabla_58_nom_Sja4_ast,
                fttabla.tabla_59_nom_Sji4_ast,
                fttabla.tabla_60_nom_SVa3,
                fttabla.tabla_61_nom_SVi3,
                fttabla.tabla_62_nom_SVa4,
                fttabla.tabla_63_nom_SVi4,
                fttabla.tabla_64_nom_SVa3_ast,
                fttabla.tabla_65_nom_SVi3_ast,
                fttabla.tabla_66_nom_SVa4_ast,
                fttabla.tabla_67_nom_SVi4_ast,
                fttabla.tabla_84_nom_bobstVM_max_i,
                fttabla.tabla_85_nom_hobstVM_con_i,
                fttabla.tabla_86_nom_bobstVM_max_a,
                fttabla.tabla_87_nom_hobstVM_con_a,
                fttabla.tabla_88_nom_bobstVM_con_i,
                fttabla.tabla_89_nom_hobstVM_max_i,
                fttabla.tabla_90_nom_bobstVM_con_a,
                fttabla.tabla_91_nom_hobstVM_max_a,
                fttabla.tabla_92_nom_bobstV0_max_i,
                fttabla.tabla_93_nom_hobstV0_con_i,
                fttabla.tabla_94_nom_bobstV0_max_a,
                fttabla.tabla_95_nom_hobstV0_con_a,
                fttabla.tabla_96_nom_bobstV0_con_i,
                fttabla.tabla_97_nom_hobstV0_max_i,
                fttabla.tabla_98_nom_bobstV0_con_a,
                fttabla.tabla_99_nom_hobstV0_max_a,
                fttabla.tabla_104_nom_ba,
                fttabla.tabla_105_nom_ha,
                fttabla.tabla_106_nom_bi,
                fttabla.tabla_107_nom_hi,
            ]
            self.columns = 39

class Tabla_Pant(ft.ResponsiveRow):
        def __init__(self, fttablaPant):
            super().__init__()
            self.controls = [
                fttablaPant.tablaPant_00_Punto,
                fttablaPant.tablaPant_01_X_ref,
                fttablaPant.tablaPant_02_Y_ref,
                fttablaPant.tablaPant_03_Sai,
                fttablaPant.tablaPant_04_qsa,
                fttablaPant.tablaPant_05_qsi,
                fttablaPant.tablaPant_06_Dbgai,
                fttablaPant.tablaPant_07_Dbcai,
                fttablaPant.tablaPant_08_Dbsuspai,
                fttablaPant.tablaPant_09_Dbcargai,
                fttablaPant.tablaPant_10_Dbetaai,
                fttablaPant.tablaPant_11_aosca,
                fttablaPant.tablaPant_12_aosci,
                fttablaPant.tablaPant_13_Dbosca,
                fttablaPant.tablaPant_14_Dbosci,
                fttablaPant.tablaPant_15_TVia,
                fttablaPant.tablaPant_16_Sja,
                fttablaPant.tablaPant_17_Sji,
                fttablaPant.tablaPant_18_bobst_a,
                fttablaPant.tablaPant_19_bobst_i,
                fttablaPant.tablaPant_20_bobst_a_hmax,
                fttablaPant.tablaPant_21_bobst_i_hmax,
                fttablaPant.tablaPant_22_bobst_a_hmax_heff_elec,
                fttablaPant.tablaPant_23_bobst_i_hmax_heff_elec,
                fttablaPant.tablaPant_24_bobst_a_hmax_elec,
                fttablaPant.tablaPant_25_bobst_i_hmax_elec,
                fttablaPant.tablaPant_26_X_mec,
                fttablaPant.tablaPant_27_Y_mec,
                fttablaPant.tablaPant_28_X_elec,
                fttablaPant.tablaPant_29_Y_elec,
            ]
            self.columns = 30

tabla_var_1 = Tabla_Var(ftt_1)
tabla_var_2 = Tabla_Var(ftt_2)
tabla_des_1 = Tabla_Des(fttabla_1)
tabla_des_2 = Tabla_Des(fttabla_2)
tabla_lim_1 = Tabla_Lim(fttabla_1)
tabla_lim_2 = Tabla_Lim(fttabla_2)
tabla_nom_1 = Tabla_Nom(fttabla_1)
tabla_nom_2 = Tabla_Nom(fttabla_2)
tabla_pant_1 = Tabla_Pant(fttablaPant_1)
tabla_pant_2 = Tabla_Pant(fttablaPant_2)
