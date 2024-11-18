import flet as ft
from dataclasses import dataclass
from componentes.mis_componentes import MiColumnaTabla, MiText
from estilos.estilos import Tamanyos

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

fttabla_1 = ftTabla()
fttabla_2 = ftTabla()

tabla_des_1 = ft.ResponsiveRow([
    fttabla_1.tabla_00_Punto_des,
    fttabla_1.tabla_01_X_des,
    fttabla_1.tabla_02_Y_des,
    fttabla_1.tabla_03_esPT,
    fttabla_1.tabla_04_k,
    fttabla_1.tabla_05_s0,
    fttabla_1.tabla_06_Sa,
    fttabla_1.tabla_07_Si,
    fttabla_1.tabla_08_qsDai,
    fttabla_1.tabla_09_qsIai,
    fttabla_1.tabla_10_Tvia_ai,
    fttabla_1.tabla_11_Dbgai,
    fttabla_1.tabla_12_Dbcai,
    fttabla_1.tabla_13_Dbsuspai,
    fttabla_1.tabla_14_Dbcargaai,
    fttabla_1.tabla_15_Dbetaai,
    fttabla_1.tabla_16_aosca,
    fttabla_1.tabla_17_aosci,
    fttabla_1.tabla_18_Dbosca,
    fttabla_1.tabla_19_Dbosci,
    fttabla_1.tabla_20_M3h,
    fttabla_1.tabla_21_DhRv,
    fttabla_1.tabla_22_DhPTDai,
    fttabla_1.tabla_23_DhPTIai,
    fttabla_1.tabla_24_TN,
    fttabla_1.tabla_25_Dhga,
    fttabla_1.tabla_26_Dhgi,
    fttabla_1.tabla_27_Dhc,
    fttabla_1.tabla_28_Dhgca,
    fttabla_1.tabla_29_Dhgci,
    fttabla_1.tabla_30_Dhsuspai,
    fttabla_1.tabla_31_Dhcargai,
    fttabla_1.tabla_32_Dhetaai,
    fttabla_1.tabla_33_Dhosca,
    fttabla_1.tabla_34_Dhosci,
    fttabla_1.tabla_35_M3h,
],
columns=36)

tabla_lim_1 = ft.ResponsiveRow([
    fttabla_1.tabla_00_Punto_lim,
    fttabla_1.tabla_01_X_lim,
    fttabla_1.tabla_02_Y_lim,
    fttabla_1.tabla_36_lim_Sja1,
    fttabla_1.tabla_37_lim_Sji1,
    fttabla_1.tabla_38_lim_Sja2,
    fttabla_1.tabla_39_lim_Sji2,
    fttabla_1.tabla_40_lim_Sja1_ast,
    fttabla_1.tabla_41_lim_Sji1_ast,
    fttabla_1.tabla_42_lim_Sja2_ast,
    fttabla_1.tabla_43_lim_Sji2_ast,
    fttabla_1.tabla_44_lim_SVa1,
    fttabla_1.tabla_45_lim_SVi1,
    fttabla_1.tabla_46_lim_SVa2,
    fttabla_1.tabla_47_lim_SVi2,
    fttabla_1.tabla_48_lim_SVa1_ast,
    fttabla_1.tabla_49_lim_SVi1_ast,
    fttabla_1.tabla_50_lim_SVa2_ast,
    fttabla_1.tabla_51_lim_SVi2_ast,
    fttabla_1.tabla_68_lim_bobstVM_max_i,
    fttabla_1.tabla_69_lim_hobstVM_con_i,
    fttabla_1.tabla_70_lim_bobstVM_max_a,
    fttabla_1.tabla_71_lim_hobstVM_con_a,
    fttabla_1.tabla_72_lim_bobstVM_con_i,
    fttabla_1.tabla_73_lim_hobstVM_max_i,
    fttabla_1.tabla_74_lim_bobstVM_con_a,
    fttabla_1.tabla_75_lim_hobstVM_max_a,
    fttabla_1.tabla_76_lim_bobstV0_max_i,
    fttabla_1.tabla_77_lim_hobstV0_con_i,
    fttabla_1.tabla_78_lim_bobstV0_max_a,
    fttabla_1.tabla_79_lim_hobstV0_con_a,
    fttabla_1.tabla_80_lim_bobstV0_con_i,
    fttabla_1.tabla_81_lim_hobstV0_max_i,
    fttabla_1.tabla_82_lim_bobstV0_con_a,
    fttabla_1.tabla_83_lim_hobstV0_max_a,
    fttabla_1.tabla_100_lim_ba,
    fttabla_1.tabla_101_lim_ha,
    fttabla_1.tabla_102_lim_bi,
    fttabla_1.tabla_103_lim_hi,

],
columns=39)

