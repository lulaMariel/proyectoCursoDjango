from django.urls import path
# from .views import inicio, servicio, tienda, blog, contacto
from web_prueba import views

urlpatterns = [
    path('', views.inicio, name="inicio"),
    path('inicio/', views.inicio, name="inicio"),
    path('servicios/', views.servicio, name="servicios"),
    path('tienda/', views.tienda, name="tienda"),
    path('blog/', views.blog, name="blog"),
    path('contacto/', views.contacto, name="contacto"),
]
