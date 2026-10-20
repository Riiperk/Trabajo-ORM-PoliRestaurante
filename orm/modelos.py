# ============================================================
# modelos.py
# Modelo ORM para la tabla categorias de PoliRestaurante.
#
# La tabla ya fue creada manualmente en PostgreSQL.
# Este archivo solamente realiza el mapeo objeto-relacional.
# ============================================================

from sqlalchemy import Boolean, Integer, String
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class Base(DeclarativeBase):
    """
    Clase base para los modelos de SQLAlchemy ORM.
    """

    pass


class Categoria(Base):
    """
    Representa un registro de la tabla categorias.
    """

    __tablename__ = "categorias"

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        autoincrement=True
    )

    nombre: Mapped[str] = mapped_column(
        String(100),
        nullable=False,
        unique=True
    )

    descripcion: Mapped[str | None] = mapped_column(
        String(300),
        nullable=True
    )

    activa: Mapped[bool] = mapped_column(
        Boolean,
        nullable=False,
        default=True
    )

    def __repr__(self):
        return (
            "Categoria("
            f"id={self.id}, "
            f"nombre='{self.nombre}', "
            f"descripcion='{self.descripcion}', "
            f"activa={self.activa}"
            ")"
        )