"""Auditoría del algoritmo (unittest) y comprobación de la integración web."""
import unittest

from django.test import SimpleTestCase
from django.urls import reverse

from .calculos import calcular_emisiones_carbono
from .metricas import obtener_metricas_consumo


# Punto A: la clase hereda exactamente de unittest.TestCase.
class TestCalculoEmisiones(unittest.TestCase):
    def test_calculo_nominal_factor_por_defecto(self):
        self.assertAlmostEqual(calcular_emisiones_carbono(100.0), 40.0)

    def test_calculo_nominal_factor_personalizado(self):
        self.assertAlmostEqual(calcular_emisiones_carbono(250.0, 0.5), 125.0)

    def test_consumo_cero(self):
        self.assertEqual(calcular_emisiones_carbono(0), 0.0)

    def test_consumo_negativo_lanza_value_error(self):
        with self.assertRaises(ValueError):
            calcular_emisiones_carbono(-50.0)


# Punto B: se verifican agregación de datos y renderizado de la vista.
class TestMetricasConsumo(unittest.TestCase):
    def test_emisiones_y_planta_de_mayor_consumo_acumulado(self):
        registros = [
            {"planta": "Norte", "consumo_kwh": 1200},
            {"planta": "Sur", "consumo_kwh": 850},
            {"planta": "Norte", "consumo_kwh": 1400},
        ]
        resultado = obtener_metricas_consumo(registros)
        self.assertAlmostEqual(resultado["total_emisiones"], 1380.0)
        self.assertEqual(resultado["planta_top"], "Norte")
        self.assertEqual(resultado["consumo_por_planta"]["Norte"], 2600.0)

    def test_historial_vacio(self):
        resultado = obtener_metricas_consumo([])
        self.assertEqual(resultado["total_emisiones"], 0.0)
        self.assertEqual(resultado["planta_top"], "Sin datos")

    def test_consumo_negativo_en_historial(self):
        with self.assertRaises(ValueError):
            obtener_metricas_consumo([{"planta": "Norte", "consumo_kwh": -3}])


class TestVistaPanel(SimpleTestCase):
    def test_vista_renderiza_plantilla_y_contexto(self):
        respuesta = self.client.get(reverse("panel_sustentabilidad"))
        self.assertEqual(respuesta.status_code, 200)
        self.assertTemplateUsed(respuesta, "sustentabilidad/panel.html")
        self.assertEqual(respuesta.context["total_emisiones"], 1380.0)
        self.assertEqual(respuesta.context["planta_top"], "Planta Norte")
        self.assertContains(respuesta, "ECOTECH SOLUTIONS")
