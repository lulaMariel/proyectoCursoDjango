from django.shortcuts import render
from aservicios.models import Servicio

def servicio(request):

    servicios = Servicio.objects.all

    return render(request, "aservicios/servicios_view.html", {"servicios": servicios})