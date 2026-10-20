# ============================================================
# menu_driver.py
# Menú interactivo para gestionar categorías mediante
# psycopg y sentencias SQL directas.
# ============================================================

from driver.categoria_dao import CategoriaDAODriver


def mostrar_categoria(categoria):
    """
    Muestra una categoría obtenida mediante psycopg.
    """

    if categoria is None:
        print("Categoría no encontrada.")
        return

    print(f"ID: {categoria[0]}")
    print(f"Nombre: {categoria[1]}")
    print(f"Descripción: {categoria[2]}")
    print(f"Activa: {'Sí' if categoria[3] else 'No'}")


def listar_categorias(categoria_dao):
    """
    Consulta y muestra todas las categorías.
    """

    categorias = categoria_dao.obtener_todas()

    if not categorias:
        print("No hay categorías registradas.")
        return

    print("\n=== CATEGORÍAS REGISTRADAS ===")

    for categoria in categorias:
        print(
            f"ID: {categoria[0]} | "
            f"Nombre: {categoria[1]} | "
            f"Descripción: {categoria[2] or 'Sin descripción'} | "
            f"Activa: {'Sí' if categoria[3] else 'No'}"
        )


def crear_categoria(categoria_dao):
    """
    Solicita los datos y registra una categoría.
    """

    print("\n=== CREAR CATEGORÍA ===")

    nombre = input("Nombre: ").strip()
    descripcion = input("Descripción: ").strip()

    if not nombre:
        print("El nombre es obligatorio.")
        return

    if not descripcion:
        descripcion = None

    categoria_existente = categoria_dao.obtener_por_nombre(
        nombre
    )

    if categoria_existente is not None:
        print("Ya existe una categoría con ese nombre.")
        return

    categoria = categoria_dao.crear(
        nombre=nombre,
        descripcion=descripcion,
        activa=True
    )

    print("Categoría creada correctamente.")
    mostrar_categoria(categoria)


def consultar_categoria(categoria_dao):
    """
    Consulta una categoría por su ID.
    """

    print("\n=== CONSULTAR CATEGORÍA ===")

    try:
        categoria_id = int(
            input("ID de la categoría: ").strip()
        )
    except ValueError:
        print("El ID debe ser un número entero.")
        return

    categoria = categoria_dao.obtener_por_id(
        categoria_id
    )

    mostrar_categoria(categoria)


def actualizar_categoria(categoria_dao):
    """
    Actualiza una categoría existente.
    """

    print("\n=== ACTUALIZAR CATEGORÍA ===")

    try:
        categoria_id = int(
            input("ID de la categoría: ").strip()
        )
    except ValueError:
        print("El ID debe ser un número entero.")
        return

    categoria_actual = categoria_dao.obtener_por_id(
        categoria_id
    )

    if categoria_actual is None:
        print("Categoría no encontrada.")
        return

    print("Deja un campo vacío para conservar su valor.")

    nombre = input(
        f"Nombre [{categoria_actual[1]}]: "
    ).strip()

    descripcion_actual = categoria_actual[2] or ""

    descripcion = input(
        f"Descripción [{descripcion_actual}]: "
    ).strip()

    estado_actual = "s" if categoria_actual[3] else "n"

    activa = input(
        f"¿Está activa? (s/n) [{estado_actual}]: "
    ).strip().lower()

    if not nombre:
        nombre = categoria_actual[1]

    if not descripcion:
        descripcion = categoria_actual[2]

    if activa == "":
        activa_booleano = categoria_actual[3]
    elif activa == "s":
        activa_booleano = True
    elif activa == "n":
        activa_booleano = False
    else:
        print("El estado debe ser 's' o 'n'.")
        return

    categoria_mismo_nombre = (
        categoria_dao.obtener_por_nombre(nombre)
    )

    if (
        categoria_mismo_nombre is not None
        and categoria_mismo_nombre[0] != categoria_id
    ):
        print("Ya existe otra categoría con ese nombre.")
        return

    categoria_actualizada = categoria_dao.actualizar(
        categoria_id=categoria_id,
        nombre=nombre,
        descripcion=descripcion,
        activa=activa_booleano
    )

    print("Categoría actualizada correctamente.")
    mostrar_categoria(categoria_actualizada)


def eliminar_categoria(categoria_dao):
    """
    Elimina una categoría por su ID.
    """

    print("\n=== ELIMINAR CATEGORÍA ===")

    try:
        categoria_id = int(
            input("ID de la categoría: ").strip()
        )
    except ValueError:
        print("El ID debe ser un número entero.")
        return

    categoria = categoria_dao.obtener_por_id(
        categoria_id
    )

    if categoria is None:
        print("Categoría no encontrada.")
        return

    mostrar_categoria(categoria)

    confirmacion = input(
        "¿Confirma la eliminación? (s/n): "
    ).strip().lower()

    if confirmacion != "s":
        print("Eliminación cancelada.")
        return

    eliminada = categoria_dao.eliminar(
        categoria_id
    )

    if eliminada:
        print("Categoría eliminada correctamente.")
    else:
        print("No fue posible eliminar la categoría.")


def ejecutar_menu_driver():
    """
    Ejecuta el menú del CRUD mediante driver.
    """

    categoria_dao = CategoriaDAODriver()

    while True:
        print("\n======================================")
        print(" POLIRESTAURANTE - CRUD CON DRIVER")
        print("======================================")
        print("1. Crear categoría")
        print("2. Listar categorías")
        print("3. Consultar categoría por ID")
        print("4. Actualizar categoría")
        print("5. Eliminar categoría")
        print("0. Regresar al menú principal")

        opcion = input("Seleccione una opción: ").strip()

        try:
            if opcion == "1":
                crear_categoria(categoria_dao)
            elif opcion == "2":
                listar_categorias(categoria_dao)
            elif opcion == "3":
                consultar_categoria(categoria_dao)
            elif opcion == "4":
                actualizar_categoria(categoria_dao)
            elif opcion == "5":
                eliminar_categoria(categoria_dao)
            elif opcion == "0":
                print("Regresando al menú principal.")
                break
            else:
                print("Opción inválida.")

        except Exception as error:
            print("No fue posible completar la operación.")
            print(f"Detalle: {error}")


if __name__ == "__main__":
    ejecutar_menu_driver()