import flet as ft
from flet.controls.user_control import UserControl
from gui.utils.logo_utils import get_logo_image
from app.operations.rrhh.reportes_ops import (
    generar_reporte_pdf_rrhh,
    generar_grafico_empleados_por_depto
)

class ReportesRRHHPage(UserControl):
    def build(self):
        return ft.Column([
            ft.Text("Reportes RRHH", size=20, weight="bold"),
            ft.Row([
                ft.ElevatedButton("Generar PDF Empleados", on_click=self._pdf),
                ft.ElevatedButton("Ver Gráfico Empleados", on_click=self._grafico)
            ])
        ], alignment=ft.MainAxisAlignment.CENTER)

    def _pdf(self, e):
        path = generar_reporte_pdf_rrhh()
        ft.snack_bar.SnackBar(ft.Text(f"PDF generado: {path}")).open = True; self.page.update()

    def _grafico(self, e):
        img = generar_grafico_empleados_por_depto()
        dlg = ft.AlertDialog(
            title=ft.Text("Empleados por Departamento"),
            content=ft.Image(src=img, width=400, height=300),
            actions=[ft.TextButton("Cerrar", on_click=lambda e: dlg.close())]
        )
        self.page.dialog = dlg; dlg.open = True; self.page.update()
