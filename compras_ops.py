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

def obtener_compras():
    db = get_db()
    return list(db["compras"].find().sort("fecha", -1))

def agregar_compra(proveedor, producto, cantidad, costo_unitario, responsable):
    total = cantidad * costo_unitario
    db = get_db()
    db["compras"].insert_one({
        "proveedor": proveedor,
        "producto": producto,
        "cantidad": cantidad,
        "costo_unitario": costo_unitario,
        "total": total,
        "responsable": responsable,
        "fecha": datetime.now()
    })

def eliminar_compra(compra_id):
    db = get_db()
    db["compras"].delete_one({"_id": ObjectId(compra_id)})
