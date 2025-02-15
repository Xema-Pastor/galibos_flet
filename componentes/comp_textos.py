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