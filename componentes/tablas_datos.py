import flet as ft

def tabla_3221():
    return ft.DataTable(
            columns = [
                ft.DataColumn(ft.Text("3.2.2.1.- Salientes", size=15)),
                ft.DataColumn(ft.Text("")),
                ft.DataColumn(ft.Text("")),
                ft.DataColumn(ft.Text("")),
            ],
            rows = [
                ft.DataRow([
                    ft.DataCell(ft.Text("Radio de curvatura"),),
                    ft.DataCell(ft.Text("R="),),
                    ft.DataCell(ft.Text("Variable1"),),
                    ft.DataCell(ft.Text("m"),),
            ]),
                ft.DataRow([
                    ft.DataCell(ft.Text("Ancho de vía nominal"),),
                    ft.DataCell(ft.Text("lN="),),
                    ft.DataCell(ft.Text("Variable2"),),
                    ft.DataCell(ft.Text("m"),),
            ]),
                ft.DataRow([
                    ft.DataCell(ft.Text("Sobreancho máximo"),),
                    ft.DataCell(ft.Text("Dl="),),
                    ft.DataCell(ft.Text("Variable3"),),
                    ft.DataCell(ft.Text("m"),),
            ]),
                ft.DataRow([
                    ft.DataCell(ft.Text("Ancho de vía"),),
                    ft.DataCell(ft.Text("I=Dl+lN="),),
                    ft.DataCell(ft.Text("Variable4"),),
                    ft.DataCell(ft.Text("m"),),
            ]),
            ])

def tabla_3222():
    return ft.DataTable(
            columns = [
                ft.DataColumn(ft.Text("3.2.2.2.- Desplazamientos cuasiestáticos laterales", size=15)),
                ft.DataColumn(ft.Text("")),
                ft.DataColumn(ft.Text("")),
                ft.DataColumn(ft.Text("")),
            ],
            rows = [
                ft.DataRow([
                    ft.DataCell(ft.Text("Peralte de la vía"),),
                    ft.DataCell(ft.Text("D="),),
                    ft.DataCell(ft.Text("Variable1"),),
                    ft.DataCell(ft.Text("m"),),
            ]),
                ft.DataRow([
                    ft.DataCell(ft.Text("Peralte por convenio de la vía"),),
                    ft.DataCell(ft.Text("D0="),),
                    ft.DataCell(ft.Text("Variable2"),),
                    ft.DataCell(ft.Text("m"),),
            ]),
                ft.DataRow([
                    ft.DataCell(ft.Text("Peralte de equilibrio"),),
                    ft.DataCell(ft.Text("heq="),),
                    ft.DataCell(ft.Text("Variable3"),),
                    ft.DataCell(ft.Text("m"),),
            ]),
                ft.DataRow([
                    ft.DataCell(ft.Text("Insuficiencia de peralte"),),
                    ft.DataCell(ft.Text("I="),),
                    ft.DataCell(ft.Text("Variable4"),),
                    ft.DataCell(ft.Text("m"),),
            ]),
                ft.DataRow([
                    ft.DataCell(ft.Text("Insuficiencia de peralte por convenio"),),
                    ft.DataCell(ft.Text("I0="),),
                    ft.DataCell(ft.Text("Variable5"),),
                    ft.DataCell(ft.Text("m"),),
            ]),
                ft.DataRow([
                    ft.DataCell(ft.Text("Distancia entre círculos de rodadura"),),
                    ft.DataCell(ft.Text("L="),),
                    ft.DataCell(ft.Text("Variable5"),),
                    ft.DataCell(ft.Text("m"),),
            ]),
                ft.DataRow([
                    ft.DataCell(ft.Text("Altura  del  centro  de  balanceo  del  vehículo, por convenio"),),
                    ft.DataCell(ft.Text("hco="),),
                    ft.DataCell(ft.Text("Variable6"),),
                    ft.DataCell(ft.Text("m"),),
            ]),
            ])

