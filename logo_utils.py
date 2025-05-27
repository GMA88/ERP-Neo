import os
import base64
import flet as ft

# Cache para el Base64 del logo
_logo_b64 = None

def get_logo_image() -> ft.Image:
    """
    Devuelve un ft.Image con el logo embebido en base64.
    Busca en:
      1) <project_root>/gui/utils/assets/logo.(png|jpg|jpeg|svg)
      2) <project_root>/assets/logo.(png|jpg|jpeg|svg)
    """
    global _logo_b64
    if _logo_b64 is None:
        here = os.path.dirname(__file__)
        # posibles carpetas donde buscar
        search_dirs = [
            os.path.join(here, "assets"),         # gui/utils/assets/
            os.path.abspath(os.path.join(here, "..", "..", "assets"))  # <root>/assets/
        ]
        exts = ["png", "jpg", "jpeg", "svg"]
        logo_path = None

        # buscar archivo existente
        for d in search_dirs:
            for ext in exts:
                candidate = os.path.join(d, f"logo.{ext}")
                if os.path.exists(candidate):
                    logo_path = candidate
                    break
            if logo_path:
                break

        if not logo_path:
            raise FileNotFoundError(
                f"No encontré tu logo en ninguna de estas rutas:\n"
                + "\n".join(search_dirs)
                + f"\nCon extensiones posibles: {exts}"
            )

        # cargar y codificar en base64
        with open(logo_path, "rb") as f:
            _logo_b64 = base64.b64encode(f.read()).decode("ascii")

    # retornar widget Image ya listo
    return ft.Image(
        src_base64=_logo_b64,
        width=200,
        height=60,
        fit=ft.ImageFit.CONTAIN
    )
