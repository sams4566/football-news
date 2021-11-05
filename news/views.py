from django.shortcuts import redirect, render
from .models import Article

def display_articles(request):
    articles = Article.objects.all()
    context = {
        'articles': articles
    }
    return render(request, 'index.html', context)

def add_article(request):
    if request.method == 'POST':
        name = request.POST.get('article_name')
        Article.objects.create(name=name)
        return redirect('display_articles')
    return render(request, 'add_article.html')