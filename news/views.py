from django.shortcuts import redirect, render, get_object_or_404
from .models import Article, Comment, Category
from .forms import ArticleForm, CommentForm, CategoryForm
from django.contrib.auth.models import User

def display_categories(request):
    categories = Category.objects.all() 
    context = {
        'categories': categories
    }
    return render(request, 'categories.html', context)

def add_category(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('display_categories')
    form = CategoryForm()
    context = {
        "form": CategoryForm()
    }
    return render(request, 'add_category.html', context)

def display_articles(request):
    articles = list(Article.objects.all().filter(approved=True))    
    def sort_article(article):
        return article.upvotes_count() - article.downvotes_count()
    articles.sort(key=sort_article, reverse=True)
    context = {
        'articles': articles
    }
    return render(request, 'index.html', context)

def add_article(request):
    if request.method == 'POST':
        article_form = ArticleForm(request.POST, request.FILES)
        if article_form.is_valid():
            article_form.instance.author = request.user
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

def edit_article(request, article_id, *args, **kwargs):
    article = get_object_or_404(Article, id=article_id)
    if request.method == 'POST':
        form = ArticleForm(request.POST, request.FILES, instance=article)
        if form.is_valid():
            form.save()
            return redirect('view_article', article_id=article_id)
    form = ArticleForm(instance=article)
    context = {
        'form': form
    }
    return render(request, 'edit_article.html', context)

def view_article(request, article_id, *args, **kwargs):
    article = get_object_or_404(Article, id=article_id)
    comments = article.post_comment.order_by('time_created_comment')
    if request.method == 'POST':
        form = CommentForm(request.POST, instance=article)
        if form.is_valid():
            obj = Comment()
            obj.body = form.cleaned_data['body']
            obj.users_name = request.user
            obj.post = article
            obj.save()
            return redirect('view_article', article_id=article_id)
    form = CommentForm()     
    upvoted = False
    if article.upvote.filter(id=request.user.id).exists():
        upvoted = True   
    downvoted = False
    if article.downvote.filter(id=request.user.id).exists():
        downvoted = True 

    vote_count = article.upvote.count() - article.downvote.count()

    context = {
        "article": article,
        "article_comment": form,
        "comments": comments,
        "upvoted": upvoted,
        "downvoted": downvoted,
        "vote_count": vote_count,
    }
    return render(request, 'article.html', context)

def upvote_article(request, article_id, *args, **kwargs):
    article = get_object_or_404(Article, id=article_id)
    if article.upvote.filter(id=request.user.id).exists():
        article.upvote.remove(request.user)
    else:
        article.upvote.add(request.user)
        article.downvote.remove(request.user)
    return redirect('view_article', article_id=article_id)

def downvote_article(request, article_id, *args, **kwargs):
    article = get_object_or_404(Article, id=article_id)
    if article.downvote.filter(id=request.user.id).exists():
        article.downvote.remove(request.user)
    else:
        article.downvote.add(request.user)
        article.upvote.remove(request.user)
    return redirect('view_article', article_id=article_id)

def delete_article(request, article_id):
    article = get_object_or_404(Article, id=article_id)
    article.delete()
    return redirect('display_articles')

def delete_comment(request, comment_id, *args, **kwargs):
    comment = get_object_or_404(Comment, id=comment_id)
    article_id = comment.post_id
    comment.delete()
    return redirect('view_article', article_id=article_id)

