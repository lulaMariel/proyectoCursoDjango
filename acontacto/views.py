from django.shortcuts import redirect, render
from .forms import FormularioContacto

def contacto(request):
    formulario_contacto = FormularioContacto

    if request.method == "POST":
        formulario_contacto = FormularioContacto(data = request.POST)

        if formulario_contacto.is_valid():
            nombre = request.POST.get('nombre')
            email = request.POST.get('email')
            contenido = request.POST.get('contenido')

            return redirect('/contacto/?valido')

    return render(request, "aContacto/contacto_view.html", {'mi_formulario': formulario_contacto})