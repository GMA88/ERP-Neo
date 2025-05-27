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

def obtener_ventas_materiales():
    db = get_db()
    return list(db["ventas_materiales"].find().sort("fecha", -1))

def agregar_venta_material(producto, cantidad, precio_unitario, cliente, vendedor):
    total = cantidad * precio_unitario
    db = get_db()
    db["ventas_materiales"].insert_one({
        "producto": producto,
        "cantidad": cantidad,
        "precio_unitario": precio_unitario,
        "total": total,
        "cliente": cliente,
        "vendedor": vendedor,
        "fecha": datetime.now()
    })

def eliminar_venta_material(venta_id):
    db = get_db()
    db["ventas_materiales"].delete_one({"_id": ObjectId(venta_id)})
