from django.urls import path
from aServicios import views


urlpatterns = [
    path('', views.servicio, name="servicios"),
]