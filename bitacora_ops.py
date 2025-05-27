from app.database.database import get_db
from datetime import datetime
from bson.objectid import ObjectId

def add_bitacora(evento: str, responsable: str, fecha: datetime = None) -> None:
    """
    Registra una entrada en la bitácora de seguridad.
    - evento: descripción del evento o incidencia.
    - responsable: usuario que registra el evento.
    - fecha: datetime de registro (por defecto ahora).
    """
    db = get_db()
    if db is None:
        raise ConnectionError("No se pudo conectar a la base de datos.")
    db["seguridad_bitacora"].insert_one({
        "evento": evento,
        "responsable": responsable,
        "fecha": fecha or datetime.now()
    })


def get_bitacoras(limit: int = 100) -> list[dict]:
    """
    Obtiene las entradas de bitácora más recientes.
    - limit: número máximo de registros a devolver.
    """
    db = get_db()
    if db is None:
        raise ConnectionError("No se pudo conectar a la base de datos.")
    return list(
        db["seguridad_bitacora"]
        .find()
        .sort("fecha", -1)
        .limit(limit)
    )


def eliminar_bitacora(bitacora_id: str) -> bool:
    """
    Elimina una entrada de la bitácora por su _id.
    Retorna True si se eliminó un registro.
    """
    db = get_db()
    if db is None:
        raise ConnectionError("No se pudo conectar a la base de datos.")
    result = db["seguridad_bitacora"].delete_one({"_id": ObjectId(bitacora_id)})
    return result.deleted_count > 0
