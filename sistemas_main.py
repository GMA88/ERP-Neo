# gui/sistemas/sistemas_main.py
import flet as ft

# 1️⃣  Importaciones estáticas de los sub-módulos
from gui.sistemas.analisis_datos_financieros_window import mostrar_analisis_page
from gui.sistemas.desarrollo_software_window        import mostrar_desarrollo_page
from gui.sistemas.diseno_ui_window                  import mostrar_diseno_page
from gui.sistemas.proyectos_electronica_window      import mostrar_proyectos_page

from gui.utils.logo_utils import get_logo_image
#  (no importamos main_window aquí para evitar ciclo)

def mostrar_sistemas_main(page: ft.Page):
    page.title = "Sistemas"
    page.controls.clear()

    # Logo corporativo
    page.controls.append(get_logo_image())

    page.appbar = ft.AppBar(title=ft.Text("Módulo de Sistemas"))

    # Import diferido para romper ciclo
    def volver_menu_principal(e):
        from gui.main_window import mostrar_main
        mostrar_main(page, "sistemas")

    page.controls.append(
        ft.Column(
            [
                ft.Text("Seleccione un submódulo de Sistemas",
                        style="titleMedium"),
                ft.ElevatedButton("Análisis de Datos Financieros",
                                  on_click=lambda e: mostrar_analisis_page(page)),
                ft.ElevatedButton("Desarrollo de Software",
                                  on_click=lambda e: mostrar_desarrollo_page(page)),
                ft.ElevatedButton("Diseño de UI",
                                  on_click=lambda e: mostrar_diseno_page(page)),
                ft.ElevatedButton("Proyectos de Electrónica",
                                  on_click=lambda e: mostrar_proyectos_page(page)),
                ft.Divider(),
                ft.ElevatedButton("← Volver al Menú Principal",
                                  on_click=volver_menu_principal),
            ],
            spacing=15,
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER
        )
    )
    page.update()
