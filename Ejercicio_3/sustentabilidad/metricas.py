"""Procesamiento de métricas por planta (Punto B)."""
from .calculos import calcular_emisiones_carbono


def obtener_metricas_consumo(registros):
    """Suma emisiones y determina la planta con mayor consumo acumulado.

    Si una misma planta aparece varias veces, sus consumos se acumulan.
    Un historial vacío produce 0 y la etiqueta 'Sin datos'.
    """
    total_emisiones = 0.0
    total_consumo_kwh = 0.0
    consumo_por_planta = {}

    for registro in registros:
        planta = registro["planta"]
        consumo_kwh = float(registro["consumo_kwh"])

        # Se reutiliza el algoritmo auditado; un negativo lanza ValueError.
        emisiones = calcular_emisiones_carbono(consumo_kwh)
        total_emisiones += emisiones
        total_consumo_kwh += consumo_kwh
        consumo_por_planta[planta] = (
            consumo_por_planta.get(planta, 0.0) + consumo_kwh
        )

    if consumo_por_planta:
        planta_top = max(consumo_por_planta, key=consumo_por_planta.get)
    else:
        planta_top = "Sin datos"

    desglose_plantas = [
        {
            "planta": planta,
            "consumo_kwh": consumo,
            "emisiones_kg": calcular_emisiones_carbono(consumo),
        }
        for planta, consumo in consumo_por_planta.items()
    ]

    return {
        "total_emisiones": total_emisiones,
        "planta_top": planta_top,
        "total_consumo_kwh": total_consumo_kwh,
        "consumo_por_planta": consumo_por_planta,
        "desglose_plantas": desglose_plantas,
    }
