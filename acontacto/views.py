from django.shortcuts import render
from .forms import FormularioContacto

def contacto(request):
    formulario_contacto = FormularioContacto

    return render(request, "acontacto/contacto_view.html", {'mi_formulario': formulario_contacto})