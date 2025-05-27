from app.database.database import get_db

def get_configuraciones():
    """
    Devuelve todas las configuraciones almacenadas.
    """
    db = get_db()
    if db is None:
        raise ConnectionError("No se pudo conectar a la base de datos.")
    return list(db["configuraciones"].find())

def update_configuracion(nombre: str, valor: str):
    """
    Inserta o actualiza una configuración por su nombre.
    """
    db = get_db()
    if db is None:
        raise ConnectionError("No se pudo conectar a la base de datos.")
    db["configuraciones"].update_one(
        {"nombre": nombre},
        {"$set": {"valor": valor}},
        upsert=True
    )
