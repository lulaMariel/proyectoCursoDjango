from django.urls import path
# from .views import inicio, servicio, tienda, blog, contacto
from aWeb_prueba import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.inicio, name="inicio"),
    path('inicio/', views.inicio, name="inicio"),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
