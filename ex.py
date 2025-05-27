#!/usr/bin/env python
# app/scripts/test_db_connection.py

from app.database.database import get_db

def test_connection() -> bool:
    """
    Intenta conectar con la base de datos, hacer ping al servidor y listar colecciones.
    Devuelve True si todo funciona, False en caso contrario.
    """
    db = get_db()
    if db is None:
        print("❌ Error: No se pudo obtener la conexión a la base de datos.")
        return False

    try:
        # Hace ping al servidor MongoDB
        db.client.admin.command('ping')
        print("✅ Ping a MongoDB exitoso.")
    except Exception as e:
        print(f"❌ Error haciendo ping: {e!r}")
        return False

    try:
        # Lista unas cuantas colecciones
        colecciones = db.list_collection_names()
        print(f"✅ Colecciones disponibles ({len(colecciones)}): {colecciones}")
    except Exception as e:
        print(f"❌ Error listando colecciones: {e!r}")
        return False

    return True

if __name__ == "__main__":
    ok = test_connection()
    exit(0 if ok else 1)
