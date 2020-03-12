from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator

from .models import Post, Category


def index(request):
    posts_data = Post.objects.filter(is_draft=False).order_by('-created_at')
    paginator = Paginator(posts_data, 5)

    page = request.GET.get('page')
    posts = paginator.get_page(page)

    data = {'posts': posts}
    return render(request, 'index.html', data)


def show_category(request, slug):
    category = get_object_or_404(Category, slug=slug)
    posts_data = Post.objects.filter(category_id=category.id, is_draft=False).order_by('-created_at')
    paginator = Paginator(posts_data, 5)

    page = request.GET.get('page')
    posts = paginator.get_page(page)

    data = {'category': category, 'posts': posts}
    return render(request, 'show_category.html', data)


def show_post(request, slug):
    post = get_object_or_404(Post, slug=slug, is_draft=False)
    data = {'post': post}
    return render(request, 'show_post.html', data)
