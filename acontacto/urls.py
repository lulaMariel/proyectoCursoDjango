from django.urls import path
from aContacto import views

urlpatterns = [
    path('', views.contacto, name="contacto"),
] 