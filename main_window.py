# gui/main_window.py

import flet as ft
from gui.admin.admin_main import mostrar_admin_main
from gui.rrhh.hr_main import mostrar_rrhh_main
from gui.sistemas.sistemas_main import mostrar_sistemas_main
from gui.operaciones.operaciones_main import mostrar_operaciones_main
from gui.almacen.almacen_main import mostrar_almacen_main
from gui.ventas.ventas_main import mostrar_ventas_main
from gui.seguridad.seguridad_main import mostrar_seguridad_main
from gui.utils.logo_utils import get_logo_image

# Mapeo de roles a vistas
_ROLE_VIEWS = {
    "admin":             ("Administración",      mostrar_admin_main),
    "recursos_humanos":  ("Recursos Humanos",    mostrar_rrhh_main),
    "sistemas":          ("Sistemas",            mostrar_sistemas_main),
    "operaciones":       ("Operaciones",         mostrar_operaciones_main),
    "almacen":           ("Almacén",             mostrar_almacen_main),
    "ventas":            ("Ventas",              mostrar_ventas_main),
    "seguridad":         ("Seguridad",           mostrar_seguridad_main),
}

def mostrar_main(page: ft.Page, role: str):
    page.title = "Neology – Menú Principal"
    page.controls.clear()

    # 1) Logo al tope
    page.controls.append(get_logo_image())

    page.appbar = ft.AppBar(
        title=ft.Text("Menú Principal"),
        # import dinámico de login en el callback para evitar import circular
        actions=[ft.IconButton(
            icon=ft.icons.LOGOUT,
            on_click=lambda e: __import__("gui.login_window", fromlist=["mostrar_login"])
                                .mostrar_login(page)
        )]
    )

    # Si es admin mostramos todos, si no, solo su rol
    items = _ROLE_VIEWS.items() if role == "admin" else [(role, _ROLE_VIEWS[role])]

    botones = [
        ft.ElevatedButton(
            text=label,
            width=200, height=50,
            on_click=lambda e, fn=fn: fn(page)
        )
        for _, (label, fn) in items
    ]

    page.controls.append(
        ft.Column(
            botones,
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=20
        )
    )
    page.update()
