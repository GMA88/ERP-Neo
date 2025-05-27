# app/operations/rrhh/empleados_ops.py

from app.database.database import get_db
from bson.objectid import ObjectId
from datetime import datetime

def get_empleados():
    """Devuelve la lista de todos los empleados."""
    db = get_db()
    if db is None:
        raise ConnectionError("No hay conexión a la base de datos")
    return list(db["rrhh_empleados"].find())

def get_empleado(empleado_id: str) -> dict:
    """Devuelve un empleado por _id o lanza ValueError."""
    db = get_db()
    if db is None:
        raise ConnectionError("No hay conexión a la base de datos")
    try:
        oid = ObjectId(empleado_id)
    except:
        raise ValueError(f"ID inválido: {empleado_id}")
    emp = db["rrhh_empleados"].find_one({"_id": oid})
    if not emp:
        raise ValueError(f"No existe empleado con id={empleado_id}")
    return emp

def add_empleado(nombre: str,
                 puesto: str,
                 departamento: str,
                 salario: float,
                 fecha_contratacion: datetime,
                 email: str,
                 telefono: str) -> bool:
    """Inserta un nuevo empleado."""
    db = get_db()
    if db is None:
        raise ConnectionError("No hay conexión a la base de datos")
    db["rrhh_empleados"].insert_one({
        "nombre": nombre,
        "puesto": puesto,
        "departamento": departamento,
        "salario": salario,
        "fecha_contratacion": fecha_contratacion,
        "email": email,
        "telefono": telefono
    })
    return True

def delete_empleado(empleado_id: str) -> bool:
    """Elimina un empleado por _id."""
    db = get_db()
    if db is None:
        raise ConnectionError("No hay conexión a la base de datos")
    try:
        oid = ObjectId(empleado_id)
    except:
        raise ValueError(f"ID inválido: {empleado_id}")
    result = db["rrhh_empleados"].delete_one({"_id": oid})
    return result.deleted_count > 0

# Aliases en español
agregar_empleado = add_empleado
eliminar_empleado = delete_empleado
obtener_empleados = get_empleados
