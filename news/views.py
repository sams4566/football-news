from django.shortcuts import redirect, render, get_object_or_404
from .models import Article, Comment
from .forms import ArticleForm, CommentForm

def display_articles(request):
    articles = Article.objects.all().filter(approved=True)
    context = {
        'articles': articles
    }
    return render(request, 'index.html', context)

def add_article(request):
    if request.method == 'POST':
        article_form = ArticleForm(request.POST, request.FILES)
        if article_form.is_valid():
            article_form.save()
            return redirect('display_articles')
    article_form = ArticleForm()
    context = {
        "article_form": ArticleForm()
    }
    return render(request, 'add_article.html', context)

    # if request.method == 'POST':
    #     name = request.POST.get('article_name')
    #     Article.objects.create(name=name)
    #     return redirect('display_articles')
    # return render(request, 'add_article.html')

def view_article(request, article_id, *args, **kwargs):

    article = get_object_or_404(Article, id=article_id)
    comments = article.post_comment.order_by('time_created_comment')
    if request.method == 'POST':
        form = CommentForm(request.POST, instance=article)
        if form.is_valid():
            obj = Comment()
            obj.body = form.cleaned_data['body']
            obj.users_name = form.cleaned_data['users_name']
            obj.email = form.cleaned_data['email']
            obj.post = article
            obj.save()
            return redirect('view_article', article_id=article_id)
    form = CommentForm()        
    context = {
        "article": article,
        "article_comment": form,
        "comments": comments,
    }
    return render(request, 'article.html', context)


def delete_article(request, article_id):
    article = get_object_or_404(Article, id=article_id)
    article.delete()
    return redirect('display_articles')

