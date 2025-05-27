from app.database.database import get_db
from bson.objectid import ObjectId
from datetime import datetime
from datetime import datetime
from app.database.database import get_db
from bson.objectid import ObjectId
from app.operations.validations import cliente_exists

def add_venta_proyecto(proyecto_id, cliente_id, monto, vendedor_id):
    if not cliente_exists(cliente_id):
        raise ValueError(f"Cliente no registrado: {cliente_id}")
    # (opcional) validar vendedor_id también contra empleados
    db = get_db()
    db["ventas_proyectos"].insert_one({
        "proyecto_id": proyecto_id,
        "cliente_id": cliente_id,
        "monto": monto,
        "vendedor_id": vendedor_id,
        "fecha": datetime.now()
    })
    return True

def obtener_ventas_proyectos():
    db = get_db()
    return list(db["ventas_proyectos"].find().sort("fecha", -1))

def agregar_venta_proyecto(proyecto, cliente, monto, responsable):
    db = get_db()
    db["ventas_proyectos"].insert_one({
        "proyecto": proyecto,
        "cliente": cliente,
        "monto": monto,
        "responsable": responsable,
        "fecha": datetime.now()
    })

def eliminar_venta_proyecto(venta_id):
    db = get_db()
    db["ventas_proyectos"].delete_one({"_id": ObjectId(venta_id)})
