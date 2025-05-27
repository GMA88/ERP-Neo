from app.database.database import get_db
from bson.objectid import ObjectId

def obtener_capacitaciones():
    db = get_db()
    return list(db["rrhh_capacitaciones"].find().sort("fecha", -1))

def agregar_capacitacion(titulo, fecha, responsable, descripcion):
    db = get_db()
    db["rrhh_capacitaciones"].insert_one({
        "titulo": titulo,
        "fecha": fecha,
        "responsable": responsable,
        "descripcion": descripcion
    })

def eliminar_capacitacion(cap_id):
    db = get_db()
    db["rrhh_capacitaciones"].delete_one({"_id": ObjectId(cap_id)})
