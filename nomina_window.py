import flet as ft
import importlib
from app.operations.rrhh.nomina_ops import obtener_nomina, agregar_nomina, eliminar_nomina
from gui.utils.logo_utils import get_logo_image

def mostrar_nomina_page(page: ft.Page):
    page.title = "Nómina"
    page.controls.clear()

    # 1) Logo al tope
    page.controls.append(get_logo_image())

    page.appbar = ft.AppBar(title=ft.Text("Nómina"))

    empleado = ft.TextField(label="ID Empleado", width=200)
    mes      = ft.TextField(label="Mes/Año (MM-YYYY)", width=200)
    monto    = ft.TextField(label="Monto", keyboard_type=ft.KeyboardType.NUMBER, width=200)
    lista    = ft.ListView(expand=True, spacing=5, height=300)

    def cargar():
        lista.controls.clear()
        for n in obtener_nomina():
            texto = f"Empleado {n['empleado_id']} — {n['mes']} — ${n['monto']}"
            lista.controls.append(
                ft.Row([
                    ft.Text(texto, expand=True),
                    ft.IconButton(icon=ft.icons.DELETE, on_click=lambda evt, _id=n["_id"]: borrar(_id))
                ])
            )
        page.update()

    def agregar(evt):
        agregar_nomina(empleado.value, mes.value, float(monto.value))
        empleado.value = mes.value = monto.value = ""
        cargar()

    def borrar(_id):
        eliminar_nomina(str(_id))
        cargar()

    page.controls.extend([
        empleado, mes, monto,
        ft.Row([
            ft.ElevatedButton("Agregar Pago", on_click=agregar),
            ft.ElevatedButton("Refrescar", on_click=lambda e: cargar())
        ], spacing=10),
        ft.Divider(),
        lista,
        ft.ElevatedButton(
            "← Volver RRHH",
            on_click=lambda e: importlib
                .import_module("gui.rrhh.hr_main")
                .mostrar_rrhh_main(page)
        )
    ])
    cargar()
