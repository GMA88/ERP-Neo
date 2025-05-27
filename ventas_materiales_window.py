import flet as ft
import importlib
from app.operations.almacen.ventas_materiales_ops import (
    obtener_ventas_materiales,
    agregar_venta_material,
    eliminar_venta_material
)
from gui.utils.logo_utils import get_logo_image

def mostrar_ventas_materiales_page(page: ft.Page):
    page.title = "Ventas de Materiales"
    page.scroll = ft.ScrollMode.AUTO
    page.controls.clear()

    # 1) Logo al tope
    page.controls.append(get_logo_image())

    page.appbar = ft.AppBar(title=ft.Text("Ventas de Materiales"))

    producto = ft.TextField(label="Producto", width=300)
    cantidad = ft.TextField(label="Cantidad", keyboard_type=ft.KeyboardType.NUMBER, width=200)
    precio   = ft.TextField(label="Precio Unitario", keyboard_type=ft.KeyboardType.NUMBER, width=200)
    cliente  = ft.TextField(label="Cliente", width=300)
    vendedor = ft.TextField(label="Vendedor", width=300)
    lista    = ft.ListView(expand=True, spacing=5, height=300)

    def cargar():
        lista.controls.clear()
        for v in obtener_ventas_materiales():
            texto = f"{v['producto']} • Cant:{v['cantidad']} • Total:${v['total']:.2f} • Cliente:{v['cliente']}"
            lista.controls.append(
                ft.Row([
                    ft.Text(texto, expand=True),
                    ft.IconButton(icon=ft.icons.DELETE, on_click=lambda e, _id=v["_id"]: borrar(_id))
                ])
            )
        page.update()

    def agregar(e):
        if producto.value and cantidad.value and precio.value and cliente.value and vendedor.value:
            agregar_venta_material(
                producto.value,
                int(cantidad.value),
                float(precio.value),
                cliente.value,
                vendedor.value
            )
            producto.value = cantidad.value = precio.value = cliente.value = vendedor.value = ""
            cargar()

    def borrar(_id):
        eliminar_venta_material(str(_id))
        cargar()

    page.controls.extend([
        producto, cantidad, precio, cliente, vendedor,
        ft.Row([
            ft.ElevatedButton("Registrar Venta", on_click=agregar),
            ft.ElevatedButton("Refrescar",      on_click=lambda e: cargar())
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
