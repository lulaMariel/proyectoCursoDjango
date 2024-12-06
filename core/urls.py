from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('servicios/', include('aservicios.urls')),
    path('', include('aweb_prueba.urls')),
]