tabla_nom_1 = ft.ResponsiveRow([
    fttabla_1.tabla_00_Punto_nom,
    fttabla_1.tabla_01_X_nom,
    fttabla_1.tabla_02_Y_nom,
    fttabla_1.tabla_52_nom_Sja3,
    fttabla_1.tabla_53_nom_Sji3,
    fttabla_1.tabla_54_nom_Sja4,
    fttabla_1.tabla_55_nom_Sji4,
    fttabla_1.tabla_56_nom_Sja3_ast,
    fttabla_1.tabla_57_nom_Sji3_ast,
    fttabla_1.tabla_58_nom_Sja4_ast,
    fttabla_1.tabla_59_nom_Sji4_ast,
    fttabla_1.tabla_60_nom_SVa3,
    fttabla_1.tabla_61_nom_SVi3,
    fttabla_1.tabla_62_nom_SVa4,
    fttabla_1.tabla_63_nom_SVi4,
    fttabla_1.tabla_64_nom_SVa3_ast,
    fttabla_1.tabla_65_nom_SVi3_ast,
    fttabla_1.tabla_66_nom_SVa4_ast,
    fttabla_1.tabla_67_nom_SVi4_ast,
    fttabla_1.tabla_84_nom_bobstVM_max_i,
    fttabla_1.tabla_85_nom_hobstVM_con_i,
    fttabla_1.tabla_86_nom_bobstVM_max_a,
    fttabla_1.tabla_87_nom_hobstVM_con_a,
    fttabla_1.tabla_88_nom_bobstVM_con_i,
    fttabla_1.tabla_89_nom_hobstVM_max_i,
    fttabla_1.tabla_90_nom_bobstVM_con_a,
    fttabla_1.tabla_91_nom_hobstVM_max_a,
    fttabla_1.tabla_92_nom_bobstV0_max_i,
    fttabla_1.tabla_93_nom_hobstV0_con_i,
    fttabla_1.tabla_94_nom_bobstV0_max_a,
    fttabla_1.tabla_95_nom_hobstV0_con_a,
    fttabla_1.tabla_96_nom_bobstV0_con_i,
    fttabla_1.tabla_97_nom_hobstV0_max_i,
    fttabla_1.tabla_98_nom_bobstV0_con_a,
    fttabla_1.tabla_99_nom_hobstV0_max_a,
    fttabla_1.tabla_104_nom_ba,
    fttabla_1.tabla_105_nom_ha,
    fttabla_1.tabla_106_nom_bi,
    fttabla_1.tabla_107_nom_hi,
],
columns=39,)

tabla_des_2 = ft.ResponsiveRow([
    fttabla_2.tabla_00_Punto_des,
    fttabla_2.tabla_01_X_des,
    fttabla_2.tabla_02_Y_des,
    fttabla_2.tabla_03_esPT,
    fttabla_2.tabla_04_k,
    fttabla_2.tabla_05_s0,
    fttabla_2.tabla_06_Sa,
    fttabla_2.tabla_07_Si,
    fttabla_2.tabla_08_qsDai,
    fttabla_2.tabla_09_qsIai,
    fttabla_2.tabla_10_Tvia_ai,
    fttabla_2.tabla_11_Dbgai,
    fttabla_2.tabla_12_Dbcai,
    fttabla_2.tabla_13_Dbsuspai,
    fttabla_2.tabla_14_Dbcargaai,
    fttabla_2.tabla_15_Dbetaai,
    fttabla_2.tabla_16_aosca,
    fttabla_2.tabla_17_aosci,
    fttabla_2.tabla_18_Dbosca,
    fttabla_2.tabla_19_Dbosci,
    fttabla_2.tabla_20_M3h,
    fttabla_2.tabla_21_DhRv,
    fttabla_2.tabla_22_DhPTDai,
    fttabla_2.tabla_23_DhPTIai,
    fttabla_2.tabla_24_TN,
    fttabla_2.tabla_25_Dhga,
    fttabla_2.tabla_26_Dhgi,
    fttabla_2.tabla_27_Dhc,
    fttabla_2.tabla_28_Dhgca,
    fttabla_2.tabla_29_Dhgci,
    fttabla_2.tabla_30_Dhsuspai,
    fttabla_2.tabla_31_Dhcargai,
    fttabla_2.tabla_32_Dhetaai,
    fttabla_2.tabla_33_Dhosca,
    fttabla_2.tabla_34_Dhosci,
    fttabla_2.tabla_35_M3h,
],
columns=36)

