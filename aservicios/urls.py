from django.urls import path
from aservicios import views


urlpatterns = [
    path('', views.servicio, name="servicios"),
]