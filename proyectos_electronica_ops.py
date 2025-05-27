from app.database.database import get_db
from bson.objectid import ObjectId
from datetime import datetime
from datetime import datetime
from app.database.database import get_db
from app.operations.validations import empleado_exists

def add_tarea_financiera(titulo, descripcion, responsable_id):
    if not empleado_exists(responsable_id):
        raise ValueError(f"Responsable no registrado: {responsable_id}")
    db = get_db()
    db["sistemas_analisis_financiero"].insert_one({
        "titulo": titulo,
        "descripcion": descripcion,
        "responsable_id": responsable_id,
        "fecha": datetime.now()
    })
    return True

def obtener_proyectos_electronica():
    db = get_db()
    return list(db["sistemas_proyectos_electronica"].find().sort("fecha", -1))

def agregar_proyecto_electronica(nombre, tipo, responsable):
    db = get_db()
    db["sistemas_proyectos_electronica"].insert_one({
        "nombre": nombre,
        "tipo": tipo,
        "responsable": responsable,
        "fecha": datetime.now()
    })

def eliminar_proyecto_electronica(proyecto_id):
    db = get_db()
    db["sistemas_proyectos_electronica"].delete_one({"_id": ObjectId(proyecto_id)})
