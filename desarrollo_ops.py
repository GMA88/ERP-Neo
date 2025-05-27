from app.database.database import get_db
from bson.objectid import ObjectId
from app.database.database import get_db
from datetime import datetime
from app.operations.validations import empleado_exists

def add_proyecto_mantenimiento(nombre, descripcion, responsable_id):
    if not empleado_exists(responsable_id):
        raise ValueError(f"Empleado no registrado: {responsable_id}")
    db = get_db()
    db["operaciones_mantenimiento"].insert_one({
        "nombre": nombre,
        "descripcion": descripcion,
        "responsable_id": responsable_id,
        "fecha": datetime.now()
    })
    return True

def get_desarrollos():
    db = get_db()
    return list(db["operaciones_desarrollo"].find().sort("fecha_inicio", -1))

def add_desarrollo(proyecto, descripcion, responsable, fecha_inicio, estado):
    db = get_db()
    db["operaciones_desarrollo"].insert_one({
        "proyecto": proyecto,
        "descripcion": descripcion,
        "responsable": responsable,
        "fecha_inicio": fecha_inicio,
        "estado": estado
    })

def delete_desarrollo(desarrollo_id):
    db = get_db()
    db["operaciones_desarrollo"].delete_one({"_id": ObjectId(desarrollo_id)})
