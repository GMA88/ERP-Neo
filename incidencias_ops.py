from app.database.database import get_db
from bson.objectid import ObjectId
from datetime import datetime

def obtener_incidencias():
    db = get_db()
    return list(db["seguridad_incidencias"].find())

def agregar_incidencia(reporte, responsable):
    db = get_db()
    db["seguridad_incidencias"].insert_one({
        "reporte": reporte,
        "responsable": responsable,
        "fecha": datetime.now()
    })

def eliminar_incidencia(incidencia_id):
    db = get_db()
    db["seguridad_incidencias"].delete_one({"_id": ObjectId(incidencia_id)})
