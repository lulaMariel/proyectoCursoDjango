from django.shortcuts import render

def inicio(request):
    return render(request, "aweb_prueba/inicio_view.html")