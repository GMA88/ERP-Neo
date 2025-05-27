import flet as ft
import importlib
from app.operations.sistemas.analisis_datos_financieros_ops import (
    obtener_analisis,
    agregar_analisis,
    eliminar_analisis
)
from gui.utils.logo_utils import get_logo_image

def mostrar_analisis_page(page: ft.Page):
    page.title = "Análisis de Datos Financieros"
    page.controls.clear()

    # 1) Logo al tope
    page.controls.append(get_logo_image())

    page.appbar = ft.AppBar(title=ft.Text("Análisis de Datos Financieros"))

    descripcion    = ft.TextField(label="Descripción", width=400)
    responsable    = ft.TextField(label="Responsable", width=300)
    lista_analisis = ft.ListView(expand=True, spacing=5, height=300)

    def cargar():
        lista_analisis.controls.clear()
        for reg in obtener_analisis():
            fecha = reg["fecha"].strftime("%Y-%m-%d")
            texto = f"{reg['descripcion']} — {reg['responsable']} — {fecha}"
            lista_analisis.controls.append(
                ft.Row([
                    ft.Text(texto),
                    ft.IconButton(icon=ft.icons.DELETE, on_click=lambda e, id=reg["_id"]: borrar(id))
                ])
            )
        page.update()

    def agregar(e):
        if descripcion.value and responsable.value:
            agregar_analisis(descripcion.value, responsable.value)
            descripcion.value = responsable.value = ""
            cargar()

    def borrar(id):
        eliminar_analisis(str(id))
        cargar()

    page.controls.extend([
        descripcion,
        responsable,
        ft.Row([
            ft.ElevatedButton("Agregar Análisis", on_click=agregar),
            ft.ElevatedButton("Refrescar", on_click=lambda e: cargar())
        ], spacing=10),
        ft.Divider(),
        lista_analisis,
        ft.ElevatedButton(
            "← Volver a Sistemas",
            on_click=lambda e: importlib
                .import_module("gui.sistemas.sistemas_main")
                .mostrar_sistemas_main(page)
        )
    ])
    cargar()
