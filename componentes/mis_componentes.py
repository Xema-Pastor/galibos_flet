import flet as ft
from estilos.estilos import Tamanyos

class MiFila(ft.Row):
    def __init__(self, text1, text2, tamanyo_texto, tamanyo_sub):
        super().__init__()
        self.text_1 = ft.Text(text1, size=tamanyo_texto)
        self.text_2 = ft.Text(text2, size=tamanyo_sub)
        self.spacing = 0
        self.vertical_alignment = ft.CrossAxisAlignment.END
        self.alignment = ft.MainAxisAlignment.END

        self.controls = [
            self.text_1,
            self.text_2,
        ]

class MiText(ft.Column):
    def __init__(self, text1, text2, tamanyo_texto = Tamanyos.TABLA_NORMAL.value, tamanyo_sub = Tamanyos.TABLA_SUBTITULO.value):
        super().__init__()
        self.texto = MiFila(text1, text2, tamanyo_texto, tamanyo_sub)

        self.controls = [
            self.texto
        ]
    
class MiColumnaTabla(ft.Column):
    def __init__(self):
        super().__init__()
        self.col = 1
        self.spacing = 8
        self.horizontal_alignment = ft.CrossAxisAlignment.END

class MiFilaDatos(ft.Row):
    def __init__(self, texto, abreviatura, unidades, componente):
        super().__init__()
        self.controls = [
            ft.Text(texto,width=350),
            ft.Text(abreviatura,width=100),
            componente,
            ft.Text(unidades,width=60),
        ]

class MiFilaDatos2(ft.Row):
    def __init__(self, texto, abreviatura, abreviatura_sub, unidades, componente):
        super().__init__()
        mitext =  MiText(abreviatura, abreviatura_sub, Tamanyos.NORMAL.value, Tamanyos.TABLA_SUBTITULO.value)
        mitext.width = 50
        self.controls = [
            ft.Text(texto,width=300),
            mitext,
            #ft.Text(abreviatura,width=100),
            ft.Text("="),
            componente,
            ft.Text(unidades,width=40),
        ]

class MiEtiquetaPestanya(ft.Row):
    def __init__(self, texto, accion):
        super().__init__()
        mitext = ft.Text(texto)
        self.controls = [
            mitext,
            ft.IconButton(
                            icon = ft.icons.CONTENT_COPY,
                            icon_size = 15,
                            tooltip = f"Copiar {texto}",
                            data = texto,
                            on_click = accion)
            ]
        