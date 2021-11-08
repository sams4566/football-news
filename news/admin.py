from django.contrib import admin
from .models import Article

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):

    list_display = ('name', 'approved')
    actions = ['approve_selected_articles']
    
    def approve_selected_articles(self, request, list_of_articles):
        list_of_articles.update(approved=True)
