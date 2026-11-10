"""Ejercicio 1: limpieza de sensores y resumen de temperaturas."""


def limpiar_registro_sensor(registro_raw):
    """Devuelve un nuevo diccionario con los datos del sensor normalizados."""
    sensor_id = str(registro_raw["sensor_id"]).strip()

    # Se eliminan espacios y unidades, y se convierte el texto a float.
    temperatura_texto = str(registro_raw["temperatura"]).strip()
    temperatura_texto = temperatura_texto.upper().replace("°C", "")
    temperatura_texto = temperatura_texto.replace("C", "").replace(",", ".")
    temperatura = float(temperatura_texto.strip())

    # .get() evita errores cuando no existe el dato de ubicación.
    ubicacion = str(registro_raw.get("ubicacion") or "Desconocida").strip()
    if not ubicacion:
        ubicacion = "Desconocida"

    return {
        "sensor_id": sensor_id,
        "temperatura": temperatura,
        "ubicacion": ubicacion,
    }


def generar_resumen_sensores(lista_sensores_limpios, umbral_temperatura):
    """Retorna (IDs con alerta, promedio térmico de todos los sensores)."""
    if not lista_sensores_limpios:
        return ([], 0.0)

    lista_sensores_alerta = []
    suma_temperaturas = 0.0

    for sensor in lista_sensores_limpios:
        temperatura = sensor["temperatura"]
        suma_temperaturas += temperatura
        if temperatura > umbral_temperatura:
            lista_sensores_alerta.append(sensor["sensor_id"])

    promedio_temperatura = suma_temperaturas / len(lista_sensores_limpios)
    return (lista_sensores_alerta, promedio_temperatura)


if __name__ == "__main__":
    # Paso 1: datos crudos recibidos desde los sensores.
    registros_crudos = [
        {"sensor_id": " SENSOR-001 ", "temperatura": "24.5C", "ubicacion": "Planta Norte"},
        {"sensor_id": " SENSOR-002 ", "temperatura": " 31.2 °C ", "ubicacion": "Planta Sur"},
        {"sensor_id": " SENSOR-003 ", "temperatura": "28.0C"},
    ]

    # Paso 2: limpieza individual con la función del Punto A.
    sensores_limpios = []
    for registro in registros_crudos:
        sensores_limpios.append(limpiar_registro_sensor(registro))

    # Paso 3: análisis de registros ya limpios con la función del Punto B.
    umbral = 25.0
    sensores_alerta, temperatura_promedio = generar_resumen_sensores(
        sensores_limpios, umbral
    )

    # Paso 4: reporte final.
    print("=" * 50)
    print("ECOTECH SOLUTIONS - REPORTE DE SENSORES")
    print("=" * 50)
    for sensor in sensores_limpios:
        print(
            f"{sensor['sensor_id']} | "
            f"{sensor['temperatura']:.1f} °C | "
            f"Ubicación: {sensor['ubicacion']}"
        )
    print("-" * 50)
    print(f"Umbral configurado: {umbral:.1f} °C")
    print(f"Sensores en alerta: {sensores_alerta}")
    print(f"Temperatura promedio global: {temperatura_promedio:.2f} °C")
