import flet as ft
import importlib
from app.operations.rrhh.reclutamiento_ops import (
    obtener_candidatos,
    agregar_candidato,
    eliminar_candidato
)
from app.operations.rrhh.seguro_ops import (
    obtener_seguro,
    agregar_seguro,
    eliminar_seguro
)
from gui.utils.logo_utils import get_logo_image

def mostrar_reclutamiento_seguro_page(page: ft.Page):
    page.title = "Reclutamiento & Seguro"
    page.controls.clear()

    # 1) Logo al tope
    page.controls.append(get_logo_image())

    page.appbar = ft.AppBar(title=ft.Text("Reclutamiento & Seguro"))

    # Columnas para cada pestaña
    tab_reclu = ft.Column(scroll=ft.ScrollMode.AUTO, spacing=10)
    tab_seg   = ft.Column(scroll=ft.ScrollMode.AUTO, spacing=10)

    # --- Reclutamiento ---
    nombre    = ft.TextField(label="Candidato", width=300)
    puesto    = ft.TextField(label="Puesto Aplicado", width=300)
    contacto  = ft.TextField(label="Contacto", width=300)
    lista_rec = ft.ListView(expand=True, spacing=5, height=200)

    def cargar_reclu():
        lista_rec.controls.clear()
        for c in obtener_candidatos():
            txt = f"{c['nombre']} — {c['puesto']} — {c['estatus']}"
            lista_rec.controls.append(
                ft.Row([
                    ft.Text(txt, expand=True),
                    ft.IconButton(icon=ft.icons.DELETE,
                                  on_click=lambda e, _id=c["_id"]: borrar_candidato(_id))
                ])
            )
        page.update()

    def agregar_cand(e):
        if nombre.value and puesto.value and contacto.value:
            agregar_candidato(nombre.value, puesto.value, contacto.value)
            nombre.value = puesto.value = contacto.value = ""
            cargar_reclu()

    def borrar_candidato(_id):
        eliminar_candidato(str(_id))
        cargar_reclu()

    tab_reclu.controls.extend([
        nombre,
        puesto,
        contacto,
        ft.Row([
            ft.ElevatedButton("Registrar", on_click=agregar_cand),
            ft.ElevatedButton("Refrescar",  on_click=lambda e: cargar_reclu())
        ], spacing=10),
        ft.Divider(),
        lista_rec,
        # ← Aquí va el botón justo debajo de la lista de reclutamiento
        ft.Divider(),
        ft.ElevatedButton(
            "← Volver RRHH",
            icon=ft.icons.ARROW_BACK_IOS,
            on_click=lambda e: importlib
                .import_module("gui.rrhh.hr_main")
                .mostrar_rrhh_main(page)
        )
    ])
    cargar_reclu()

    # --- Seguro Social ---
    empleado   = ft.TextField(label="Empleado", width=300)
    movimiento = ft.Dropdown(
        label="Movimiento",
        options=[ft.dropdown.Option("Alta"), ft.dropdown.Option("Baja")]
    )
    lista_seg  = ft.ListView(expand=True, spacing=5, height=200)

    def cargar_seg():
        lista_seg.controls.clear()
        for s in obtener_seguro():
            txt = f"{s['nombre_empleado']} — {s['tipo_movimiento']} — {s['fecha'].strftime('%Y-%m-%d')}"
            lista_seg.controls.append(
                ft.Row([
                    ft.Text(txt, expand=True),
                    ft.IconButton(icon=ft.icons.DELETE,
                                  on_click=lambda e, _id=s["_id"]: borrar_seguro(_id))
                ])
            )
        page.update()

    def agregar_seg(e):
        if empleado.value and movimiento.value:
            agregar_seguro(empleado.value, movimiento.value)
            empleado.value = ""
            movimiento.value = None
            cargar_seg()

    def borrar_seguro(_id):
        eliminar_seguro(str(_id))
        cargar_seg()

    tab_seg.controls.extend([
        empleado,
        movimiento,
        ft.Row([
            ft.ElevatedButton("Registrar", on_click=agregar_seg),
            ft.ElevatedButton("Refrescar",  on_click=lambda e: cargar_seg())
        ], spacing=10),
        ft.Divider(),
        lista_seg,
        # ← Aquí va el botón justo debajo de la lista de seguro
        ft.Divider(),
        ft.ElevatedButton(
            "← Volver RRHH",
            icon=ft.icons.ARROW_BACK_IOS,
            on_click=lambda e: importlib
                .import_module("gui.rrhh.hr_main")
                .mostrar_rrhh_main(page)
        )
    ])
    cargar_seg()

    # Finalmente renderizamos el Tabs en la página
    page.controls.append(
        ft.Column(
            [
                ft.Tabs(
                    selected_index=0,
                    tabs=[
                        ft.Tab(text="Reclutamiento", content=tab_reclu),
                        ft.Tab(text="Seguro Social", content=tab_seg),
                    ],
                    expand=1
                )
            ],
            expand=1
        )
    )
    page.update()
