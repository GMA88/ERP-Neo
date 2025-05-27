# app/operations/validations.py

from app.database.database import get_db
from bson.objectid import ObjectId

def empleado_exists(empleado_id: str) -> bool:
    """
    Devuelve True si existe un empleado con ese _id en la colección 'rrhh_empleados'.
    """
    db = get_db()
    if db is None:
        raise ConnectionError("No hay conexión a la base de datos")
    try:
        oid = ObjectId(empleado_id)
    except Exception:
        return False
    return db["rrhh_empleados"].count_documents({"_id": oid}, limit=1) == 1

def cliente_exists(cliente_id: str) -> bool:
    """
    Devuelve True si existe un cliente con ese _id en la colección 'ventas_clientes'.
    """
    db = get_db()
    if db is None:
        raise ConnectionError("No hay conexión a la base de datos")
    try:
        oid = ObjectId(cliente_id)
    except Exception:
        return False
    return db["ventas_clientes"].count_documents({"_id": oid}, limit=1) == 1

def get_empleado(empleado_id: str) -> dict:
    """
    Devuelve el documento completo de rrhh_empleados, o lanza ValueError si no existe.
    """
    db = get_db()
    if db is None:
        raise ConnectionError("No hay conexión a la base de datos")
    try:
        oid = ObjectId(empleado_id)
    except Exception:
        raise ValueError(f"ID de empleado inválido: {empleado_id}")
    emp = db["rrhh_empleados"].find_one({"_id": oid})
    if not emp:
        raise ValueError(f"No existe empleado con id={empleado_id}")
    return emp

def get_cliente(cliente_id: str) -> dict:
    """
    Devuelve el documento completo de ventas_clientes, o lanza ValueError si no existe.
    """
    db = get_db()
    if db is None:
        raise ConnectionError("No hay conexión a la base de datos")
    try:
        oid = ObjectId(cliente_id)
    except Exception:
        raise ValueError(f"ID de cliente inválido: {cliente_id}")
    cli = db["ventas_clientes"].find_one({"_id": oid})
    if not cli:
        raise ValueError(f"No existe cliente con id={cliente_id}")
    return cli
