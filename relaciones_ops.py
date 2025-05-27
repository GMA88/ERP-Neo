from app.database.database import get_db
from bson.objectid import ObjectId
from datetime import datetime

def obtener_relaciones():
    db = get_db()
    return list(db["ventas_relaciones"].find().sort("fecha", -1))

def agregar_relacion(empresa, tipo, sector, contacto, responsable):
    db = get_db()
    db["ventas_relaciones"].insert_one({
        "empresa": empresa,
        "tipo": tipo,
        "sector": sector,
        "contacto": contacto,
        "responsable": responsable,
        "fecha_registro": datetime.now()
    })

def eliminar_relacion(relacion_id):
    db = get_db()
    db["ventas_relaciones"].delete_one({"_id": ObjectId(relacion_id)})

def cliente_exists(cliente_id: str) -> bool:
    db = get_db()
    try:
        obj = ObjectId(cliente_id)
    except:
        return False
    return db["ventas_clientes"].count_documents({"_id": obj}, limit=1) == 1
