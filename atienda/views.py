from django.shortcuts import render

def tienda(request):
    return render(request, "atienda/tienda_view.html")