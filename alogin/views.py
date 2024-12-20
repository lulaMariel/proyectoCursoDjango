from django.shortcuts import render, redirect
from django.views.generic import View
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages

class registroView(View):
    def get(self, request):
        form = UserCreationForm()

        return render(request, 'aLogin/registro.html', {'form': form})

    def post(self, request):
        form = UserCreationForm(request.POST)

        if form.is_valid():
            usuario = form.save()
            login(request, usuario)

            return redirect('inicio')
        else:
            for mensaje in form.error_messages:
                messages.error(request, form.error_messages[mensaje])
            return render(request, 'aLogin/registro.html', {'form': form})

def cerrar_sesion(request):
    logout(request)

    return redirect('inicio')

def loginView(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data = request.POST)
        if form.is_valid():
            nombre_usuario = form.cleaned_data.get('username')
            contraseña_usuario = form.cleaned_data.get('password')
            usuario = authenticate(username = nombre_usuario, password = contraseña_usuario)
            if usuario is not None:
                login(request, usuario)
                return redirect('inicio')
            else:
                messages.error(request, 'Usuario no encontrado')
        else:
            messages.error(request, 'Nombre de usuario o contraseña incorrecta')

    form = AuthenticationForm()
    return render(request, 'aLogin/login.html', {'form': form})