def tabla_3223():
    return ft.DataTable(
            columns = [
                ft.DataColumn(ft.Text("3.2.2.3.- Desplazamientos aleatorios laterales", size=15)),
                ft.DataColumn(ft.Text("")),
                ft.DataColumn(ft.Text("")),
                ft.DataColumn(ft.Text("")),
            ],
            rows = [
                ft.DataRow([
                    ft.DataCell(ft.Text("Tipo de vía"),),
                    ft.DataCell(ft.Text(""),),
                    ft.DataCell(ft.Text("Variable1"),),
                    ft.DataCell(ft.Text(""),),
            ]),
                ft.DataRow([
                    ft.DataCell(ft.Text("Desplazaiento lateral de la vía"),),
                    ft.DataCell(ft.Text("Tvia="),),
                    ft.DataCell(ft.Text("Variable2"),),
                    ft.DataCell(ft.Text("m"),),
            ]),
                ft.DataRow([
                    ft.DataCell(ft.Text("Diferencia entre peralte real y teórico"),),
                    ft.DataCell(ft.Text("TD="),),
                    ft.DataCell(ft.Text("Variable3"),),
                    ft.DataCell(ft.Text("m"),),
            ]),
                ft.DataRow([
                    ft.DataCell(ft.Text("Velocidad máxima de la vía"),),
                    ft.DataCell(ft.Text("V="),),
                    ft.DataCell(ft.Text("Variable4"),),
                    ft.DataCell(ft.Text("km/h"),),
            ]),
                ft.DataRow([
                    ft.DataCell(ft.Text("Tolerancias en el reglaje de la suspensión"),),
                    ft.DataCell(ft.Text("asusp="),),
                    ft.DataCell(ft.Text("Variable5"),),
                    ft.DataCell(ft.Text("º"),),
            ]),
                ft.DataRow([
                    ft.DataCell(ft.Text("Reparto desigual de cargas"),),
                    ft.DataCell(ft.Text("acarga="),),
                    ft.DataCell(ft.Text("Variable5"),),
                    ft.DataCell(ft.Text("º"),),
            ]),
                ft.DataRow([
                    ft.DataCell(ft.Text("Giro total"),),
                    ft.DataCell(ft.Text("n0="),),
                    ft.DataCell(ft.Text("Variable6"),),
                    ft.DataCell(ft.Text("º"),),
            ]),
                ft.DataRow([
                    ft.DataCell(ft.Text("Estado de la vía"),),
                    ft.DataCell(ft.Text(""),),
                    ft.DataCell(ft.Text("Variable6"),),
                    ft.DataCell(ft.Text(""),),
            ]),
                ft.DataRow([
                    ft.DataCell(ft.Text("Giro por oscilaciones aleatorias por irregularidades de la vía"),),
                    ft.DataCell(ft.Text("aosc,i,s0=0,4="),),
                    ft.DataCell(ft.Text("Variable6"),),
                    ft.DataCell(ft.Text("º"),),
            ]),
                ft.DataRow([
                    ft.DataCell(ft.Text(""),),
                    ft.DataCell(ft.Text("aosc,i,s0=0,3="),),
                    ft.DataCell(ft.Text("Variable6"),),
                    ft.DataCell(ft.Text("º"),),
            ]),
                ft.DataRow([
                    ft.DataCell(ft.Text(""),),
                    ft.DataCell(ft.Text("aosc,a,s0=0,4="),),
                    ft.DataCell(ft.Text("Variable6"),),
                    ft.DataCell(ft.Text("º"),),
            ]),
                ft.DataRow([
                    ft.DataCell(ft.Text(""),),
                    ft.DataCell(ft.Text("aosc,a,s0=0,3="),),
                    ft.DataCell(ft.Text("Variable6"),),
                    ft.DataCell(ft.Text("º"),),
            ]),
            ])
