from app.database.database import get_db
from bson.objectid import ObjectId

def obtener_candidatos():
    db = get_db()
    return list(db["rrhh_reclutamiento"].find())

def agregar_candidato(nombre, puesto, contacto):
    db = get_db()
    db["rrhh_reclutamiento"].insert_one({
        "nombre": nombre,
        "puesto": puesto,
        "contacto": contacto,
        "estatus": "Pendiente"
    })

def eliminar_candidato(candidato_id):
    db = get_db()
    db["rrhh_reclutamiento"].delete_one({"_id": ObjectId(candidato_id)})
