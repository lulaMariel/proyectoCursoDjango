from django.urls import path
from .views import registroView, cerrar_sesion, loginView

urlpatterns = [
    path('', registroView.as_view(), name="registro"),
    path('iniciar_sesion', loginView, name="login"),
    path('cerrar_sesion', cerrar_sesion, name="cerrar_sesion"),
] 