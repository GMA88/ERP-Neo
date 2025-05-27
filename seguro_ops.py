from app.database.database import get_db
from bson.objectid import ObjectId
from datetime import datetime
from app.operations.rrhh.empleados_ops import agregar_empleado, eliminar_empleado
# app/operations/rrhh/seguro_ops.py
from datetime import datetime
from app.database.database import get_db
from bson.objectid import ObjectId
from app.operations.rrhh.empleados_ops import add_empleado, delete_empleado

def alta_seguro(empleado_id: str, movimiento: str):
    # 1) Validar que el empleado ya exista en RRHH
    from app.operations.rrhh.empleados_ops import get_empleado
    get_empleado(empleado_id)  # lanza ValueError si no existe

    db = get_db()
    db["rrhh_seguro"].insert_one({
        "empleado_id": empleado_id,
        "movimiento": movimiento,
        "fecha": datetime.now()
    })
    return True

def baja_seguro(empleado_id: str):
    # 1) Eliminar de la colección de seguros
    db = get_db()
    db["rrhh_seguro"].delete_many({"empleado_id": empleado_id})
    # 2) Borrar al empleado completamente si así lo deseas:
    delete_empleado(empleado_id)
    return True


def obtener_seguro():
    db = get_db()
    return list(db["rrhh_seguro"].find())

def agregar_seguro(nombre_empleado, tipo_movimiento):
    db = get_db()
    db["rrhh_seguro"].insert_one({
        "nombre_empleado": nombre_empleado,
        "tipo_movimiento": tipo_movimiento,
        "fecha": datetime.now()
    })

def eliminar_seguro(seguro_id):
    db = get_db()
    db["rrhh_seguro"].delete_one({"_id": ObjectId(seguro_id)})
    #eliminar_empleado(empleado_id)
