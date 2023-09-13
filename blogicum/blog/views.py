from django.shortcuts import render
from django.http import HttpResponseNotFound


def index(request):
    template_name = 'blog/index.html'
    context = {'posts': posts}
    return render(request, template_name, context)


def post_detail(request, pk):
    template_name = 'blog/detail.html'
    for post in posts:
        if post['id'] == pk:
            return render(request, template_name, {'post': post})
    return HttpResponseNotFound("<h1>Page not found</h1>")


def category_posts(request, category_slug):
    template_name = 'blog/category.html'
    context = {'slug': category_slug}
    return render(request, template_name, context)
