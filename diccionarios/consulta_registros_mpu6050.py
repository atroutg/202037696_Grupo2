# Diccionario anidado corregido del MPU6050
# Autor: Armando Trout Garcia

registro_mpu = {
    "0x3B": {
        "register_name": "ACCEL_XOUT_H",
        "bit_mask": 0xFF,
        "sampling_rate": 1000
    },
    "0x3D": {
        "register_name": "ACCEL_YOUT_H",
        "bit_mask": 0xFF,
        "sampling_rate": 1000
    },
    "0x6B": {
        "register_name": "PWR_MGMT_1",
        "bit_mask": 0x40,
        "sampling_rate": 100
    }
}

max_intentos = 3
intento = 0
encontrado = False

print("Bienvenido al sistema de consulta de registros del MPU6050.")

# Se permite un máximo de 3 intentos para realizar la consulta.
while intento < max_intentos and not encontrado:

    consulta = input(
        "Ingrese una dirección hexadecimal o nombre de registro: "
    ).strip()

    # Consulta directa por dirección hexadecimal
    datos = registro_mpu.get(consulta)
    # Si se encuentra por dirección, se guarda la dirección encontrada
    direccion_encontrada = consulta if datos is not None else None

    # Si no se encuentra por dirección, se busca por nombre
    if datos is None:
        # Se recorre el diccionario para buscar por nombre de registro 
        for direccion, especificaciones in registro_mpu.items():

            nombre_registro = especificaciones.get("register_name")
            # Se compara el nombre de registro en mayúsculas con la consulta en mayúsculas
            if nombre_registro == consulta.upper():
                datos = especificaciones
                direccion_encontrada = direccion
                break

    if datos is not None:
        print("\nConsulta exitosa")
        print(f"Dirección: {direccion_encontrada}")
        print(f"Registro: {datos.get('register_name')}")
        print(f"Máscara de bits: {hex(datos.get('bit_mask'))}")
        print(f"Tasa de muestreo: {datos.get('sampling_rate')} Hz")
        encontrado = True
    else:
        intento += 1
        print(
            f"Registro no encontrado. "
            f"Intento {intento} de {max_intentos}."
        )

if not encontrado:
    print("Se alcanzó el número máximo de intentos.")