from django.urls import path
from acarrito import views

app_name = 'carrito'

urlpatterns = [
    path('agregar/<int:producto_id>/', views.agregar_producto_view, name="agregar"),
    path('eliminar/<int:producto_id>/', views.eliminar_producto_view, name="eliminar"),
    path('restar/<int:producto_id>/', views.restar_producto_view, name="restar"),
    path('limpiar/', views.limpiar_carrito_view, name="limpiar"),
]