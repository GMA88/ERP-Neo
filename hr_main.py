# gui/rrhh/rrhh_main.py
import flet as ft

# 1️⃣  Importaciones estáticas  –  PyInstaller las incluye
from gui.rrhh.empleados_window            import mostrar_empleados_page
from gui.rrhh.capacitaciones_window       import mostrar_capacitaciones_page
from gui.rrhh.eventos_window              import mostrar_eventos_page
from gui.rrhh.nomina_window               import mostrar_nomina_page
from gui.rrhh.reclutamiento_seguro_window import mostrar_reclutamiento_seguro_page

from gui.utils.logo_utils import get_logo_image
# (NO importamos main_window aquí ⇒ evitamos ciclo)

def mostrar_rrhh_main(page: ft.Page):
    page.title = "RRHH"
    page.controls.clear()

    # Logo
    page.controls.append(get_logo_image())

    page.appbar = ft.AppBar(title=ft.Text("Recursos Humanos"))

    # callback diferido para romper ciclo
    def volver_menu_principal(e):
        from gui.main_window import mostrar_main   # import tardío
        mostrar_main(page, "recursos_humanos")

    page.controls.append(
        ft.Column(
            [
                ft.Text("Seleccione un submódulo de RRHH",
                        style="titleMedium"),
                ft.ElevatedButton("Empleados",
                                  on_click=lambda e: mostrar_empleados_page(page)),
                ft.ElevatedButton("Capacitaciones",
                                  on_click=lambda e: mostrar_capacitaciones_page(page)),
                ft.ElevatedButton("Eventos",
                                  on_click=lambda e: mostrar_eventos_page(page)),
                ft.ElevatedButton("Nómina",
                                  on_click=lambda e: mostrar_nomina_page(page)),
                ft.ElevatedButton("Reclutamiento / Seguro",
                                  on_click=lambda e: mostrar_reclutamiento_seguro_page(page)),
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
