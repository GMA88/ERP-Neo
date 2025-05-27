import flet as ft
import importlib
from app.operations.admin.gestion_usuarios import get_usuarios, add_usuario, delete_usuario
from gui.utils.logo_utils import get_logo_image

def mostrar_gestion_usuarios(page: ft.Page):
    page.title = "Gestión de Usuarios"
    page.scroll = ft.ScrollMode.AUTO
    page.controls.clear()

    # 1) Logo al tope
    page.controls.append(get_logo_image())

    page.appbar = ft.AppBar(title=ft.Text("Gestión de Usuarios"))

    usuario_in = ft.TextField(label="Usuario", width=300)
    pass_in    = ft.TextField(label="Contraseña", password=True, can_reveal_password=True, width=300)
    rol_in     = ft.TextField(label="Rol", width=300)
    mensaje    = ft.Text("", color=ft.colors.RED)
    lista      = ft.ListView(expand=True, spacing=5, height=300)

    def cargar():
        lista.controls.clear()
        for u in get_usuarios():
            lista.controls.append(
                ft.Row([
                    ft.Text(f"{u['usuario']} ({u['rol']})", expand=True),
                    ft.IconButton(
                        icon=ft.icons.DELETE,
                        tooltip="Eliminar",
                        on_click=lambda e, _id=u["_id"]: borrar(_id)
                    )
                ])
            )
        page.update()

    def agregar(e):
        if usuario_in.value and pass_in.value and rol_in.value:
            add_usuario(usuario_in.value, pass_in.value, rol_in.value)
            usuario_in.value = pass_in.value = rol_in.value = ""
            mensaje.value = "Usuario agregado."
        else:
            mensaje.value = "Faltan datos."
        cargar()
        page.update()

    def borrar(_id):
        delete_usuario(str(_id))
        cargar()

    page.controls.extend([
        usuario_in,
        pass_in,
        rol_in,
        ft.Row([
            ft.ElevatedButton("Agregar", on_click=agregar),
            ft.ElevatedButton("Refrescar", on_click=lambda e: cargar())
        ], spacing=10),
        mensaje,
        ft.Divider(),
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
