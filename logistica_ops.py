from app.database.database import get_db
from bson.objectid import ObjectId
from datetime import datetime
from app.database.database import get_db
from datetime import datetime
from app.operations.validations import empleado_exists

def add_compra(item, cantidad, responsable_id):
    if not empleado_exists(responsable_id):
        raise ValueError(f"Responsable no registrado: {responsable_id}")
    db = get_db()
    db["almacen_compras"].insert_one({
        "item": item,
        "cantidad": cantidad,
        "responsable_id": responsable_id,
        "fecha": datetime.now()
    })
    return True

def obtener_logistica():
    db = get_db()
    return list(db["logistica"].find().sort("fecha_registro", -1))

def agregar_logistica(tipo, descripcion, destino, fecha_envio, responsable):
    db = get_db()
    db["logistica"].insert_one({
        "tipo": tipo,
        "descripcion": descripcion,
        "destino": destino,
        "fecha_envio": fecha_envio,
        "responsable": responsable,
        "fecha_registro": datetime.now()
    })

def eliminar_logistica(logistica_id):
    db = get_db()
    db["logistica"].delete_one({"_id": ObjectId(logistica_id)})
