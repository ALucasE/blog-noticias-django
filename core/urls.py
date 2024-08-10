"""
URL configuration for blog_noticias_gaming project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path
from .views import home, get_post_author, get_post_category, get_post_dates, get_post, like_post


urlpatterns = [
    path('', home, name='inicio'),
    path('author/<int:author_id>', get_post_author, name='author'),
    path('category/<int:category_id>', get_post_category, name='category'),
    path('dates/<int:month_id>/<int:year_id>', get_post_dates, name='dates'),
    path('post/<int:post_id>', get_post, name='post'),
    path('like/<int:pk>', like_post, name='like_post'),

]
