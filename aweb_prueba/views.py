from django.shortcuts import render
from aCarrito.carrito import Carrito

def inicio(request):
    carrito = Carrito(request)

    return render(request, "aWeb_prueba/inicio_view.html")