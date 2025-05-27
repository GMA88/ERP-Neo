import flet as ft
import importlib
from app.operations.operaciones.desarrollo_ops import (
    get_desarrollos,
    add_desarrollo,
    delete_desarrollo
)
from gui.utils.logo_utils import get_logo_image

def mostrar_desarrollo_page(page: ft.Page):
    page.title = "Desarrollo de Proyectos"
    page.scroll = ft.ScrollMode.AUTO
    page.controls.clear()

    # 1) Logo al tope
    page.controls.append(get_logo_image())

    page.appbar = ft.AppBar(title=ft.Text("Desarrollo de Proyectos"))

    proyecto      = ft.TextField(label="Nombre del Proyecto", width=300)
    descripcion   = ft.TextField(label="Descripción", multiline=True, width=400)
    desarrollador = ft.TextField(label="Responsable/Desarrollador", width=300)
    fecha_inicio  = ft.TextField(label="Fecha Inicio (YYYY-MM-DD)", width=200)
    estado        = ft.Dropdown(
        label="Estado",
        options=[
            ft.dropdown.Option("Planificado"),
            ft.dropdown.Option("En Desarrollo"),
            ft.dropdown.Option("Completado")
        ]
    )
    lista         = ft.ListView(expand=True, spacing=5, height=300)

    def cargar():
        lista.controls.clear()
        for d in get_desarrollos():
            texto = f"{d['proyecto']} — {d['estado']} — {d['fecha_inicio']}"
            lista.controls.append(
                ft.Row([
                    ft.Text(texto, expand=True),
                    ft.IconButton(icon=ft.icons.DELETE, on_click=lambda e, _id=d["_id"]: borrar(_id))
                ])
            )
        page.update()

    def agregar(e):
        if proyecto.value and descripcion.value and desarrollador.value and fecha_inicio.value and estado.value:
            add_desarrollo(
                proyecto.value,
                descripcion.value,
                desarrollador.value,
                fecha_inicio.value,
                estado.value
            )
            proyecto.value = descripcion.value = desarrollador.value = fecha_inicio.value = ""
            estado.value = None
            cargar()

    def borrar(_id):
        delete_desarrollo(str(_id))
        cargar()

    page.controls.extend([
        proyecto, descripcion, desarrollador, fecha_inicio, estado,
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
