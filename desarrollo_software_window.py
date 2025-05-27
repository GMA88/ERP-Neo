import flet as ft
import importlib
from app.operations.sistemas.desarrollo_software_ops import (
    obtener_proyectos,
    agregar_proyecto,
    eliminar_proyecto
)
from gui.utils.logo_utils import get_logo_image

def mostrar_desarrollo_page(page: ft.Page):
    page.title = "Desarrollo de Software"
    page.controls.clear()

    # 1) Logo al tope
    page.controls.append(get_logo_image())

    page.appbar = ft.AppBar(title=ft.Text("Desarrollo de Software"))

    nombre      = ft.TextField(label="Nombre del Proyecto", width=300)
    descripcion = ft.TextField(label="Descripción", multiline=True, width=400)
    responsable = ft.TextField(label="Responsable", width=300)
    lista       = ft.ListView(expand=True, spacing=5, height=300)

    def cargar():
        lista.controls.clear()
        for p in obtener_proyectos():
            fecha = p["fecha"].strftime("%Y-%m-%d")
            texto = f"{p['nombre']} — {p['responsable']} — {fecha}"
            lista.controls.append(
                ft.Row([
                    ft.Text(texto),
                    ft.IconButton(icon=ft.icons.DELETE, on_click=lambda e, id=p["_id"]: borrar(id))
                ])
            )
        page.update()

    def agregar(e):
        if nombre.value and descripcion.value and responsable.value:
            agregar_proyecto(nombre.value, descripcion.value, responsable.value)
            nombre.value = descripcion.value = responsable.value = ""
            cargar()

    def borrar(id):
        eliminar_proyecto(str(id))
        cargar()

    page.controls.extend([
        nombre,
        descripcion,
        responsable,
        ft.Row([
            ft.ElevatedButton("Agregar Proyecto", on_click=agregar),
            ft.ElevatedButton("Refrescar", on_click=lambda e: cargar())
        ], spacing=10),
        ft.Divider(),
        lista,
        ft.ElevatedButton(
            "← Volver a Sistemas",
            on_click=lambda e: importlib
                .import_module("gui.sistemas.sistemas_main")
                .mostrar_sistemas_main(page)
        )
    ])
    cargar()
