from django.shortcuts import render, get_object_or_404
from datetime import datetime as dt
from django.db.models import Q

from blog.models import Post, Category


def index(request):
    template_name = 'blog/index.html'
    post_list = Post.objects.select_related(
        'author', 'location', 'category'
    ).filter(
        pub_date__lte=dt.now(),
        is_published=True,
        category__is_published=True
    ).order_by(
        '-pub_date'
    )[:5]
    context = {'post_list': post_list}
    return render(request, template_name, context)


def post_detail(request, pk):
    template_name = 'blog/detail.html'
    post = get_object_or_404(
        Post.objects.select_related(
            'author', 'location', 'category'
        ).filter(
            Q(pub_date__lte=dt.now())
            & Q(is_published=True)
            & Q(category__is_published=True)
        ),
        pk=pk
    )
    context = {'post': post}
    return render(request, template_name, context)


def category_posts(request, category_slug):
    template_name = 'blog/category.html'
    category = get_object_or_404(
        Category,
        slug=category_slug,
        is_published=True
    )
    post_list = Post.objects.select_related(
        'location',
        'author',
        'category'
    ).filter(
        is_published=True,
        category__is_published=True,
        pub_date__date__lt=dt.now(),
    ).filter(category=category,)
    context = {'category': category,
               'post_list': post_list}
    return render(request, template_name, context)
