from django.shortcuts import render, redirect
from .carrito import Carrito
from atienda.models import Producto

def agregar_producto_view(request, producto_id):
    carrito = Carrito(request)
    producto = Producto.objects.get(id = producto_id)
    carrito.agregar_producto(producto = producto)

    return redirect('tienda')

def restar_producto_view(request, producto_id):
    carrito = Carrito(request)
    producto = Producto.objects.get(id = producto_id)
    carrito.restar_producto(producto = producto)

    return redirect('tienda')

def eliminar_producto_view(request, producto_id):
    carrito = Carrito(request)
    producto = Producto.objects.get(id = producto_id)
    carrito.eliminar_producto(producto = producto)

    return redirect('tienda')

def limpiar_carrito_view(request, producto_id):
    carrito = Carrito(request)
    carrito.limpar_carrito()

    return redirect('tienda')