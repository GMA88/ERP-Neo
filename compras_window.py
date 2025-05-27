import flet as ft
import importlib
from app.operations.almacen.compras_ops import obtener_compras, agregar_compra, eliminar_compra
from gui.utils.logo_utils import get_logo_image

def mostrar_compras_page(page: ft.Page):
    page.title = "Compras"
    page.scroll = ft.ScrollMode.AUTO
    page.controls.clear()

    # 1) Logo al tope
    page.controls.append(get_logo_image())

    page.appbar = ft.AppBar(title=ft.Text("Compras"))

    proveedor   = ft.TextField(label="Proveedor", width=300)
    producto    = ft.TextField(label="Producto", width=300)
    cantidad    = ft.TextField(label="Cantidad", keyboard_type=ft.KeyboardType.NUMBER, width=200)
    costo       = ft.TextField(label="Costo Unitario", keyboard_type=ft.KeyboardType.NUMBER, width=200)
    responsable = ft.TextField(label="Responsable", width=300)
    lista       = ft.ListView(expand=True, spacing=5, height=300)

    def cargar():
        lista.controls.clear()
        for c in obtener_compras():
            texto = f"{c['proveedor']} • {c['producto']} • Cant:{c['cantidad']} • Total:${c['total']:.2f}"
            lista.controls.append(
                ft.Row([
                    ft.Text(texto, expand=True),
                    ft.IconButton(icon=ft.icons.DELETE, on_click=lambda e, _id=c["_id"]: borrar(_id))
                ])
            )
        page.update()

    def agregar(e):
        if proveedor.value and producto.value and cantidad.value and costo.value and responsable.value:
            agregar_compra(
                proveedor.value,
                producto.value,
                int(cantidad.value),
                float(costo.value),
                responsable.value
            )
            proveedor.value = producto.value = cantidad.value = costo.value = responsable.value = ""
            cargar()

    def borrar(_id):
        eliminar_compra(str(_id))
        cargar()

    page.controls.extend([
        proveedor, producto, cantidad, costo, responsable,
        ft.Row([
            ft.ElevatedButton("Agregar", on_click=agregar),
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
