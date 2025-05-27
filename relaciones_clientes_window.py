import flet as ft
import importlib
from app.operations.ventas.relaciones_ops import (
    obtener_relaciones,
    agregar_relacion,
    eliminar_relacion
)
from gui.utils.logo_utils import get_logo_image

def mostrar_relaciones_clientes(page: ft.Page):
    page.title = "Relaciones con Clientes"
    page.scroll = ft.ScrollMode.AUTO
    page.controls.clear()

    # 1) Logo al tope
    page.controls.append(get_logo_image())

    page.appbar = ft.AppBar(title=ft.Text("Relaciones con Clientes"))

    empresa     = ft.TextField(label="Empresa", width=300)
    tipo        = ft.TextField(label="Tipo de Relación", width=300)
    sector      = ft.TextField(label="Sector", width=300)
    contacto    = ft.TextField(label="Contacto", width=300)
    responsable = ft.TextField(label="Responsable", width=300)
    lista_rel   = ft.ListView(expand=True, spacing=5, height=300)

    def cargar():
        lista_rel.controls.clear()
        for r in obtener_relaciones():
            texto = f"{r['empresa']} • {r['tipo']} • {r['sector']}"
            lista_rel.controls.append(
                ft.Row([
                    ft.Text(texto, expand=True),
                    ft.IconButton(icon=ft.icons.DELETE, on_click=lambda e, _id=r["_id"]: borrar(_id))
                ])
            )
        page.update()

    def agregar(e):
        if empresa.value and tipo.value and sector.value and contacto.value and responsable.value:
            agregar_relacion(
                empresa.value,
                tipo.value,
                sector.value,
                contacto.value,
                responsable.value
            )
            empresa.value = tipo.value = sector.value = contacto.value = responsable.value = ""
            cargar()

    def borrar(_id):
        eliminar_relacion(str(_id))
        cargar()

    page.controls.extend([
        empresa, tipo, sector, contacto, responsable,
        ft.Row([
            ft.ElevatedButton("Registrar", on_click=agregar),
            ft.ElevatedButton("Refrescar",  on_click=lambda e: cargar())
        ], spacing=10),
        ft.Divider(),
        lista_rel,
        ft.Divider(),
        ft.ElevatedButton(
            "← Volver a Ventas",
            on_click=lambda e: importlib
                .import_module("gui.ventas.ventas_main")
                .mostrar_ventas_main(page)
        )
    ])
    cargar()
