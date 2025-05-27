from app.database.database import get_db
from fpdf import FPDF
import matplotlib.pyplot as plt

def generar_reporte_pdf_rrhh(path="reporte_rrhh.pdf"):
    db = get_db()
    empleados = list(db["rrhh_empleados"].find())
    pdf = FPDF(); pdf.add_page(); pdf.set_font("Arial", size=12)
    pdf.cell(0, 10, "Reporte RRHH: Empleados", ln=True)
    for e in empleados:
        pdf.cell(0, 8, f"{e['nombre']} – {e['puesto']} – ${e['salario']}", ln=True)
    pdf.output(path)
    return path

def generar_grafico_empleados_por_depto(path="grafico_rrhh_empleados.png"):
    db = get_db()
    pipeline = [{"$group": {"_id": "$departamento", "count": {"$sum":1}}}]
    datos = list(db["rrhh_empleados"].aggregate(pipeline))
    labels = [d["_id"] for d in datos]
    counts = [d["count"] for d in datos]
    plt.figure(figsize=(6,4))
    plt.bar(labels, counts)
    plt.title("Empleados por Departamento")
    plt.tight_layout()
    plt.savefig(path)
    plt.close()
    return path
