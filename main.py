# ============================================================
# main.py
# Punto de entrada principal de la actividad.
# Permite elegir entre CRUD con driver y CRUD con ORM.
# ============================================================

from driver.menu_driver import ejecutar_menu_driver
from orm.menu_orm import ejecutar_menu_orm


def ejecutar_aplicacion():
    while True:
        print("\n==========================================")
        print(" POLIRESTAURANTE - ACCESO A DATOS")
        print("==========================================")
        print("1. CRUD con driver y SQL manual")
        print("2. CRUD con SQLAlchemy ORM")
        print("0. Salir")

        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            ejecutar_menu_driver()
        elif opcion == "2":
            ejecutar_menu_orm()
        elif opcion == "0":
            print("Aplicación finalizada.")
            break
        else:
            print("Opción inválida.")


if __name__ == "__main__":
    ejecutar_aplicacion()