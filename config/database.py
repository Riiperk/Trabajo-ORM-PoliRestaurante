# ============================================================
# database.py
# Centraliza la configuración de conexión a PostgreSQL.
# La configuración se obtiene desde el archivo .env.
# ============================================================

import os

from dotenv import load_dotenv


# Carga las variables definidas en el archivo .env
load_dotenv()


DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")


def obtener_configuracion_driver() -> dict:
    """
    Retorna la configuración utilizada por psycopg
    para conectarse directamente a PostgreSQL.
    """
    return {
        "host": DB_HOST,
        "port": DB_PORT,
        "dbname": DB_NAME,
        "user": DB_USER,
        "password": DB_PASSWORD,
    }


def obtener_url_orm() -> str:
    """
    Construye la URL utilizada por SQLAlchemy ORM.
    """
    return (
        f"postgresql+psycopg://{DB_USER}:{DB_PASSWORD}"
        f"@{DB_HOST}:{DB_PORT}/{DB_NAME}"
    )