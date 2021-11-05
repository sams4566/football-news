from django.shortcuts import render, get_object_or_404
from .models import Article

def display_posts(request):
    articles = Article.objects.all()
    context = {
        'articles': articles
    }
    return render(request, 'index.html', context)
