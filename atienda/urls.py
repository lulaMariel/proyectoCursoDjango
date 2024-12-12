from django.urls import path
from atienda import views

urlpatterns = [
    path('', views.tienda, name="tienda"),
]