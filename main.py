"""
Sistema de Automatización Industrial.
Lenguajes Interpretados - UNAD.
Grupo 202037696_2.
Autor: Armando Guillermo Trout Garcia.
"""

import runpy
from pathlib import Path


RUTA_BASE = Path(__file__).resolve().parent


def ejecutar_modulo(ruta):
    """Ejecuta el módulo seleccionado por el usuario."""
    archivo = RUTA_BASE / ruta

    if not archivo.is_file():
        print(f"\nNo se encontró el módulo: {ruta}")
        return

    runpy.run_path(str(archivo), run_name="__main__")


def mostrar_menu():
    """Muestra las opciones del sistema integrado."""
    print("\n" + "=" * 60)
    print("       SISTEMA DE AUTOMATIZACIÓN INDUSTRIAL")
    print("                 UNAD - GRUPO 2")
    print("=" * 60)
    print("1. Control de temperatura en autoclave - MAX31855")
    print("2. Consulta de registros de memoria - MPU6050")
    print("0. Salir del sistema")
    print("=" * 60)


def main():
    """Gestiona la ejecución del programa principal."""

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            ejecutar_modulo(
                "modulos_control/control_autoclave_max31855.py"
            )

        elif opcion == "2":
            ejecutar_modulo(
                "diccionarios/consulta_registros_mpu6050.py"
            )

        elif opcion == "0":
            print("\nSistema finalizado correctamente.")
            break

        else:
            print("\nOpción no válida. Intente nuevamente.")


if __name__ == "__main__":
    main()
