import os
import webbrowser
import importlib
import flet as ft
import pandas as pd
import plotly.express as px
import base64
from datetime import datetime
from app.database.database import get_db
from gui.utils.logo_utils import get_logo_image

def mostrar_reportes_graficas_page(page: ft.Page):
    page.title = "Reportes y Gráficas"
    page.scroll = ft.ScrollMode.AUTO
    page.controls.clear()

    # 1) Logo al tope
    page.controls.append(get_logo_image())

    page.appbar = ft.AppBar(title=ft.Text("Reportes y Gráficas"))

    db = get_db()

    # — filtros —
    subm_dd = ft.Dropdown(
        label="Submódulo",
        width=200,
        options=[
            ft.dropdown.Option("Accesos"),
            ft.dropdown.Option("Incidencias"),
            ft.dropdown.Option("Bitácora")
        ],
        value="Bitácora"
    )
    start_tf = ft.TextField(label="Desde (YYYY-MM-DD)", width=180)
    end_tf   = ft.TextField(label="Hasta  (YYYY-MM-DD)", width=180)
    btn_filtrar = ft.ElevatedButton("Aplicar filtros")

    # — tabla resumen —
    tabla = ft.DataTable(
        columns=[
            ft.DataColumn(ft.Text("Grupo", weight="bold")),
            ft.DataColumn(ft.Text("Cantidad", weight="bold")),
        ],
        rows=[],
        width=400
    )

    # — imagen del gráfico —
    img = ft.Image(width=700)

    # — botones —
    btn_back = ft.ElevatedButton(
        "← Volver Seguridad",
        icon=ft.icons.ARROW_BACK_IOS,
        on_click=lambda e: importlib
            .import_module("gui.seguridad.seguridad_main")
            .mostrar_seguridad_main(page)
    )

    def refresh(e=None):
        # 1) Elegir colección y campo según submódulo
        cfg = {
            "Accesos":     ("seguridad_accesos",    "tipo",   "Tipo de Acceso"),
            "Incidencias": ("seguridad_incidencias","nivel",  "Nivel de Incidencia"),
            "Bitácora":    ("seguridad_bitacora",   "evento", "Tipo de Evento")
        }[subm_dd.value]
        coll_name, field, label = cfg
        coll = db[coll_name]

        # 2) Construir query
        q = {}
        if start_tf.value:
            try: q.setdefault("fecha", {})["$gte"] = datetime.fromisoformat(start_tf.value)
            except: pass
        if end_tf.value:
            try: q.setdefault("fecha", {})["$lte"] = datetime.fromisoformat(end_tf.value)
            except: pass

        # 3) Fetch y agrupación
        docs = list(coll.find(q))
        vals = [d.get(field, "N/A") for d in docs]
        counts = pd.Series(vals).value_counts()

        # 4) Actualizar tabla
        tabla.rows.clear()
        for v, c in counts.items():
            tabla.rows.append(
                ft.DataRow(cells=[ft.DataCell(ft.Text(str(v))), ft.DataCell(ft.Text(str(c)))])
            )

        # 5) Generar gráfico Plotly y convertir a PNG
        dfc = counts.reset_index()
        dfc.columns = [label, "Count"]
        if dfc.empty:
            fig = px.bar(x=[], y=[], title="No hay datos")
        else:
            fig = px.bar(
                dfc,
                x=label,
                y="Count",
                title=f"{label} vs Cantidad",
                labels={"Count": "Cantidad", label: label}
            )
        # exportar png a bytes
        img_bytes = fig.to_image(format="png", width=700, height=400, engine="kaleido")
        b64 = base64.b64encode(img_bytes).decode("ascii")
        img.src_base64 = b64

        page.update()

    # asignar callback
    btn_filtrar.on_click = refresh

    # montar UI
    page.controls.extend([
        ft.Text("🛠 Filtros", size=16),
        ft.Row(
            [subm_dd, start_tf, end_tf, btn_filtrar],
            wrap=True, spacing=10
        ),
        ft.Divider(),
        ft.Text("📊 Resumen Agrupado", size=18),
        tabla,
        ft.Divider(),
        ft.Text("📈 Gráfico", size=18),
        img,
        ft.Divider(),
        btn_back
    ])

    # carga inicial
    refresh()
