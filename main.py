import os, sys

# Si estamos ejecutando dentro del EXE (sys._MEIPASS existe),
# base_dir será la carpeta temporal donde PyInstaller descomprime todo.
if getattr(sys, "frozen", False):
    base_dir = sys._MEIPASS
else:
    base_dir = os.path.dirname(__file__)

# Apuntamos FLET_HOME a nuestro runtime empaquetado
os.environ["FLET_HOME"] = os.path.join(base_dir, "flet_runtime")

import flet as ft
from gui.login_window import mostrar_login

def main(page: ft.Page):
    # Configuración básica de la ventana
    page.window_title = "ERP System"
    page.padding = 20
    page.vertical_alignment = ft.MainAxisAlignment.START

    # Iniciamos en el login
    mostrar_login(page)

if __name__ == "__main__":
    # Arranca el servidor de Flet
    ft.app(target=main)
