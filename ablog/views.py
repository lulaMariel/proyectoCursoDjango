from django.shortcuts import render
from ablog.models import Post


def blog(request):

    posts = Post.objects.all

    return render(request, "ablog/blog_view.html", {'posts': posts})