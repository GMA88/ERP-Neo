import flet as ft
import importlib
from app.operations.sistemas.proyectos_electronica_ops import (
    obtener_proyectos_electronica,
    agregar_proyecto_electronica,
    eliminar_proyecto_electronica
)
from gui.utils.logo_utils import get_logo_image

def mostrar_proyectos_page(page: ft.Page):
    page.title = "Proyectos de Electrónica"
    page.controls.clear()

    # 1) Logo al tope
    page.controls.append(get_logo_image())

    page.appbar = ft.AppBar(title=ft.Text("Proyectos de Electrónica"))

    nombre      = ft.TextField(label="Nombre del Proyecto", width=300)
    tipo        = ft.TextField(label="Tipo de Electrónica", width=300)
    responsable = ft.TextField(label="Responsable", width=300)
    lista       = ft.ListView(expand=True, spacing=5, height=300)

    def cargar():
        lista.controls.clear()
        for p in obtener_proyectos_electronica():
            fecha = p["fecha"].strftime("%Y-%m-%d")
            texto = f"{p['nombre']} — {p['tipo']} — {p['responsable']} — {fecha}"
            lista.controls.append(
                ft.Row([
                    ft.Text(texto),
                    ft.IconButton(icon=ft.icons.DELETE, on_click=lambda e, id=p["_id"]: borrar(id))
                ])
            )
        page.update()

    def agregar(e):
        if nombre.value and tipo.value and responsable.value:
            agregar_proyecto_electronica(nombre.value, tipo.value, responsable.value)
            nombre.value = tipo.value = responsable.value = ""
            cargar()

    def borrar(id):
        eliminar_proyecto_electronica(str(id))
        cargar()

    page.controls.extend([
        nombre,
        tipo,
        responsable,
        ft.Row([
            ft.ElevatedButton("Agregar Proyecto", on_click=agregar),
            ft.ElevatedButton("Refrescar Lista", on_click=lambda e: cargar())
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
