from django.shortcuts import redirect, render, get_object_or_404
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


def view_article(request, article_id):
    return render(request, 'article.html')


def delete_article(request, article_id):
    article = get_object_or_404(Article, id=article_id)
    article.delete()
    return redirect('display_articles')
