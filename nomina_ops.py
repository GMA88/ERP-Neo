from app.database.database import get_db
from bson.objectid import ObjectId
# app/operations/rrhh/nomina_ops.py
from datetime import datetime
from app.database.database import get_db
from app.operations.validations import empleado_exists

def add_pago(empleado_id: str, monto: float, responsable: str):
    if not empleado_exists(empleado_id):
        raise ValueError(f"No existe empleado con id={empleado_id}")
    db = get_db()
    db["rrhh_nomina"].insert_one({
        "empleado_id": empleado_id,
        "monto": monto,
        "responsable": responsable,
        "fecha": datetime.now()
    })
    return True

def obtener_nomina():
    db = get_db()
    return list(db["rrhh_nomina"].find().sort("mes", -1))

def agregar_nomina(empleado_id, mes, monto):
    db = get_db()
    db["rrhh_nomina"].insert_one({
        "empleado_id": empleado_id,
        "mes": mes,
        "monto": monto
    })

def eliminar_nomina(nomina_id):
    db = get_db()
    db["rrhh_nomina"].delete_one({"_id": ObjectId(nomina_id)})
