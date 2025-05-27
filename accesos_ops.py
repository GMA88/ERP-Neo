from app.database.database import get_db
from bson.objectid import ObjectId
from datetime import datetime
# app/operations/seguridad/accesos_ops.py
from datetime import datetime
from app.database.database import get_db
from app.operations.validations import empleado_exists

def add_acceso(empleado_id: str, tipo: str):
    if not empleado_exists(empleado_id):
        raise ValueError(f"Empleado {empleado_id} no registrado")
    db = get_db()
    db["seguridad_accesos"].insert_one({
        "empleado_id": empleado_id,
        "tipo": tipo,
        "fecha": datetime.now()
    })
    return True

def obtener_accesos():
    db = get_db()
    return list(db["seguridad_accesos"].find())

def agregar_acceso(nombre, area, motivo):
    db = get_db()
    db["seguridad_accesos"].insert_one({
        "nombre": nombre,
        "area": area,
        "motivo": motivo,
        "fecha": datetime.now()
    })

def eliminar_acceso(acceso_id):
    db = get_db()
    db["seguridad_accesos"].delete_one({"_id": ObjectId(acceso_id)})
