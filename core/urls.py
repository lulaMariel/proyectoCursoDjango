from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('aweb_prueba.urls')),
    path('servicios/', include('aservicios.urls')),
    path('blog/', include('ablog.urls')),
    path('contacto/', include('acontacto.urls')),
]
