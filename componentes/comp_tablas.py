import flet as ft
from dataclasses import dataclass
from componentes.mis_componentes import MiColumnaTabla, MiText
from estilos.estilos import Tamanyos

#COMPONENTES DE TABLAS
@dataclass
class ftTabla:
    tabla_00_Punto_des = MiColumnaTabla()
    tabla_00_Punto_lim = MiColumnaTabla()
    tabla_00_Punto_nom = MiColumnaTabla()
    tabla_01_X_des = MiColumnaTabla()
    tabla_01_X_lim = MiColumnaTabla()
    tabla_01_X_nom = MiColumnaTabla()
    tabla_02_Y_des = MiColumnaTabla()
    tabla_02_Y_lim = MiColumnaTabla()
    tabla_02_Y_nom = MiColumnaTabla()
    tabla_03_esPT = MiColumnaTabla()
    tabla_04_k = MiColumnaTabla()
    tabla_05_s0 = MiColumnaTabla()
    tabla_06_Sa = MiColumnaTabla()
    tabla_07_Si = MiColumnaTabla()
    tabla_08_qsDai = MiColumnaTabla()
    tabla_09_qsIai = MiColumnaTabla()
    tabla_10_Tvia_ai = MiColumnaTabla()
    tabla_11_Dbgai = MiColumnaTabla()
    tabla_12_Dbcai = MiColumnaTabla()
    tabla_13_Dbsuspai = MiColumnaTabla()
    tabla_14_Dbcargaai = MiColumnaTabla()
    tabla_15_Dbetaai = MiColumnaTabla()
    tabla_16_aosca = MiColumnaTabla()
    tabla_17_aosci = MiColumnaTabla()
    tabla_18_Dbosca = MiColumnaTabla()
    tabla_19_Dbosci = MiColumnaTabla()
    tabla_20_M3h = MiColumnaTabla()
    tabla_21_DhRv = MiColumnaTabla()
    tabla_22_DhPTDai = MiColumnaTabla()
    tabla_23_DhPTIai = MiColumnaTabla()
    tabla_24_TN = MiColumnaTabla()
    tabla_25_Dhga = MiColumnaTabla()
    tabla_26_Dhgi = MiColumnaTabla()
    tabla_27_Dhc = MiColumnaTabla()
    tabla_28_Dhgca = MiColumnaTabla()
    tabla_29_Dhgci = MiColumnaTabla()
    tabla_30_Dhsuspai = MiColumnaTabla()
    tabla_31_Dhcargai = MiColumnaTabla()
    tabla_32_Dhetaai = MiColumnaTabla()
    tabla_33_Dhosca = MiColumnaTabla()
    tabla_34_Dhosci = MiColumnaTabla()
    tabla_35_M3h = MiColumnaTabla()
    tabla_36_lim_Sja1 = MiColumnaTabla()
    tabla_37_lim_Sji1 = MiColumnaTabla()
    tabla_38_lim_Sja2 = MiColumnaTabla()
    tabla_39_lim_Sji2 = MiColumnaTabla()
    tabla_40_lim_Sja1_ast = MiColumnaTabla()
    tabla_41_lim_Sji1_ast = MiColumnaTabla()
    tabla_42_lim_Sja2_ast = MiColumnaTabla()
    tabla_43_lim_Sji2_ast = MiColumnaTabla()
    tabla_44_lim_SVa1 = MiColumnaTabla()
    tabla_45_lim_SVi1 = MiColumnaTabla()
    tabla_46_lim_SVa2 = MiColumnaTabla()
    tabla_47_lim_SVi2 = MiColumnaTabla()
    tabla_48_lim_SVa1_ast = MiColumnaTabla()
    tabla_49_lim_SVi1_ast = MiColumnaTabla()
    tabla_50_lim_SVa2_ast = MiColumnaTabla()
    tabla_51_lim_SVi2_ast = MiColumnaTabla()
    tabla_52_nom_Sja3 = MiColumnaTabla()
    tabla_53_nom_Sji3 = MiColumnaTabla()
    tabla_54_nom_Sja4 = MiColumnaTabla()
    tabla_55_nom_Sji4 = MiColumnaTabla()
    tabla_56_nom_Sja3_ast = MiColumnaTabla()
    tabla_57_nom_Sji3_ast = MiColumnaTabla()
    tabla_58_nom_Sja4_ast = MiColumnaTabla()
    tabla_59_nom_Sji4_ast = MiColumnaTabla()
    tabla_60_nom_SVa3 = MiColumnaTabla()
    tabla_61_nom_SVi3 = MiColumnaTabla()
    tabla_62_nom_SVa4 = MiColumnaTabla()
    tabla_63_nom_SVi4 = MiColumnaTabla()
    tabla_64_nom_SVa3_ast = MiColumnaTabla()
    tabla_65_nom_SVi3_ast = MiColumnaTabla()
    tabla_66_nom_SVa4_ast = MiColumnaTabla()
    tabla_67_nom_SVi4_ast = MiColumnaTabla()
    tabla_68_lim_bobstVM_max_i = MiColumnaTabla()
    tabla_69_lim_hobstVM_con_i = MiColumnaTabla()
    tabla_70_lim_bobstVM_max_a = MiColumnaTabla()
    tabla_71_lim_hobstVM_con_a = MiColumnaTabla()
    tabla_72_lim_bobstVM_con_i = MiColumnaTabla()
    tabla_73_lim_hobstVM_max_i = MiColumnaTabla()
    tabla_74_lim_bobstVM_con_a = MiColumnaTabla()
    tabla_75_lim_hobstVM_max_a = MiColumnaTabla()
    tabla_76_lim_bobstV0_max_i = MiColumnaTabla()
    tabla_77_lim_hobstV0_con_i = MiColumnaTabla()
    tabla_78_lim_bobstV0_max_a = MiColumnaTabla()
    tabla_79_lim_hobstV0_con_a = MiColumnaTabla()
    tabla_80_lim_bobstV0_con_i = MiColumnaTabla()
    tabla_81_lim_hobstV0_max_i = MiColumnaTabla()
    tabla_82_lim_bobstV0_con_a = MiColumnaTabla()
    tabla_83_lim_hobstV0_max_a = MiColumnaTabla()
    tabla_84_nom_bobstVM_max_i = MiColumnaTabla()
    tabla_85_nom_hobstVM_con_i = MiColumnaTabla()
    tabla_86_nom_bobstVM_max_a = MiColumnaTabla()
    tabla_87_nom_hobstVM_con_a = MiColumnaTabla()
    tabla_88_nom_bobstVM_con_i = MiColumnaTabla()
    tabla_89_nom_hobstVM_max_i = MiColumnaTabla()
    tabla_90_nom_bobstVM_con_a = MiColumnaTabla()
    tabla_91_nom_hobstVM_max_a = MiColumnaTabla()
    tabla_92_nom_bobstV0_max_i = MiColumnaTabla()
    tabla_93_nom_hobstV0_con_i = MiColumnaTabla()
    tabla_94_nom_bobstV0_max_a = MiColumnaTabla()
    tabla_95_nom_hobstV0_con_a = MiColumnaTabla()
    tabla_96_nom_bobstV0_con_i = MiColumnaTabla()
    tabla_97_nom_hobstV0_max_i = MiColumnaTabla()
    tabla_98_nom_bobstV0_con_a = MiColumnaTabla()
    tabla_99_nom_hobstV0_max_a = MiColumnaTabla()

    def limpiar_tabla(self,elemento: ft.Column, text1: str, text2: str, unidades: str):
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

fttabla = ftTabla()

tabla_des = ft.ResponsiveRow([
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
],
columns=36)

tabla_lim = ft.ResponsiveRow([
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
],
columns=35)

tabla_nom = ft.ResponsiveRow([
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
    ftTabla.tabla_99_nom_hobstV0_max_a,
],
columns=35,)
