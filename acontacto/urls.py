from django.urls import path
from acontacto import views

urlpatterns = [
    path('', views.contacto, name="contacto"),
] 