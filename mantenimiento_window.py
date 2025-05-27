import flet as ft
import importlib
from app.operations.operaciones.mantenimiento_ops import (
    get_mantenimientos,
    add_mantenimiento,
    delete_mantenimiento
)
from gui.utils.logo_utils import get_logo_image

def mostrar_mantenimiento_page(page: ft.Page):
    page.title = "Mantenimiento de Proyectos"
    page.scroll = ft.ScrollMode.AUTO
    page.controls.clear()

    # 1) Logo al tope
    page.controls.append(get_logo_image())

    page.appbar = ft.AppBar(title=ft.Text("Mantenimiento de Proyectos"))

    proyecto     = ft.TextField(label="Proyecto", width=300)
    descripcion  = ft.TextField(label="Descripción", multiline=True, width=400)
    responsable  = ft.TextField(label="Responsable", width=300)
    fecha_inicio = ft.TextField(label="Fecha Inicio (YYYY-MM-DD)", width=200)
    estado       = ft.Dropdown(
        label="Estado",
        options=[
            ft.dropdown.Option("Pendiente"),
            ft.dropdown.Option("En Progreso"),
            ft.dropdown.Option("Finalizado")
        ]
    )
    lista        = ft.ListView(expand=True, spacing=5, height=300)

    def cargar():
        lista.controls.clear()
        for m in get_mantenimientos():
            texto = f"{m['proyecto']} — {m['estado']} — {m['fecha_inicio']}"
            lista.controls.append(
                ft.Row([
                    ft.Text(texto, expand=True),
                    ft.IconButton(icon=ft.icons.DELETE, on_click=lambda e, _id=m["_id"]: borrar(_id))
                ])
            )
        page.update()

    def agregar(e):
        if proyecto.value and descripcion.value and responsable.value and fecha_inicio.value and estado.value:
            add_mantenimiento(
                proyecto.value,
                descripcion.value,
                responsable.value,
                fecha_inicio.value,
                estado.value
            )
            proyecto.value = descripcion.value = responsable.value = fecha_inicio.value = ""
            estado.value = None
            cargar()

    def borrar(_id):
        delete_mantenimiento(str(_id))
        cargar()

    page.controls.extend([
        proyecto, descripcion, responsable, fecha_inicio, estado,
        ft.Row([
            ft.ElevatedButton("Registrar", on_click=agregar),
            ft.ElevatedButton("Refrescar", on_click=lambda e: cargar())
        ], spacing=10),
        ft.Divider(),
        lista,
        ft.Divider(),
        ft.ElevatedButton(
            "← Volver Operaciones",
            icon=ft.icons.ARROW_BACK_IOS,
            on_click=lambda e: importlib
                .import_module("gui.operaciones.operaciones_main")
                .mostrar_operaciones_main(page)
        )
    ])
    cargar()
