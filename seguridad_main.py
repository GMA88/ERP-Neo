# gui/seguridad/seguridad_main.py
import flet as ft

# 1️⃣ Importaciones estáticas de los sub-módulos
from gui.seguridad.accesos_window          import mostrar_accesos_page
from gui.seguridad.incidencias_window      import mostrar_incidencias_page
from gui.seguridad.bitacora_window         import mostrar_bitacora_page
from gui.seguridad.reportes_graficas_window import mostrar_reportes_graficas_page

from gui.utils.logo_utils import get_logo_image
# (no importamos main_window aquí → se hace diferido)

def mostrar_seguridad_main(page: ft.Page):
    page.title = "Seguridad"
    page.controls.clear()

    # Logo corporativo
    page.controls.append(get_logo_image())

    page.appbar = ft.AppBar(title=ft.Text("Módulo de Seguridad"))

    # Callback diferido para romper ciclo main_window ↔ seguridad_main
    def volver_menu_principal(e):
        from gui.main_window import mostrar_main         # import tardío
        mostrar_main(page, "seguridad")

    page.controls.append(
        ft.Column(
            [
                ft.Text("Seleccione un submódulo de Seguridad",
                        style="titleMedium"),
                ft.ElevatedButton("Control de Accesos",
                                  on_click=lambda e: mostrar_accesos_page(page)),
                ft.ElevatedButton("Incidencias",
                                  on_click=lambda e: mostrar_incidencias_page(page)),
                ft.ElevatedButton("Bitácora",
                                  on_click=lambda e: mostrar_bitacora_page(page)),
                ft.ElevatedButton("Reportes y Gráficas",
                                  on_click=lambda e: mostrar_reportes_graficas_page(page)),
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
