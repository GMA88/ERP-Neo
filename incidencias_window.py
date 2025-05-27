import flet as ft
import importlib
from app.operations.seguridad.incidencias_ops import (
    obtener_incidencias,
    agregar_incidencia,
    eliminar_incidencia
)
from gui.utils.logo_utils import get_logo_image

def mostrar_incidencias_page(page: ft.Page):
    page.title = "Incidencias"
    page.scroll = ft.ScrollMode.AUTO
    page.controls.clear()

    # 1) Logo al tope
    page.controls.append(get_logo_image())

    page.appbar = ft.AppBar(title=ft.Text("Incidencias"))

    descripcion = ft.TextField(label="Descripción", multiline=True, width=400)
    nivel       = ft.Dropdown(
        label="Nivel",
        options=[ft.dropdown.Option("Baja"), ft.dropdown.Option("Media"), ft.dropdown.Option("Alta")]
    )
    fecha       = ft.TextField(label="Fecha (YYYY-MM-DD HH:MM)", width=250)
    lista       = ft.ListView(expand=True, spacing=5, height=300)

    def cargar():
        lista.controls.clear()
        for i in obtener_incidencias():
            desc = i.get("descripcion") or "N/A"
            niv  = i.get("nivel") or "N/A"
            fecha_val = i.get("fecha")
            fecha_str = fecha_val.strftime("%Y-%m-%d %H:%M") if hasattr(fecha_val, "strftime") else str(fecha_val)
            texto = f"{desc} • Nivel: {niv} • {fecha_str}"
            lista.controls.append(
                ft.Row([
                    ft.Text(texto, expand=True),
                    ft.IconButton(
                        icon=ft.icons.DELETE,
                        tooltip="Eliminar",
                        on_click=lambda e, _id=i["_id"]: borrar(_id)
                    )
                ])
            )
        page.update()

    def registrar(e):
        if descripcion.value and nivel.value and fecha.value:
            agregar_incidencia(descripcion.value, nivel.value, fecha.value)
            descripcion.value = ""
            nivel.value = None
            fecha.value = ""
            cargar()

    def borrar(_id):
        eliminar_incidencia(str(_id))
        cargar()

    page.controls.extend([
        descripcion, nivel, fecha,
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
