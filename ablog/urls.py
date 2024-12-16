from django.urls import path
from aBlog import views

urlpatterns = [
    path('', views.blog, name="blog"),
    path('categorias/<categoria_id>/', views.categoria, name="categorias"),
]