import flet as ft
import importlib
from app.operations.almacen.garantias_ops import obtener_garantias, agregar_garantia, eliminar_garantia
from gui.utils.logo_utils import get_logo_image

def mostrar_garantias_page(page: ft.Page):
    page.title = "Garantías"
    page.scroll = ft.ScrollMode.AUTO
    page.controls.clear()

    # 1) Logo al tope
    page.controls.append(get_logo_image())

    page.appbar = ft.AppBar(title=ft.Text("Garantías"))

    origen      = ft.Dropdown(label="Origen", options=[ft.dropdown.Option("compra"), ft.dropdown.Option("venta")])
    tipo        = ft.Dropdown(label="Tipo",   options=[ft.dropdown.Option("Compra"), ft.dropdown.Option("Venta")])
    producto    = ft.TextField(label="Producto", width=300)
    responsable = ft.TextField(label="Responsable", width=300)
    fecha_ini   = ft.TextField(label="Fecha Inicio (YYYY-MM-DD)", width=200)
    duracion    = ft.TextField(label="Duración (meses)", keyboard_type=ft.KeyboardType.NUMBER, width=200)
    lista       = ft.ListView(expand=True, spacing=5, height=300)

    def cargar():
        lista.controls.clear()
        for g in obtener_garantias(origen.value):
            fin = g["fecha_fin"].strftime("%Y-%m-%d")
            texto = f"[{g['estado']}] {g['tipo']} • {g['producto']} • Fin: {fin}"
            lista.controls.append(
                ft.Row([
                    ft.Text(texto, expand=True),
                    ft.IconButton(icon=ft.icons.DELETE, on_click=lambda e, _id=g["_id"]: borrar(_id))
                ])
            )
        page.update()

    def agregar(e):
        if origen.value and tipo.value and producto.value and responsable.value and fecha_ini.value and duracion.value:
            agregar_garantia(
                tipo.value,
                producto.value,
                responsable.value,
                fecha_ini.value,
                int(duracion.value),
                origen.value
            )
            producto.value = responsable.value = fecha_ini.value = duracion.value = ""
            cargar()

    def borrar(_id):
        eliminar_garantia(str(_id))
        cargar()

    page.controls.extend([
        origen, tipo, producto,
        responsable, fecha_ini, duracion,
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
