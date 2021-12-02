from django.shortcuts import redirect, render, get_object_or_404
from .models import Article, Comment, Category
from .forms import ArticleForm, CommentForm, CategoryForm
from django.contrib.auth.models import User
from django.core.paginator import Paginator
from django.contrib import messages


def display_categories(request):
    """
    Displays the list of categories stored in the Category data
    model when the 'Categories' option is selected from the navbar.
    """
    categories = Category.objects.all().filter(approve_category=True)
    context = {"categories": categories}
    return render(request, "categories.html", context)


def add_category(request):
    """
    When the 'Add Category' button from the categories.html page
    is selected the add_category.html page is displayed. The user
    can add a new category and will be returned to the categories.html
    page once submitted.
    """
    categories = list(Category.objects.all())
    form = CategoryForm()
    if request.method == "POST":
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.instance.category_author = request.user
            for category in categories:
                name = form.instance.category_name
                if category.category_name == name:
                    messages.add_message(
                        request,
                        messages.INFO,
                        "A category with the same name already exists.",
                    )
                    context = {"form": form}
                    return render(request, "add_category.html", context)
            form.save()
            messages.add_message(
                request, messages.INFO, "Your category is awaiting approval"
            )
            return redirect("display_categories")
    context = {"form": form}
    return render(request, "add_category.html", context)


def edit_category(request, category_id):
    """
    If the user has created a category, they have the option to edit
    its name. On the categories.html page, the user can click the
    'Edit Category' button which will bring them to the
    edit_category.html page with the prepopulated category name
    already entered. The user can then click the 'Update Category'
    button which will take them back to the categories.html page.
    """
    category = get_object_or_404(Category, id=category_id)
    print(category.category_author)
    categories = list(Category.objects.all())
    form = CategoryForm(instance=category)
    if request.method == "POST":
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            for category in categories:
                name = form.instance.category_name
                if category.category_name == name:
                    messages.add_message(
                        request,
                        messages.INFO,
                        "A category with the same name already exists.",
                    )
                    context = {"form": form}
                    return render(request, "edit_category.html", context)
            form.save()
            return redirect("display_categories")
    context = {"form": form}
    return render(request, "edit_category.html", context)


def delete_category(request, category_id):
    """
    If the user has created a category, they have the option to delete
    it. On the categories.html page, the user can click the
    'Delete Category' button which will remove the category from the
    Category data model and return the user to the categories.html
    page
    """
    category = get_object_or_404(Category, id=category_id)
    category.delete()
    return redirect("display_categories")


def display_top_articles(request):
    """
    Displays the list of articles stored in the Article data model
    when the user first enters the site and when the 'Home'
    option in the navbar is selected. The articles are displayed
    with the most popular at the top.
    """
    articles = list(Article.objects.all().filter(approved=True))

    def sort_article(article):
        return article.upvotes_count() - article.downvotes_count()
    articles.sort(key=sort_article, reverse=True)
    paginator = Paginator(articles, 6)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    context = {"articles": articles, "page_obj": page_obj}
    return render(request, "index.html", context)


def display_articles(request, category_id):
    """
    Displays the list of articles stored in the Article data
    model for a specific category when the user clicks 'View
    articles' on a specific category on the categories.html
    page. The articles are displayed with the most recently
    published articles at the top.
    """
    category = get_object_or_404(Category, id=category_id)
    articles = Article.objects.filter(
        approved=True, category_id=category_id
        ).order_by("-time_created")
    paginator = Paginator(articles, 6)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    context = {
        "articles": articles,
        "page_obj": page_obj,
        "category": category
        }
    return render(request, "category_articles.html", context)


def add_article(request, category_id):
    """
    When the 'Add Article' button from the category_articles.html page
    is selected the add_article.html page is displayed. The user
    can add the new articles details and will be returned to the
    categories_articles.html page once submitted.
    """
    category = get_object_or_404(Category, id=category_id)
    articles = list(Article.objects.all())
    form = ArticleForm()
    if request.method == "POST":
        form = ArticleForm(request.POST, request.FILES)
        if form.is_valid():
            form.instance.author = request.user
            form.instance.category = category
            summernote = request.POST.get("editordata")
            form.instance.content = summernote
            for article in articles:
                name = form.instance.headline
                if article.headline == name:
                    messages.add_message(
                        request,
                        messages.INFO,
                        "An article with the same headline already exists.",
                    )
                    context = {"form": form}
                    return render(request, "add_article.html", context)
            form.save()
            messages.add_message(
                request, messages.INFO, "Your article is awaiting approval"
            )
            return redirect("display_articles", category_id=category_id)
    context = {"form": form}
    return render(request, "add_article.html", context)


