from django.urls import path
from aTienda import views

urlpatterns = [
    path('', views.tienda, name="tienda"),
]