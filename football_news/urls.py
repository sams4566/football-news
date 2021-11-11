"""football_news URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import include, path
from news import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('', views.display_articles, name='display_articles'),
    path('add', views.add_article, name='add_article'),
    path('article/<article_id>', views.view_article, name='view_article'),
    path('upvote/<article_id>', views.upvote_article, name='upvote_article'),
    path('downvote/<article_id>', views.downvote_article, name='downvote_article'),
    path('delete/<article_id>', views.delete_article, name='delete_article'),
    path('delete1/<comment_id>', views.delete_comment, name='delete_comment'),
]
