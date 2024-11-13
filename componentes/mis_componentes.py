import flet as ft
from estilos.estilos import Tamanyos

class MiFila(ft.Row):
    def __init__(self, text1, text2):
        super().__init__()
        self.text_1 = ft.Text(text1, size=Tamanyos.TABLA_NORMAL.value)
        self.text_2 = ft.Text(text2, size=Tamanyos.TABLA_SUBTITULO.value)
        self.spacing = 0
        self.vertical_alignment = ft.CrossAxisAlignment.END
        self.alignment = ft.MainAxisAlignment.END

        self.controls = [
            self.text_1,
            self.text_2,
        ]

class MiText(ft.Column):
    def __init__(self, text1, text2):
        super().__init__()
        self.texto = MiFila(text1, text2)

        self.controls = [
            self.texto
        ]
    
class MiColumnaTabla(ft.Column):
    def __init__(self):
        super().__init__()
        self.col = 1
        self.spacing = 8
        self.horizontal_alignment = ft.CrossAxisAlignment.END
