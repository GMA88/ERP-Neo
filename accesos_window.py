import flet as ft
import importlib
from app.operations.seguridad.accesos_ops import (
    obtener_accesos,
    agregar_acceso,
    eliminar_acceso
)
from gui.utils.logo_utils import get_logo_image

def mostrar_accesos_page(page: ft.Page):
    page.title = "Control de Accesos"
    page.scroll = ft.ScrollMode.AUTO
    page.controls.clear()

    # 1) Logo al tope
    page.controls.append(get_logo_image())

    page.appbar = ft.AppBar(title=ft.Text("Control de Accesos"))

    empleado = ft.TextField(label="Empleado (ID o Nombre)", width=250)
    tipo     = ft.Dropdown(
        label="Tipo de Acceso",
        options=[ft.dropdown.Option("Entrada"), ft.dropdown.Option("Salida")]
    )
    fecha    = ft.TextField(label="Fecha (YYYY-MM-DD HH:MM)", width=250)
    lista    = ft.ListView(expand=True, spacing=5, height=300)

    def cargar():
        lista.controls.clear()
        for a in obtener_accesos():
            emp   = a.get("empleado") or "N/A"
            tip   = a.get("tipo") or "N/A"
            fecha_val = a.get("fecha")
            fecha_str = fecha_val.strftime("%Y-%m-%d %H:%M") if hasattr(fecha_val, "strftime") else str(fecha_val)
            texto = f"{emp} • {tip} • {fecha_str}"
            lista.controls.append(
                ft.Row([
                    ft.Text(texto, expand=True),
                    ft.IconButton(
                        icon=ft.icons.DELETE,
                        tooltip="Eliminar",
                        on_click=lambda e, _id=a["_id"]: borrar(_id)
                    )
                ])
            )
        page.update()

    def registrar(e):
        if empleado.value and tipo.value and fecha.value:
            agregar_acceso(empleado.value, tipo.value, fecha.value)
            empleado.value = ""
            tipo.value = None
            fecha.value = ""
            cargar()

    def borrar(_id):
        eliminar_acceso(str(_id))
        cargar()

    page.controls.extend([
        empleado, tipo, fecha,
        ft.Row([
            ft.ElevatedButton("Registrar", on_click=registrar),
            ft.ElevatedButton("Refrescar",  on_click=lambda e: cargar())
        ], spacing=10),
        ft.Divider(),
        lista,
        ft.Divider(),
        ft.ElevatedButton(
            "← Volver Seguridad",
            icon=ft.icons.ARROW_BACK_IOS,
            on_click=lambda e: importlib
                .import_module("gui.seguridad.seguridad_main")
                .mostrar_seguridad_main(page)
        )
    ])
    cargar()
