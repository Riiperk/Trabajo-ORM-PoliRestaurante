# ============================================================
# probar_driver.py
# Prueba completa del CRUD de categorías mediante psycopg.
# ============================================================

from driver.categoria_dao import CategoriaDAODriver


def mostrar_categoria(categoria):
    if categoria is None:
        print("Categoría no encontrada.")
        return

    print(f"ID: {categoria[0]}")
    print(f"Nombre: {categoria[1]}")
    print(f"Descripción: {categoria[2]}")
    print(f"Activa: {categoria[3]}")


def probar_crud():
    categoria_dao = CategoriaDAODriver()

    print("=== 1. CONSULTAR CATEGORÍAS EXISTENTES ===")

    categorias = categoria_dao.obtener_todas()

    if not categorias:
        print("No hay categorías registradas.")
    else:
        for categoria in categorias:
            print(
                f"ID: {categoria[0]} | "
                f"Nombre: {categoria[1]} | "
                f"Descripción: {categoria[2]} | "
                f"Activa: {categoria[3]}"
            )

    print("\n=== 2. CREAR CATEGORÍA DE PRUEBA ===")

    categoria_existente = categoria_dao.obtener_por_nombre(
        "Postres de prueba"
    )

    if categoria_existente is not None:
        categoria_dao.eliminar(categoria_existente[0])

    categoria_creada = categoria_dao.crear(
        nombre="Postres de prueba",
        descripcion="Categoría temporal para comprobar el CRUD",
        activa=True
    )

    mostrar_categoria(categoria_creada)

    categoria_id = categoria_creada[0]

    print("\n=== 3. CONSULTAR CATEGORÍA POR ID ===")

    categoria_consultada = categoria_dao.obtener_por_id(
        categoria_id
    )

    mostrar_categoria(categoria_consultada)

    print("\n=== 4. ACTUALIZAR CATEGORÍA ===")

    categoria_actualizada = categoria_dao.actualizar(
        categoria_id=categoria_id,
        nombre="Postres",
        descripcion="Postres y productos dulces",
        activa=True
    )

    mostrar_categoria(categoria_actualizada)

    print("\n=== 5. CONSULTAR CATEGORÍA POR NOMBRE ===")

    categoria_por_nombre = categoria_dao.obtener_por_nombre(
        "Postres"
    )

    mostrar_categoria(categoria_por_nombre)

    print("\n=== 6. ELIMINAR CATEGORÍA DE PRUEBA ===")

    eliminada = categoria_dao.eliminar(categoria_id)

    if eliminada:
        print("Categoría eliminada correctamente.")
    else:
        print("No fue posible eliminar la categoría.")

    print("\n=== 7. COMPROBAR ELIMINACIÓN ===")

    categoria_eliminada = categoria_dao.obtener_por_id(
        categoria_id
    )

    if categoria_eliminada is None:
        print("La categoría ya no existe en la base de datos.")
    else:
        print("La categoría todavía existe.")


if __name__ == "__main__":
    probar_crud()