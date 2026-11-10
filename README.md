# TP FINAL OBLIGATORIO — EcoTech Solutions

**Curso:** Programación con Python  
**Entrega:** repositorio público de GitHub con **tres carpetas**, una por ejercicio.

Este trabajo resuelve las consignas mediante código Python explicado con comentarios.
Se basa en la **Guía de repaso integradora de programación con Python** entregada en la cursada.

## Organización del proyecto

```text
TP_Final_EcoTech_Solutions/
├── Ejercicio_1/
│   ├── main.py                   # Limpieza, resumen y reporte
│   └── test_ejercicio_1.py       # Verificaciones extra
├── Ejercicio_2/
│   ├── main.py                   # Objetos, excepción y gestor JSON
│   ├── catalogo_ecotech.json     # Archivo exportado con productos válidos
│   └── test_ejercicio_2.py       # Verificaciones extra
├── Ejercicio_3/
│   ├── manage.py                 # Proyecto Django completo
│   ├── requirements.txt
│   ├── ecotech_project/          # Configuración de Django
│   └── sustentabilidad/          # Cálculo, métricas, vistas y plantilla
├── .gitignore
└── README.md
```

## Correspondencia con las consignas

| Apartado | Solución y ubicación |
| --- | --- |
| Ejercicio 1, A (20 puntos junto con B) | `Ejercicio_1/main.py` → `limpiar_registro_sensor` |
| Ejercicio 1, B | `Ejercicio_1/main.py` → `generar_resumen_sensores` + demostración |
| Ejercicio 2, A (40 puntos junto con B) | `Ejercicio_2/main.py` → `StockInvalidoError`, `DispositivoEcológico`, `PanelSolar` |
| Ejercicio 2, B | `Ejercicio_2/main.py` → `GestorInventario.guardar_catalogo_json` y `catalogo_ecotech.json` |
| Ejercicio 3, A (40 puntos junto con B) | `Ejercicio_3/sustentabilidad/calculos.py` + `tests.py` |
| Ejercicio 3, B | `Ejercicio_3/sustentabilidad/metricas.py`, `views.py` y `templates/sustentabilidad/panel.html` |

## 1. Ejecutar los ejercicios de Python

Con Python 3.10 o superior instalado, abrí una terminal en la carpeta principal:

```bash
python Ejercicio_1/main.py
python Ejercicio_2/main.py
```

**Resultado del ejercicio 1:** sensores en alerta `['SENSOR-002', 'SENSOR-003']`, promedio `27.90 °C` con umbral `25 °C`.

**Resultado del ejercicio 2:** se captura `StockInvalidoError` al intentar stock `-5`; el panel conserva `10` unidades; se genera `Ejercicio_2/catalogo_ecotech.json`.

Para ejecutar las comprobaciones extra (opcionales):

```bash
cd Ejercicio_1
python -m unittest -v test_ejercicio_1
cd ../Ejercicio_2
python -m unittest -v test_ejercicio_2
cd ..
```

## 2. Ejecutar el proyecto web Django (Ejercicio 3)

Se usa Django 5.2 LTS, compatible con Python 3.10 a 3.14.

**En Windows (PowerShell)**, desde la carpeta principal:

```powershell
cd Ejercicio_3
python -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe manage.py check
.\.venv\Scripts\python.exe manage.py test
.\.venv\Scripts\python.exe manage.py migrate
.\.venv\Scripts\python.exe manage.py runserver
```

**En Mac/Linux**, desde `Ejercicio_3`:

```bash
python3 -m venv .venv
.venv/bin/python -m pip install -r requirements.txt
.venv/bin/python manage.py check
.venv/bin/python manage.py test
.venv/bin/python manage.py migrate
.venv/bin/python manage.py runserver
```

Visitá **http://127.0.0.1:8000/**. Para detener el servidor, usá `Ctrl+C`.

**Resultado esperado del ejercicio 3:** `3450 kWh` de consumo total, `1380 kg de CO₂` estimados y `Planta Norte` como mayor consumidora (`2600 kWh`, sumando sus dos registros).

## 3. Subir a GitHub (repositorio PÚBLICO)

**Importante: no subas solo el ZIP.** GitHub debe mostrar **Ejercicio_1**, **Ejercicio_2** y **Ejercicio_3** como carpetas navegables, de manera que se puedan descargar y ejecutar los archivos.

### Opción A: desde la web (más fácil en una computadora)

1. Descargá el ZIP y **extraé su contenido**.
2. Iniciá sesión en [github.com](https://github.com/) y elegí **New repository**.
3. Escribí un nombre, por ejemplo `tp-final-python-ecotech`. Seleccioná **Public** y creá el repositorio.
4. En el repositorio, seleccioná **Add file → Upload files**.
5. Arrastrá el **contenido extraído** de `TP_Final_EcoTech_Solutions` (las tres carpetas y el archivo `README.md`); si tu navegador no admite arrastrar carpetas, usá la opción de terminal que aparece abajo.
6. Confirmá con **Commit changes** y revisá que aparezcan las tres carpetas y que dentro de `Ejercicio_3` esté `manage.py`.
7. Copiá la URL de tu repositorio público.

### Opción B: con Git desde la terminal

Abrí la terminal **dentro de** `TP_Final_EcoTech_Solutions` y ejecutá:

```bash
git init
git add .
git commit -m "Entrega del TP final Python - EcoTech Solutions"
git branch -M main
git remote add origin https://github.com/TU_USUARIO/tp-final-python-ecotech.git
git push -u origin main
```

Reemplazá `TU_USUARIO` por tu usuario de GitHub y verificá haber creado antes el repositorio público vacío.

## 4. Hacer la entrega en el aula

1. Abrí la actividad **TP FINAL OBLIGATORIO**.
2. Tocá **AGREGAR ENTREGA**.
3. Pegá la **URL del repositorio público de GitHub** (no el archivo ZIP, ni una ruta local).
4. Confirmá la entrega y verificá que el enlace se vea correctamente.

La actividad indica que la aprobación se obtiene con **60 %** y que el período de entrega va **del 29 de octubre al 9 de noviembre**.

## 5. Explicación breve para defender el trabajo

- **Ejercicio 1:** `strip()` y `replace()` limpian los textos; `float()` convierte la temperatura; `.get()` proporciona una ubicación segura. Un `for` calcula promedio e identifica alertas estrictamente superiores al umbral.
- **Ejercicio 2:** `__stock` protege el stock; `get_stock()` lo lee; `set_stock()` controla que no sea negativo y usa `StockInvalidoError`. `PanelSolar` hereda y sobrescribe la ficha técnica. `a_diccionario()` y `json.dump()` permiten persistir el catálogo.
- **Ejercicio 3:** `unittest` verifica el cálculo y el error ante consumo negativo. La función de métricas suma los consumos por planta y llama a la función auditada. La vista Django pasa el contexto a la plantilla `sustentabilidad/panel.html`.

**Alcance:** es una aplicación de demostración académica, con registros de ejemplo y configuración Django local; no utiliza datos industriales reales.
