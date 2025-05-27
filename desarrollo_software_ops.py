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

def obtener_proyectos():
    db = get_db()
    return list(db["sistemas_desarrollo_software"].find().sort("fecha", -1))

def agregar_proyecto(nombre, descripcion, responsable):
    db = get_db()
    db["sistemas_desarrollo_software"].insert_one({
        "nombre": nombre,
        "descripcion": descripcion,
        "responsable": responsable,
        "fecha": datetime.now()
    })

def eliminar_proyecto(proyecto_id):
    db = get_db()
    db["sistemas_desarrollo_software"].delete_one({"_id": ObjectId(proyecto_id)})
