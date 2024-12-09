from django.shortcuts import render
from .models import Post, Categoria


def blog(request):

    posts = Post.objects.all

    return render(request, "ablog/blog_view.html", {'posts': posts})

def categoria(request, categoria_id):

    categoria = Categoria.objects.get(id = categoria_id)
    posts = Post.objects.filter(categorias = categoria)

    return render(request, "ablog/categorias_view.html", {'categorias': categoria, 'posts': posts})