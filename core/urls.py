from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('aWeb_prueba.urls')),
    path('servicios/', include('aServicios.urls')),
    path('blog/', include('aBlog.urls')),
    path('contacto/', include('aContacto.urls')),
    path('tienda/', include('aTienda.urls')),
    path('carrito/', include('aCarrito.urls')),
    path('autenticacion/', include('aLogin.urls')),
]
