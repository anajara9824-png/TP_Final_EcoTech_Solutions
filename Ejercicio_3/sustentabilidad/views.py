"""Vista Django del panel administrativo de sustentabilidad."""
from django.shortcuts import render

from .datos import REGISTROS_CONSUMO
from .metricas import obtener_metricas_consumo


def vista_panel_sustentabilidad(request):
    """Procesa el historial y envía el contexto a panel.html."""
    contexto = obtener_metricas_consumo(REGISTROS_CONSUMO)
    return render(request, "sustentabilidad/panel.html", contexto)
