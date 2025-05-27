import flet as ft
import importlib
from datetime import datetime
from app.operations.ventas.proyectos_ops import (
    obtener_ventas_proyectos,
    agregar_venta_proyecto,
    eliminar_venta_proyecto
)
from gui.utils.logo_utils import get_logo_image

def mostrar_venta_proyectos(page: ft.Page):
    page.title = "Venta de Proyectos"
    page.scroll = ft.ScrollMode.AUTO
    page.controls.clear()

    # 1) Logo al tope
    page.controls.append(get_logo_image())

    page.appbar = ft.AppBar(title=ft.Text("Venta de Proyectos"))

    proyecto     = ft.TextField(label="Proyecto", width=300)
    cliente      = ft.TextField(label="Cliente", width=300)
    monto        = ft.TextField(label="Monto", keyboard_type=ft.KeyboardType.NUMBER, width=200)
    responsable  = ft.TextField(label="Responsable", width=300)
    lista_ventas = ft.ListView(expand=True, spacing=5, height=300)

    def cargar():
        lista_ventas.controls.clear()
        for v in obtener_ventas_proyectos():
            texto = f"{v['proyecto']} • {v['cliente']} • ${v['monto']:.2f}"
            lista_ventas.controls.append(
                ft.Row([
                    ft.Text(texto, expand=True),
                    ft.IconButton(icon=ft.icons.DELETE, on_click=lambda e, _id=v["_id"]: borrar(_id))
                ])
            )
        page.update()

    def agregar(e):
        if proyecto.value and cliente.value and monto.value and responsable.value:
            agregar_venta_proyecto(
                proyecto.value,
                cliente.value,
                float(monto.value),
                responsable.value
            )
            proyecto.value = cliente.value = monto.value = responsable.value = ""
            cargar()

    def borrar(_id):
        eliminar_venta_proyecto(str(_id))
        cargar()

    page.controls.extend([
        proyecto, cliente, monto, responsable,
        ft.Row([
            ft.ElevatedButton("Registrar", on_click=agregar),
            ft.ElevatedButton("Refrescar",  on_click=lambda e: cargar())
        ], spacing=10),
        ft.Divider(),
        lista_ventas,
        ft.Divider(),
        ft.ElevatedButton(
            "← Volver a Ventas",
            on_click=lambda e: importlib
                .import_module("gui.ventas.ventas_main")
                .mostrar_ventas_main(page)
        )
    ])
    cargar()

mostrar_venta_proyectos_page = mostrar_venta_proyectos