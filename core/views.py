from django.shortcuts import render
from django.core.paginator import Paginator
from .models import Post

# Create your views here.

def home(request):
    posts_page = Paginator(Post.objects.filter(published=True), 2)
    page = request.GET.get('page')
    posts = posts_page.get_page(page)
    numbers_page = 'p' * posts.paginator.num_pages
    print(posts)
    contexto = {
        'posts': posts,
        'pages': numbers_page
    }

    return render(request, 'core/index.html', contexto)

def post(request, post_id):
    post = Post.objects.get(id=post_id)
    contexto = {
        'post' : post,
    }
    return render(request, 'core/post.html', contexto)

def author(request):
    contexto = {}
    
    return render(request, 'core/index.html', contexto)

def category(request):
    contexto = {}
    
    return render(request, 'core/index.html', contexto)

def dates(request):
    contexto = {}
    
    return render(request, 'core/index.html', contexto)