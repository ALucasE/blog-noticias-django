from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from .models import Post, Category, Usuario
from django.http import HttpResponseRedirect
from django.urls import reverse

# Create your views here.

def home(request):

    if not request.session.get('items_per_page'):
        request.session['items_per_page'] = 2
    
    if request.method == 'GET' and 'items_per_page' in request.GET:
        request.session['items_per_page'] = int(request.GET['items_per_page'])
    
    items_per_page = request.session['items_per_page']

    posts_page = Paginator(Post.objects.filter(published=True), items_per_page)
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
        total_likes = post.total_likes()
        contexto = {
            'post' : post,
            'total_likes' : total_likes
        }
        return render(request, 'core/post.html', contexto)
    except Exception:
        return render(request, 'core/404.html')


def get_post_author(request, author_id):
    try:
        author = get_object_or_404(Usuario, id=author_id)
        contexto = {
            'author':author,
        }
        return render(request, 'core/author.html', contexto)
    except Exception:
        return render(request, 'core/404.html')

def get_post_category(request, category_id):
    try:
        category = get_object_or_404(Category, id=category_id)
        contexto = {
            'category':category,
        }
        return render(request, 'core/category.html', contexto)
    except Exception:
        return render(request, 'core/404.html')
    

def get_post_dates(request, month_id, year_id):
    posts = Post.objects.filter(published=True, created__month=month_id, created__year=year_id)
    contexto = {
        'posts' : posts
    }
    return render(request, 'core/date.html', contexto)

def like_post(request, pk):
    post = get_object_or_404(Post, id=request.POST.get('post_id'))
    post.likes.add(request.user)
    
    return HttpResponseRedirect(reverse('post', args=[str(pk)]))