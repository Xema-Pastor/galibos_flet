"""Pestaña "?": logo, versión de la aplicación y persona de contacto."""
import flet as ft

from configuracion import NOMBRE_PROGRAMA, VERSION, CONTACTO_NOMBRE, CONTACTO_CORREO

LOGO = "typsa_logo.png"     # En la carpeta assets


def contenido_acerca() -> ft.Column:
    # Dentro de ft.Tabs el contenido debe ir en una Column con expand (como las demás pestañas):
    # un Container con una Row directamente no se llega a dibujar
    return ft.Column(expand=1, scroll=ft.ScrollMode.AUTO, controls=[_ficha()])


def _ficha() -> ft.Container:
    return ft.Container(
        padding=20,
        content=ft.Row(
            spacing=30,
            vertical_alignment=ft.CrossAxisAlignment.CENTER,
            controls=[
                ft.Image(src=LOGO, width=150, height=150, fit=ft.ImageFit.CONTAIN),
                ft.Column(
                    # expand: dentro de una Row el ancho no está acotado; sin esto el Divider
                    # pide ancho infinito, Flutter falla al maquetar y la pestaña se ve vacía
                    expand=True,
                    spacing=8,
                    controls=[
                        ft.Text(NOMBRE_PROGRAMA, size=18, weight=ft.FontWeight.BOLD),
                        ft.Text(f"Versión {VERSION}", size=14),
                        ft.Divider(height=20),
                        ft.Text("Contacto", size=14, weight=ft.FontWeight.BOLD),
                        ft.Text(CONTACTO_NOMBRE, size=14),
                        ft.Text(spans=[ft.TextSpan(
                            CONTACTO_CORREO,
                            url=f"mailto:{CONTACTO_CORREO}",
                            style=ft.TextStyle(color=ft.colors.BLUE_300,
                                               decoration=ft.TextDecoration.UNDERLINE),
                        )], size=14),
                    ],
                ),
            ],
        ),
    )
