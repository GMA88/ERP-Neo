# gui/ventas/ventas_main.py
import flet as ft

# 1️⃣  Importaciones estáticas de los submódulos de Ventas
from gui.ventas.venta_proyectos_window      import mostrar_venta_proyectos_page
from gui.ventas.relaciones_clientes_window  import mostrar_relaciones_clientes

from gui.utils.logo_utils import get_logo_image
# (no importamos main_window aquí ⇒ se hace dentro del callback)

def mostrar_ventas_main(page: ft.Page):
    page.title = "Ventas"
    page.controls.clear()

    # Logo
    page.controls.append(get_logo_image())

    page.appbar = ft.AppBar(title=ft.Text("Módulo de Ventas"))

    # Callback diferido para romper ciclo con main_window
    def volver_menu_principal(e):
        from gui.main_window import mostrar_main   # import tardío → sin ciclo
        mostrar_main(page, "ventas")

    page.controls.append(
        ft.Column(
            [
                ft.Text("Seleccione un submódulo de Ventas",
                        style="titleMedium"),
                ft.ElevatedButton("Venta de Proyectos",
                                  on_click=lambda e: mostrar_venta_proyectos_page(page)),
                ft.ElevatedButton("Relaciones con Clientes",
                                  on_click=lambda e: mostrar_relaciones_clientes(page)),
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
