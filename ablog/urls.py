from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from ablog import views

urlpatterns = [
    path('', views.blog, name="blog"),
    path('categorias/<categoria_id>/', views.categoria, name="categorias"),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
