import flet as ft
from app.auth.login import login_user
from gui.main_window import mostrar_main
from gui.utils.logo_utils import get_logo_image

def mostrar_login(page: ft.Page):
    page.title = "Iniciar Sesión"
    page.controls.clear()

    # 1) Logo al tope
    page.controls.append(get_logo_image())

    page.appbar = ft.AppBar(title=ft.Text("Iniciar Sesión"), bgcolor=ft.colors.SURFACE_VARIANT)

    usuario = ft.TextField(label="Usuario", width=300)
    contrasena = ft.TextField(label="Contraseña", password=True, can_reveal_password=True, width=300)
    mensaje = ft.Text("", color=ft.colors.RED)

    def on_login(e):
        role = login_user(usuario.value, contrasena.value)
        if role:
            # Navegar al main, pasando rol
            mostrar_main(page, role)
        else:
            mensaje.value = "Usuario o contraseña incorrectos."
            page.update()

    btn = ft.ElevatedButton("Entrar", on_click=on_login)

    page.controls.append(
        ft.Column(
            [
                usuario,
                contrasena,
                btn,
                mensaje
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=10
        )
    )
    page.update()
