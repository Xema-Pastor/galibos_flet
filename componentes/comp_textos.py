import flet as ft
from dataclasses import dataclass
from datos_variables import via1, via2

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

ftt_1 = ftText(via1)
ftt_2 = ftText(via2)