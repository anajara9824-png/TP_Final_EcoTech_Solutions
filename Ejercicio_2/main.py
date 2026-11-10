"""Ejercicio 2: clases de productos, validaciones y persistencia JSON."""

import json
from pathlib import Path


class StockInvalidoError(Exception):
    """Error de negocio para un stock no válido."""
    pass


class DispositivoEcológico:
    """Clase base de productos ecológicos."""

    def __init__(self, modelo, precio, stock):
        self.modelo = modelo
        self.precio = float(precio)
        self.set_stock(stock)

    def get_stock(self):
        """Getter: permite leer el atributo encapsulado."""
        return self.__stock

    def set_stock(self, nuevo_stock):
        """Setter: evita stock negativo (y exige cantidades enteras)."""
        if (not isinstance(nuevo_stock, int)
                or isinstance(nuevo_stock, bool)
                or nuevo_stock < 0):
            raise StockInvalidoError(
                "El stock debe ser un número entero mayor o igual a cero."
            )
        self.__stock = nuevo_stock

    def obtener_ficha_tecnica(self):
        """Ficha comercial genérica de un dispositivo ecológico."""
        return (
            f"Modelo: {self.modelo} | Precio: ${self.precio:.2f} | "
            f"Stock: {self.get_stock()} unidades"
        )

    def a_diccionario(self):
        """Convierte la instancia a datos primitivos para guardarlos en JSON."""
        return {
            "tipo": "DispositivoEcológico",
            "modelo": self.modelo,
            "precio": self.precio,
            "stock": self.get_stock(),
        }


class PanelSolar(DispositivoEcológico):
    """Clase hija que añade la potencia específica del panel solar."""

    def __init__(self, modelo, precio, stock, eficiencia_watts):
        super().__init__(modelo, precio, stock)
        self.eficiencia_watts = int(eficiencia_watts)

    def obtener_ficha_tecnica(self):
        """Polimorfismo: personaliza la ficha del producto especializado."""
        ficha_base = super().obtener_ficha_tecnica()
        return f"{ficha_base} | Potencia: {self.eficiencia_watts} W"

    def a_diccionario(self):
        """Incluye también la información particular del panel solar."""
        datos = super().a_diccionario()
        datos["tipo"] = "PanelSolar"
        datos["eficiencia_watts"] = self.eficiencia_watts
        return datos


class GestorInventario:
    """Guarda el catálogo de instancias como archivo JSON."""

    def guardar_catalogo_json(self, lista_dispositivos, ruta_archivo):
        catalogo = [dispositivo.a_diccionario() for dispositivo in lista_dispositivos]
        ruta = Path(ruta_archivo)
        ruta.parent.mkdir(parents=True, exist_ok=True)
        with open(ruta, "w", encoding="utf-8") as archivo:
            json.dump(catalogo, archivo, indent=4, ensure_ascii=False)
        return ruta


if __name__ == "__main__":
    # Paso 1: crear un objeto de la clase base y otro de la clase hija.
    termostato = DispositivoEcológico("Termostato-Pro", 350.0, 8)
    panel = PanelSolar("SolarMax-500", 1200.0, 10, 500)
    dispositivos = [termostato, panel]

    # Paso 2: verificar que el setter impide modificar el stock a -5.
    print("ECOTECH SOLUTIONS - CONTROL DE INVENTARIO")
    try:
        panel.set_stock(-5)
    except StockInvalidoError as error:
        print(f"Excepción StockInvalidoError capturada: {error}")

    # Paso 3: comprobar que el stock válido quedó intacto.
    print(f"Stock del panel luego del intento: {panel.get_stock()} unidades")
    print("\nFICHAS TÉCNICAS")
    for dispositivo in dispositivos:
        print(dispositivo.obtener_ficha_tecnica())

    # Paso 4: exportar únicamente productos válidos a catalogo_ecotech.json.
    ruta_json = Path(__file__).with_name("catalogo_ecotech.json")
    gestor = GestorInventario()
    gestor.guardar_catalogo_json(dispositivos, ruta_json)
    print(f"\nCatálogo JSON guardado correctamente en: {ruta_json.name}")
