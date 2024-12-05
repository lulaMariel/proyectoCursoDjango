from django.shortcuts import render, HttpResponse

def inicio(request):
    return render(request, "web_prueba/inicio_view.html")

def servicio(request):
    return render(request, "web_prueba/servicios_view.html")

def tienda(request):
    return render(request, "web_prueba/tienda_view.html")

def blog(request):
    return render(request, "web_prueba/blog_view.html")

def contacto(request):
    return render(request, "web_prueba/contacto_view.html")
