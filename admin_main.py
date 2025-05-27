# gui/admin/admin_main.py
import flet as ft
from gui.admin.gestion_usuarios_window import mostrar_gestion_usuarios
from gui.admin.configuraciones_window import mostrar_configuraciones
from gui.utils.logo_utils            import get_logo_image
# ⬇️  ¡OJO!  Quitamos el import estático de main_window para eliminar el círculo

def mostrar_admin_main(page: ft.Page):
    page.title = "Administración"
    page.controls.clear()

    page.controls.append(get_logo_image())
    page.appbar = ft.AppBar(title=ft.Text("Módulo de Administración"))

    # callback seguro (import tardío → sin ciclo)
    def volver_menu_principal(e):
        from gui.main_window import mostrar_main   # import aquí
        mostrar_main(page, "admin")

    page.controls.append(
        ft.Column(
            [
                ft.Text("Seleccione un submódulo de Administración",
                        style="titleMedium"),
                ft.ElevatedButton("Gestión de Usuarios",
                                  on_click=lambda e: mostrar_gestion_usuarios(page)),
                ft.ElevatedButton("Configuraciones",
                                  on_click=lambda e: mostrar_configuraciones(page)),
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