tabla_lim_2 = ft.ResponsiveRow([
    fttabla_2.tabla_00_Punto_lim,
    fttabla_2.tabla_01_X_lim,
    fttabla_2.tabla_02_Y_lim,
    fttabla_2.tabla_36_lim_Sja1,
    fttabla_2.tabla_37_lim_Sji1,
    fttabla_2.tabla_38_lim_Sja2,
    fttabla_2.tabla_39_lim_Sji2,
    fttabla_2.tabla_40_lim_Sja1_ast,
    fttabla_2.tabla_41_lim_Sji1_ast,
    fttabla_2.tabla_42_lim_Sja2_ast,
    fttabla_2.tabla_43_lim_Sji2_ast,
    fttabla_2.tabla_44_lim_SVa1,
    fttabla_2.tabla_45_lim_SVi1,
    fttabla_2.tabla_46_lim_SVa2,
    fttabla_2.tabla_47_lim_SVi2,
    fttabla_2.tabla_48_lim_SVa1_ast,
    fttabla_2.tabla_49_lim_SVi1_ast,
    fttabla_2.tabla_50_lim_SVa2_ast,
    fttabla_2.tabla_51_lim_SVi2_ast,
    fttabla_2.tabla_68_lim_bobstVM_max_i,
    fttabla_2.tabla_69_lim_hobstVM_con_i,
    fttabla_2.tabla_70_lim_bobstVM_max_a,
    fttabla_2.tabla_71_lim_hobstVM_con_a,
    fttabla_2.tabla_72_lim_bobstVM_con_i,
    fttabla_2.tabla_73_lim_hobstVM_max_i,
    fttabla_2.tabla_74_lim_bobstVM_con_a,
    fttabla_2.tabla_75_lim_hobstVM_max_a,
    fttabla_2.tabla_76_lim_bobstV0_max_i,
    fttabla_2.tabla_77_lim_hobstV0_con_i,
    fttabla_2.tabla_78_lim_bobstV0_max_a,
    fttabla_2.tabla_79_lim_hobstV0_con_a,
    fttabla_2.tabla_80_lim_bobstV0_con_i,
    fttabla_2.tabla_81_lim_hobstV0_max_i,
    fttabla_2.tabla_82_lim_bobstV0_con_a,
    fttabla_2.tabla_83_lim_hobstV0_max_a,
    fttabla_2.tabla_100_lim_ba,
    fttabla_2.tabla_101_lim_ha,
    fttabla_2.tabla_102_lim_bi,
    fttabla_2.tabla_103_lim_hi,
],
columns=39)

tabla_nom_2 = ft.ResponsiveRow([
    fttabla_2.tabla_00_Punto_nom,
    fttabla_2.tabla_01_X_nom,
    fttabla_2.tabla_02_Y_nom,
    fttabla_2.tabla_52_nom_Sja3,
    fttabla_2.tabla_53_nom_Sji3,
    fttabla_2.tabla_54_nom_Sja4,
    fttabla_2.tabla_55_nom_Sji4,
    fttabla_2.tabla_56_nom_Sja3_ast,
    fttabla_2.tabla_57_nom_Sji3_ast,
    fttabla_2.tabla_58_nom_Sja4_ast,
    fttabla_2.tabla_59_nom_Sji4_ast,
    fttabla_2.tabla_60_nom_SVa3,
    fttabla_2.tabla_61_nom_SVi3,
    fttabla_2.tabla_62_nom_SVa4,
    fttabla_2.tabla_63_nom_SVi4,
    fttabla_2.tabla_64_nom_SVa3_ast,
    fttabla_2.tabla_65_nom_SVi3_ast,
    fttabla_2.tabla_66_nom_SVa4_ast,
    fttabla_2.tabla_67_nom_SVi4_ast,
    fttabla_2.tabla_84_nom_bobstVM_max_i,
    fttabla_2.tabla_85_nom_hobstVM_con_i,
    fttabla_2.tabla_86_nom_bobstVM_max_a,
    fttabla_2.tabla_87_nom_hobstVM_con_a,
    fttabla_2.tabla_88_nom_bobstVM_con_i,
    fttabla_2.tabla_89_nom_hobstVM_max_i,
    fttabla_2.tabla_90_nom_bobstVM_con_a,
    fttabla_2.tabla_91_nom_hobstVM_max_a,
    fttabla_2.tabla_92_nom_bobstV0_max_i,
    fttabla_2.tabla_93_nom_hobstV0_con_i,
    fttabla_2.tabla_94_nom_bobstV0_max_a,
    fttabla_2.tabla_95_nom_hobstV0_con_a,
    fttabla_2.tabla_96_nom_bobstV0_con_i,
    fttabla_2.tabla_97_nom_hobstV0_max_i,
    fttabla_2.tabla_98_nom_bobstV0_con_a,
    fttabla_2.tabla_99_nom_hobstV0_max_a,
    fttabla_2.tabla_104_nom_ba,
    fttabla_2.tabla_105_nom_ha,
    fttabla_2.tabla_106_nom_bi,
    fttabla_2.tabla_107_nom_hi,
],
columns=39,)
