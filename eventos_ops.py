from app.database.database import get_db
from bson.objectid import ObjectId

def obtener_eventos():
    db = get_db()
    return list(db["rrhh_eventos"].find().sort("fecha", -1))

def agregar_evento(titulo, fecha, lugar, descripcion):
    db = get_db()
    db["rrhh_eventos"].insert_one({
        "titulo": titulo,
        "fecha": fecha,
        "lugar": lugar,
        "descripcion": descripcion
    })

def eliminar_evento(evento_id):
    db = get_db()
    db["rrhh_eventos"].delete_one({"_id": ObjectId(evento_id)})
