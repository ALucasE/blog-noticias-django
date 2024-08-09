from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from .models import Post, Category

# Create your views here.

def home(request):
    posts_page = Paginator(Post.objects.filter(published=True), 2)
    page = request.GET.get('page')
    posts = posts_page.get_page(page)
    numbers_page = 'p' * posts.paginator.num_pages
    contexto = {
        'posts': posts,
        'pages': numbers_page
    }

    return render(request, 'core/index.html', contexto)

def get_post(request, post_id):
    try:
        post = get_object_or_404(Post, id=post_id)
        contexto = {
            'post' : post
        }
        return render(request, 'core/post.html', contexto)
    except Exception:
        return render(request, 'core/404.html')


def author(request):
    contexto = {}
    
    return render(request, 'core/index.html', contexto)

def get_category(request, category_id):
    try:
        category = get_object_or_404(Category, id=category_id)
        contexto = {
            'category':category,
        }
        return render(request, 'core/category.html', contexto)
    except Exception:
        return render(request, 'core/404.html')
    

def dates(request):
    contexto = {}
    
    return render(request, 'core/index.html', contexto)