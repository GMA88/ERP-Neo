import flet as ft
import importlib
from app.operations.sistemas.diseno_ui_ops import (
    obtener_disenos,
    agregar_diseno,
    eliminar_diseno
)
from gui.utils.logo_utils import get_logo_image

def mostrar_diseno_page(page: ft.Page):
    page.title = "Diseño de UI"
    page.controls.clear()

    # 1) Logo al tope
    page.controls.append(get_logo_image())

    page.appbar = ft.AppBar(title=ft.Text("Diseño de UI"))

    nombre      = ft.TextField(label="Nombre del Proyecto UI", width=300)
    herramienta = ft.TextField(label="Herramienta", width=300)
    responsable = ft.TextField(label="Responsable", width=300)
    lista       = ft.ListView(expand=True, spacing=5, height=300)

    def cargar():
        lista.controls.clear()
        for d in obtener_disenos():
            fecha = d["fecha"].strftime("%Y-%m-%d")
            texto = f"{d['nombre']} — {d['herramienta']} — {d['responsable']} — {fecha}"
            lista.controls.append(
                ft.Row([
                    ft.Text(texto),
                    ft.IconButton(icon=ft.icons.DELETE, on_click=lambda e, id=d["_id"]: borrar(id))
                ])
            )
        page.update()

    def agregar(e):
        if nombre.value and herramienta.value and responsable.value:
            agregar_diseno(nombre.value, herramienta.value, responsable.value)
            nombre.value = herramienta.value = responsable.value = ""
            cargar()

    def borrar(id):
        eliminar_diseno(str(id))
        cargar()

    page.controls.extend([
        nombre,
        herramienta,
        responsable,
        ft.Row([
            ft.ElevatedButton("Agregar Diseño", on_click=agregar),
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
