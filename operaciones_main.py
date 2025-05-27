# gui/operaciones/operaciones_main.py
import flet as ft

# 1️⃣  Importaciones estáticas de los sub-módulos
from gui.operaciones.mantenimiento_window import mostrar_mantenimiento_page
from gui.operaciones.desarrollo_window    import mostrar_desarrollo_page

from gui.utils.logo_utils import get_logo_image
# (no importamos main_window aquí para evitar ciclo)


def mostrar_operaciones_main(page: ft.Page):
    page.title = "Operaciones"
    page.controls.clear()

    # Logo corporativo
    page.controls.append(get_logo_image())

    page.appbar = ft.AppBar(title=ft.Text("Módulo de Operaciones"))

    # Callback diferido para romper ciclo
    def volver_menu_principal(e):
        from gui.main_window import mostrar_main
        mostrar_main(page, "operaciones")

    page.controls.append(
        ft.Column(
            [
                ft.Text("Seleccione un submódulo de Operaciones",
                        style="titleMedium"),
                ft.ElevatedButton(
                    "Mantenimiento de Proyectos",
                    on_click=lambda e: mostrar_mantenimiento_page(page)
                ),
                ft.ElevatedButton(
                    "Desarrollo de Proyectos",
                    on_click=lambda e: mostrar_desarrollo_page(page)
                ),
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
