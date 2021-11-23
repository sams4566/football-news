"""premier_league_news URL Configuration

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
    path('summernote/', include('django_summernote.urls')),
    path('', views.display_top_articles, name='display_top_articles'),
    path('categories', views.display_categories, name='display_categories'),
    path('category/add', views.add_category, name='category'),
    path('category/edit/<category_id>', views.edit_category, name='edit_category'),
    path('category/delete/<category_id>', views.delete_category, name='delete_category'),
    path('category/articles/<category_id>', views.display_articles, name='display_articles'),
    path('article/add/<category_id>', views.add_article, name='add_article'),
    path('article/edit/<article_id>', views.edit_article, name='edit_article'),
    path('article/view/<article_id>', views.view_article, name='view_article'),
    path('article/upvote/<article_id>', views.upvote_article, name='upvote_article'),
    path('article/upvote2/<article_id>', views.upvote_article2, name='upvote_article2'),
    path('article/upvote3/<article_id>', views.upvote_article3, name='upvote_article3'),
    path('article/downvote/<article_id>', views.downvote_article, name='downvote_article'),
    path('article/downvote2/<article_id>', views.downvote_article2, name='downvote_article2'),
    path('article/downvote3/<article_id>', views.downvote_article3, name='downvote_article3'),
    path('article/delete/<article_id>', views.delete_article, name='delete_article'),
    path('comment/delete/<comment_id>', views.delete_comment, name='delete_comment'),
]
