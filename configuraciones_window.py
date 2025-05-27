import flet as ft
import importlib
from app.operations.admin.configuraciones import get_configuraciones, update_configuracion
from gui.utils.logo_utils import get_logo_image

def mostrar_configuraciones(page: ft.Page):
    page.title = "Configuraciones"
    page.scroll = ft.ScrollMode.AUTO
    page.controls.clear()

    # 1) Logo al tope
    page.controls.append(get_logo_image())

    page.appbar = ft.AppBar(title=ft.Text("Configuraciones"))

    nombre_in = ft.TextField(label="Nombre", width=300)
    valor_in  = ft.TextField(label="Valor", width=300)
    mensaje   = ft.Text("", color=ft.colors.GREEN)
    lista     = ft.Column()

    def cargar():
        lista.controls.clear()
        for c in get_configuraciones():
            lista.controls.append(ft.Text(f"{c['nombre']} = {c['valor']}"))
        page.update()

    def guardar(e):
        if nombre_in.value and valor_in.value:
            update_configuracion(nombre_in.value, valor_in.value)
            mensaje.value = "Configuración actualizada."
            nombre_in.value = valor_in.value = ""
            cargar()
        else:
            mensaje.value = "Faltan datos."
        page.update()

    page.controls.extend([
        nombre_in,
        valor_in,
        ft.Row([
            ft.ElevatedButton("Guardar", on_click=guardar),
            ft.ElevatedButton("Refrescar", on_click=lambda e: cargar())
        ], spacing=10),
        mensaje,
        ft.Divider(),
        ft.Text("Configuraciones existentes:", style="titleSmall"),
        lista,
        ft.Divider(),
        ft.ElevatedButton(
            "← Volver Administración",
            icon=ft.icons.ARROW_BACK_IOS,
            on_click=lambda e: importlib
                .import_module("gui.admin.admin_main")
                .mostrar_admin_main(page)
        )
    ])
    cargar()
