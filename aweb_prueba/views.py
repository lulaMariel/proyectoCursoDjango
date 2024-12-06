from django.shortcuts import render

def inicio(request):
    return render(request, "aweb_prueba/inicio_view.html")

def tienda(request):
    return render(request, "aweb_prueba/tienda_view.html")

def blog(request):
    return render(request, "aweb_prueba/blog_view.html")

def contacto(request):
    return render(request, "aweb_prueba/contacto_view.html")
