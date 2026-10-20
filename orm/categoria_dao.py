# ============================================================
# categoria_dao.py
# DAO para la tabla categorias de PoliRestaurante.
# Implementa CRUD mediante SQLAlchemy ORM.
# ============================================================

from sqlalchemy import create_engine, func, select
from sqlalchemy.orm import sessionmaker

from config.database import obtener_url_orm
from orm.modelos import Categoria


# Motor de conexión para SQLAlchemy.
motor = create_engine(
    obtener_url_orm(),
    echo=False
)

# Fábrica de sesiones ORM.
SessionLocal = sessionmaker(
    bind=motor,
    expire_on_commit=False
)


class CategoriaDAOORM:
    """
    Gestiona la tabla categorias mediante objetos
    y sesiones de SQLAlchemy ORM.
    """

    def crear(
        self,
        nombre,
        descripcion=None,
        activa=True
    ):
        """
        Crea una categoría mediante SQLAlchemy ORM.

        Retorna:
            El objeto Categoria creado.
        """

        categoria = Categoria(
            nombre=nombre,
            descripcion=descripcion,
            activa=activa
        )

        with SessionLocal() as sesion:
            sesion.add(categoria)
            sesion.commit()
            sesion.refresh(categoria)

        return categoria

    def obtener_por_id(self, categoria_id):
        """
        Busca una categoría por su identificador.

        Retorna:
            El objeto Categoria encontrado o None.
        """

        with SessionLocal() as sesion:
            categoria = sesion.get(
                Categoria,
                categoria_id
            )

        return categoria

    def obtener_por_nombre(self, nombre):
        """
        Busca una categoría por su nombre,
        ignorando diferencias entre mayúsculas y minúsculas.

        Retorna:
            El objeto Categoria encontrado o None.
        """

        consulta = select(Categoria).where(
            func.lower(Categoria.nombre) == nombre.lower()
        )

        with SessionLocal() as sesion:
            categoria = sesion.scalars(
                consulta
            ).first()

        return categoria

    def obtener_todas(self):
        """
        Consulta todas las categorías.

        Retorna:
            Una lista de objetos Categoria ordenados por ID.
        """

        consulta = select(Categoria).order_by(
            Categoria.id
        )

        with SessionLocal() as sesion:
            categorias = list(
                sesion.scalars(consulta).all()
            )

        return categorias

    def actualizar(
        self,
        categoria_id,
        nombre,
        descripcion=None,
        activa=True
    ):
        """
        Actualiza una categoría mediante SQLAlchemy ORM.

        Retorna:
            El objeto Categoria actualizado o None.
        """

        with SessionLocal() as sesion:
            categoria = sesion.get(
                Categoria,
                categoria_id
            )

            if categoria is None:
                return None

            categoria.nombre = nombre
            categoria.descripcion = descripcion
            categoria.activa = activa

            sesion.commit()
            sesion.refresh(categoria)

        return categoria

    def eliminar(self, categoria_id):
        """
        Elimina una categoría mediante SQLAlchemy ORM.

        Retorna:
            True si fue eliminada.
            False si no existía.
        """

        with SessionLocal() as sesion:
            categoria = sesion.get(
                Categoria,
                categoria_id
            )

            if categoria is None:
                return False

            sesion.delete(categoria)
            sesion.commit()

        return True