from django.db import models
from django.contrib.auth.models import AbstractUser
from ckeditor.fields import RichTextField

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=150, unique=True, verbose_name='Nombre')
    active = models.BooleanField(default=True, verbose_name='Activo')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')
    updated = models.DateTimeField(auto_now=True, verbose_name='Fecha de modificación')

    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'
        ordering = ['name']

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=150, unique=True, verbose_name='Nombre')
    active = models.BooleanField(default=True, verbose_name='Activo')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')
    updated = models.DateTimeField(auto_now=True, verbose_name='Fecha de modificación')

    class Meta:
        verbose_name = 'Etiqueta'
        verbose_name_plural = 'Etiquetas'
        ordering = ['name']

    def __str__(self):
        return self.name


# AUTHOR = HEREDA DE USUARIOS DJANGO
# Recomendado apenas se empieza a usar auth
class Usuario(AbstractUser):
    pass


# POST = Publicacion Publicaciones
class Post(models.Model):
    title = models.CharField(max_length=200, verbose_name='Titulo')
    lead = models.TextField(verbose_name='Entrada')
    # content = models.TextField(verbose_name='Contenido')
    content = RichTextField(verbose_name='Contenido')
    image = models.ImageField(upload_to='post', null=True, blank=True, verbose_name='Imagen')
    published = models.BooleanField(default=False, verbose_name='Publicado')
    #Campos con relaciones
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='get_posts', verbose_name='Categoria')
    author = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='get_posts', verbose_name='Autor')
    tags = models.ManyToManyField(Tag, verbose_name='Etiqueta')
    likes = models.ManyToManyField(Usuario, related_name='blog_posts', verbose_name='Me gusta')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')
    updated = models.DateTimeField(auto_now=True, verbose_name='Fecha de modificación')

    def total_likes(self):
        return self.likes.count()

    class Meta:
        verbose_name = 'Publicacion'
        verbose_name_plural = 'Publicaciones'
        ordering = ['-created']

    def __str__(self):
        return self.title


################################################################################################

################################################################################################

#ABOUT
class About(models.Model):
    desciption = models.TextField(verbose_name='Descripcion')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')
    updated = models.DateTimeField(auto_now=True, verbose_name='Fecha de modificación')
    class Meta:
        verbose_name = 'Acerca de'
        verbose_name_plural = 'Acerca de nosotros'
        ordering = ['-created']

    def __str__(self):
        return self.desciption
    

#REDES SOCIALES
class Link(models.Model):
    key = models.CharField(max_length=100, verbose_name='Clave')
    name =models.CharField(max_length=100, verbose_name='Red social')
    url = models.URLField(max_length=250, blank=True, null=True, verbose_name='Enlace')
    icon = models.CharField(max_length=150, blank=True, null=True, verbose_name='Icono')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')
    updated = models.DateTimeField(auto_now=True, verbose_name='Fecha de modificación')
    class Meta:
        verbose_name = 'Red socila'
        verbose_name_plural = 'Redes sociales'
        ordering = ['name']

    def __str__(self):
        return self.name