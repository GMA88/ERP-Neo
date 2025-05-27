import flet as ft
import importlib
from app.operations.rrhh.eventos_ops import obtener_eventos, agregar_evento, eliminar_evento
from gui.utils.logo_utils import get_logo_image

def mostrar_eventos_page(page: ft.Page):
    page.title = "Eventos"
    page.controls.clear()

    # 1) Logo al tope
    page.controls.append(get_logo_image())

    page.appbar = ft.AppBar(title=ft.Text("Eventos"))

    titulo      = ft.TextField(label="Título", width=300)
    fecha       = ft.TextField(label="Fecha (YYYY-MM-DD)", width=200)
    lugar       = ft.TextField(label="Lugar", width=300)
    descripcion = ft.TextField(label="Descripción", multiline=True, width=400)
    lista       = ft.ListView(expand=True, spacing=5, height=300)

    def cargar():
        lista.controls.clear()
        for ev in obtener_eventos():
            texto = f"{ev['titulo']} — {ev['fecha']} — {ev['lugar']}"
            lista.controls.append(
                ft.Row([
                    ft.Text(texto, expand=True),
                    ft.IconButton(icon=ft.icons.DELETE, on_click=lambda evt, _id=ev["_id"]: borrar(_id))
                ])
            )
        page.update()

    def agregar(evt):
        agregar_evento(titulo.value, fecha.value, lugar.value, descripcion.value)
        titulo.value = fecha.value = lugar.value = descripcion.value = ""
        cargar()

    def borrar(_id):
        eliminar_evento(str(_id))
        cargar()

    page.controls.extend([
        titulo, fecha, lugar, descripcion,
        ft.Row([
            ft.ElevatedButton("Agregar Evento", on_click=agregar),
            ft.ElevatedButton("Refrescar", on_click=lambda e: cargar())
        ], spacing=10),
        ft.Divider(),
        lista,
        ft.ElevatedButton(
            "← Volver RRHH",
            on_click=lambda e: importlib
                .import_module("gui.rrhh.hr_main")
                .mostrar_rrhh_main(page)
        )
    ])
    cargar()
