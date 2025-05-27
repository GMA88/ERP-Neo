import flet as ft
import importlib
from app.operations.seguridad.bitacora_ops import (
    get_bitacoras,
    eliminar_bitacora
)
from gui.utils.logo_utils import get_logo_image

def mostrar_bitacora_page(page: ft.Page):
    page.title = "Bitácora"
    page.scroll = ft.ScrollMode.AUTO
    page.controls.clear()

    # 1) Logo al tope
    page.controls.append(get_logo_image())

    page.appbar = ft.AppBar(title=ft.Text("Bitácora de Seguridad"))

    lista = ft.ListView(expand=True, spacing=5, height=350)

    def cargar():
        lista.controls.clear()
        for b in get_bitacoras():
            txt = f"{b['fecha'].strftime('%Y-%m-%d %H:%M:%S')} • {b['responsable']} • {b['evento']}"
            lista.controls.append(
                ft.Row([
                    ft.Text(txt, expand=True),
                    ft.IconButton(icon=ft.icons.DELETE,
                                  tooltip="Eliminar",
                                  on_click=lambda e, _id=b["_id"]: borrar(_id))
                ])
            )
        page.update()

    def borrar(_id):
        eliminar_bitacora(str(_id))
        cargar()

    page.controls.extend([
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
