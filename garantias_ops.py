from app.database.database import get_db
from bson.objectid import ObjectId
from datetime import datetime, timedelta
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

def obtener_garantias(origen=None):
    """
    origen: None → todas, "compra" o "venta" para filtrar.
    """
    db = get_db()
    query = {}
    if origen:
        query["origen"] = origen
    return list(db["garantias"].find(query).sort("fecha_inicio", -1))

def agregar_garantia(tipo, producto, responsable, fecha_inicio_str, duracion_meses, origen):
    """
    origen: "compra" o "venta"
    """
    db = get_db()
    fecha_inicio = datetime.strptime(fecha_inicio_str, "%Y-%m-%d")
    fecha_fin = fecha_inicio + timedelta(days=30 * duracion_meses)
    db["garantias"].insert_one({
        "origen": origen,
        "tipo": tipo,
        "producto": producto,
        "responsable": responsable,
        "fecha_inicio": fecha_inicio,
        "fecha_fin": fecha_fin,
        "duracion_meses": duracion_meses,
        "estado": "Activa" if fecha_fin >= datetime.now() else "Expirada"
    })

def eliminar_garantia(garantia_id):
    db = get_db()
    db["garantias"].delete_one({"_id": ObjectId(garantia_id)})