def view_article(request, article_id):
    """
    When the user clicks 'View Article' on a specific article they
    will be taken to article.html which displays the articles details
    stored in the database. The user can add a comment and like the
    article if they are logged in. The comments are are displayed
    at the bottom of the page.
    """
    article = get_object_or_404(Article, id=article_id)
    category_id = article.category_id
    category = get_object_or_404(Category, id=category_id)
    comments = article.article_comment.order_by("time_created_comment")
    if request.method == "POST":
        form = CommentForm(request.POST, instance=article)
        if form.is_valid():
            obj = Comment()
            obj.body = form.cleaned_data["body"]
            obj.users_name = request.user
            obj.article = article
            obj.save()
            return redirect("view_article", article_id=article_id)
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
        "form": form,
        "comments": comments,
        "upvoted": upvoted,
        "downvoted": downvoted,
        "vote_count": vote_count,
        "category": category,
    }
    return render(request, "article.html", context)


def edit_article(request, article_id):
    """
    If the user has created an article, they have the option to edit
    it. On the article.html page, the user can click the
    'Edit Article' button which will bring them to the edit_article
    page with the prepopulated article details already entered. The
    user can then click the 'Update Article' button which will take
    them back to the article.html page.
    """
    article = get_object_or_404(Article, id=article_id)
    articles = list(Article.objects.all())
    form = ArticleForm(instance=article)
    if request.method == "POST":
        form = ArticleForm(request.POST, request.FILES, instance=article)
        if form.is_valid():
            summernote = request.POST.get("editordata")
            form.instance.content = summernote
            form.save()
            return redirect("view_article", article_id=article_id)
    context = {
        "form": form,
        "article": article,
    }
    return render(request, "edit_article.html", context)


def delete_article(request, article_id):
    """
    If the user has created the article, they have the option to
    delete it. On the article.html page, the user can click the
    'Delete Article' button which will remove the article from the
    Article data model and return the user to the
    category_articles.html page
    """
    article = get_object_or_404(Article, id=article_id)
    category_id = article.category_id
    article.delete()
    return redirect("display_articles", category_id=category_id)


def delete_comment(request, comment_id):
    """
    If the user has written a comment, they have the option to
    delete it. On the bottom of the article.html page in the
    comments section, the user can click the 'Delete Comment'
    button below there comment which will remove the comment
    from the Comment data model.
    """
    comment = get_object_or_404(Comment, id=comment_id)
    article_id = comment.article_id
    comment.delete()
    return redirect("view_article", article_id=article_id)


def upvote_article(request, article_id):
    """
    When the upvote button is pressed on the article.html
    page the same page is loaded with either adding or
    removing the users upvote to the Article data model.
    """
    article = get_object_or_404(Article, id=article_id)
    if article.upvote.filter(id=request.user.id).exists():
        article.upvote.remove(request.user)
    else:
        article.upvote.add(request.user)
        article.downvote.remove(request.user)
    return redirect("view_article", article_id=article_id)


def upvote_article2(request, article_id, *args, **kwargs):
    """
    When the upvote button is pressed on the index.html
    page the same page is loaded with either adding or
    removing the users upvote to the Article data model.
    """
    article = get_object_or_404(Article, id=article_id)
    if article.upvote.filter(id=request.user.id).exists():
        article.upvote.remove(request.user)
    else:
        article.upvote.add(request.user)
        article.downvote.remove(request.user)
    return redirect("display_top_articles")


def upvote_article3(request, article_id):
    """
    When the upvote button is pressed on the
    category-articles.html page the same page is loaded
    with either adding or removing the users upvote to
    the Article data model.
    """
    article = get_object_or_404(Article, id=article_id)
    category_id = article.category_id
    if article.upvote.filter(id=request.user.id).exists():
        article.upvote.remove(request.user)
    else:
        article.upvote.add(request.user)
        article.downvote.remove(request.user)
    return redirect("display_articles", category_id=category_id)


def downvote_article(request, article_id):
    """
    When the downvote button is pressed on the article.html
    page the same page is loaded with either adding or
    removing the users downvote to the Article data model.
    """
    article = get_object_or_404(Article, id=article_id)
    if article.downvote.filter(id=request.user.id).exists():
        article.downvote.remove(request.user)
    else:
        article.downvote.add(request.user)
        article.upvote.remove(request.user)
    return redirect("view_article", article_id=article_id)


def downvote_article2(request, article_id):
    """
    When the downvote button is pressed on the index.html
    page the same page is loaded with either adding or
    removing the users downvote to the Article data model.
    """
    article = get_object_or_404(Article, id=article_id)
    if article.downvote.filter(id=request.user.id).exists():
        article.downvote.remove(request.user)
    else:
        article.downvote.add(request.user)
        article.upvote.remove(request.user)
    return redirect("display_top_articles")


def downvote_article3(request, article_id):
    """
    When the downvote button is pressed on the
    category-articles.html page the same page is loaded
    with either adding or removing the users downvote to
    the Article data model.
    """
    article = get_object_or_404(Article, id=article_id)
    category_id = article.category_id
    if article.downvote.filter(id=request.user.id).exists():
        article.downvote.remove(request.user)
    else:
        article.downvote.add(request.user)
        article.upvote.remove(request.user)
    return redirect("display_articles", category_id=category_id)
