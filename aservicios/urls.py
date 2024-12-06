from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from aservicios import views


urlpatterns = [
    path('servicios/', views.servicio, name="servicios"),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)