from .models import About, Link, Category

# About
def ctx_dic_about(request):
    abouts = About.objects.latest('created')
    ctx_about={
        'ABOUT' : abouts
    }
    return ctx_about

# Categorias
def ctx_dic_category(request):
    categories = Category.objects.filter(active=True)
    ctx_category = {
        'categories':categories
    }
    return ctx_category

# Archivos


# Redes sociales
def ctx_dic_link(request):
    ctx_link = {}
    links = Link.objects.all()
    for link in links:
        ctx_link[link.key] = {'url': link.url, 'icon': link.icon, 'name': link.name}
    return {'ctx_link': ctx_link}

