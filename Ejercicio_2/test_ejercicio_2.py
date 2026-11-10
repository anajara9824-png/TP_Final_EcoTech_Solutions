"""Comprobaciones automáticas adicionales del Ejercicio 2."""
import json
import tempfile
import unittest
from pathlib import Path
from main import (
    DispositivoEcológico, PanelSolar, StockInvalidoError, GestorInventario
)


class TestInventario(unittest.TestCase):
    def test_stock_invalido_no_modifica_valor_anterior(self):
        panel = PanelSolar("Panel", 1000.0, 4, 300)
        with self.assertRaises(StockInvalidoError):
            panel.set_stock(-2)
        self.assertEqual(panel.get_stock(), 4)

    def test_stock_invalido_en_constructor(self):
        with self.assertRaises(StockInvalidoError):
            DispositivoEcológico("Sensor", 100, -1)

    def test_ficha_polimorfica_y_json(self):
        panel = PanelSolar("Panel", 1500, 3, 450)
        self.assertIn("450 W", panel.obtener_ficha_tecnica())
        with tempfile.TemporaryDirectory() as carpeta:
            ruta = Path(carpeta) / "catalogo_ecotech.json"
            GestorInventario().guardar_catalogo_json([panel], ruta)
            with open(ruta, encoding="utf-8") as archivo:
                datos = json.load(archivo)
            self.assertEqual(datos[0]["stock"], 3)
            self.assertEqual(datos[0]["eficiencia_watts"], 450)


if __name__ == "__main__":
    unittest.main()
