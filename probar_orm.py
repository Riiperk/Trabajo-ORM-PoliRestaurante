# ============================================================
# probar_orm.py
# Prueba completa del CRUD de categorías con SQLAlchemy ORM.
# ============================================================

from orm.categoria_dao import CategoriaDAOORM


def mostrar_categoria(categoria):
    """
    Muestra los datos de una categoría.
    """

    if categoria is None:
        print("Categoría no encontrada.")
        return

    print(f"ID: {categoria.id}")
    print(f"Nombre: {categoria.nombre}")
    print(f"Descripción: {categoria.descripcion}")
    print(f"Activa: {categoria.activa}")


def probar_crud_orm():
    categoria_dao = CategoriaDAOORM()

    print("=== 1. CONSULTAR CATEGORÍAS EXISTENTES ===")

    categorias = categoria_dao.obtener_todas()

    if not categorias:
        print("No hay categorías registradas.")
    else:
        for categoria in categorias:
            print(
                f"ID: {categoria.id} | "
                f"Nombre: {categoria.nombre} | "
                f"Descripción: {categoria.descripcion} | "
                f"Activa: {categoria.activa}"
            )

    print("\n=== 2. PREPARAR CATEGORÍA DE PRUEBA ===")

    categoria_existente = categoria_dao.obtener_por_nombre(
        "Entradas ORM"
    )

    if categoria_existente is not None:
        categoria_dao.eliminar(categoria_existente.id)
        print("Se eliminó una prueba anterior.")

    print("\n=== 3. CREAR CATEGORÍA CON ORM ===")

    categoria_creada = categoria_dao.crear(
        nombre="Entradas ORM",
        descripcion="Categoría temporal creada con SQLAlchemy ORM",
        activa=True
    )

    mostrar_categoria(categoria_creada)

    categoria_id = categoria_creada.id

    print("\n=== 4. CONSULTAR CATEGORÍA POR ID ===")

    categoria_consultada = categoria_dao.obtener_por_id(
        categoria_id
    )

    mostrar_categoria(categoria_consultada)

    print("\n=== 5. ACTUALIZAR CATEGORÍA CON ORM ===")

    categoria_actualizada = categoria_dao.actualizar(
        categoria_id=categoria_id,
        nombre="Entradas",
        descripcion="Entradas y aperitivos del restaurante",
        activa=True
    )

    mostrar_categoria(categoria_actualizada)

    print("\n=== 6. CONSULTAR CATEGORÍA POR NOMBRE ===")

    categoria_por_nombre = categoria_dao.obtener_por_nombre(
        "Entradas"
    )

    mostrar_categoria(categoria_por_nombre)

    print("\n=== 7. ELIMINAR CATEGORÍA CON ORM ===")

    eliminada = categoria_dao.eliminar(categoria_id)

    if eliminada:
        print("Categoría eliminada correctamente.")
    else:
        print("No fue posible eliminar la categoría.")

    print("\n=== 8. COMPROBAR ELIMINACIÓN ===")

    categoria_eliminada = categoria_dao.obtener_por_id(
        categoria_id
    )

    if categoria_eliminada is None:
        print("La categoría ya no existe en la base de datos.")
    else:
        print("La categoría todavía existe.")


if __name__ == "__main__":
    probar_crud_orm()