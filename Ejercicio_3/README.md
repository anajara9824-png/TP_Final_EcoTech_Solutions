# Ejercicio 3 — Django, métricas y pruebas

Esta carpeta contiene **el proyecto completo de Django** necesario para ejecutarlo de forma local.

- `sustentabilidad/calculos.py`: `calcular_emisiones_carbono` (rechaza consumos negativos).
- `sustentabilidad/tests.py`: `TestCalculoEmisiones(unittest.TestCase)` y pruebas adicionales.
- `sustentabilidad/metricas.py`: `obtener_metricas_consumo(registros)`.
- `sustentabilidad/views.py`: `vista_panel_sustentabilidad(request)`.
- `sustentabilidad/templates/sustentabilidad/panel.html`: plantilla HTML.
- `ecotech_project/`: configuración, rutas y archivos de entrada del proyecto.
- `requirements.txt`: dependencia necesaria.

## Cómo probarlo

Abrí una terminal **dentro de `Ejercicio_3`** y ejecutá:

```bash
python -m pip install -r requirements.txt
python manage.py check
python manage.py test
python manage.py migrate
python manage.py runserver
```

Abrí `http://127.0.0.1:8000/` en el navegador.

Para salir del servidor, presioná `Ctrl+C` en la terminal.

**Datos esperados:** consumo global de 3450 kWh; emisiones de 1380 kg CO₂; planta de mayor consumo: Planta Norte (2600 kWh).
Las cifras son de ejemplo, no corresponden a mediciones reales.

**Nota:** la configuración `DEBUG=True` es exclusivamente para uso académico local y no está preparada para producción.
