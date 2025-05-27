from app.database.database import get_db
from bson.objectid import ObjectId

def get_usuarios():
    db = get_db()
    return list(db["usuarios"].find())

def add_usuario(usuario, contrasena, rol):
    db = get_db()
    db["usuarios"].insert_one({
        "usuario": usuario,
        "contrasena": contrasena,
        "rol": rol
    })

def delete_usuario(usuario_id):
    db = get_db()
    result = db["usuarios"].delete_one({"_id": ObjectId(usuario_id)})
    return result.deleted_count > 0
