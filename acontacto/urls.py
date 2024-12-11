from django.urls import path
# from .views import inicio, servicio, tienda, blog, contacto
from acontacto import views

urlpatterns = [
    path('', views.contacto, name="contacto"),
] 