from django.contrib import admin
from .models import Article, Comment, Category

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('category_name', 'approve_category',)
    actions = ['approve_selected_categories']

    def approve_selected_categories(self, request, list_of_categories):
        list_of_categories.update(approve_category=True)

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):

    list_display = ('headline', 'approved', 'time_created', 'updated_time', 'author',)
    actions = ['approve_selected_articles']
    
    def approve_selected_articles(self, request, list_of_articles):
        list_of_articles.update(approved=True)

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):

    list_display = ('article',)
    list_filter = ('article',)
