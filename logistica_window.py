import flet as ft
import importlib
from app.operations.almacen.logistica_ops import obtener_logistica, agregar_logistica, eliminar_logistica
from gui.utils.logo_utils import get_logo_image

def mostrar_logistica_page(page: ft.Page):
    page.title = "Logística"
    page.scroll = ft.ScrollMode.AUTO
    page.controls.clear()

    # 1) Logo al tope
    page.controls.append(get_logo_image())

    page.appbar = ft.AppBar(title=ft.Text("Logística"))

    tipo        = ft.Dropdown(label="Tipo",    options=[ft.dropdown.Option("Equipo"), ft.dropdown.Option("Material")])
    descripcion = ft.TextField(label="Descripción", width=400)
    destino     = ft.TextField(label="Destino", width=300)
    fecha_envio = ft.TextField(label="Fecha Envío (YYYY-MM-DD)", width=200)
    responsable = ft.TextField(label="Responsable", width=300)
    lista       = ft.ListView(expand=True, spacing=5, height=300)

    def cargar():
        lista.controls.clear()
        for l in obtener_logistica():
            texto = f"{l['tipo']} → {l['destino']} ({l['descripcion']})"
            lista.controls.append(
                ft.Row([
                    ft.Text(texto, expand=True),
                    ft.IconButton(icon=ft.icons.DELETE, on_click=lambda e, _id=l["_id"]: borrar(_id))
                ])
            )
        page.update()

    def agregar(e):
        if tipo.value and descripcion.value and destino.value and fecha_envio.value and responsable.value:
            agregar_logistica(
                tipo.value,
                descripcion.value,
                destino.value,
                fecha_envio.value,
                responsable.value
            )
            descripcion.value = destino.value = fecha_envio.value = responsable.value = ""
            cargar()

    def borrar(_id):
        eliminar_logistica(str(_id))
        cargar()

    page.controls.extend([
        tipo, descripcion, destino, fecha_envio, responsable,
        ft.Row([
            ft.ElevatedButton("Registrar", on_click=agregar),
            ft.ElevatedButton("Refrescar", on_click=lambda e: cargar())
        ], spacing=10),
        ft.Divider(),
        lista,
        ft.Divider(),
        ft.ElevatedButton(
            "← Volver Almacén",
            on_click=lambda e: importlib
                .import_module("gui.almacen.almacen_main")
                .mostrar_almacen_main(page)
        )
    ])
    cargar()
