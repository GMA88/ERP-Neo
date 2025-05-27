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

def obtener_disenos():
    db = get_db()
    return list(db["sistemas_diseno_ui"].find().sort("fecha", -1))

def agregar_diseno(nombre, herramienta, responsable):
    db = get_db()
    db["sistemas_diseno_ui"].insert_one({
        "nombre": nombre,
        "herramienta": herramienta,
        "responsable": responsable,
        "fecha": datetime.now()
    })

def eliminar_diseno(diseno_id):
    db = get_db()
    db["sistemas_diseno_ui"].delete_one({"_id": ObjectId(diseno_id)})
