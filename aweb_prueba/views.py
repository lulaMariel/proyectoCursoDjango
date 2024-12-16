from django.shortcuts import render
from acarrito.carrito import Carrito

def inicio(request):
    carrito = Carrito(request)

    return render(request, "aweb_prueba/inicio_view.html")