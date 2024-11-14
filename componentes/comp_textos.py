import flet as ft
from dataclasses import dataclass
from datos_variables import var

@dataclass
class ftText:
    t_R = ft.Text(var.R,width=50)
    t_RV = ft.Text(var.R,width=50)
    t_LN = ft.Text(var.LN,width=50)
    t_DL = ft.Text(var.DL,width=50)
    t_LND = ft.Text(var.LND,width=50)
    t_DhRV = ft.Text(var.LND,width=50)

    t_D = ft.Text(var.D,width=50)
    t_D0 = ft.Text(var.D0,width=50)
    t_heq = ft.Text(var.heq,width=50)
    t_I = ft.Text(var.I,width=50)
    t_I0 = ft.Text(var.I0,width=50)
    t_L = ft.Text(var.L,width=50)
    t_hco = ft.Text(var.hco,width=50)

    t_tvia = ft.Text(var.TVIA,width=50)
    t_td = ft.Text(var.TD,width=50)
    t_vmax = ft.Text(var.vmax,width=50)
    t_asusp = ft.Text(var.asusp,width=50)
    t_acarga = ft.Text(var.acarga,width=50)
    t_eta0 = ft.Text(var.eta0,width=50)
    t_aosc_i_s0_04b = ft.Text(var.aosc_i_s0_04b,width=50)
    t_aosc_i_s0_03b = ft.Text(var.aosc_i_s0_03b,width=50)
    t_aosc_a_s0_04b = ft.Text(var.aosc_a_s0_04b,width=50)
    t_aosc_a_s0_03b = ft.Text(var.aosc_a_s0_03b,width=50)

ftt = ftText()