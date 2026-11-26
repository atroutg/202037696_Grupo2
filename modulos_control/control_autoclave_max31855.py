import time
# Armando Trout Garcia
# Variables iniciales de simulación
temperatura = 110 # Temperatura inicial del autoclave en grados Celsius
sistema_activo = True

# Variables de control del muestreo
muestra = 0
max_muestras = 12 # Número máximo de muestras a tomar
periodo_muestreo = 0.1 # Tiempo en segundos entre cada muestra

while sistema_activo==True and muestra < max_muestras:

    muestra += 1

    print(
        f"Muestra {muestra:02d} | "
        f"Temperatura: {temperatura:.2f} °C"
    )

    if temperatura > 130:
        print("ALERTA CRÍTICA: Parada de emergencia")
        sistema_activo = False # se detiene el sistema por seguridad

    elif temperatura < 115:
        print("Estado: Calentando autoclave")
        temperatura += 2

    elif temperatura >= 115 and temperatura <= 121:
        print("Estado: Fase estable de esterilización")
        temperatura += 1

    else:
        print("Estado: Enfriamiento activo")
        temperatura -= 3

    if sistema_activo==True:
        time.sleep(periodo_muestreo)

if sistema_activo==True:
    print(
        "Fin de simulación: "
        "se alcanzó el límite de muestras."
    )