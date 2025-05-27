# generar_usuarios_de_prueba.py

from passlib.context import CryptContext

pwd_ctx = CryptContext(schemes=["bcrypt"], deprecated="auto")

# Define aquí tus usuarios: (username, plain_password, role)
usuarios = [
    ("user01", "pass01", "ventas"),
    ("user02", "pass02", "finanzas"),
    ("user03", "pass03", "seguridad"),
    ("user04", "pass04", "rrhh"),
    ("user05", "pass05", "admin"),
]

for username, plain_pw, role in usuarios:
    hashed = pwd_ctx.hash(plain_pw)
    print(
        "INSERT INTO usuarios (username, hashed_password, role) VALUES "
        f"('{username}', '{hashed}', '{role}');"
    )
