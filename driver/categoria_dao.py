# ============================================================
# categoria_dao.py
# DAO para la tabla categorias de PoliRestaurante.
# Implementa CRUD mediante psycopg y SQL directo.
# ============================================================

import psycopg

from config.database import obtener_configuracion_driver


class CategoriaDAODriver:
    """
    Gestiona el acceso directo a la tabla categorias
    mediante el driver psycopg.
    """

    def crear(
        self,
        nombre,
        descripcion=None,
        activa=True
    ):
        """
        Registra una categoría.

        Retorna:
            La categoría creada.
        """

        consulta = """
            INSERT INTO categorias (
                nombre,
                descripcion,
                activa
            )
            VALUES (%s, %s, %s)
            RETURNING id, nombre, descripcion, activa;
        """

        configuracion = obtener_configuracion_driver()

        with psycopg.connect(**configuracion) as conexion:
            with conexion.cursor() as cursor:
                cursor.execute(
                    consulta,
                    (nombre, descripcion, activa)
                )
                categoria_creada = cursor.fetchone()

            conexion.commit()

        return categoria_creada

    def obtener_por_id(self, categoria_id):
        """
        Busca una categoría por su identificador.

        Retorna:
            La categoría encontrada o None.
        """

        consulta = """
            SELECT id, nombre, descripcion, activa
            FROM categorias
            WHERE id = %s;
        """

        configuracion = obtener_configuracion_driver()

        with psycopg.connect(**configuracion) as conexion:
            with conexion.cursor() as cursor:
                cursor.execute(
                    consulta,
                    (categoria_id,)
                )
                categoria = cursor.fetchone()

        return categoria

    def obtener_por_nombre(self, nombre):
        """
        Busca una categoría por su nombre.

        Retorna:
            La categoría encontrada o None.
        """

        consulta = """
            SELECT id, nombre, descripcion, activa
            FROM categorias
            WHERE LOWER(nombre) = LOWER(%s);
        """

        configuracion = obtener_configuracion_driver()

        with psycopg.connect(**configuracion) as conexion:
            with conexion.cursor() as cursor:
                cursor.execute(
                    consulta,
                    (nombre,)
                )
                categoria = cursor.fetchone()

        return categoria

    def obtener_todas(self):
        """
        Consulta todas las categorías.

        Retorna:
            Una lista con las categorías ordenadas por ID.
        """

        consulta = """
            SELECT id, nombre, descripcion, activa
            FROM categorias
            ORDER BY id;
        """

        configuracion = obtener_configuracion_driver()

        with psycopg.connect(**configuracion) as conexion:
            with conexion.cursor() as cursor:
                cursor.execute(consulta)
                categorias = cursor.fetchall()

        return categorias

    def actualizar(
        self,
        categoria_id,
        nombre,
        descripcion=None,
        activa=True
    ):
        """
        Actualiza una categoría existente.

        Retorna:
            La categoría actualizada o None si no existe.
        """

        consulta = """
            UPDATE categorias
            SET nombre = %s,
                descripcion = %s,
                activa = %s
            WHERE id = %s
            RETURNING id, nombre, descripcion, activa;
        """

        configuracion = obtener_configuracion_driver()

        with psycopg.connect(**configuracion) as conexion:
            with conexion.cursor() as cursor:
                cursor.execute(
                    consulta,
                    (
                        nombre,
                        descripcion,
                        activa,
                        categoria_id
                    )
                )
                categoria_actualizada = cursor.fetchone()

            conexion.commit()

        return categoria_actualizada

    def eliminar(self, categoria_id):
        """
        Elimina una categoría por su identificador.

        Retorna:
            True si fue eliminada.
            False si no existía.
        """

        consulta = """
            DELETE FROM categorias
            WHERE id = %s
            RETURNING id;
        """

        configuracion = obtener_configuracion_driver()

        with psycopg.connect(**configuracion) as conexion:
            with conexion.cursor() as cursor:
                cursor.execute(
                    consulta,
                    (categoria_id,)
                )
                categoria_eliminada = cursor.fetchone()

            conexion.commit()

        return categoria_eliminada is not None