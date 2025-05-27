import flet as ft
import importlib
from app.operations.rrhh.capacitaciones_ops import obtener_capacitaciones, agregar_capacitacion, eliminar_capacitacion
from gui.utils.logo_utils import get_logo_image

def mostrar_capacitaciones_page(page: ft.Page):
    page.title = "Capacitaciones"
    page.controls.clear()

    # 1) Logo al tope
    page.controls.append(get_logo_image())

    page.appbar = ft.AppBar(title=ft.Text("Capacitaciones"))

    titulo      = ft.TextField(label="Título", width=300)
    fecha       = ft.TextField(label="Fecha (YYYY-MM-DD)", width=200)
    responsable = ft.TextField(label="Responsable", width=300)
    descripcion = ft.TextField(label="Descripción", multiline=True, width=400)
    lista       = ft.ListView(expand=True, spacing=5, height=300)

    def cargar():
        lista.controls.clear()
        for c in obtener_capacitaciones():
            texto = f"{c['titulo']} — {c['fecha']} — {c['responsable']}"
            lista.controls.append(
                ft.Row([
                    ft.Text(texto, expand=True),
                    ft.IconButton(icon=ft.icons.DELETE, on_click=lambda evt, _id=c["_id"]: borrar(_id))
                ])
            )
        page.update()

    def agregar(evt):
        agregar_capacitacion(titulo.value, fecha.value, responsable.value, descripcion.value)
        titulo.value = fecha.value = responsable.value = descripcion.value = ""
        cargar()

    def borrar(_id):
        eliminar_capacitacion(str(_id))
        cargar()

    page.controls.extend([
        titulo, fecha, responsable, descripcion,
        ft.Row([
            ft.ElevatedButton("Agregar", on_click=agregar),
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
