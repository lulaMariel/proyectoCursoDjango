from django.shortcuts import render
from aServicios.models import Servicio

def servicio(request):

    servicios = Servicio.objects.all

    return render(request, "aServicios/servicios_view.html", {"servicios": servicios})