# gui/almacen/almacen_main.py
import flet as ft

# 1️⃣  Importaciones ESTÁTICAS de los submódulos (PyInstaller los ve)
from gui.almacen.compras_window            import mostrar_compras_page
from gui.almacen.garantias_window          import mostrar_garantias_page
from gui.almacen.logistica_window          import mostrar_logistica_page
from gui.almacen.ventas_materiales_window  import mostrar_ventas_materiales_page

from gui.utils.logo_utils import get_logo_image
# No importamos main_window aquí para evitar ciclo


def mostrar_almacen_main(page: ft.Page):
    page.title = "Almacén"
    page.controls.clear()

    # Logo
    page.controls.append(get_logo_image())

    page.appbar = ft.AppBar(title=ft.Text("Módulo de Almacén"))

    # ──────────────────────────
    # Callback seguro (import diferido → sin ciclo)
    def volver_menu_principal(e):
        from gui.main_window import mostrar_main   # import aquí
        mostrar_main(page, "almacen")
    # ──────────────────────────

    page.controls.append(
        ft.Column(
            [
                ft.Text("Seleccione un submódulo de Almacén",
                        style="titleMedium"),
                ft.ElevatedButton("Compras",
                                  on_click=lambda e: mostrar_compras_page(page)),
                ft.ElevatedButton("Garantías",
                                  on_click=lambda e: mostrar_garantias_page(page)),
                ft.ElevatedButton("Logística",
                                  on_click=lambda e: mostrar_logistica_page(page)),
                ft.ElevatedButton("Ventas de Materiales",
                                  on_click=lambda e: mostrar_ventas_materiales_page(page)),
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
