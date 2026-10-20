# ============================================================
# probar_conexion.py
# Comprueba la conexión a la base de datos de PoliRestaurante.
# ============================================================

import psycopg

from config.database import obtener_configuracion_driver


def probar_conexion():
    try:
        configuracion = obtener_configuracion_driver()

        with psycopg.connect(**configuracion) as conexion:
            with conexion.cursor() as cursor:
                cursor.execute(
                    "SELECT current_database(), current_user;"
                )

                resultado = cursor.fetchone()

                if resultado is not None:
                    base_datos, usuario = resultado

                    print("Conexión realizada correctamente.")
                    print(f"Base de datos: {base_datos}")
                    print(f"Usuario: {usuario}")

    except Exception as error:
        print("No fue posible conectar con PostgreSQL.")
        print(f"Detalle: {error}")


if __name__ == "__main__":
    probar_conexion()