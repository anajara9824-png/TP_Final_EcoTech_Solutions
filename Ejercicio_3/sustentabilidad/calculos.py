"""Algoritmo que se audita en el Punto A del Ejercicio 3."""


def calcular_emisiones_carbono(consumo_kwh, factor_emision=0.4):
    """Calcula kg de CO2 y rechaza consumos negativos."""
    if consumo_kwh < 0:
        raise ValueError("El consumo energético no puede ser negativo.")
    return consumo_kwh * factor_emision
