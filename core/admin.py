from django.contrib import admin
from .models import Category, Tag, Usuario, Post, About, Link

# Register your models here.

#CATEGORIAS
class CategoryAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    list_display = ('name', 'active', 'created')
    search_fields = ('name',)

admin.site.register(Category, CategoryAdmin)


#ETIQUETAS
class TagAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    list_display = ('name', 'active', 'created')
    search_fields = ('name',)

admin.site.register(Tag, TagAdmin)


#USUARIOS
admin.site.register(Usuario)


#PUBLICACIONES
class PostAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    list_display = ('title', 'published', 'categoty', 'author', 'created')
    ordering = ('author','-created')
    search_fields = ('title', 'author__username',)
    list_filter = ('author', 'categoty', 'tags')

admin.site.register(Post, PostAdmin)


#ABOUT
class AboutAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    list_display = ('desciption', 'created')

admin.site.register(About, AboutAdmin)


#REDES SOCILAES
class LinkAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    list_display = ('name', 'key', 'url', 'created')

admin.site.register(Link, LinkAdmin)
