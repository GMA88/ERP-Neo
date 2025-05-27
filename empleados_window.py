import flet as ft
import importlib
from app.operations.rrhh.empleados_ops import obtener_empleados, agregar_empleado, eliminar_empleado
from gui.utils.logo_utils import get_logo_image

def mostrar_empleados_page(page: ft.Page):
    page.title = "Empleados"
    page.controls.clear()

    # 1) Logo al tope
    page.controls.append(get_logo_image())

    page.appbar = ft.AppBar(title=ft.Text("Empleados"))

    nombre     = ft.TextField(label="Nombre completo")
    puesto     = ft.TextField(label="Puesto")
    departamento = ft.TextField(label="Departamento")
    salario    = ft.TextField(label="Salario", keyboard_type=ft.KeyboardType.NUMBER)
    email      = ft.TextField(label="Email")
    telefono   = ft.TextField(label="Teléfono")
    lista      = ft.ListView(expand=True, spacing=5, height=300)

    def cargar():
        lista.controls.clear()
        for e in obtener_empleados():
            texto = f"{e['nombre']} — {e['puesto']} — {e['departamento']} — ${e['salario']}"
            lista.controls.append(
                ft.Row([
                    ft.Text(texto, expand=True),
                    ft.IconButton(
                        icon=ft.icons.DELETE,
                        on_click=lambda evt, _id=e["_id"]: borrar(_id)
                    )
                ])
            )
        page.update()

    def agregar(evt):
        agregar_empleado(
            nombre.value,
            puesto.value,
            departamento.value,
            float(salario.value or 0),
            email.value,
            telefono.value
        )
        for fld in (nombre, puesto, departamento, salario, email, telefono):
            fld.value = ""
        cargar()

    def borrar(_id):
        eliminar_empleado(str(_id))
        cargar()

    page.controls.extend([
        nombre, puesto, departamento, salario, email, telefono,
        ft.Row([
            ft.ElevatedButton("Agregar", on_click=agregar),
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
