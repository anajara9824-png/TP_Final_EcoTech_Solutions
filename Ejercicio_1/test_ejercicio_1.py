"""Comprobaciones automáticas adicionales del Ejercicio 1."""
import unittest
from main import limpiar_registro_sensor, generar_resumen_sensores


class TestSensores(unittest.TestCase):
    def test_limpieza_y_ubicacion_faltante(self):
        registro = {"sensor_id": " SENSOR-3 ", "temperatura": " 24.5 °C "}
        limpio = limpiar_registro_sensor(registro)
        self.assertEqual(limpio["sensor_id"], "SENSOR-3")
        self.assertEqual(limpio["temperatura"], 24.5)
        self.assertIsInstance(limpio["temperatura"], float)
        self.assertEqual(limpio["ubicacion"], "Desconocida")
        self.assertEqual(registro["sensor_id"], " SENSOR-3 ")

    def test_resumen_y_umbral_estricto(self):
        sensores = [
            {"sensor_id": "A", "temperatura": 25.0},
            {"sensor_id": "B", "temperatura": 35.0},
        ]
        self.assertEqual(generar_resumen_sensores(sensores, 25.0), (["B"], 30.0))

    def test_sin_sensores(self):
        self.assertEqual(generar_resumen_sensores([], 25.0), ([], 0.0))


if __name__ == "__main__":
    unittest.main()
